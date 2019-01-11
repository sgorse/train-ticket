FROM java:8-jre

# Install maven NOT WORKING PROPERLY
RUN echo 'deb http://http.debian.net/debian jessie-backports main' > /etc/apt/sources.list.d/jessie-backports.list
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get clean
RUN apt-get update
RUN apt-get install net-tools
#RUN apt-get -y install maven
#

ADD ./target/ts-login-service-1.0.jar /app/
CMD ["java", "-Xmx200m", "-jar", "/app/ts-login-service-1.0.jar"]