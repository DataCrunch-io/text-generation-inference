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

# Num Shards: 2
## Tensor Parallel (TP) - 2 GPUs
| Step           | Batch Size | Average    | Lowest     | Highest    | p50        | p90        | p99        |
|----------------|------------|------------|------------|------------|------------|------------|------------|
| Prefill        | 1          | 18.84 ms   | 18.40 ms   | 20.29 ms   | 18.88 ms   | 20.29 ms   | 20.29 ms   |
|                | 2          | 23.19 ms   | 21.72 ms   | 26.02 ms   | 22.93 ms   | 26.02 ms   | 26.02 ms   |
|                | 4          | 30.95 ms   | 28.86 ms   | 39.44 ms   | 30.48 ms   | 39.44 ms   | 39.44 ms   |
|                | 8          | 44.27 ms   | 41.97 ms   | 47.09 ms   | 44.39 ms   | 47.09 ms   | 47.09 ms   |
|                | 16         | 72.33 ms   | 70.41 ms   | 79.20 ms   | 71.57 ms   | 79.20 ms   | 79.20 ms   |
|                | 32         | 133.38 ms  | 130.65 ms  | 135.62 ms  | 133.62 ms  | 135.62 ms  | 135.62 ms  |
| Decode (token) | 1          | 14.29 ms   | 14.13 ms   | 14.45 ms   | 14.30 ms   | 14.33 ms   | 14.33 ms   |
|                | 2          | 14.87 ms   | 14.60 ms   | 15.08 ms   | 14.92 ms   | 14.87 ms   | 14.87 ms   |
|                | 4          | 15.42 ms   | 15.26 ms   | 15.68 ms   | 15.50 ms   | 15.33 ms   | 15.33 ms   |
|                | 8          | 16.52 ms   | 16.35 ms   | 16.88 ms   | 16.53 ms   | 16.35 ms   | 16.35 ms   |
|                | 16         | 18.86 ms   | 18.64 ms   | 19.10 ms   | 18.96 ms   | 18.68 ms   | 18.68 ms   |
|                | 32         | 24.00 ms   | 23.76 ms   | 24.13 ms   | 24.07 ms   | 24.13 ms   | 24.13 ms   |
| Decode (total) | 1          | 1414.51 ms | 1398.69 ms | 1430.28 ms | 1415.73 ms | 1418.34 ms | 1418.34 ms |
|                | 2          | 1472.34 ms | 1445.01 ms | 1492.61 ms | 1477.20 ms | 1471.70 ms | 1471.70 ms |
|                | 4          | 1526.89 ms | 1510.39 ms | 1552.28 ms | 1534.96 ms | 1517.83 ms | 1517.83 ms |
|                | 8          | 1635.83 ms | 1618.50 ms | 1671.57 ms | 1636.14 ms | 1618.50 ms | 1618.50 ms |
|                | 16         | 1867.19 ms | 1845.93 ms | 1890.86 ms | 1876.79 ms | 1849.76 ms | 1849.76 ms |
|                | 32         | 2376.47 ms | 2352.04 ms | 2389.06 ms | 2382.52 ms | 2389.06 ms | 2389.06 ms |


| Step    | Batch Size | Average             | Lowest              | Highest             |
|---------|------------|---------------------|---------------------|---------------------|
| Prefill | 1          | 53.11 tokens/secs   | 49.29 tokens/secs   | 54.35 tokens/secs   |
|         | 2          | 86.59 tokens/secs   | 76.87 tokens/secs   | 92.09 tokens/secs   |
|         | 4          | 130.23 tokens/secs  | 101.43 tokens/secs  | 138.61 tokens/secs  |
|         | 8          | 180.87 tokens/secs  | 169.89 tokens/secs  | 190.60 tokens/secs  |
|         | 16         | 221.45 tokens/secs  | 202.03 tokens/secs  | 227.24 tokens/secs  |
|         | 32         | 239.95 tokens/secs  | 235.95 tokens/secs  | 244.94 tokens/secs  |
| Decode  | 1          | 69.99 tokens/secs   | 69.22 tokens/secs   | 70.78 tokens/secs   |
|         | 2          | 134.49 tokens/secs  | 132.65 tokens/secs  | 137.02 tokens/secs  |
|         | 4          | 259.37 tokens/secs  | 255.11 tokens/secs  | 262.18 tokens/secs  |
|         | 8          | 484.20 tokens/secs  | 473.81 tokens/secs  | 489.34 tokens/secs  |
|         | 16         | 848.38 tokens/secs  | 837.71 tokens/secs  | 858.10 tokens/secs  |
|         | 32         | 1333.11 tokens/secs | 1326.05 tokens/secs | 1346.91 tokens/secs |

# Num Shards: 4
## Tensor Parallel (TP) - 4 GPUs
| Step           | Batch Size | Average    | Lowest     | Highest    | p50        | p90        | p99        |
|----------------|------------|------------|------------|------------|------------|------------|------------|
| Prefill        | 1          | 19.16 ms   | 18.53 ms   | 20.18 ms   | 19.04 ms   | 20.18 ms   | 20.18 ms   |
|                | 2          | 23.13 ms   | 21.38 ms   | 31.60 ms   | 22.28 ms   | 31.60 ms   | 31.60 ms   |
|                | 4          | 26.49 ms   | 24.93 ms   | 31.86 ms   | 26.24 ms   | 31.86 ms   | 31.86 ms   |
|                | 8          | 40.07 ms   | 34.83 ms   | 61.21 ms   | 37.86 ms   | 61.21 ms   | 61.21 ms   |
|                | 16         | 56.17 ms   | 53.36 ms   | 65.34 ms   | 55.42 ms   | 65.34 ms   | 65.34 ms   |
|                | 32         | 98.74 ms   | 97.55 ms   | 100.23 ms  | 98.93 ms   | 100.23 ms  | 100.23 ms  |
| Decode (token) | 1          | 14.77 ms   | 14.49 ms   | 15.05 ms   | 14.96 ms   | 14.57 ms   | 14.57 ms   |
|                | 2          | 15.50 ms   | 15.20 ms   | 16.02 ms   | 15.57 ms   | 15.29 ms   | 15.29 ms   |
|                | 4          | 16.14 ms   | 15.55 ms   | 16.39 ms   | 16.26 ms   | 16.31 ms   | 16.31 ms   |
|                | 8          | 17.46 ms   | 17.10 ms   | 17.92 ms   | 17.65 ms   | 17.19 ms   | 17.19 ms   |
|                | 16         | 19.70 ms   | 19.41 ms   | 19.99 ms   | 19.79 ms   | 19.63 ms   | 19.63 ms   |
|                | 32         | 24.51 ms   | 24.32 ms   | 24.82 ms   | 24.52 ms   | 24.82 ms   | 24.82 ms   |
| Decode (total) | 1          | 1462.74 ms | 1434.70 ms | 1490.02 ms | 1480.83 ms | 1442.20 ms | 1442.20 ms |
|                | 2          | 1534.14 ms | 1505.21 ms | 1585.68 ms | 1541.67 ms | 1513.29 ms | 1513.29 ms |
|                | 4          | 1598.09 ms | 1539.33 ms | 1622.25 ms | 1609.65 ms | 1614.98 ms | 1614.98 ms |
|                | 8          | 1728.13 ms | 1692.83 ms | 1773.77 ms | 1747.04 ms | 1701.88 ms | 1701.88 ms |
|                | 16         | 1950.71 ms | 1921.21 ms | 1978.82 ms | 1959.30 ms | 1943.52 ms | 1943.52 ms |
|                | 32         | 2426.79 ms | 2407.90 ms | 2457.12 ms | 2427.89 ms | 2457.12 ms | 2457.12 ms |


| Step    | Batch Size | Average             | Lowest              | Highest             |
|---------|------------|---------------------|---------------------|---------------------|
| Prefill | 1          | 52.21 tokens/secs   | 49.55 tokens/secs   | 53.96 tokens/secs   |
|         | 2          | 87.49 tokens/secs   | 63.29 tokens/secs   | 93.55 tokens/secs   |
|         | 4          | 151.62 tokens/secs  | 125.54 tokens/secs  | 160.42 tokens/secs  |
|         | 8          | 205.75 tokens/secs  | 130.69 tokens/secs  | 229.66 tokens/secs  |
|         | 16         | 285.75 tokens/secs  | 244.88 tokens/secs  | 299.83 tokens/secs  |
|         | 32         | 324.10 tokens/secs  | 319.27 tokens/secs  | 328.05 tokens/secs  |
| Decode  | 1          | 67.69 tokens/secs   | 66.44 tokens/secs   | 69.00 tokens/secs   |
|         | 2          | 129.10 tokens/secs  | 124.87 tokens/secs  | 131.54 tokens/secs  |
|         | 4          | 247.86 tokens/secs  | 244.11 tokens/secs  | 257.25 tokens/secs  |
|         | 8          | 458.40 tokens/secs  | 446.51 tokens/secs  | 467.86 tokens/secs  |
|         | 16         | 812.08 tokens/secs  | 800.48 tokens/secs  | 824.48 tokens/secs  |
|         | 32         | 1305.48 tokens/secs | 1289.31 tokens/secs | 1315.67 tokens/secs |

# Num Shards: 8
## Tensor Parallel (TP) - 8 GPUs
| Step           | Batch Size | Average    | Lowest     | Highest    | p50        | p90        | p99        |
|----------------|------------|------------|------------|------------|------------|------------|------------|
| Prefill        | 1          | 19.30 ms   | 18.83 ms   | 19.65 ms   | 19.43 ms   | 19.65 ms   | 19.65 ms   |
|                | 2          | 25.56 ms   | 22.98 ms   | 31.81 ms   | 23.74 ms   | 31.81 ms   | 31.81 ms   |
|                | 4          | 29.45 ms   | 26.45 ms   | 36.12 ms   | 28.90 ms   | 36.12 ms   | 36.12 ms   |
|                | 8          | 40.40 ms   | 32.40 ms   | 55.63 ms   | 41.76 ms   | 55.63 ms   | 55.63 ms   |
|                | 16         | 54.80 ms   | 48.98 ms   | 65.22 ms   | 53.11 ms   | 65.22 ms   | 65.22 ms   |
|                | 32         | 87.36 ms   | 82.07 ms   | 99.15 ms   | 86.82 ms   | 99.15 ms   | 99.15 ms   |
| Decode (token) | 1          | 14.99 ms   | 14.53 ms   | 15.62 ms   | 15.09 ms   | 15.62 ms   | 15.62 ms   |
|                | 2          | 15.92 ms   | 15.35 ms   | 16.34 ms   | 16.12 ms   | 16.18 ms   | 16.18 ms   |
|                | 4          | 17.55 ms   | 16.88 ms   | 18.27 ms   | 17.67 ms   | 17.92 ms   | 17.92 ms   |
|                | 8          | 18.59 ms   | 18.28 ms   | 18.95 ms   | 18.75 ms   | 18.39 ms   | 18.39 ms   |
|                | 16         | 20.45 ms   | 20.11 ms   | 20.94 ms   | 20.44 ms   | 20.57 ms   | 20.57 ms   |
|                | 32         | 25.22 ms   | 24.77 ms   | 25.61 ms   | 25.27 ms   | 25.61 ms   | 25.61 ms   |
| Decode (total) | 1          | 1483.82 ms | 1438.27 ms | 1546.79 ms | 1493.65 ms | 1546.79 ms | 1546.79 ms |
|                | 2          | 1575.81 ms | 1519.66 ms | 1617.81 ms | 1596.46 ms | 1601.97 ms | 1601.97 ms |
|                | 4          | 1737.88 ms | 1671.17 ms | 1808.26 ms | 1749.00 ms | 1773.96 ms | 1773.96 ms |
|                | 8          | 1840.78 ms | 1810.00 ms | 1876.01 ms | 1856.02 ms | 1820.60 ms | 1820.60 ms |
|                | 16         | 2024.64 ms | 1991.46 ms | 2072.72 ms | 2023.75 ms | 2036.90 ms | 2036.90 ms |
|                | 32         | 2497.21 ms | 2452.78 ms | 2535.83 ms | 2501.39 ms | 2535.83 ms | 2535.83 ms |


| Step    | Batch Size | Average             | Lowest              | Highest             |
|---------|------------|---------------------|---------------------|---------------------|
| Prefill | 1          | 51.83 tokens/secs   | 50.88 tokens/secs   | 53.10 tokens/secs   |
|         | 2          | 79.28 tokens/secs   | 62.87 tokens/secs   | 87.01 tokens/secs   |
|         | 4          | 136.81 tokens/secs  | 110.73 tokens/secs  | 151.25 tokens/secs  |
|         | 8          | 203.63 tokens/secs  | 143.81 tokens/secs  | 246.94 tokens/secs  |
|         | 16         | 294.58 tokens/secs  | 245.31 tokens/secs  | 326.68 tokens/secs  |
|         | 32         | 367.44 tokens/secs  | 322.75 tokens/secs  | 389.92 tokens/secs  |
| Decode  | 1          | 66.76 tokens/secs   | 64.00 tokens/secs   | 68.83 tokens/secs   |
|         | 2          | 125.72 tokens/secs  | 122.39 tokens/secs  | 130.29 tokens/secs  |
|         | 4          | 228.00 tokens/secs  | 219.00 tokens/secs  | 236.96 tokens/secs  |
|         | 8          | 430.32 tokens/secs  | 422.17 tokens/secs  | 437.57 tokens/secs  |
|         | 16         | 782.46 tokens/secs  | 764.21 tokens/secs  | 795.40 tokens/secs  |
|         | 32         | 1268.76 tokens/secs | 1249.30 tokens/secs | 1291.59 tokens/secs |

