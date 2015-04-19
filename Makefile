build:
	docker-compose build

up:
	docker-compose up -d

log:
	docker-compose logs

syncdb:
	docker-compose run web python manage.py syncdb

collectstatic:
	docker-compose run web python manage.py collectstatic

test:
	docker-compose run web python manage.py test

bash:
	docker-compose run web /bin/bash

mysqlshell:
	docker-compose run web mysql -uroot -p -hdb

shell:
	docker-compose run web python manage.py shell

stop:
	docker-compose stop
