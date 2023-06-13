# Deployment Arguments
## Constant
- model_id: "bigscience/bloomz-7b1-mt"
- revision: None
- sharded: None
- quantize: None
- trust_remote_code: false
- max_concurrent_requests: 128
- max_best_of: 2
- max_stop_sequences: 4
- max_input_length: 1000
- max_total_tokens: 1512
- max_batch_size: None
- waiting_served_ratio: 1.2
- max_batch_total_tokens: 32000
- max_waiting_tokens: 20
- port: 5555
- shard_uds_path: "/tmp/text-generation-server"
- master_addr: "localhost"
- master_port: 29500
- huggingface_hub_cache: None
- weights_cache_override: None
- disable_custom_kernels: false
- json_output: false
- otlp_endpoint: None
- cors_allow_origin: []
- watermark_gamma: None
- watermark_delta: None
## Variables
- CUDA_VISIBLE_DEVICES (Tensor Parallelism): [0,1,2,3,4,5,6,7]

# Experiment Generation Argumetns
| Parameter          | Value                 |
|--------------------|-----------------------|
| Model              | bigscience/mt0-xxl-mt |
| Sequence Length    | 200                   |
| Decode Length      | 200                   |
| N Runs             | 10                    |
| Warmups            | 1                     |
| Temperature        | None                  |
| Top K              | None                  |
| Top P              | None                  |
| Typical P          | None                  |
| Repetition Penalty | None                  |
| Watermark          | false                 |
| Do Sample          | false                 |

# Tensor Parallel (TP) - 2 GPUs
| Step           | Batch Size | Average     | Lowest      | Highest     | p50         | p90         | p99         |
|----------------|------------|-------------|-------------|-------------|-------------|-------------|-------------|
| Prefill        | 1          | 64.70 ms    | 63.38 ms    | 66.77 ms    | 64.67 ms    | 66.77 ms    | 66.77 ms    |
|                | 2          | 76.36 ms    | 76.02 ms    | 76.81 ms    | 76.29 ms    | 76.81 ms    | 76.81 ms    |
|                | 4          | 116.85 ms   | 116.24 ms   | 117.71 ms   | 116.86 ms   | 117.71 ms   | 117.71 ms   |
|                | 8          | 186.90 ms   | 178.82 ms   | 190.29 ms   | 189.48 ms   | 190.29 ms   | 190.29 ms   |
|                | 16         | 328.53 ms   | 315.78 ms   | 342.85 ms   | 328.09 ms   | 342.85 ms   | 342.85 ms   |
|                | 32         | 586.82 ms   | 575.52 ms   | 602.81 ms   | 585.83 ms   | 602.81 ms   | 602.81 ms   |
| Decode (token) | 1          | 43.23 ms    | 43.04 ms    | 43.71 ms    | 43.18 ms    | 43.06 ms    | 43.06 ms    |
|                | 2          | 45.25 ms    | 44.92 ms    | 46.34 ms    | 45.01 ms    | 46.34 ms    | 46.34 ms    |
|                | 4          | 47.21 ms    | 46.78 ms    | 47.75 ms    | 47.27 ms    | 47.03 ms    | 47.03 ms    |
|                | 8          | 50.50 ms    | 50.09 ms    | 51.01 ms    | 50.38 ms    | 50.87 ms    | 50.87 ms    |
|                | 16         | 58.48 ms    | 58.03 ms    | 58.74 ms    | 58.56 ms    | 58.25 ms    | 58.25 ms    |
|                | 32         | 87.50 ms    | 87.43 ms    | 87.58 ms    | 87.51 ms    | 87.58 ms    | 87.58 ms    |
| Decode (total) | 1          | 8603.19 ms  | 8564.67 ms  | 8698.47 ms  | 8592.95 ms  | 8569.48 ms  | 8569.48 ms  |
|                | 2          | 9004.70 ms  | 8939.13 ms  | 9221.93 ms  | 8956.69 ms  | 9221.93 ms  | 9221.93 ms  |
|                | 4          | 9395.23 ms  | 9309.96 ms  | 9502.30 ms  | 9407.41 ms  | 9360.12 ms  | 9360.12 ms  |
|                | 8          | 10049.20 ms | 9968.80 ms  | 10151.10 ms | 10025.73 ms | 10122.62 ms | 10122.62 ms |
|                | 16         | 11637.65 ms | 11548.78 ms | 11689.76 ms | 11653.04 ms | 11592.06 ms | 11592.06 ms |
|                | 32         | 17412.72 ms | 17398.39 ms | 17427.47 ms | 17414.45 ms | 17427.47 ms | 17427.47 ms |


| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 15.46 tokens/secs  | 14.98 tokens/secs  | 15.78 tokens/secs  |
|         | 2          | 26.19 tokens/secs  | 26.04 tokens/secs  | 26.31 tokens/secs  |
|         | 4          | 34.23 tokens/secs  | 33.98 tokens/secs  | 34.41 tokens/secs  |
|         | 8          | 42.82 tokens/secs  | 42.04 tokens/secs  | 44.74 tokens/secs  |
|         | 16         | 48.74 tokens/secs  | 46.67 tokens/secs  | 50.67 tokens/secs  |
|         | 32         | 54.54 tokens/secs  | 53.09 tokens/secs  | 55.60 tokens/secs  |
| Decode  | 1          | 23.13 tokens/secs  | 22.88 tokens/secs  | 23.23 tokens/secs  |
|         | 2          | 44.20 tokens/secs  | 43.16 tokens/secs  | 44.52 tokens/secs  |
|         | 4          | 84.73 tokens/secs  | 83.77 tokens/secs  | 85.50 tokens/secs  |
|         | 8          | 158.43 tokens/secs | 156.83 tokens/secs | 159.70 tokens/secs |
|         | 16         | 273.60 tokens/secs | 272.38 tokens/secs | 275.70 tokens/secs |
|         | 32         | 365.71 tokens/secs | 365.40 tokens/secs | 366.01 tokens/secs |

# Tensor Parallel (TP) - 4 GPUs
| Step           | Batch Size | Average     | Lowest      | Highest     | p50         | p90         | p99         |
|----------------|------------|-------------|-------------|-------------|-------------|-------------|-------------|
| Prefill        | 1          | 65.95 ms    | 64.65 ms    | 67.08 ms    | 66.46 ms    | 67.08 ms    | 67.08 ms    |
|                | 2          | 80.42 ms    | 79.76 ms    | 81.38 ms    | 80.49 ms    | 81.38 ms    | 81.38 ms    |
|                | 4          | 121.95 ms   | 121.08 ms   | 122.79 ms   | 122.05 ms   | 122.79 ms   | 122.79 ms   |
|                | 8          | 196.25 ms   | 195.55 ms   | 197.57 ms   | 196.16 ms   | 197.57 ms   | 197.57 ms   |
|                | 16         | 354.85 ms   | 347.88 ms   | 358.68 ms   | 356.37 ms   | 358.68 ms   | 358.68 ms   |
|                | 32         | 632.39 ms   | 622.80 ms   | 647.66 ms   | 633.26 ms   | 647.66 ms   | 647.66 ms   |
| Decode (token) | 1          | 43.41 ms    | 43.34 ms    | 43.49 ms    | 43.41 ms    | 43.46 ms    | 43.46 ms    |
|                | 2          | 45.27 ms    | 45.22 ms    | 45.35 ms    | 45.26 ms    | 45.34 ms    | 45.34 ms    |
|                | 4          | 47.08 ms    | 46.96 ms    | 47.33 ms    | 47.05 ms    | 47.08 ms    | 47.08 ms    |
|                | 8          | 50.90 ms    | 50.28 ms    | 51.39 ms    | 50.98 ms    | 51.28 ms    | 51.28 ms    |
|                | 16         | 62.06 ms    | 61.98 ms    | 62.17 ms    | 62.06 ms    | 62.17 ms    | 62.17 ms    |
|                | 32         | 94.33 ms    | 94.26 ms    | 94.39 ms    | 94.32 ms    | 94.39 ms    | 94.39 ms    |
| Decode (total) | 1          | 8638.33 ms  | 8624.79 ms  | 8654.30 ms  | 8637.60 ms  | 8648.26 ms  | 8648.26 ms  |
|                | 2          | 9008.82 ms  | 8998.42 ms  | 9024.84 ms  | 9006.67 ms  | 9022.37 ms  | 9022.37 ms  |
|                | 4          | 9368.32 ms  | 9345.69 ms  | 9418.51 ms  | 9362.43 ms  | 9368.98 ms  | 9368.98 ms  |
|                | 8          | 10128.79 ms | 10006.48 ms | 10226.40 ms | 10145.46 ms | 10204.26 ms | 10204.26 ms |
|                | 16         | 12350.65 ms | 12335.03 ms | 12371.78 ms | 12350.73 ms | 12371.78 ms | 12371.78 ms |
|                | 32         | 18771.13 ms | 18758.23 ms | 18783.66 ms | 18770.08 ms | 18783.66 ms | 18783.66 ms |


| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 15.17 tokens/secs  | 14.91 tokens/secs  | 15.47 tokens/secs  |
|         | 2          | 24.87 tokens/secs  | 24.58 tokens/secs  | 25.07 tokens/secs  |
|         | 4          | 32.80 tokens/secs  | 32.58 tokens/secs  | 33.04 tokens/secs  |
|         | 8          | 40.76 tokens/secs  | 40.49 tokens/secs  | 40.91 tokens/secs  |
|         | 16         | 45.09 tokens/secs  | 44.61 tokens/secs  | 45.99 tokens/secs  |
|         | 32         | 50.61 tokens/secs  | 49.41 tokens/secs  | 51.38 tokens/secs  |
| Decode  | 1          | 23.04 tokens/secs  | 22.99 tokens/secs  | 23.07 tokens/secs  |
|         | 2          | 44.18 tokens/secs  | 44.10 tokens/secs  | 44.23 tokens/secs  |
|         | 4          | 84.97 tokens/secs  | 84.51 tokens/secs  | 85.17 tokens/secs  |
|         | 8          | 157.18 tokens/secs | 155.68 tokens/secs | 159.10 tokens/secs |
|         | 16         | 257.80 tokens/secs | 257.36 tokens/secs | 258.13 tokens/secs |
|         | 32         | 339.24 tokens/secs | 339.02 tokens/secs | 339.48 tokens/secs |