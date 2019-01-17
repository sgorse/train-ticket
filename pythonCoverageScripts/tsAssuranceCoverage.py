import commands
import os

os.chdir("/app/ts-assurance-service")

bc2 = "mvn jacoco:dump -Djacoco.address=ts-assurance-service -Djacoco.port=6306"
print(commands.getoutput(bc2))

bc3 = "mvn sonar:sonar -Dsonar.host.url=http://sonar:9000"
print(commands.getoutput(bc3))

