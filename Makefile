run:
	docker run \
		-it \
		--mount type=bind,source="${shell pwd}"/src,target=/app \
		e719a12253cf

build:
	docker build --tag=nlp-test .
