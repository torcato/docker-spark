#!/bin/bash

source /root/spark_files/spark_env.sh

CMD="/opt/spark/bin/spark-class org.apache.spark.deploy.worker.Worker -h $SPARK_LOCAL_IP $master"
echo $CMD
$CMD

