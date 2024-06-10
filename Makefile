SHELL := /bin/bash
.ONESHELL:
.PHONY: lint format test
.SILENT: lint format test
.NOTPARALLEL: lint format test

####################################################################################################

lint: fix := false
lint:
	[ -s .venv/bin/activate ] && source .venv/bin/activate
ifeq ($(fix), true)
	ruff check --fix
else
	ruff check
endif

####################################################################################################

format:
	[ -s .venv/bin/activate ] && source .venv/bin/activate
	ruff format

####################################################################################################

unittest: file := ./test/
unittest:
	[ -s .venv/bin/activate ] && source .venv/bin/activate
	python -m pytest ${file}
