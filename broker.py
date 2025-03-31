from confluent_kafka import Producer, Consumer, KafkaError
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class KafkaClient:
    def __init__(self, brokers=None, group_id=None):
        self.brokers = brokers or os.getenv('KAFKA_BROKERS', 'localhost:9092')
        self.group_id = group_id or os.getenv('KAFKA_GROUP_ID', 'my_group')
        self.producer = Producer({'bootstrap.servers': self.brokers})
        self.consumer = Consumer({
            'bootstrap.servers': self.brokers,
            'group.id': self.group_id,
            'auto.offset.reset': 'earliest'
        })

    def publish(self, topic, key, message):
        """Publish a message to a Kafka topic."""
        def delivery_report(err, msg):
            if err:
                print(f'Message delivery failed: {err}')
            else:
                print(f'Message delivered to {msg.topic()} [{msg.partition()}]')
        
        self.producer.produce(topic, key=key, value=message, callback=delivery_report)
        self.producer.flush()

    def subscribe(self, topic, callback):
        """Subscribe to a Kafka topic and process messages."""
        self.consumer.subscribe([topic])
        print(f"Subscribed to topic: {topic}")

        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        print(f"Consumer error: {msg.error()}")
                        break
                callback(msg.key().decode('utf-8') if msg.key() else None, msg.value().decode('utf-8'))
        except KeyboardInterrupt:
            print("Consumer stopped.")
        finally:
            self.consumer.close()

