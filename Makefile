setup-db:
	docker exec -it autolycus_al-db_1 mongo --eval "use admin; db.createUser({user: 'root', pwd: 'root', roles: [{ role: 'root', db: 'admin' } ]})"

run-cli:	
	set -e
	( \
       source '$(shell pwd)/env/bin/activate'; \
	   export PYTHONPATH=./; \
	   python pkg/cli.py; \
    )

run-back:
	set -e
	( \
       source '$(shell pwd)/env/bin/activate'; \
	   export PYTHONPATH=./; \
	   python api/main.py; \
    )

run-front:
	cd front && npm run dev

setup:
	chmod +x add_hosts.sh
	sudo ./add_hosts.sh

run:
	docker compose up -d
	make -j 2 run-front run-back
	# docker compose up -d
	# python -m webbrowser "http://0.0.0.0:5000/docs"
	# python -m webbrowser "http://0.0.0.0:3000/"
	# python -m webbrowser "http://0.0.0.0:27017/"



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
