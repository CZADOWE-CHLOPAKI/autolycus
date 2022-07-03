setup-db:
	docker exec -it autolycus_al-db_1 mongo --eval "use admin; db.createUser({user: 'root', pwd: 'root', roles: [{ role: 'root', db: 'admin' } ]})"

run-cli:	
	set -e
	( \
       source '$(shell pwd)/env/bin/activate'; \
	   export PYTHONPATH=./; \
	   python pkg/cli.py; \
    )

run-front:
	cd front && npm run dev

run:
	docker compose up -d
	make run-front

up:
	make run
all:
	make run
dev:
	make run

logs_back:
	docker logs autolycus_back_1 -f

restart_back:
	docker restart autolycus_back_1

enter_back:
	docker exec -u root -it autolycus_back_1 bash

rebuild:
	docker-compose up -d --build

restart:
	docker-compose restart

freeze:
	pip freeze > requirements.txt

clean:
	rm -rf ./images
	rm -rf ./output
