PROJECT = $(shell basename $(CURDIR))
DC = docker compose
DCR = ${DC} run --rm --no-deps ${PROJECT}
DAY = 2022/$(shell printf '%02d' $(day))
CURRENTFILE = ${DAY}/code.py

.PHONY: init
init: destroy build shell ## Setup project with python resources

.PHONY: destroy
destroy: ## Delete the previous setup
	${DC} down --remove-orphans --rmi local

.PHONY: build
build: ## Build the project
	${DC} build ${PROJECT}

.PHONY: up
up: ## Start the service
	${DC} up -d

.PHONY: shell
shell: ##- Run a bash shell
	${DCR} bash

.PHONY: run
run: ## Run the project
	${DCR} python ${CURRENTFILE}

.PHONY: in
in: ## Fetches a day's inputs
	curl 'https://adventofcode.com/2022/day/${day}/input' -H "cookie: session=${AOCTOKEN}" > ${DAY}/input.txt
