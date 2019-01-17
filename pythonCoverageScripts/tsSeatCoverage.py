import commands
import os

os.chdir("/app/ts-seat-service")

bc2 = "mvn jacoco:dump -Djacoco.address=ts-seat-service -Djacoco.port=6327"
print(commands.getoutput(bc2))

bc3 = "mvn sonar:sonar -Dsonar.host.url=http://sonar:9000"
print(commands.getoutput(bc3))

