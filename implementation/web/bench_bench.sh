#!/bin/sh

export PIPENV_PIPFILE=../mockdown/Pipfile
LOGLEVEL=INFO timeout 120 pipenv run -- mockdown run -pb 178.75 1652.1 180 1652.1 -pm hierarchical --learning-method noisetolerant -dn 0 tmp.json response.json