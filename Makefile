setup-db:
	docker exec -it autolycus_al-db_1 mongo --eval "db.createUser({user: 'root', pwd: 'root', roles: [{ role: 'userAdminAnyDatabase', db: 'admin' } ]})"

run-cli:	
	set -e
	( \
       source '$(shell pwd)/env/bin/activate'; \
	   export PYTHONPATH=./; \
	   python pkg/cli.py; \
    )


setup:
	chmod +x add_hosts.sh
	sudo ./add_hosts.sh

run:
	docker compose up -d
	cd front && yarn dev
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
