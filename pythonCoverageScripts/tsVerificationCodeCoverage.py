import commands
import os

os.chdir("/app/ts-verification-code-service")

bc2 = "mvn jacoco:dump -Djacoco.address=ts-verification-code-service -Djacoco.port=6336"
print(commands.getoutput(bc2))

bc3 = "mvn sonar:sonar -Dsonar.host.url=http://sonar:9000"
print(commands.getoutput(bc3))

