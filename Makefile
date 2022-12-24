PROJECT = $(shell basename $(CURDIR))
DC = docker compose
YEAR ?= $(shell date +%Y)
DAY ?= $(shell date +%e | xargs)
DCR = ${DC} run --rm --no-deps ${PROJECT}
workdir = aoc/${YEAR}/$(shell printf '%02d' $(DAY))

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
	${DCR} python ${workdir}/code.py

.PHONY: in
in: ## Fetches a day's inputs
	curl 'https://adventofcode.com/${YEAR}/day/${DAY}/input' -H "cookie: session=${AOCTOKEN}" > ${workdir}/input.txt
	cat ${workdir}/input.txt

.PHONY: day
day: ## Create a new day
	mkdir -p ${workdir}
	cp -n template/* ${workdir}/
	git add .

.PHONY: what
what: ## What day is it?
	@echo ${workdir}
