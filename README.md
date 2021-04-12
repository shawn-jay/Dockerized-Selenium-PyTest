# Selenium PyTest running on Dockerized Jenkins that is executing tests on BrowserStack
Purpose of this project is to be able to run Selenium  automation pytests using Command Line values within a dockerized Jenkins. 

A dockerized Jenkins will look at this project. It will pull the workspace into the Jenkins container, and then execute the Dockerfile found within this repostory. The repository will then report back a result.xml file of py.tests that were ran on it within the Jenkins container.

You will also see the results of the tests on BrowserStack. The tests are ran on Firefox, Safari and Chrome
