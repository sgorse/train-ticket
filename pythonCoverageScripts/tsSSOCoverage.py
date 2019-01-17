import commands
import os

os.chdir("/app/ts-sso-service")

bc2 = "mvn jacoco:dump -Djacoco.address=ts-sso-service -Djacoco.port=6329"
print(commands.getoutput(bc2))

bc3 = "mvn sonar:sonar -Dsonar.host.url=http://sonar:9000"
print(commands.getoutput(bc3))

