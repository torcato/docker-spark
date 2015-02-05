#!/bin/bash

#this line returns the current ip address of the machine
export SPARK_LOCAL_IP=$(ifconfig | awk -F':' '/inet addr/&&!/127.0.0.1/{split($2,_," ");print _[1]}')

echo "SPARK_LOCAL_IP=$SPARK_LOCAL_IP"
echo "SPARK_MASTER_IP=$SPARK_MASTER_IP"
echo "SPARK_MASTER_PORT= $SPARK_MASTER_PORT"
echo "SPARK_MASTER_WEBUI_PORT=$SPARK_MASTER_WEBUI"

export master="spark://$SPARK_MASTER_IP:$SPARK_MASTER_PORT"
#writes some settings to the spark conf
echo "spark.master              $master"            >> /opt/spark/conf/spark-defaults.conf
#echo "spark.eventLog.enabled    false"              >> /opt/spark/conf/spark-defaults.conf

# this makes the spark driver to use IP instead of the hostname (might not be necessary with DNS)
echo "spark.driver.host         $SPARK_LOCAL_IP"   >> /opt/spark/conf/spark-defaults.conf
echo "adding to hosts file $SPARK_LOCAL_IP   $(hostname -f)"
echo "$SPARK_LOCAL_IP   $(hostname -f)" >> /dns/hosts.txt



