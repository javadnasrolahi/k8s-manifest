from time import sleep
import time
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(
    bootstrap_servers=['kafka-service:9094'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
print('connected')
for j in range(9999):
    print("Iteration", j)
    data = {'epoch-time': time.time()}
    producer.send('input', value=data)
    sleep(1)