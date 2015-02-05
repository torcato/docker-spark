# Dockerfiles and scripts for Spark

## Contents

Docker images and scripts for running a several Spark workers in a single machine for testing.

## The sub-folders
   * dns : Contains a docker image for a DNS server to use in the cluster. You can register a new host in the DNS by adding a entry in the "hosts.txt"  file in the share volume "/dns"
   * jdk-base: Base docker image with djk8 from oracle installed. Used by the Hadoop and Spark images
   * spark-only: Docker image for spark without hadoop (scala version 2.10.3, spark version 1.2.0)
   * hadoop-base: Base docker image with Hadoop, used by spark-hadoop image (hadoop version 2.6.0)
   * spark-hadoop: Docker image with spark compiled to be used with hadoop (scala version 2.10.3, spark version 1.2.0)
   * bin : Folder with scripts to start and stop the cluster
## Usage

Clone the repository 
  $git clone https://github.com/torcato/docker-spark.git
  
### Build the images

Go to the folder where you cloned the repository.
The images have dependencies between them, so issue the following commands in the same order to build all the images.

  $sudo docker build -t rawlabs/dns ./dns
  $sudo docker build -t rawlabs/jdk-base ./jdk-base
  $sudo docker build -t rawlabs/hadoop-base
  $sudo docker build -t rawlabs/spark-hadoop spark-hadoop
  $sudo docker build -t rawlabs/spark-only ./spark-only

The spark-only builds Spark from the source code, it takes quite a long time downloading dependencies and building, so just be patient.

### Running an small cluster

To start a small cluster use type 
  $bin/start_cluster.py spark
This will start 4 docker images:
dns.spark : DNS server for the cluster
master.spark: Spark master node
and 2 worker nodes (default): worker0.spark and worker1.spark

to start a cluster with 10 worker nodes type:
  $bin/start_cluster.py -n 10 spark

warning: If your current user is not part of the docker group, you will have to run the scripts with sudo.

To start a spark shell using the just created cluster type :
  $bin/spark_shell spark

To stop the cluster type:
  $bin/stop_cluster.py spark
  
# Using the data volume

All the docker containers share a volume /data with the host container so that you can work with files.
By default it will try to link a ./data folder in your current folder, use the -d option to specify another path for the shared folder ammong containers.

 

