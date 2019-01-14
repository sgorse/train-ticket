import commands
import os

os.chdir("/app/ts-admin-order-service")

bc2 = "mvn jacoco:dump -Djacoco.address=ts-admin-order-service -Djacoco.port=6302"
print(commands.getoutput(bc2))

bc3 = "mvn sonar:sonar -Dsonar.host.url=http://sonar:9000"
print(commands.getoutput(bc3))

