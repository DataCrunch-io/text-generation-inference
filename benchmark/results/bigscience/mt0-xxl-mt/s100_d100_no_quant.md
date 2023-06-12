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
| Sequence Length    | 100                   |
| Decode Length      | 100                   |
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
| Step           | Batch Size | Average    | Lowest     | Highest    | p50        | p90        | p99        |
|----------------|------------|------------|------------|------------|------------|------------|------------|
| Prefill        | 1          | 65.65 ms   | 62.84 ms   | 76.21 ms   | 64.65 ms   | 76.21 ms   | 76.21 ms   |
|                | 2          | 67.76 ms   | 65.88 ms   | 70.41 ms   | 67.63 ms   | 70.41 ms   | 70.41 ms   |
|                | 4          | 75.58 ms   | 74.83 ms   | 77.27 ms   | 75.45 ms   | 77.27 ms   | 77.27 ms   |
|                | 8          | 115.94 ms  | 115.27 ms  | 116.83 ms  | 115.85 ms  | 116.83 ms  | 116.83 ms  |
|                | 16         | 183.37 ms  | 176.94 ms  | 187.75 ms  | 184.80 ms  | 187.75 ms  | 187.75 ms  |
|                | 32         | 326.75 ms  | 308.01 ms  | 336.95 ms  | 332.58 ms  | 336.95 ms  | 336.95 ms  |
| Decode (token) | 1          | 43.46 ms   | 43.03 ms   | 44.75 ms   | 43.37 ms   | 43.03 ms   | 43.03 ms   |
|                | 2          | 44.91 ms   | 44.33 ms   | 45.67 ms   | 45.22 ms   | 44.73 ms   | 44.73 ms   |
|                | 4          | 46.08 ms   | 45.60 ms   | 46.53 ms   | 46.16 ms   | 45.60 ms   | 45.60 ms   |
|                | 8          | 48.31 ms   | 47.64 ms   | 50.17 ms   | 48.31 ms   | 47.64 ms   | 47.64 ms   |
|                | 16         | 53.42 ms   | 52.72 ms   | 54.21 ms   | 53.15 ms   | 53.95 ms   | 53.95 ms   |
|                | 32         | 63.96 ms   | 63.35 ms   | 64.97 ms   | 63.74 ms   | 64.97 ms   | 64.97 ms   |
| Decode (total) | 1          | 4302.14 ms | 4260.36 ms | 4430.01 ms | 4293.85 ms | 4260.36 ms | 4260.36 ms |
|                | 2          | 4445.96 ms | 4388.19 ms | 4521.91 ms | 4477.18 ms | 4427.93 ms | 4427.93 ms |
|                | 4          | 4561.93 ms | 4514.04 ms | 4606.10 ms | 4569.90 ms | 4514.04 ms | 4514.04 ms |
|                | 8          | 4783.05 ms | 4716.24 ms | 4967.08 ms | 4782.98 ms | 4716.24 ms | 4716.24 ms |
|                | 16         | 5288.29 ms | 5219.32 ms | 5367.16 ms | 5261.67 ms | 5341.60 ms | 5341.60 ms |
|                | 32         | 6331.85 ms | 6271.47 ms | 6431.84 ms | 6310.37 ms | 6431.84 ms | 6431.84 ms |


| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 15.28 tokens/secs  | 13.12 tokens/secs  | 15.91 tokens/secs  |
|         | 2          | 29.52 tokens/secs  | 28.40 tokens/secs  | 30.36 tokens/secs  |
|         | 4          | 52.93 tokens/secs  | 51.77 tokens/secs  | 53.45 tokens/secs  |
|         | 8          | 69.00 tokens/secs  | 68.47 tokens/secs  | 69.40 tokens/secs  |
|         | 16         | 87.29 tokens/secs  | 85.22 tokens/secs  | 90.43 tokens/secs  |
|         | 32         | 98.02 tokens/secs  | 94.97 tokens/secs  | 103.89 tokens/secs |
| Decode  | 1          | 23.01 tokens/secs  | 22.35 tokens/secs  | 23.24 tokens/secs  |
|         | 2          | 44.54 tokens/secs  | 43.79 tokens/secs  | 45.12 tokens/secs  |
|         | 4          | 86.81 tokens/secs  | 85.97 tokens/secs  | 87.73 tokens/secs  |
|         | 8          | 165.62 tokens/secs | 159.45 tokens/secs | 167.93 tokens/secs |
|         | 16         | 299.56 tokens/secs | 295.13 tokens/secs | 303.49 tokens/secs |
|         | 32         | 500.37 tokens/secs | 492.55 tokens/secs | 505.14 tokens/secs |

# Tensor Parallel (TP) - 4 GPUs
| Step           | Batch Size | Average    | Lowest     | Highest    | p50        | p90        | p99        |
|----------------|------------|------------|------------|------------|------------|------------|------------|
| Prefill        | 1          | 65.38 ms   | 64.55 ms   | 66.60 ms   | 65.25 ms   | 66.60 ms   | 66.60 ms   |
|                | 2          | 71.42 ms   | 68.14 ms   | 82.47 ms   | 70.92 ms   | 82.47 ms   | 82.47 ms   |
|                | 4          | 80.10 ms   | 78.81 ms   | 82.04 ms   | 79.93 ms   | 82.04 ms   | 82.04 ms   |
|                | 8          | 120.82 ms  | 119.82 ms  | 122.41 ms  | 120.75 ms  | 122.41 ms  | 122.41 ms  |
|                | 16         | 194.54 ms  | 192.82 ms  | 196.22 ms  | 194.84 ms  | 196.22 ms  | 196.22 ms  |
|                | 32         | 348.26 ms  | 341.40 ms  | 353.08 ms  | 348.62 ms  | 353.08 ms  | 353.08 ms  |
| Decode (token) | 1          | 44.16 ms   | 43.90 ms   | 44.74 ms   | 44.11 ms   | 44.28 ms   | 44.28 ms   |
|                | 2          | 45.33 ms   | 44.88 ms   | 45.96 ms   | 45.50 ms   | 44.96 ms   | 44.96 ms   |
|                | 4          | 45.98 ms   | 45.52 ms   | 46.31 ms   | 46.15 ms   | 45.52 ms   | 45.52 ms   |
|                | 8          | 48.50 ms   | 47.82 ms   | 50.81 ms   | 48.24 ms   | 50.81 ms   | 50.81 ms   |
|                | 16         | 53.71 ms   | 53.14 ms   | 54.18 ms   | 53.74 ms   | 54.12 ms   | 54.12 ms   |
|                | 32         | 67.21 ms   | 66.84 ms   | 67.57 ms   | 67.22 ms   | 67.57 ms   | 67.57 ms   |
| Decode (total) | 1          | 4372.18 ms | 4346.49 ms | 4429.16 ms | 4367.17 ms | 4383.70 ms | 4383.70 ms |
|                | 2          | 4487.79 ms | 4442.75 ms | 4550.06 ms | 4504.82 ms | 4451.02 ms | 4451.02 ms |
|                | 4          | 4551.71 ms | 4506.90 ms | 4585.02 ms | 4569.24 ms | 4506.90 ms | 4506.90 ms |
|                | 8          | 4801.99 ms | 4734.35 ms | 5030.46 ms | 4775.69 ms | 5030.46 ms | 5030.46 ms |
|                | 16         | 5317.14 ms | 5260.64 ms | 5363.61 ms | 5320.45 ms | 5357.81 ms | 5357.81 ms |
|                | 32         | 6653.78 ms | 6616.89 ms | 6689.57 ms | 6654.29 ms | 6689.57 ms | 6689.57 ms |


| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 15.30 tokens/secs  | 15.02 tokens/secs  | 15.49 tokens/secs  |
|         | 2          | 28.08 tokens/secs  | 24.25 tokens/secs  | 29.35 tokens/secs  |
|         | 4          | 49.95 tokens/secs  | 48.76 tokens/secs  | 50.75 tokens/secs  |
|         | 8          | 66.22 tokens/secs  | 65.36 tokens/secs  | 66.77 tokens/secs  |
|         | 16         | 82.25 tokens/secs  | 81.54 tokens/secs  | 82.98 tokens/secs  |
|         | 32         | 91.89 tokens/secs  | 90.63 tokens/secs  | 93.73 tokens/secs  |
| Decode  | 1          | 22.64 tokens/secs  | 22.35 tokens/secs  | 22.78 tokens/secs  |
|         | 2          | 44.12 tokens/secs  | 43.52 tokens/secs  | 44.57 tokens/secs  |
|         | 4          | 87.00 tokens/secs  | 86.37 tokens/secs  | 87.87 tokens/secs  |
|         | 8          | 164.98 tokens/secs | 157.44 tokens/secs | 167.29 tokens/secs |
|         | 16         | 297.92 tokens/secs | 295.32 tokens/secs | 301.10 tokens/secs |
|         | 32         | 476.13 tokens/secs | 473.57 tokens/secs | 478.78 tokens/secs |

# Tensor Parallel (TP) - 8 GPUs
| Step           | Batch Size | Average    | Lowest     | Highest    | p50        | p90        | p99        |
|----------------|------------|------------|------------|------------|------------|------------|------------|
| Prefill        | 1          | 66.82 ms   | 65.42 ms   | 69.20 ms   | 67.12 ms   | 69.20 ms   | 69.20 ms   |
|                | 2          | 71.15 ms   | 68.35 ms   | 74.46 ms   | 70.92 ms   | 74.46 ms   | 74.46 ms   |
|                | 4          | 82.19 ms   | 80.45 ms   | 85.67 ms   | 82.05 ms   | 85.67 ms   | 85.67 ms   |
|                | 8          | 121.43 ms  | 120.68 ms  | 122.39 ms  | 122.39 ms  | 121.07 ms  | 121.07 ms  |
|                | 16         | 194.62 ms  | 193.22 ms  | 198.68 ms  | 198.68 ms  | 196.15 ms  | 196.15 ms  |
|                | 32         | 352.84 ms  | 351.57 ms  | 355.94 ms  | 352.01 ms  | 351.73 ms  | 351.73 ms  |
| Decode (token) | 1          | 43.75 ms   | 43.28 ms   | 44.48 ms   | 43.76 ms   | 44.48 ms   | 44.48 ms   |
|                | 2          | 45.42 ms   | 44.85 ms   | 46.71 ms   | 45.48 ms   | 46.71 ms   | 46.71 ms   |
|                | 4          | 46.27 ms   | 45.64 ms   | 46.86 ms   | 46.39 ms   | 46.86 ms   | 46.86 ms   |
|                | 8          | 48.21 ms   | 47.75 ms   | 48.74 ms   | 47.75 ms   | 47.86 ms   | 47.86 ms   |
|                | 16         | 52.88 ms   | 52.40 ms   | 53.40 ms   | 53.25 ms   | 52.75 ms   | 52.75 ms   |
|                | 32         | 68.08 ms   | 67.64 ms   | 68.83 ms   | 67.79 ms   | 68.63 ms   | 68.63 ms   |
| Decode (total) | 1          | 4331.47 ms | 4284.69 ms | 4404.06 ms | 4332.21 ms | 4404.06 ms | 4404.06 ms |
|                | 2          | 4496.79 ms | 4440.35 ms | 4624.23 ms | 4502.36 ms | 4624.23 ms | 4624.23 ms |
|                | 4          | 4580.68 ms | 4518.18 ms | 4638.96 ms | 4592.97 ms | 4638.96 ms | 4638.96 ms |
|                | 8          | 4772.62 ms | 4727.41 ms | 4825.19 ms | 4727.59 ms | 4738.39 ms | 4738.39 ms |
|                | 16         | 5235.03 ms | 5187.29 ms | 5286.93 ms | 5272.01 ms | 5222.40 ms | 5222.40 ms |
|                | 32         | 6739.78 ms | 6696.20 ms | 6813.94 ms | 6711.45 ms | 6794.18 ms | 6794.18 ms |


| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 14.97 tokens/secs  | 14.45 tokens/secs  | 15.29 tokens/secs  |
|         | 2          | 28.13 tokens/secs  | 26.86 tokens/secs  | 29.26 tokens/secs  |
|         | 4          | 48.68 tokens/secs  | 46.69 tokens/secs  | 49.72 tokens/secs  |
|         | 8          | 65.88 tokens/secs  | 65.36 tokens/secs  | 66.29 tokens/secs  |
|         | 16         | 82.22 tokens/secs  | 80.53 tokens/secs  | 82.81 tokens/secs  |
|         | 32         | 90.69 tokens/secs  | 89.90 tokens/secs  | 91.02 tokens/secs  |
| Decode  | 1          | 22.86 tokens/secs  | 22.48 tokens/secs  | 23.11 tokens/secs  |
|         | 2          | 44.04 tokens/secs  | 42.82 tokens/secs  | 44.59 tokens/secs  |
|         | 4          | 86.46 tokens/secs  | 85.36 tokens/secs  | 87.65 tokens/secs  |
|         | 8          | 165.96 tokens/secs | 164.14 tokens/secs | 167.53 tokens/secs |
|         | 16         | 302.59 tokens/secs | 299.61 tokens/secs | 305.36 tokens/secs |
|         | 32         | 470.06 tokens/secs | 464.93 tokens/secs | 473.10 tokens/secs |