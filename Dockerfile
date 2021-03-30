FROM python:3.8-slim-buster
MAINTAINER shawn.s.jafari@gmail.com
COPY . /SeleniumFramework
WORKDIR /SeleniumFramework
RUN pip3 install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null