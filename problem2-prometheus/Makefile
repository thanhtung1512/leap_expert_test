.PHONY: build run stop clean

build:
	@docker-compose build

run: build
	@docker-compose up -d

stop:
	@docker-compose down

clean: stop
	@docker-compose rm -f
	@docker image prune -af
