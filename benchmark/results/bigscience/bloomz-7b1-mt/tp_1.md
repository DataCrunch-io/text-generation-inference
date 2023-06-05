```bash
text-generation-launcher --model-id bigscience/bloomz-7b1-mt --num-shard 1 --port 8080
```

# text_generation_launcher: Args
- model_id: "bigscience/bloomz-7b1-mt"
- revision: None
- sharded: None
- num_shard: Some(1)
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
- port: 8080
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

# Experiment Generation Argumetns

| Parameter          | Value                    |
|--------------------|--------------------------|
| Model              | bigscience/bloomz-7b1-mt |
| Sequence Length    | 1024                     |
| Decode Length      | 8                        |
| N Runs             | 10                       |
| Warmups            | 1                        |
| Temperature        | None                     |
| Top K              | None                     |
| Top P              | None                     |
| Typical P          | None                     |
| Repetition Penalty | None                     |
| Watermark          | false                    |
| Do Sample          | false                    |

| Step           | Batch Size | Average    | Lowest     | Highest    | p50        | p90        | p99        |
|----------------|------------|------------|------------|------------|------------|------------|------------|
| Prefill        | 1          | 139.82 ms  | 139.29 ms  | 140.60 ms  | 139.86 ms  | 140.60 ms  | 140.60 ms  |
|                | 2          | 270.53 ms  | 270.06 ms  | 271.42 ms  | 270.46 ms  | 271.42 ms  | 271.42 ms  |
|                | 4          | 511.82 ms  | 511.38 ms  | 512.75 ms  | 511.72 ms  | 512.75 ms  | 512.75 ms  |
|                | 8          | 944.88 ms  | 921.12 ms  | 969.25 ms  | 947.14 ms  | 969.25 ms  | 969.25 ms  |
|                | 16         | 2059.86 ms | 2032.14 ms | 2116.41 ms | 2057.71 ms | 2116.41 ms | 2116.41 ms |
|                | 32         | 3868.30 ms | 3822.36 ms | 3918.47 ms | 3880.60 ms | 3918.47 ms | 3918.47 ms |
| Decode (token) | 1          | 28.75 ms   | 28.69 ms   | 28.82 ms   | 28.75 ms   | 28.82 ms   | 28.82 ms   |
|                | 2          | 35.70 ms   | 35.67 ms   | 35.73 ms   | 35.70 ms   | 35.73 ms   | 35.73 ms   |
|                | 4          | 49.27 ms   | 49.23 ms   | 49.33 ms   | 49.27 ms   | 49.33 ms   | 49.33 ms   |
|                | 8          | 72.77 ms   | 71.75 ms   | 73.83 ms   | 72.92 ms   | 73.83 ms   | 73.83 ms   |
|                | 16         | 127.26 ms  | 126.62 ms  | 127.71 ms  | 127.29 ms  | 127.71 ms  | 127.71 ms  |
|                | 32         | 243.98 ms  | 242.84 ms  | 245.63 ms  | 243.86 ms  | 245.63 ms  | 245.63 ms  |
| Decode (total) | 1          | 201.26 ms  | 200.84 ms  | 201.72 ms  | 201.27 ms  | 201.72 ms  | 201.72 ms  |
|                | 2          | 249.89 ms  | 249.67 ms  | 250.12 ms  | 249.90 ms  | 250.12 ms  | 250.12 ms  |
|                | 4          | 344.90 ms  | 344.64 ms  | 345.33 ms  | 344.91 ms  | 345.33 ms  | 345.33 ms  |
|                | 8          | 509.37 ms  | 502.28 ms  | 516.82 ms  | 510.41 ms  | 516.82 ms  | 516.82 ms  |
|                | 16         | 890.81 ms  | 886.38 ms  | 893.99 ms  | 891.02 ms  | 893.99 ms  | 893.99 ms  |
|                | 32         | 1707.85 ms | 1699.87 ms | 1719.45 ms | 1706.99 ms | 1719.45 ms | 1719.45 ms |

| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 7.15 tokens/secs   | 7.11 tokens/secs   | 7.18 tokens/secs   |
|         | 2          | 7.39 tokens/secs   | 7.37 tokens/secs   | 7.41 tokens/secs   |
|         | 4          | 7.82 tokens/secs   | 7.80 tokens/secs   | 7.82 tokens/secs   |
|         | 8          | 8.47 tokens/secs   | 8.25 tokens/secs   | 8.69 tokens/secs   |
|         | 16         | 7.77 tokens/secs   | 7.56 tokens/secs   | 7.87 tokens/secs   |
|         | 32         | 8.27 tokens/secs   | 8.17 tokens/secs   | 8.37 tokens/secs   |
| Decode  | 1          | 34.78 tokens/secs  | 34.70 tokens/secs  | 34.85 tokens/secs  |
|         | 2          | 56.03 tokens/secs  | 55.97 tokens/secs  | 56.07 tokens/secs  |
|         | 4          | 81.18 tokens/secs  | 81.08 tokens/secs  | 81.24 tokens/secs  |
|         | 8          | 109.95 tokens/secs | 108.35 tokens/secs | 111.49 tokens/secs |
|         | 16         | 125.73 tokens/secs | 125.28 tokens/secs | 126.36 tokens/secs |
|         | 32         | 131.16 tokens/secs | 130.27 tokens/secs | 131.77 tokens/secs |