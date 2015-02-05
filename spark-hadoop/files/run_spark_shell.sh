#!/bin/bash

source /root/spark_files/spark_env.sh

#changes the logging level for the shell 
rm log4j.properties
mv log4j.shell.properties log4j.properties

CMD="/opt/spark/bin/spark-shell --master $master"
echo $CMD
$CMD


