#!/bin/bash
master="master.$1"
worker="$2.$1"
dns="dns.$1"
dns_dir="/tmp/dns_$1"
dns_file="$dns_dir/hosts.txt"

dns_ip=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' $dns)

docker rm $worker

cmd="docker run -ti \
    --hostname $worker \
    --name $worker \
    --volume=$PWD/data:/data \
    --volume=$dns_dir:/dns
    --dns $dns_ip \
    -e SPARK_MASTER_IP=$master \
    -e SPARK_MASTER_PORT=7077 \
    diasepfl/spark-only ./run_bash.sh"

echo $cmd
$cmd
