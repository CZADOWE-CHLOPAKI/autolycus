setup-python:
	python3 -m venv env
	set -e
	( \
       source '$(shell pwd)/env/bin/activate'; \
	   pip -V; \
       pip3 install -r requirements.txt; \
    )

setup-front:
	npm install --prefix ./front/

setup:
	make setup-front
	make setup-python

run-python:	
	set -e
	( \
       source '$(shell pwd)/env/bin/activate'; \
	   python src/main.py; \
    )

run-front:
	npm run dev --prefix ./front/

run:
	make run-front
up:
	make run
all:
	make run
dev:
	make run

freeze:
	pip freeze > requirements.txt