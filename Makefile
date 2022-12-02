PROJECT = $(shell basename $(CURDIR))
DC = docker compose
DCR = ${DC} run --rm --no-deps ${PROJECT}

CURRENTFILE = 2022/${day}/code.py

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
	${DC} up

.PHONY: shell
shell: ##- Run a bash shell
	${DCR} bash

.PHONY: run
run: ## Run the project
	${DCR} python ${CURRENTFILE}
