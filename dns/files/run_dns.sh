#!/bin/bash

IP=$(ifconfig | awk -F':' '/inet addr/&&!/127.0.0.1/{split($2,_," ");print _[1]}')
echo "NAMESERVER_IP=$IP"

echo "user=root" > /etc/dnsmasq.conf
#echo "listen-address=$IP" >> /etc/dnsmasq.conf
#echo "domain=$CLUSTER"  >> /etc/dnsmasq.conf
echo "nameserver 8.8.8.8" >> /etc/resolv.dnsmasq.conf
echo "addn-hosts=/dns/hosts.txt"  >> /etc/dnsmasq.conf

file=/dns/hosts.txt

echo "$IP   $(hostname -f)" > $file

dnsmasq

while [ 1 ];
do
    #checks if the hosts file changed and restarts the dns server 
    old=$(stat -c "%Y" $file)
    sleep 1
    current=$(stat -c "%Y" $file)
    if [ "$old" != "$current" ]; then
        echo "File changed restarting DNS"
        pkill dnsmasq
        dnsmasq
    fi
done
