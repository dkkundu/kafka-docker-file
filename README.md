# kafka-docker-file
Install Kafka and Zookeeper using Docker Compose by setting up a docker-compose.yml

## Steps to Start Kafka & Zookeeper

1️⃣ **Start Kafka & Zookeeper**  
Run the following command:
```sh
docker-compose up -d
```

2️⃣ **Verify Installation**  
Check if the containers are running:
```sh
docker ps
```

3️⃣ **Test Kafka**  
To create a test topic, run:
```sh
docker exec -it kafka kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

To list topics:
```sh
docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092
```

## Additional Setup

To ensure unnecessary files are not tracked by Git, add the following to your `.gitignore` file:

# Ignore Python virtual environments
venv/

# Ignore Python cache files
__pycache__/

Now, Kafka and Zookeeper are running in Docker! 🚀
