from kafka import KafkaConsumer
import json
from .models import BuyCar, Person, Car

consumer = KafkaConsumer(
    'buy_car_topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def consume_messages():
    for message in consumer:
        buy_car_data = json.loads(message.value.decode('utf-8'))
        person = Person.objects.get(id=buy_car_data['person'])
        car = Car.objects.get(id=buy_car_data['car'])
        BuyCar.objects.create(person=person, car=car, message=buy_car_data['message'])
