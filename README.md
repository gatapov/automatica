# Automatica test

Automatica test local deploy

## Requirements

Python 3.8+

PostgreSQL

## Getting started
Create database

```
sudo -u postgres psql
CREATE DATABASE db_name;
CREATE USER db_user WITH password 'db_password';
GRANT ALL ON DATABASE db_name TO db_user;
\q

```
Create virtualenv
```
mkdir automatica
cd automatica
python3 -m venv env
. ./env/bin/activate
```

Init project:
```
git clone https://github.com/gatapov/automatica.git
cd automatica
pip3 install -r requirements.txt
```

Create .env file

```
cp .env.sample .env
```
Edit .env file

```
DEBUG= for enable debug 1 or 0 to disable debug
SECRET_KEY=secret key

DATABASE_NAME=db name
DATABASE_USER=db user
DATABASE_PASSWORD=db user password
DATABASE_HOST=localhost
DATABASE_PORT=5432

```

Run migrations
```
./manage.py migrate
```

Create superuser
```
./manage.py createsuperuser
```

Run server
```
./manage.py runserver
```