#!/bin/bash

/opt/spark1.6/bin/spark-submit \
    --driver-memory 1G \
    --executor-memory 1G \
    --total-executor-cores 2 \
    --class com.lzz.WordsCount \
    --master spark://elm-local-dev-01:7077 /opt/spark/sparklearn-1.0-SNAPSHOT.jar
