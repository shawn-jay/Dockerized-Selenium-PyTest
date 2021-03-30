FROM selenium/standalone-chrome
MAINTAINER shawn.s.jafari@gmail.com
COPY . /SeleniumFramework
WORKDIR /SeleniumFramework
RUN pip3 install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "tests/home/login_tests.py", "--browser chrome", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null