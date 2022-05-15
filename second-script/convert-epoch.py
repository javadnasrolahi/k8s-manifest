from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import loads
from time import sleep
from json import dumps
import datetime

consumer = KafkaConsumer(
    'input',
    bootstrap_servers=['kafka:9094'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=['kafka:9094'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
print('connected')

for event in consumer:
    event_data = event.value
    # Do whatever you want
    print(event_data)
    data = {'iso-time': datetime.datetime.fromtimestamp(event_data['epoch-time']).isoformat()}
    print(data)
    producer.send('output', value=data)
    print("#################")
    