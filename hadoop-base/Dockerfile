FROM diasepfl/jdk-base
MAINTAINER Cesar Matos <cesar.matos@epfl.ch>

# Setup a volume for data
VOLUME ["/data"]

# install hadoop
ENV HADOOP_VERSION 2.6.0
ENV HADOOP_INSTALL /opt/hadoop

ADD http://mirror.switch.ch/mirror/apache/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz /
RUN tar -xvf hadoop-$HADOOP_VERSION.tar.gz
RUN mv hadoop-$HADOOP_VERSION $HADOOP_INSTALL
RUN rm hadoop-$HADOOP_VERSION.tar.gz

ENV PATH $PATH:$HADOOP_INSTALL/bin
ENV PATH $PATH:$HADOOP_INSTALL/sbin
ENV HADOOP_MAPRED_HOME $HADOOP_INSTALL
ENV HADOOP_COMMON_HOME $HADOOP_INSTALL
ENV HADOOP_HDFS_HOME $HADOOP_INSTALL
ENV YARN_HOME $HADOOP_INSTALL
ENV HADOOP_COMMON_LIB_NATIVE_DIR $HADOOP_INSTALL/lib/native
ENV HADOOP_OPTS "-Djava.library.path=$HADOOP_INSTALL/lib"

