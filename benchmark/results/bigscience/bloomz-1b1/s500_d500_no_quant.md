# Deployment Arguments
## Constant
- model_id: "bigscience/bloomz-1b1"
- revision: None
- sharded: true
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
- num_shards: [2,4,8]

# Experiment Generation Argumetns
| Parameter          | Value                 |
|--------------------|-----------------------|
| Model              | bigscience/bloomz-1b1 |
| Sequence Length    | 500                   |
| Decode Length      | 500                   |
| N Runs             | 10                    |
| Warmups            | 1                     |
| Temperature        | None                  |
| Top K              | None                  |
| Top P              | None                  |
| Typical P          | None                  |
| Repetition Penalty | None                  |
| Watermark          | false                 |
| Do Sample          | false                 |

# Num Shards: 2
## Tensor Parallel (TP) - 2 GPUs
| Step           | Batch Size | Average     | Lowest      | Highest     | p50         | p90         | p99         |
|----------------|------------|-------------|-------------|-------------|-------------|-------------|-------------|
| Prefill        | 1          | 39.20 ms    | 35.88 ms    | 56.42 ms    | 36.64 ms    | 56.42 ms    | 56.42 ms    |
|                | 2          | 47.97 ms    | 46.30 ms    | 54.17 ms    | 47.43 ms    | 54.17 ms    | 54.17 ms    |
|                | 4          | 85.43 ms    | 84.18 ms    | 87.73 ms    | 85.54 ms    | 87.73 ms    | 87.73 ms    |
|                | 8          | 160.25 ms   | 158.72 ms   | 162.54 ms   | 160.11 ms   | 162.54 ms   | 162.54 ms   |
|                | 16         | 307.03 ms   | 304.27 ms   | 311.06 ms   | 307.57 ms   | 311.06 ms   | 311.06 ms   |
|                | 32         | 673.61 ms   | 593.19 ms   | 965.32 ms   | 604.60 ms   | 965.32 ms   | 965.32 ms   |
| Decode (token) | 1          | 14.70 ms    | 14.41 ms    | 15.01 ms    | 14.78 ms    | 14.41 ms    | 14.41 ms    |
|                | 2          | 14.95 ms    | 14.88 ms    | 15.04 ms    | 14.93 ms    | 14.97 ms    | 14.97 ms    |
|                | 4          | 15.57 ms    | 15.46 ms    | 15.72 ms    | 15.60 ms    | 15.53 ms    | 15.53 ms    |
|                | 8          | 16.70 ms    | 16.59 ms    | 16.83 ms    | 16.76 ms    | 16.64 ms    | 16.64 ms    |
|                | 16         | 19.14 ms    | 18.97 ms    | 19.38 ms    | 19.18 ms    | 19.04 ms    | 19.04 ms    |
|                | 32         | 26.21 ms    | 26.12 ms    | 26.32 ms    | 26.23 ms    | 26.32 ms    | 26.32 ms    |
| Decode (total) | 1          | 7334.36 ms  | 7191.39 ms  | 7488.37 ms  | 7375.16 ms  | 7191.39 ms  | 7191.39 ms  |
|                | 2          | 7459.61 ms  | 7423.85 ms  | 7504.25 ms  | 7451.03 ms  | 7470.20 ms  | 7470.20 ms  |
|                | 4          | 7771.64 ms  | 7715.64 ms  | 7845.58 ms  | 7783.91 ms  | 7750.62 ms  | 7750.62 ms  |
|                | 8          | 8333.45 ms  | 8279.71 ms  | 8397.35 ms  | 8361.44 ms  | 8304.37 ms  | 8304.37 ms  |
|                | 16         | 9548.74 ms  | 9466.71 ms  | 9672.29 ms  | 9569.94 ms  | 9498.93 ms  | 9498.93 ms  |
|                | 32         | 13081.24 ms | 13034.05 ms | 13135.92 ms | 13089.03 ms | 13135.92 ms | 13135.92 ms |


| Step    | Batch Size | Average             | Lowest              | Highest             |
|---------|------------|---------------------|---------------------|---------------------|
| Prefill | 1          | 25.99 tokens/secs   | 17.72 tokens/secs   | 27.87 tokens/secs   |
|         | 2          | 41.76 tokens/secs   | 36.92 tokens/secs   | 43.20 tokens/secs   |
|         | 4          | 46.83 tokens/secs   | 45.59 tokens/secs   | 47.52 tokens/secs   |
|         | 8          | 49.92 tokens/secs   | 49.22 tokens/secs   | 50.40 tokens/secs   |
|         | 16         | 52.12 tokens/secs   | 51.44 tokens/secs   | 52.58 tokens/secs   |
|         | 32         | 49.24 tokens/secs   | 33.15 tokens/secs   | 53.95 tokens/secs   |
| Decode  | 1          | 68.05 tokens/secs   | 66.64 tokens/secs   | 69.39 tokens/secs   |
|         | 2          | 133.79 tokens/secs  | 132.99 tokens/secs  | 134.43 tokens/secs  |
|         | 4          | 256.84 tokens/secs  | 254.41 tokens/secs  | 258.70 tokens/secs  |
|         | 8          | 479.04 tokens/secs  | 475.39 tokens/secs  | 482.14 tokens/secs  |
|         | 16         | 836.16 tokens/secs  | 825.45 tokens/secs  | 843.38 tokens/secs  |
|         | 32         | 1220.69 tokens/secs | 1215.60 tokens/secs | 1225.10 tokens/secs |