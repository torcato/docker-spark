#!/bin/bash

sudo docker build -t diasepfl/dns ./dns
sudo docker build -t diasepfl/jdk-base ./jdk-base
sudo docker build -t diasepfl/hadoop-base
sudo docker build -t diasepfl/spark-hadoop spark-hadoop
sudo docker build -t diasepfl/spark-only ./spark-only
