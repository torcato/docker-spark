FROM ubuntu:14.04
MAINTAINER Cesar Matos <cesar.matos@epfl.ch>

# install a few other useful packages 
RUN apt-get update && apt-get install -y \
    less \
    net-tools \
    vim \
    openssh-server \
    iputils-ping \
    python2.7

#install oracle 8
RUN  wget --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    http://download.oracle.com/otn-pub/java/jdk/8u31-b13/jdk-8u31-linux-x64.tar.gz

RUN tar -xvf jdk-8u31-linux-x64.tar.gz
RUN mkdir /usr/lib/jvm/
RUN mv jdk1.8.0_31 /usr/lib/jvm/oracle_jdk8
RUN rm jdk-8u31-linux-x64.tar.gz

# the 1081 priority number is because the priority number of open jdk 7 is 1071
# with 1081 we will not be replaced as default if something else installs open jdk7 
RUN update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/oracle_jdk8/bin/java" 1081
RUN update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/oracle_jdk8/bin/javac" 1081
RUN update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/lib/jvm/oracle_jdk8/bin/javaws" 1081

#RUN chmod a+x /usr/bin/java
#RUN chmod a+x /usr/bin/javac
#RUN chmod a+x /usr/bin/javaws
#RUN chown -R root:root usr/lib/jvm/oracle_jdk8

ENV  J2SDKDIR /usr/lib/jvm/oracle_jdk8
ENV  J2REDIR /usr/lib/jvm/oracle_jdk8/jre
ENV  PATH $PATH:/usr/lib/jvm/oracle_jdk8/bin:/usr/lib/jvm/oracle_jdk8/db/bin:/usr/lib/jvm/oracle_jdk8/jre/bin
ENV  JAVA_HOME /usr/lib/jvm/oracle_jdk8
ENV  DERBY_HOME /usr/lib/jvm/oracle_jdk8/db


