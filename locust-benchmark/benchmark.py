import datetime
import time
import os
totalRuns=1
total_requests_query = "http://localhost:9090/api/v1/query?query=sum(istio_requests_total)[1h:1s]"
#sum(istio_requests_total{destination_app="collector"})[1h:1s]
#sum(istio_requests_total{namespace=~"sock-shop|hawk-ns",destination_service_name="collector"})[1h:1s]
for r in range(totalRuns):
    print(f"Run: {r}/{totalRuns}")
    os.system(f"locust --csv=testresults/{r}")
    print("Sleep 10 seconds")
    time.sleep(10)
    print("Downloading Prometheus data")
    os.system(f'curl -o testresults/{r}_prometheus_total_requests.json -g "{total_requests_query}"')
