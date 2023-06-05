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
| Prefill        | 1          | 141.97 ms  | 141.41 ms  | 143.99 ms  | 141.65 ms  | 143.99 ms  | 143.99 ms  |
|                | 2          | 274.07 ms  | 273.46 ms  | 275.13 ms  | 273.84 ms  | 275.13 ms  | 275.13 ms  |
|                | 4          | 519.51 ms  | 518.06 ms  | 520.97 ms  | 519.91 ms  | 520.97 ms  | 520.97 ms  |
|                | 8          | 978.26 ms  | 952.53 ms  | 996.25 ms  | 979.46 ms  | 996.25 ms  | 996.25 ms  |
|                | 16         | 2111.44 ms | 2079.28 ms | 2195.45 ms | 2099.73 ms | 2195.45 ms | 2195.45 ms |
|                | 32         | 3951.55 ms | 3912.70 ms | 4007.31 ms | 3951.40 ms | 4007.31 ms | 4007.31 ms |
| Decode (token) | 1          | 29.11 ms   | 29.04 ms   | 29.27 ms   | 29.11 ms   | 29.27 ms   | 29.27 ms   |
|                | 2          | 35.91 ms   | 35.85 ms   | 35.99 ms   | 35.89 ms   | 35.99 ms   | 35.99 ms   |
|                | 4          | 49.60 ms   | 49.53 ms   | 49.70 ms   | 49.58 ms   | 49.70 ms   | 49.70 ms   |
|                | 8          | 73.30 ms   | 72.18 ms   | 74.44 ms   | 73.15 ms   | 74.44 ms   | 74.44 ms   |
|                | 16         | 127.93 ms  | 127.48 ms  | 128.53 ms  | 127.95 ms  | 128.53 ms  | 128.53 ms  |
|                | 32         | 244.77 ms  | 244.21 ms  | 245.78 ms  | 244.72 ms  | 245.78 ms  | 245.78 ms  |
| Decode (total) | 1          | 203.79 ms  | 203.29 ms  | 204.93 ms  | 203.80 ms  | 204.93 ms  | 204.93 ms  |
|                | 2          | 251.38 ms  | 250.97 ms  | 251.93 ms  | 251.23 ms  | 251.93 ms  | 251.93 ms  |
|                | 4          | 347.19 ms  | 346.73 ms  | 347.89 ms  | 347.08 ms  | 347.89 ms  | 347.89 ms  |
|                | 8          | 513.07 ms  | 505.29 ms  | 521.10 ms  | 512.02 ms  | 521.10 ms  | 521.10 ms  |
|                | 16         | 895.54 ms  | 892.39 ms  | 899.72 ms  | 895.63 ms  | 899.72 ms  | 899.72 ms  |
|                | 32         | 1713.37 ms | 1709.50 ms | 1720.45 ms | 1713.01 ms | 1720.45 ms | 1720.45 ms |

| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 7.04 tokens/secs   | 6.94 tokens/secs   | 7.07 tokens/secs   |
|         | 2          | 7.30 tokens/secs   | 7.27 tokens/secs   | 7.31 tokens/secs   |
|         | 4          | 7.70 tokens/secs   | 7.68 tokens/secs   | 7.72 tokens/secs   |
|         | 8          | 8.18 tokens/secs   | 8.03 tokens/secs   | 8.40 tokens/secs   |
|         | 16         | 7.58 tokens/secs   | 7.29 tokens/secs   | 7.69 tokens/secs   |
|         | 32         | 8.10 tokens/secs   | 7.99 tokens/secs   | 8.18 tokens/secs   |
| Decode  | 1          | 34.35 tokens/secs  | 34.16 tokens/secs  | 34.43 tokens/secs  |
|         | 2          | 55.69 tokens/secs  | 55.57 tokens/secs  | 55.78 tokens/secs  |
|         | 4          | 80.65 tokens/secs  | 80.49 tokens/secs  | 80.75 tokens/secs  |
|         | 8          | 109.16 tokens/secs | 107.46 tokens/secs | 110.83 tokens/secs |
|         | 16         | 125.06 tokens/secs | 124.48 tokens/secs | 125.51 tokens/secs |
|         | 32         | 130.74 tokens/secs | 130.20 tokens/secs | 131.03 tokens/secs |
