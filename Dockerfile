FROM python:3.8

MAINTAINER shawn.s.jafari@gmail.com
COPY . /SeleniumFramework
WORKDIR /SeleniumFramework

# install google chrome
#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
#https://askubuntu.com/questions/198014/install-google-chrome-ubuntu-12-04-without-sudo
#RUN apt-get -y update
#RUN apt-get install -y curl
#RUN apt-get install -y google-chrome-stable

# install chromedriver
#RUN apt-get install -yqq unzip
#RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
#RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN pip3 install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "tests/home/login_tests.py", "--browser=Safari", "--junitxml=reports/result.xml", "--sec $BrowserStack"]
RUN ["pytest", "-v", "tests/home/login_tests.py", "--browser=Chrome", "--junitxml=reports/result.xml", "--sec $BrowserStack"]
RUN ["pytest", "-v", "tests/home/products_tests.py", "--browser=Firefox", "--junitxml=reports/result.xml", "--sec $BrowserStack"]
CMD tail -f /dev/null