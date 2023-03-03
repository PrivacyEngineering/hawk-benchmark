import datetime
import time
import os
import pandas as pd
import json
totalRuns=3
endpoint = "prometheus.istio-system.svc.cluster.local:9090/api/v1/query?query="
total_requests_query = f"{endpoint}sum(istio_requests_total{{namespace=~'sock-shop|hawk-ns'}})[1h:1s]"
total_requests_collector_query = f"{endpoint}sum(istio_requests_total{{namespace=~'sock-shop|hawk-ns',destination_service_name='collector'}})[1h:1s]"
latency_ms_collector_query = f"{endpoint}(sum(increase(istio_request_duration_milliseconds_sum{{destination_app='collector'}}[1h]))/sum(increase(istio_request_duration_milliseconds_count{{destination_app='collector'}}[1h])))[1h:1s]"

def get_prometheus_query(r,download_filename,first,last,query)->pd.Series:
    filename = f"testresults/{r}_{download_filename}"
    os.system(f'curl -o {filename} -g "{query}"')
    with open(filename, 'r') as f:
        data = json.load(f)["data"]["result"][0]["values"]
    df = pd.DataFrame(data).convert_dtypes().set_index(0,drop=True)
    return pd.to_numeric(df.loc[first:last][1])

for r in range(totalRuns):
    print(f"Run: {r}/{totalRuns}")
    os.system(f"locust --csv=testresults/{r}")
    hist_df = pd.read_csv(f"testresults/{r}_stats_history.csv")
    first = int(hist_df["Timestamp"].head(1).values[0])
    last = int(hist_df["Timestamp"].tail(1).values[0])
    hist_df.set_index("Timestamp",inplace=True)
    print("Sleep 10 seconds...")
    time.sleep(10)
    print("Get requests total...")
    hist_df["Istio_Requests_Total"] = get_prometheus_query(r,"istio_total_requests.json",first,last,total_requests_query)
    print("Get requests collector...")
    hist_df["Istio_Requests_Collector_Total"] = get_prometheus_query(r,"istio_total_requests_collector.json",first,last,total_requests_collector_query)
    print("Get latency collector...")
    hist_df["Collector_ms_Latency"] = get_prometheus_query(r,"collector_latency.json",first,last,latency_ms_collector_query)
    hist_df.to_csv(f"testresults/{r}_combined.csv")