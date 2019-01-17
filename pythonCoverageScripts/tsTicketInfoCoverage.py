import commands
import os

os.chdir("/app/ts-ticketinfo-service")

bc2 = "mvn jacoco:dump -Djacoco.address=ts-ticketinfo-service -Djacoco.port=6331"
print(commands.getoutput(bc2))

bc3 = "mvn sonar:sonar -Dsonar.host.url=http://sonar:9000"
print(commands.getoutput(bc3))

