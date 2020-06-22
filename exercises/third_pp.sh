#!/bin/sh

mkdir venvs
python3.6 -m venv venvs/pg
source venvs/pg/bin/activate
pip install psycopg2
