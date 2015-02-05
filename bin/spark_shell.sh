#!/bin/bash

master="master.$1"
port=$2
image=rawlabs/spark-only
shell="shell.$1"

if [ "$master" == "" ]; then
    echo "spark master name not defined" 
    echo "usage:"
    echo "$0 master_name [port]"
    exit 1
fi

if [ "$port" == "" ]; then
    port=7077
    echo "using default port 7077"
fi

echo "master = $master , port = $port"

#!/bin/bash
master="master.$1"
dns="dns.$1"
dns_dir="/tmp/dns_$1"

dns_ip=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' $dns)


cmd="docker run -ti \
    --volume=$PWD/data:/data \
    --volume=$dns_dir:/dns
    --dns $dns_ip \
    -e SPARK_MASTER_IP=$master \
    -e SPARK_MASTER_PORT=7077 \
     $image ./run_spark_shell.sh "

echo $cmd
$cmd
