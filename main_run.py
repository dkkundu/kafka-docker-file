# Example Usage
if __name__ == "__main__":
    kafka_client = KafkaClient()
    topic_name = "my_topic"
    
    # Publish a message
    kafka_client.publish(topic_name, key="msg1", message="Hello, Kafka!")
    
    # Consume messages
    def process_message(key, value):
        print(f"Received: Key={key}, Value={value}")
    
    kafka_client.subscribe(topic_name, process_message)
