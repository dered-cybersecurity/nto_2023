#!/bin/bash
set -ex

curl --fail http://localhost:3000/
CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/auth)

if [ "${CODE}" = "500" ]; then
    exit 0;
else
    exit 1;
fi
