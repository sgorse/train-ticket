import commands
import os

os.chdir("/app/ts-travel2-service")

bc2 = "mvn jacoco:dump -Djacoco.address=ts-travel2-service -Djacoco.port=6335"
print(commands.getoutput(bc2))

bc3 = "mvn sonar:sonar -Dsonar.host.url=http://sonar:9000"
print(commands.getoutput(bc3))

