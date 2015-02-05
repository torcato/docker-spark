#!/bin/bash

source /root/spark_files/spark_env.sh

/opt/spark/sbin/start-master.sh

while [ 1 ];
do
	tail -f /opt/spark/logs/*.out
        sleep 1
done
