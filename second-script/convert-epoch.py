from kafka import KafkaConsumer
import time

bootstrap_servers = ['kafka-service:9094']

while True:
    try:
        consumer = KafkaConsumer('input',
                                bootstrap_servers = bootstrap_servers,
                                auto_offset_reset='earliest',
                                enable_auto_commit=False,
                                #metadata_max_age_ms = 2000
                                )
        break
    except : 
        print("conver epoch : Kafka isn't available")
        time.sleep(3)
        
        
for message in consumer:
    print (f"recived from kafka: {message.value}")

consumer.close()