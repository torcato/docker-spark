#!/bin/bash

master="master.$1"
dns="dns.$1"
dns_dir="/tmp/dns_$1"
dns_file="$dns_dir/hosts.txt"

dns_ip=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' $dns)


echo starting master node spark.master
cmd="docker run -ti \
    --hostname $master \
    --name  $master \
    --volume=$PWD/data:/data \
    --volume=$dns_dir:/dns \
    --link=$dns:$dns \
    --dns $dns_ip \
    -e SPARK_MASTER_IP=$master \
    -e SPARK_MASTER_PORT=7077 \
    -e SPARK_MASTER_WEBUI_PORT=8080 \
    -p 8080:8080 \
    -p 7077:7077 \
    rawlabs/spark-only /bin/bash"
echo $cmd
$cmd
