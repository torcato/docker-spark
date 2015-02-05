#!/usr/bin/env python

import sys
import commands
import argparse

parser = argparse.ArgumentParser(description='stops a spark cluster')
parser.add_argument(  help='spark cluster name', dest='cluster')
parser.add_argument('-v', '--verbose', help='print all commands', action='store_true')
parser.add_argument('-k', '--kill', help='kills dockers', action='store_true')

args = parser.parse_args()

print 'stoping cluster name= %s ' % args.cluster
#print 'number of workers = %d ' % args.workers

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

s, o = commands.getstatusoutput('docker ps -a')
lines = [line.split() for line in o.split('\n')]
containers = [c[0]  for c in lines if c[-1].endswith('.' + args.cluster)]

# will stop all containers now
for c in containers:
    if args.kill:
        print "killing container %s" % c
        __exec('docker kill %s' % c, check=False)
    else:
        print "stopping container %s" % c
        __exec('docker stop %s' % c, check=False)
        
    __exec('docker rm %s' % c, check=False)


