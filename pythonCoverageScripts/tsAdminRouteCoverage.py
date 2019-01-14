import commands
import os

os.chdir("/app/ts-admin-route-service")

bc2 = "mvn jacoco:dump -Djacoco.address=ts-admin-route-service -Djacoco.port=6303"
print(commands.getoutput(bc2))

bc3 = "mvn sonar:sonar -Dsonar.host.url=http://sonar:9000"
print(commands.getoutput(bc3))

