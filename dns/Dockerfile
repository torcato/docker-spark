FROM ubuntu:14.04
MAINTAINER Cesar Matos <cesar.matos@epfl.ch>

VOLUME [ "/dns" ]

RUN apt-get install -y \
	dnsmasq-base \
	vim

ADD files /root/dnsmasq_files

WORKDIR /root/dnsmasq_files
CMD ["/root/dnsmasq_files/run_dns.sh"]
