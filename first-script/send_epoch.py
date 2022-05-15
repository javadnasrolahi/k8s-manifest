from time import sleep
import time
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['kafka:9094'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
print('connected')

j = 0 
while True:
    print("Iteration", j)
    data = {'epoch-time': time.time()}
    producer.send('input', value=data)
    j += 1
    sleep(1)