setup-back:
	docker-compose up -d

	#wait and then run it or run after docker compose???
	docker exec -it autolycus_al-db_1 mongo --eval "db.createUser({user: 'root', pwd: 'root', roles: [{ role: 'userAdminAnyDatabase', db: 'admin' } ]})"

setup-front:
	npm install --prefix ./front/

setup:
	make -j 2  setup-front setup-back

run-cli:	
	set -e
	( \
       source '$(shell pwd)/env/bin/activate'; \
	   export PYTHONPATH=./; \
	   python pkg/cli.py; \
    )

run-front:
	npm run dev --prefix ./front/

run-back:
	docker run -p 5000:5000 al-back



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
