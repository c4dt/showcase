#!/usr/bin/env bash

make env
. ./venv/bin/activate

if [[ -z "$1" ]]; then
  echo "Syntax: $0 labname"
  ./data.py
  exit 1
fi

for project in $( ./data.py $1 ); do
  echo
  echo "*** Checking project $1/$project"
  linkchecker -f linkcheckerrc http://localhost:8080/showcase/$project/technical
done
