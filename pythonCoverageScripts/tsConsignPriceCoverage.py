import commands
import os

os.chdir("/app/ts-consign-price-service")

bc2 = "mvn jacoco:dump -Djacoco.address=ts-consign-price-service -Djacoco.port=6310"
print(commands.getoutput(bc2))

bc3 = "mvn sonar:sonar -Dsonar.host.url=http://sonar:9000"
print(commands.getoutput(bc3))

