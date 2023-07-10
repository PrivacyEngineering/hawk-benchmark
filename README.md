# hawk-benchmark

We published Hawk at the 16th IEEE International Conference on Cloud Computing 2023, IEEE Cloud 2023.
Please find our paper on Hawk here: https://arxiv.org/abs/2306.02496

## BibTex citation:
```
@misc{grünewald2023hawk,
      title={Hawk: DevOps-driven Transparency and Accountability in Cloud Native Systems}, 
      author={Elias Grünewald and Jannis Kiesel and Siar-Remzi Akbayin and Frank Pallas},
      year={2023},
      eprint={2306.02496},
      archivePrefix={arXiv},
      primaryClass={cs.DC}
}
```
## Overview

# Cluster Settings
Our cluster runs on the Google Kubernetes Engine and has the following settings:

•	Location: us-central1-c

•	Number of nodes: 3

•	Total vCPUs: 24

•	Total memory: 90GB

•	Version: 1.25.6-gke.1000

•	Location type: Zonal

•	Machine type: n1-standard-8

# Istio 

version: 1.18-alpha

profile: default
