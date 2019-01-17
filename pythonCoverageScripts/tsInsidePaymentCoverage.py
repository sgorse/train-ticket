import commands
import os

os.chdir("/app/ts-inside-payment-service")

bc2 = "mvn jacoco:dump -Djacoco.address=ts-inside-payment-service -Djacoco.port=6316"
print(commands.getoutput(bc2))

bc3 = "mvn sonar:sonar -Dsonar.host.url=http://sonar:9000"
print(commands.getoutput(bc3))

