import json
import time
import random
from datetime import datetime, timezone
from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers="<server-url>:<port>",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

TOPIC = "clickstream"

pages = ["/home", "/products", "/cart", "/checkout", "/search"]
actions = ["click", "view", "scroll"]
devices = ["mobile", "desktop"]
browsers = ["chrome", "firefox", "safari"]
countries = ["IN", "US", "DE", "UK"]


def generate_event():
    return {
        "user_id": random.randint(1000, 9999),
        "session_id": random.randint(100000, 999999),
        "page": random.choice(pages),
        "action": random.choice(actions),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "device": random.choice(devices),
        "browser": random.choice(browsers),
        "country": random.choice(countries),
    }


while True:
    event = generate_event()
    producer.send(TOPIC, value=event)
    #print(json.dumps(event, indent=2))  
    print(event)
    time.sleep(1)
