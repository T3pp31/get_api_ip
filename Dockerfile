FROM python:3.11
USER root

RUN apt-get update
RUN apt-get -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN apt-get install -y vim less
RUN apt-get install git

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN mkdir -p /root/src
RUN apt-get install --reinstall ca-certificates
RUN git clone https://github.com/T3pp31/get_api_ip.git
WORKDIR /root/src/get_api_ip

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install requests beautifulsoup4 pytest
