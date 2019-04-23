run:
	docker run \
		-it \
		--mount type=bind,source="${shell pwd}"/src,target=/app \
		--rm \
		nlp-test

build:
	docker build --tag=nlp-test .
