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

run-cli:	
	set -e
	( \
       source '$(shell pwd)/env/bin/activate'; \
	   python src/cli.py; \
    )

run-front:
	npm run dev --prefix ./front/

run-back:
	uvicorn src.main:app --reload


run:
	#  -j [N], --jobs[=N] Allow N jobs at once; infinite jobs with no arg.
	make -j 2 run-front run-back 

up:
	make run
all:
	make run
dev:
	make run

freeze:
	pip freeze > requirements.txt

clean:
	rm -rf ./images/*
