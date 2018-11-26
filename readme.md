## Currencies scrapper
This application allows to scrap currencies exchange rates against EUR from European Central Bank RSS.
Data is stored in Postgres database and accessible via REST API. 

Rates are scrapped on application start and every day on 14:17 (2 minutes after official release).
#### Technology stack:
Postgres, Nginx, Redis, Celery, Django
#### Time sheet:
1. 20:30-21:30
2. 23:00-00:45
#### TODO:
* add filtering by dates and currencies
* add reporting errors via email
* add backoff if new results are not present @14:17 CET
### Start project
####Prerequisites:

1. Install docker  https://docs.docker.com/install
2. Pull repository
3. Navigate to folder with repository
4. `make up` to build the project and start containers.
5. Browse the api on http://127.0.0.1:8000

### More commands
2. `make build` to build the project.
3. `make start` to start containers if project has been up already.
4. `make stop` to stop containers.
5. `make shell-web` to shell access web container.
6. `make shell-db` to shell access db container.
7. `make shell-nginx` to shell access nginx container.
8. `make logs-web` to log access web container.
9. `make logs-db` to log access db container.
10. `make logs-nginx` to log access nginx container.
11. `make collectstatic` to put static files in static directory.
12. `make log-web` to log access web container.
13. `make log-db` to log access db container.
14. `make log-nginx` to log access nginx container.
14. `make restart` to restart containers.
