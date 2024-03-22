#!/usr/bin/env bash

make env
. ./venv/bin/activate

if [[ -z "$1" ]]; then
  echo "Syntax: $0 labname"
  ./data.py
  exit 1
fi

LINKS=""
for project in $( ./data.py $1 ); do
  echo
  echo "*** Checking project $1/$project"
  LINKS="$LINKS http://localhost:8080/showcase/$project/technical"
done

linkchecker -f linkcheckerrc $LINKS
