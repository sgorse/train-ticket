import commands
import os

os.chdir("/app/ts-payment-service")

bc2 = "mvn jacoco:dump -Djacoco.address=ts-payment-service -Djacoco.port=6320"
print(commands.getoutput(bc2))

bc3 = "mvn sonar:sonar -Dsonar.host.url=http://sonar:9000"
print(commands.getoutput(bc3))

