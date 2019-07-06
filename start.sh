#!/usr/bin/env bash

cd app
python3 build_database.py
service nginx start
uwsgi --ini ../uwsgi.ini