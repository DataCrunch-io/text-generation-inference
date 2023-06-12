install-server:
	cd server && make install

install-integration-tests:
	cd integration-tests && pip install -r requirements.txt

install-router:
	cd router && cargo install --path .

install-launcher:
	cd launcher && cargo install --path .

install-benchmark:
	cd benchmark && cargo install --path .

install: install-server install-router install-launcher

server-dev:
	cd server && make run-dev

router-dev:
	cd router && cargo run -- --port 8080

rust-tests: install-router install-launcher
	cargo test

integration-tests: install-integration-tests
	pytest -s -vv -m "not private" integration-tests

update-integration-tests: install-integration-tests
	pytest -s -vv --snapshot-update integration-tests

python-server-tests:
	HF_HUB_ENABLE_HF_TRANSFER=1 pytest -s -vv -m "not private" server/tests

python-client-tests:
	pytest clients/python/tests

python-tests: python-server-tests python-client-tests

run-bloom-560m:
	text-generation-launcher --model-id bigscience/bloom-560m --num-shard 2 --port 8080

run-bloom-560m-quantize:
	text-generation-launcher --model-id bigscience/bloom-560m --num-shard 2 --quantize --port 8080

download-bloom:
	HF_HUB_ENABLE_HF_TRANSFER=1 text-generation-server download-weights bigscience/bloom

run-bloom:
	text-generation-launcher --model-id bigscience/bloom --num-shard 8 --port 8080

run-bloom-quantize:
	text-generation-launcher --model-id bigscience/bloom --num-shard 8 --quantize --port 8080

download-bloomz-7b1-mt:
	HF_HUB_ENABLE_HF_TRANSFER=1 text-generation-server download-weights bigscience/bloomz-7b1-mt

run-bloomz-7b1-mt:
	text-generation-launcher --model-id bigscience/bloomz-7b1-mt --num-shard 8 --port 8080

run-bloomz-7b1-mt-quantize:
	text-generation-launcher --model-id bigscience/bloomz-7b1-mt --num-shard 8 --quantize bitsandbytes --port 8080

run-bloomz-7b1-mt-disable-custom-kernels:
	text-generation-launcher --model-id bigscience/bloomz-7b1-mt --num-shard 8 --disable-custom-kernels --port 8080

run-bloomz-7b1-mt-cuda-visible-devices:
	CUDA_VISIBLE_DEVICES=0 text-generation-launcher --model-id bigscience/bloomz-7b1-mt --port 5555

download-mt0-xxl-mt:
	HF_HUB_ENABLE_HF_TRANSFER=1 text-generation-server download-weights bigscience/mt0-xxl-mt

run-mt0-xxl-mt:
	CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 text-generation-launcher --model-id bigscience/mt0-xxl-mt --sharded false --port 5555

download-mt0-xl:
	HF_HUB_ENABLE_HF_TRANSFER=1 text-generation-server download-weights bigscience/mt0-xl

run-mt0-xl:
	CUDA_VISIBLE_DEVICES=0,1 text-generation-launcher --model-id bigscience/mt0-xl --sharded false --port 5555