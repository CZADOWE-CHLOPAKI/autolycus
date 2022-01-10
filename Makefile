setup:
	pip install -r requirements.txt
freeze:
	pip freeze > requirements.txt
run:
	@python src/main.py