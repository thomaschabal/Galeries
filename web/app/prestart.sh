#! /usr/bin/env bash

# Let the DB start
service redis-server start
sleep 10;
# Run migrations
# export FLASK_APP=ponthe
flask db upgrade
