from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_car_buy_message(buy_car_data):
    producer.send('buy_car_topic', buy_car_data)
    producer.flush()
