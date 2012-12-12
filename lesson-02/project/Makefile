.PHONY: bootstrap clean distclean server test

ENV ?= env
PYTHON = $(ENV)/bin/python

PROJECT = project
HOST ?= 0.0.0.0
PORT ?= 8080
TEST_ARGS ?=

bootstrap:
	bootstrapper -e $(ENV) -C 'cp -n $(PROJECT)/settings_local.py{{.def,}}'

clean:
	find . -name "*.pyc" -delete

distclean: clean
	rm -rf $(ENV)/ $(PROJECT)/settings_local.py

server:
	$(ENV)/bin/gunicorn -b $(HOST):$(PORT) -w 4 $(PROJECT).main:app

test:
	$(ENV)/bin/coverage run --branch -m unittest discover $(TEST_ARGS) -s $(PROJECT)/
	$(ENV)/bin/coverage report -m --include=$(PROJECT)/*.py --omit=$(PROJECT)/tests.py
