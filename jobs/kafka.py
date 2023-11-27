from kafka import KafkaConsumer, KafkaProducer

# For a consumer
consumer = KafkaConsumer(
    'your_topic',
    bootstrap_servers='pkc-6ojv2.us-west4.gcp.confluent.cloud:9092',
    security_protocol='SASL_SSL',
    sasl_mechanism='PLAIN',
    sasl_plain_username='PB7BC75THZS7NAIZ',
    sasl_plain_password='your_password',  # Use the password you reset to
    session_timeout_ms=45000
)

# For a producer
producer = KafkaProducer(
    bootstrap_servers='pkc-6ojv2.us-west4.gcp.confluent.cloud:9092',
    security_protocol='SASL_SSL',
    sasl_mechanism='PLAIN',
    sasl_plain_username='PB7BC75THZS7NAIZ',
    sasl_plain_password='your_password',  # Use the password you reset to
)

# Remember to handle your resources properly
# e.g., consumer.close(), producer.close()
