#!/bin/bash

#while ! nc -z $(echo $POSTGRES_HOST) 5432; do sleep 3; done
#echo "Postgres started"
#while ! nc -z $(echo $REDIS_HOST) 6379; do sleep 3; done
#echo "Redis started"
#while ! nc -z $(echo $NEO4J_HOST) 7687; do sleep 3; done
#echo "Neo4j started"

#node index.js
npm start --host 0.0.0.0
