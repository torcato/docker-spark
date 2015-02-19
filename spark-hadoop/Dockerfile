FROM diasepfl/hadoop-base
MAINTAINER Cesar Matos <cesar.matos@epfl.ch>

# Install Scala + spark
ENV SCALA_VERSION 2.10.3
ENV SPARK_VERSION 1.2.0
ENV SCALA_HOME /opt/scala

ENV SPARK_HOME /opt/spark
ENV PATH $SPARK_HOME:$SCALA_HOME/bin:$PATH 

#spark worker settings for testing purposes only
ENV SPARK_WORKER_CORES 1
#SPARK_MEM is deprecated
#ENV SPARK_MEM 800m
ENV SPARK_WORKER_MEMORY 1500m
ENV SPARK_MASTER_MEM 1500m
ENV SPARK_LOCAL_DIR /tmp/spark

ADD http://www.scala-lang.org/files/archive/scala-$SCALA_VERSION.tgz /
RUN tar -xvf scala-$SCALA_VERSION.tgz
RUN mv scala-$SCALA_VERSION $SCALA_HOME
RUN rm /scala-$SCALA_VERSION.tgz

ADD http://mirror.switch.ch/mirror/apache/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop2.4.tgz /

RUN tar -xvf spark-$SPARK_VERSION-bin-hadoop2.4.tgz
RUN mv spark-$SPARK_VERSION-bin-hadoop2.4 $SPARK_HOME
RUN rm spark-$SPARK_VERSION-bin-hadoop2.4.tgz

VOLUME ["/dns"]

ADD files /root/spark_files
WORKDIR /root/spark_files

EXPOSE 7077 8080

