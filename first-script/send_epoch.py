from kafka import KafkaProducer
from requests import get
import time 

bootstrap_servers = ['kafka-service:9094']
topicName = 'input'
while True:
    try:
        producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
                                request_timeout_ms = 1000
                                )
        print("connected")
        break
    except: 
        print("send epoch : Kafka isn't available")
        time.sleep(3)
        

while True: 
    print("send epoch timestamp to kafka")
    print(f"time = time.time()")
    producer.send(topicName, str(time.time()).encode())
    producer.flush()
    print('done')
    time.sleep(1)