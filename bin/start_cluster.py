#!/usr/bin/env python

import sys
import commands
import os
import argparse
from random import randint

from time import sleep

parser = argparse.ArgumentParser(description='deploys a spark cluster using docker')
parser.add_argument(  help='spark cluster name', dest='cluster')
parser.add_argument('-i', '--image', help='docker image to use',default ='rawlabs/spark-only')
parser.add_argument('-n', '--workers', help='number of workers ', default = 2, type=int)
parser.add_argument('-d', '--data', help='shared data directory ', default='data', required=False)
parser.add_argument('-f', '--force', help='forces the deletion of old instances', action='store_true')
parser.add_argument('-v', '--verbose', help='print all commands', action='store_true')
parser.add_argument('-p', '--master_port', help=' spark master port to use', default = 7077, type=int)
parser.add_argument('-w', '--web_port', help='spark master web ui port', default = 8080, type=int)


args = parser.parse_args()
#always uses the absolute path
args.data = os.path.abspath(args.data)

print 'starting spark cluster name= %s ' % args.cluster
print 'image used = %s' %args.image
print 'number of workers = %d ' % args.workers

print "master port = %d, web ui port =%d" %(args.master_port, args.web_port)
print 'force = %s , verbose = %s' % \
    ('True' if args.force else 'False', 'True' if args.verbose else 'False')

def __exec(cmd, check=True):
    s, o = commands.getstatusoutput(cmd)
    if args.verbose:
        print cmd
    if s != 0 and check:
        print 'ERROR!!!'
        print cmd
        print s
        print o
        sys.exit(1)
    return o

# starts a dns server 
#THis is where the hosts file will be located
dnsdir="/tmp/dns_" + args.cluster
dns = "dns." + args.cluster

if args.force:
    print "stopping and deleting old DNS"
    __exec('docker stop %s' % dns, check=False)
    __exec('docker rm %s' % dns, check=False)

# I name the host, the image and pass a env. variable with the name of the spark master name
cmd =  "docker run -d \\\n"
cmd += "\t--hostname %s \\\n" % dns
cmd += "\t--name  %s \\\n" % dns
cmd += "\t--volume=%s:/dns \\\n" % dnsdir
cmd += "\t-e CLUSTER=%s \\\n" % args.cluster
cmd += "\trawlabs/dns" 
__exec(cmd)

#command to get the ip address of the dns server 
dns_ip =__exec("docker inspect --format '{{ .NetworkSettings.IPAddress }}' %s" %dns)
print "%s started, ip = %s" % (dns, dns_ip)

#Start the master
master= "master."+args.cluster
if args.force:
    print "stopping and deleting old master"
    __exec('docker stop %s' % master, check=False)
    __exec('docker rm %s' % master, check=False)

print "starting master node %s.master" % args.cluster
#name the host, the image and pass a env. variable with the name of the spark master name
cmd =  "docker run -d \\\n"
cmd += "\t--hostname %s \\\n" %master
cmd += "\t--name  %s \\\n" % master
cmd += "\t--dns %s \\\n" % dns_ip
cmd += "\t--volume=%s:/data \\\n" % args.data
cmd += "\t--volume=%s:/dns \\\n" % dnsdir
cmd += "\t-e 'SPARK_MASTER_IP=%s' \\\n" % master
cmd += "\t-e 'SPARK_MASTER_PORT=%d' \\\n" %args.master_port
cmd += "\t-e 'SPARK_MASTER_WEBUI_PORT=%d' \\\n" %args.web_port
cmd += "\t-p %d:%d \\\n" % ( args.web_port, args.web_port )
cmd += "\t-p %d:%d \\\n" %( args.master_port, args.master_port)
cmd += "\t%s ./run_spark_master.sh" % args.image
__exec(cmd)

#command to get the ip address of the master 
master_ip =__exec("docker inspect --format '{{ .NetworkSettings.IPAddress }}' %s" %master)
print "%s started, ip = %s" % (master, master_ip)

#TODO: find a better way to do this
sleep(0.1)

#Start all the workers now
for w in range(args.workers):
    worker = "worker%d.%s" % ( w, args.cluster)
    if args.force:
        print "stopping and deleting old worker #%d" % w
        __exec('docker stop %s' % worker, check=False)
        __exec('docker rm %s' % worker, check=False)
        
    print "starting worker %d" % w
    cmd = "docker run -d \\\n"
    cmd += "\t--hostname %s \\\n" % worker
    cmd += "\t--name %s \\\n" % worker
    cmd += "\t--dns %s \\\n" % dns_ip
    cmd += "\t--volume=%s:/data \\\n" % args.data
    cmd += "\t--volume=%s:/dns \\\n" % dnsdir
    cmd += "\t--link=%s:%s \\\n" % (master,master)
    cmd += "\t-e 'SPARK_MASTER_IP=%s' \\\n" % master
    cmd += "\t-e 'SPARK_MASTER_PORT=%d' \\\n" % args.master_port
    cmd += "\t%s ./run_spark_slave.sh " % args.image

    __exec(cmd)
    worker_ip =__exec("docker inspect --format '{{ .NetworkSettings.IPAddress }}' %s" %worker)
    print "%s started, ip = %s" % (worker, worker_ip) 

