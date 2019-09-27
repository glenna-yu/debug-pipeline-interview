
up: build run

build:
	docker build -t enigma.gluo/debug-pipeline-interview:0.0.1 .

build-no-cache:
	docker build --no-cache -i -t enigma.gluo/debug-pipeline-interview:0.0.1 .

run:
	docker run --rm -d -p 8080:8080 --name="debug-pipeline-interview" enigma.gluo/debug-pipeline-interview:0.0.1

stop:
	docker stop debug-pipeline-interview

ssh:
	docker exec -it debug-pipeline-interview /bin/bash

logs:
	docker logs -f debug-pipeline-interview

clean:
	docker image rm enigma.gluo/debug-pipeline-interview:0.0.1
