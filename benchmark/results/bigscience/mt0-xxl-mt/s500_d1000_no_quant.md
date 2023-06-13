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
| Sequence Length    | 500                   |
| Decode Length      | 1000                  |
| N Runs             | 10                    |
| Warmups            | 1                     |
| Temperature        | None                  |
| Top K              | None                  |
| Top P              | None                  |
| Typical P          | None                  |
| Repetition Penalty | None                  |
| Watermark          | false                 |
| Do Sample          | false                 |

# Tensor Parallel (TP) - 4 GPUs
| Step           | Batch Size | Average      | Lowest       | Highest      | p50          | p90          | p99          |
|----------------|------------|--------------|--------------|--------------|--------------|--------------|--------------|
| Prefill        | 16         | 958.80 ms    | 946.70 ms    | 970.90 ms    | 970.90 ms    | 970.90 ms    | 970.90 ms    |
| Decode (token) |            | 121.88 ms    | 121.88 ms    | 121.88 ms    | 121.88 ms    | 121.88 ms    | 121.88 ms    |
| Decode (total) |            | 121758.35 ms | 121758.35 ms | 121758.35 ms | 121758.35 ms | 121758.35 ms | 121758.35 ms |


| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 16         | 16.69 tokens/secs  | 16.48 tokens/secs  | 16.90 tokens/secs  |
| Decode  |            | 131.28 tokens/secs | 131.28 tokens/secs | 131.28 tokens/secs |
