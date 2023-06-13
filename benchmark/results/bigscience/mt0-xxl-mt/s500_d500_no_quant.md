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


# Tensor Parallel (TP) - 2 GPUs
| Step           | Batch Size | Average     | Lowest      | Highest     | p50         | p90         | p99         |
|----------------|------------|-------------|-------------|-------------|-------------|-------------|-------------|
| Prefill        | 1          | 91.75 ms    | 91.48 ms    | 92.24 ms    | 91.75 ms    | 92.24 ms    | 92.24 ms    |
|                | 2          | 165.97 ms   | 164.81 ms   | 166.54 ms   | 166.24 ms   | 166.54 ms   | 166.54 ms   |
|                | 4          | 272.55 ms   | 264.56 ms   | 282.56 ms   | 275.74 ms   | 282.56 ms   | 282.56 ms   |
|                | 8          | 495.66 ms   | 479.88 ms   | 509.42 ms   | 499.20 ms   | 509.42 ms   | 509.42 ms   |
|                | 16         | 922.25 ms   | 911.35 ms   | 929.69 ms   | 926.05 ms   | 929.69 ms   | 929.69 ms   |
|                | 32         | NaN ms      | NaN ms      | NaN ms      | NaN ms      | NaN ms      | NaN ms      |
| Decode (token) | 1          | 44.45 ms    | 43.97 ms    | 45.03 ms    | 44.59 ms    | 44.85 ms    | 44.85 ms    |
|                | 2          | 46.76 ms    | 46.34 ms    | 47.65 ms    | 46.80 ms    | 46.49 ms    | 46.49 ms    |
|                | 4          | 49.54 ms    | 49.37 ms    | 50.07 ms    | 49.50 ms    | 49.59 ms    | 49.59 ms    |
|                | 8          | 60.81 ms    | 60.78 ms    | 60.89 ms    | 60.82 ms    | 60.83 ms    | 60.83 ms    |
|                | 16         | 94.97 ms    | 94.89 ms    | 95.02 ms    | 94.98 ms    | 95.01 ms    | 95.01 ms    |
|                | 32         | NaN ms      | NaN ms      | NaN ms      | NaN ms      | NaN ms      | NaN ms      |
| Decode (total) | 1          | 22178.34 ms | 21942.49 ms | 22471.30 ms | 22251.71 ms | 22380.49 ms | 22380.49 ms |
|                | 2          | 23335.73 ms | 23123.10 ms | 23777.44 ms | 23356.17 ms | 23199.47 ms | 23199.47 ms |
|                | 4          | 24720.56 ms | 24634.00 ms | 24985.90 ms | 24702.69 ms | 24746.42 ms | 24746.42 ms |
|                | 8          | 30346.45 ms | 30327.94 ms | 30383.31 ms | 30348.34 ms | 30354.01 ms | 30354.01 ms |
|                | 16         | 47387.71 ms | 47349.25 ms | 47415.67 ms | 47393.78 ms | 47409.07 ms | 47409.07 ms |
|                | 32         | NaN ms      | NaN ms      | NaN ms      | NaN ms      | NaN ms      | NaN ms      |


| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 10.90 tokens/secs  | 10.84 tokens/secs  | 10.93 tokens/secs  |
|         | 2          | 12.05 tokens/secs  | 12.01 tokens/secs  | 12.14 tokens/secs  |
|         | 4          | 14.69 tokens/secs  | 14.16 tokens/secs  | 15.12 tokens/secs  |
|         | 8          | 16.14 tokens/secs  | 15.70 tokens/secs  | 16.67 tokens/secs  |
|         | 16         | 17.35 tokens/secs  | 17.21 tokens/secs  | 17.56 tokens/secs  |
|         | 32         | NaN tokens/secs    | NaN tokens/secs    | NaN tokens/secs    |
| Decode  | 1          | 22.50 tokens/secs  | 22.21 tokens/secs  | 22.74 tokens/secs  |
|         | 2          | 42.77 tokens/secs  | 41.97 tokens/secs  | 43.16 tokens/secs  |
|         | 4          | 80.74 tokens/secs  | 79.89 tokens/secs  | 81.03 tokens/secs  |
|         | 8          | 131.55 tokens/secs | 131.39 tokens/secs | 131.63 tokens/secs |
|         | 16         | 168.48 tokens/secs | 168.38 tokens/secs | 168.62 tokens/secs |
|         | 32         | NaN tokens/secs    | NaN tokens/secs    | NaN tokens/secs    |