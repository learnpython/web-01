.PHONY: bootstrap clean distclean server test

ENV ?= env

PROJECT = .
HOST ?= 0.0.0.0
PORT ?= 8080
TEST_ARGS ?=

bootstrap:
	bootstrapper -e $(ENV)

clean:
	find . -name "*.pyc" -delete

distclean: clean
	rm -rf $(ENV)/

server:
	PYTHONPATH=.:.. $(ENV)/bin/gunicorn -b $(HOST):$(PORT) -w 4 main:app

test:
	PYTHONPATH=.:.. $(ENV)/bin/coverage run --branch -m unittest discover $(TEST_ARGS) -s $(PROJECT)/
	PYTHONPATH=.:.. $(ENV)/bin/coverage report -m --omit=$(PROJECT)/*.py
