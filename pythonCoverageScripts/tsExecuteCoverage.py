import commands
import os

os.chdir("/app/ts-execute-service")

bc2 = "mvn jacoco:dump -Djacoco.address=ts-execute-service -Djacoco.port=6313"
print(commands.getoutput(bc2))

bc3 = "mvn sonar:sonar -Dsonar.host.url=http://sonar:9000"
print(commands.getoutput(bc3))

