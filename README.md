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
  $ git clone https://github.com/torcato/docker-spark.git
  
### Build the images

Go to the folder where you cloned the repository.
The images have dependencies between them, so issue the following commands in the same order to build all the images.

  $ sudo docker build -t rawlabs/dns ./dns
  $ sudo docker build -t rawlabs/jdk-base ./jdk-base
  $ sudo docker build -t rawlabs/hadoop-base
  $ sudo docker build -t rawlabs/spark-hadoop spark-hadoop
  $ sudo docker build -t rawlabs/spark-only ./spark-only

The spark-only builds Spark from the source code, it takes quite a long time downloading dependencies and building, so just be patient.

### Running an small cluster

To start a small cluster use type 
  $ bin/start_cluster.py test
This will start 4 docker images:
   * dns.test : DNS server for the cluster
   * master.test: Spark master node
   * and 2 worker nodes (default): worker0.test and worker1.test

To start a cluster with a different number of workers use the -n , --workers option, example for 10 workers:
  $ bin/start_cluster.py -n 10 test

   * If your current user is not part of the docker group, you will have to run the scripts with sudo.

   * The script uses the --name option in docker so if you cannot restart a spark cluster with the same name without stopping and deleting the old docker images. Use the -f, --force option to force to bypass this.

### Running applications on the cluster

To start a spark shell using the just created cluster type :
  $ bin/spark_shell.sh test

Optionally if you want to use another Spark app, you can use the script bin/worker_bash to get a bash shell in a image registered in the cluster. Example:

$ bin/worker_bash.sh test app

this will start a bash shell in a new docker container "app.test" already registered in the DNS of the cluster and with the Spark environment variables defined so that you can use other spark clients.
For instance to run a spark python shell in this container you can type:
/opt/spark/bin/pyspark


### Working with files

All the docker containers share a volume /data with the host container so that you can work with files.
By default it will try to link a ./data folder in your current folder, use the -d, --data option to specify another path for the shared folder ammong containers.
$ bin/start_cluster.py --data path/to/data test

### Stopping the cluster 

To stop the "test" cluster type:

  $ bin/stop_cluster.py test
