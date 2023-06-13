# No sharding
# bigscience/mt0-xxl-mt
benchmark-mt0-xxl-mt-s100-d100:
	text-generation-benchmark --tokenizer-name bigscience/mt0-xxl-mt --sequence-length 100 --decode-length 100

benchmark-mt0-xxl-mt-s200-d200:
	text-generation-benchmark --tokenizer-name bigscience/mt0-xxl-mt --sequence-length 200 --decode-length 200

benchmark-mt0-xxl-mt-s300-d300:
	text-generation-benchmark --tokenizer-name bigscience/mt0-xxl-mt --sequence-length 300 --decode-length 300

benchmark-mt0-xxl-mt-s400-d400:
	text-generation-benchmark --tokenizer-name bigscience/mt0-xxl-mt --sequence-length 400 --decode-length 400

benchmark-mt0-xxl-mt-s500-d500:
	text-generation-benchmark --tokenizer-name bigscience/mt0-xxl-mt --sequence-length 500 --decode-length 500

benchmark-mt0-xxl-mt-s500-d1000-bs16:
	text-generation-benchmark --tokenizer-name bigscience/mt0-xxl-mt --sequence-length 500 --decode-length 1000 --batch-size 16
# Sharding
# bigscience/bloomz-1b1
benchmark-bloomz-1b1-s100-d100:
	text-generation-benchmark --tokenizer-name bigscience/bloomz-1b1 --sequence-length 100 --decode-length 100

benchmark-bloomz-1b1-s500-d500:
	text-generation-benchmark --tokenizer-name bigscience/bloomz-1b1 --sequence-length 500 --decode-length 500

benchmark-bloomz-1b1-s500-d500-bs32:
	text-generation-benchmark --tokenizer-name bigscience/bloomz-1b1 --sequence-length 500 --decode-length 500 --batch-size 32