
rest url:
http://account-login-service:12345/welcome
return String:
"Welcome to [ Account Login Service ] !"

build:
mvn clean package

docker:
docker build -t my/ts-login-service .
docker run -p 12342:12342 --name ts-login-service my/ts-login-service
docker run -p 12342:12342 --name ts-login-service --link register-mongo:mongo-local --link ts-sso-service:ts-sso-service --link ts-verification-code-service:ts-verification-code-service my/ts-login-service


!!!!!notice: please add following lines into /etc/hosts to simulate the network access:
127.0.0.1	account-login-service

Steps for code coverage (Make sure you are in the ts-login-service directory):

1. mvn clean package
2. docker-compose up -d # Deploy the login service
3. Run the integration tests or manually invoke the service by going to http://localhost:12342/welcome
4. docker exec -it tsloginservice_maven_1 bash # Access the maven container to run mvn commands
5. mvn jacoco:dump -Djacoco.address=app # Dump the jacoco logs so SonarQube will have access.
6. mvn sonar:sonar -Dsonar.host.url=http://sonar:9000 # Run the SonarQube Analysis
7. Go to http://sonar:9000 to see the results of the coverage in SonarQube.





