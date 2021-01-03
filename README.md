### sjd.im 

All code for my personal website; development, deployment, html/css, and server. Site is available at [sjd.im](https://sjd.im)


### Local Development

The easiest way to do local development is via docker/compose. Also included are instructions for creating a virtual environment with pipenv.

#### Docker
Local development with Docker requires building the container and updating the `docker-compose.yml` file with your local version. Docker compose will mount the site directory and any local changes will be updated in the container. They are available on `localhost:5000`

Build the container:

`docker build ./Dockerfile -t sjd:1.x`

Update docker-compose.yml with your container version & run:

`docker-compose up -d`

#### Pipenv
The easiest way to setup a virtual environment for local development is with Pipenv (If you don't have pipenv, there is also a `requirements.txt` file).
```
cd src
python3 -m pipenv shell
pipenv install
source ../scripts-dev/dev_environ.sh
cd site
flask run
```

### Deployment
See `ansible/README.md` for instructions.

### License
MIT
