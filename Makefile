setup-python:
	python3 -m venv env
	set -e
	( \
       source '$(shell pwd)/env/bin/activate'; \
	   pip -V; \
       pip3 install -r requirements.txt; \
    )

setup-front:
	cd front
	npm install

setup:
	setup-front
	setup-python

run-python:	
	set -e
	( \
       source '$(shell pwd)/env/bin/activate'; \
	   python src/main.py; \
    )

run-front:
	cd front 
	npm run dev
	cd -

run:
	run-front
up:
	run
all:
	run
dev:
	run

freeze:
	pip freeze > requirements.txt