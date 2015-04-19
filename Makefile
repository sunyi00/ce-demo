build:
	docker-compose build

up:
	docker-compose up -d

log:
	docker-compose logs

syncdb:
	docker-compose run --rm web python manage.py syncdb

collectstatic:
	docker-compose run --rm web python manage.py collectstatic

bash:
	docker-compose run --rm web /bin/bash

mysqlshell:
	docker-compose run --rm web mysql -uroot -p -hdb

shell:
	docker-compose run --rm web python manage.py shell

stop:
	docker-compose stop

pylint:
	pylint 

test: mkresultdir
	docker-compose run --rm web py.test --junit-xml=unitTestResults/result.xml

test-cov: mkresultdir
	- rm -f .coverage
	docker-compose run --rm web py.test --junit-xml=unitTestResults/result.xml --cov-report=term --cov=schedules --cov=apps --cov=deploys

mkresultdir:
	- mkdir -p unitTestResults

migrate:
	docker-compose run --rm web python manage.py makemigrations
	docker-compose run --rm web python manage.py migrate
