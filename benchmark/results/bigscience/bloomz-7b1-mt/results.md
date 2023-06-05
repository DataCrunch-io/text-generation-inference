```bash
text-generation-launcher --model-id bigscience/bloomz-7b1-mt --num-shard 1 --port 8080
```

# text_generation_launcher: Args
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
## Variables
- num_shard: Some(1,2,4,8)


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

# Tensor Parallel (TP) - 1 GPUs


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

# Tensor Parallel (TP) - 2 GPUs

| Step           | Batch Size | Average   | Lowest    | Highest   | p50       | p90       | p99       |
|----------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|
| Prefill        | 1          | 106.49 ms | 104.59 ms | 115.27 ms | 105.04 ms | 115.27 ms | 115.27 ms |
|                | 2          | 172.98 ms | 172.15 ms | 178.52 ms | 172.27 ms | 178.52 ms | 178.52 ms |
|                | 4          | 335.55 ms | 332.75 ms | 339.33 ms | 335.63 ms | 339.33 ms | 339.33 ms |
|                | 8          | 662.31 ms | 658.11 ms | 668.06 ms | 662.72 ms | 668.06 ms | 668.06 ms |
|                | 16         | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    |
|                | 32         |           |           |           |           |           |           |
| Decode (token) | 1          | 17.56 ms  | 17.23 ms  | 18.58 ms  | 17.43 ms  | 17.59 ms  | 17.59 ms  |
|                | 2          | 18.09 ms  | 17.68 ms  | 18.98 ms  | 17.78 ms  | 18.98 ms  | 18.98 ms  |
|                | 4          | 19.45 ms  | 19.06 ms  | 19.98 ms  | 19.45 ms  | 19.98 ms  | 19.98 ms  |
|                | 8          | 26.20 ms  | 25.93 ms  | 26.45 ms  | 26.26 ms  | 26.12 ms  | 26.12 ms  |
|                | 16         | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    |
|                | 32         |           |           |           |           |           |           |
| Decode (total) | 1          | 122.95 ms | 120.61 ms | 130.07 ms | 122.03 ms | 123.15 ms | 123.15 ms |
|                | 2          | 126.62 ms | 123.78 ms | 132.85 ms | 124.45 ms | 132.85 ms | 132.85 ms |
|                | 4          | 136.14 ms | 133.42 ms | 139.84 ms | 136.18 ms | 139.84 ms | 139.84 ms |
|                | 8          | 183.42 ms | 181.52 ms | 185.18 ms | 183.84 ms | 182.88 ms | 182.88 ms |
|                | 16         | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    |
|                | 32         |           |           |           |           |           |           |


| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 9.40 tokens/secs   | 8.68 tokens/secs   | 9.56 tokens/secs   |
|         | 2          | 11.56 tokens/secs  | 11.20 tokens/secs  | 11.62 tokens/secs  |
|         | 4          | 11.92 tokens/secs  | 11.79 tokens/secs  | 12.02 tokens/secs  |
|         | 8          | 12.08 tokens/secs  | 11.98 tokens/secs  | 12.16 tokens/secs  |
|         | 16         | NaN tokens/secs    | NaN tokens/secs    | NaN tokens/secs    |
|         | 32         |                    |                    |                    |
| Decode  | 1          | 56.96 tokens/secs  | 53.81 tokens/secs  | 58.04 tokens/secs  |
|         | 2          | 110.65 tokens/secs | 105.38 tokens/secs | 113.11 tokens/secs |
|         | 4          | 205.72 tokens/secs | 200.23 tokens/secs | 209.86 tokens/secs |
|         | 8          | 305.31 tokens/secs | 302.41 tokens/secs | 308.50 tokens/secs |
|         | 16         | NaN tokens/secs    | NaN tokens/secs    | NaN tokens/secs    |
|         | 32         |                    |                    |                    |


# Tensor Parallel (TP) - 4 GPUs

| Step           | Batch Size | Average   | Lowest    | Highest   | p50       | p90       | p99       |
|----------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|
| Prefill        | 1          | 84.57 ms  | 82.31 ms  | 92.36 ms  | 83.10 ms  | 92.36 ms  | 92.36 ms  |
|                | 2          | 132.24 ms | 129.82 ms | 138.17 ms | 130.94 ms | 138.17 ms | 138.17 ms |
|                | 4          | 206.05 ms | 204.76 ms | 209.47 ms | 205.69 ms | 209.47 ms | 209.47 ms |
|                | 8          | 400.71 ms | 394.55 ms | 410.64 ms | 399.26 ms | 410.64 ms | 410.64 ms |
|                | 16         | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    |
|                | 32         |           |           |           |           |           |           |
| Decode (token) | 1          | 18.78 ms  | 18.01 ms  | 20.89 ms  | 18.49 ms  | 18.07 ms  | 18.07 ms  |
|                | 2          | 19.29 ms  | 18.13 ms  | 21.31 ms  | 19.11 ms  | 18.13 ms  | 18.13 ms  |
|                | 4          | 18.83 ms  | 17.98 ms  | 20.13 ms  | 19.05 ms  | 19.15 ms  | 19.15 ms  |
|                | 8          | 20.25 ms  | 19.30 ms  | 21.91 ms  | 19.90 ms  | 20.34 ms  | 20.34 ms  |
|                | 16         | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    |
|                | 32         |           |           |           |           |           |           |
| Decode (total) | 1          | 131.43 ms | 126.09 ms | 146.24 ms | 129.40 ms | 126.50 ms | 126.50 ms |
|                | 2          | 135.05 ms | 126.90 ms | 149.15 ms | 133.81 ms | 126.90 ms | 126.90 ms |
|                | 4          | 131.80 ms | 125.86 ms | 140.91 ms | 133.38 ms | 134.05 ms | 134.05 ms |
|                | 8          | 141.78 ms | 135.08 ms | 153.38 ms | 139.32 ms | 142.39 ms | 142.39 ms |
|                | 16         | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    |
|                | 32         |           |           |           |           |           |           |


| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 11.84 tokens/secs  | 10.83 tokens/secs  | 12.15 tokens/secs  |
|         | 2          | 15.13 tokens/secs  | 14.47 tokens/secs  | 15.41 tokens/secs  |
|         | 4          | 19.41 tokens/secs  | 19.10 tokens/secs  | 19.53 tokens/secs  |
|         | 8          | 19.97 tokens/secs  | 19.48 tokens/secs  | 20.28 tokens/secs  |
|         | 16         | NaN tokens/secs    | NaN tokens/secs    | NaN tokens/secs    |
|         | 32         |                    |                    |                    |
| Decode  | 1          | 53.40 tokens/secs  | 47.87 tokens/secs  | 55.52 tokens/secs  |
|         | 2          | 103.85 tokens/secs | 93.86 tokens/secs  | 110.32 tokens/secs |
|         | 4          | 212.78 tokens/secs | 198.71 tokens/secs | 222.48 tokens/secs |
|         | 8          | 395.67 tokens/secs | 365.09 tokens/secs | 414.57 tokens/secs |
|         | 16         | NaN tokens/secs    | NaN tokens/secs    | NaN tokens/secs    |
|         | 32         |                    |                    |                    |

# Tensor Parallel (TP) - 8 GPUs
## Sequence Length 1024

| Step           | Batch Size | Average   | Lowest    | Highest   | p50       | p90       | p99       |
|----------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|
| Prefill        | 1          | 71.72 ms  | 69.06 ms  | 76.86 ms  | 69.93 ms  | 76.86 ms  | 76.86 ms  |
|                | 2          | 106.53 ms | 105.16 ms | 112.60 ms | 105.80 ms | 112.60 ms | 112.60 ms |
|                | 4          | 163.82 ms | 161.22 ms | 170.12 ms | 162.40 ms | 170.12 ms | 170.12 ms |
|                | 8          | 263.44 ms | 259.82 ms | 271.69 ms | 262.85 ms | 271.69 ms | 271.69 ms |
|                | 16         | 857.91 ms | 826.66 ms | 913.01 ms | 855.88 ms | 913.01 ms | 913.01 ms |
|                | 32         | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    |
| Decode (token) | 1          | 19.64 ms  | 18.25 ms  | 22.99 ms  | 19.79 ms  | 19.32 ms  | 19.32 ms  |
|                | 2          | 20.78 ms  | 19.47 ms  | 22.47 ms  | 20.96 ms  | 21.58 ms  | 21.58 ms  |
|                | 4          | 20.42 ms  | 18.57 ms  | 22.62 ms  | 20.71 ms  | 20.28 ms  | 20.28 ms  |
|                | 8          | 19.76 ms  | 19.28 ms  | 20.64 ms  | 19.76 ms  | 20.34 ms  | 20.34 ms  |
|                | 16         | 28.12 ms  | 25.25 ms  | 39.90 ms  | 26.07 ms  | 29.39 ms  | 29.39 ms  |
|                | 32         | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    |
| Decode (total) | 1          | 137.50 ms | 127.78 ms | 160.92 ms | 138.54 ms | 135.26 ms | 135.26 ms |
|                | 2          | 145.44 ms | 136.30 ms | 157.30 ms | 146.70 ms | 151.05 ms | 151.05 ms |
|                | 4          | 142.96 ms | 130.03 ms | 158.33 ms | 144.98 ms | 141.94 ms | 141.94 ms |
|                | 8          | 138.34 ms | 134.99 ms | 144.46 ms | 138.29 ms | 142.42 ms | 142.42 ms |
|                | 16         | 196.84 ms | 176.74 ms | 279.31 ms | 182.48 ms | 205.75 ms | 205.75 ms |
|                | 32         | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    | NaN ms    |


| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 13.97 tokens/secs  | 13.01 tokens/secs  | 14.48 tokens/secs  |
|         | 2          | 18.78 tokens/secs  | 17.76 tokens/secs  | 19.02 tokens/secs  |
|         | 4          | 24.42 tokens/secs  | 23.51 tokens/secs  | 24.81 tokens/secs  |
|         | 8          | 30.37 tokens/secs  | 29.44 tokens/secs  | 30.79 tokens/secs  |
|         | 16         | 18.67 tokens/secs  | 17.52 tokens/secs  | 19.36 tokens/secs  |
|         | 32         | NaN tokens/secs    | NaN tokens/secs    | NaN tokens/secs    |
| Decode  | 1          | 51.12 tokens/secs  | 43.50 tokens/secs  | 54.78 tokens/secs  |
|         | 2          | 96.53 tokens/secs  | 89.00 tokens/secs  | 102.72 tokens/secs |
|         | 4          | 196.37 tokens/secs | 176.85 tokens/secs | 215.34 tokens/secs |
|         | 8          | 404.96 tokens/secs | 387.65 tokens/secs | 414.84 tokens/secs |
|         | 16         | 579.02 tokens/secs | 400.99 tokens/secs | 633.69 tokens/secs |
|         | 32         | NaN tokens/secs    | NaN tokens/secs    | NaN tokens/secs    |

## Sequence Length 100
### No Quantization

| Step           | Batch Size | Average   | Lowest    | Highest   | p50       | p90       | p99       |
|----------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|
| Prefill        | 1          | 22.99 ms  | 21.45 ms  | 34.74 ms  | 21.61 ms  | 34.74 ms  | 34.74 ms  |
|                | 2          | 26.19 ms  | 25.01 ms  | 30.66 ms  | 25.75 ms  | 30.66 ms  | 30.66 ms  |
|                | 4          | 34.17 ms  | 29.29 ms  | 53.63 ms  | 29.93 ms  | 53.63 ms  | 53.63 ms  |
|                | 8          | 40.05 ms  | 36.10 ms  | 54.78 ms  | 38.15 ms  | 54.78 ms  | 54.78 ms  |
|                | 16         | 67.93 ms  | 64.65 ms  | 73.51 ms  | 66.83 ms  | 73.51 ms  | 73.51 ms  |
|                | 32         | 121.51 ms | 119.56 ms | 128.44 ms | 120.66 ms | 128.44 ms | 128.44 ms |
| Decode (token) | 1          | 17.92 ms  | 17.25 ms  | 21.07 ms  | 17.58 ms  | 17.46 ms  | 17.46 ms  |
|                | 2          | 19.52 ms  | 17.70 ms  | 27.51 ms  | 18.74 ms  | 18.68 ms  | 18.68 ms  |
|                | 4          | 19.70 ms  | 18.09 ms  | 23.20 ms  | 18.89 ms  |           |           |
|                | 8          | 21.45 ms  | 19.81 ms  | 27.74 ms  | 20.16 ms  | 20.18 ms  | 20.18 ms  |
|                | 16         | 23.17 ms  | 21.57 ms  | 28.74 ms  | 22.54 ms  | 24.47 ms  | 24.47 ms  |
|                | 32         | 28.28 ms  | 26.31 ms  | 31.72 ms  | 27.50 ms  | 31.72 ms  | 31.72 ms  |
| Decode (total) | 1          | 125.46 ms | 120.73 ms | 147.49 ms | 123.05 ms | 122.21 ms | 122.21 ms |
|                | 2          | 136.61 ms | 123.91 ms | 192.59 ms | 131.16 ms | 130.74 ms | 130.74 ms |
|                | 4          | 137.93 ms | 126.66 ms | 162.38 ms | 132.24 ms | 130.72 ms | 130.72 ms |
|                | 8          | 150.13 ms | 138.66 ms | 194.21 ms | 141.16 ms | 141.29 ms | 141.29 ms |
|                | 16         | 162.19 ms | 150.96 ms | 201.20 ms | 157.78 ms | 171.27 ms | 171.27 ms |
|                | 32         | 197.98 ms | 184.14 ms | 222.06 ms | 192.50 ms | 222.06 ms | 222.06 ms |


| Step    | Batch Size | Average             | Lowest              | Highest             |
|---------|------------|---------------------|---------------------|---------------------|
| Prefill | 1          | 44.38 tokens/secs   | 28.78 tokens/secs   | 46.63 tokens/secs   |
|         | 2          | 76.60 tokens/secs   | 65.22 tokens/secs   | 79.95 tokens/secs   |
|         | 4          | 123.00 tokens/secs  | 74.59 tokens/secs   | 136.55 tokens/secs  |
|         | 8          | 202.81 tokens/secs  | 146.03 tokens/secs  | 221.62 tokens/secs  |
|         | 16         | 236.09 tokens/secs  | 217.66 tokens/secs  | 247.47 tokens/secs  |
|         | 32         | 263.47 tokens/secs  | 249.14 tokens/secs  | 267.64 tokens/secs  |
| Decode  | 1          | 56.00 tokens/secs   | 47.46 tokens/secs   | 57.98 tokens/secs   |
|         | 2          | 103.94 tokens/secs  | 72.69 tokens/secs   | 112.98 tokens/secs  |
|         | 4          | 204.80 tokens/secs  | 172.43 tokens/secs  | 221.07 tokens/secs  |
|         | 8          | 377.74 tokens/secs  | 288.34 tokens/secs  | 403.87 tokens/secs  |
|         | 16         | 695.54 tokens/secs  | 556.65 tokens/secs  | 741.91 tokens/secs  |
|         | 32         | 1135.83 tokens/secs | 1008.71 tokens/secs | 1216.45 tokens/secs |

### Quantization: bitsandbytes

| Step           | Batch Size | Average   | Lowest    | Highest   | p50       | p90       | p99       |
|----------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|
| Prefill        | 1          | 102.67 ms | 99.07 ms  | 113.39 ms | 101.43 ms | 113.39 ms | 113.39 ms |
|                | 2          | 107.96 ms | 102.99 ms | 115.46 ms | 107.14 ms | 115.46 ms | 115.46 ms |
|                | 4          | 111.12 ms | 105.59 ms | 126.41 ms | 110.88 ms | 126.41 ms | 126.41 ms |
|                | 8          | 123.72 ms | 116.41 ms | 136.28 ms | 123.27 ms | 136.28 ms | 136.28 ms |
|                | 16         | 143.63 ms | 140.72 ms | 148.09 ms | 142.87 ms | 148.09 ms | 148.09 ms |
|                | 32         | 203.45 ms | 199.22 ms | 210.47 ms | 203.12 ms | 210.47 ms | 210.47 ms |
| Decode (token) | 1          | 86.81 ms  | 85.96 ms  | 87.49 ms  | 87.04 ms  | 86.93 ms  | 86.93 ms  |
|                | 2          | 87.29 ms  | 86.02 ms  | 88.28 ms  | 87.67 ms  | 87.52 ms  | 87.52 ms  |
|                | 4          | 88.03 ms  | 86.15 ms  | 90.06 ms  | 88.36 ms  | 90.06 ms  | 90.06 ms  |
|                | 8          | 90.85 ms  | 88.91 ms  | 92.31 ms  | 91.40 ms  | 91.87 ms  | 91.87 ms  |
|                | 16         | 93.19 ms  | 90.97 ms  | 97.31 ms  | 93.09 ms  | 93.61 ms  | 93.61 ms  |
|                | 32         | 98.59 ms  | 96.63 ms  | 101.64 ms | 98.60 ms  | 101.64 ms | 101.64 ms |
| Decode (total) | 1          | 607.65 ms | 601.72 ms | 612.41 ms | 609.29 ms | 608.53 ms | 608.53 ms |
|                | 2          | 611.05 ms | 602.15 ms | 617.93 ms | 613.72 ms | 612.63 ms | 612.63 ms |
|                | 4          | 616.25 ms | 603.05 ms | 630.43 ms | 618.49 ms | 630.43 ms | 630.43 ms |
|                | 8          | 635.97 ms | 622.40 ms | 646.17 ms | 639.80 ms | 643.08 ms | 643.08 ms |
|                | 16         | 652.32 ms | 636.78 ms | 681.15 ms | 651.61 ms | 655.27 ms | 655.27 ms |
|                | 32         | 690.12 ms | 676.44 ms | 711.50 ms | 690.21 ms | 711.50 ms | 711.50 ms |


| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 9.75 tokens/secs   | 8.82 tokens/secs   | 10.09 tokens/secs  |
|         | 2          | 18.56 tokens/secs  | 17.32 tokens/secs  | 19.42 tokens/secs  |
|         | 4          | 36.09 tokens/secs  | 31.64 tokens/secs  | 37.88 tokens/secs  |
|         | 8          | 64.79 tokens/secs  | 58.70 tokens/secs  | 68.72 tokens/secs  |
|         | 16         | 111.42 tokens/secs | 108.04 tokens/secs | 113.70 tokens/secs |
|         | 32         | 157.33 tokens/secs | 152.04 tokens/secs | 160.63 tokens/secs |
| Decode  | 1          | 11.52 tokens/secs  | 11.43 tokens/secs  | 11.63 tokens/secs  |
|         | 2          | 22.91 tokens/secs  | 22.66 tokens/secs  | 23.25 tokens/secs  |
|         | 4          | 45.44 tokens/secs  | 44.41 tokens/secs  | 46.43 tokens/secs  |
|         | 8          | 88.07 tokens/secs  | 86.66 tokens/secs  | 89.97 tokens/secs  |
|         | 16         | 171.74 tokens/secs | 164.43 tokens/secs | 175.89 tokens/secs |
|         | 32         | 324.65 tokens/secs | 314.83 tokens/secs | 331.14 tokens/secs |