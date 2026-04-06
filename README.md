# Real-Time Clickstream Analytics using Aiven Kafka and OpenSearch

## Overview

This project demonstrates how to build a real-time data pipeline using Aiven services to monitor and analyze website activity.

The solution simulates clickstream events, streams them through Aiven Kafka, and visualizes insights using OpenSearch Dashboards.

---

## Architecture

<img width="2184" height="936" alt="image" src="https://github.com/user-attachments/assets/3a16f721-15fa-46e1-8665-862c284f8208" />


---

## Use Case

This solution can be used to:

- Monitor website activity in real time  
- Analyze user behavior  
- Identify popular pages and traffic trends  

---

## Technologies Used

- Aiven for Apache Kafka  
- Aiven for OpenSearch  
- Kafka Connect (OpenSearch Sink Connector)  
- Python (kafka-python, faker)

---

## Implementation

### Kafka Topic Setup

Create a topic named `clickstream` in your Aiven Kafka service.

You can create the topic using:

- Aiven Console → Topics → Create Topic  
- OR via CLI/API  


### Step 1: Clickstream Data Generation

A Python script (`producer.py`) generates simulated clickstream events and publishes them to Kafka.

Each event contains:

- `user_id`  
- `page`  
- `action`  
- `timestamp` (ISO 8601 format)  
- `device`  
- `country`  

Ensure the topic exists before running the producer.

Update the Kafka configuration in `producer.py` with your Aiven service details:

- Bootstrap server (host:port)
- Security protocol (SSL)
- Path to certificate and key files


Run the producer:

```python producer.py```

Note:

Download certificates from Aiven Console → Kafka → Connection Information
Ensure correct file paths are provided

---

## Step 2: Kafka Ingestion

Events are ingested into a Kafka topic (`clickstream`) hosted on Aiven.

Kafka acts as the real-time data backbone for the pipeline.

---

## Step 3: Stream Data to OpenSearch

Kafka Connect is used to stream data from Kafka to OpenSearch using the OpenSearch Sink Connector.

Key configuration:

```json
{
  "topics": "clickstream",
  "connection.url": "<opensearch-url>",
  "connection.username": "<username>",
  "connection.password": "<password>",
  "key.ignore": true,
  "schema.ignore": true,
  "value.converter": "org.apache.kafka.connect.storage.StringConverter",
  "index": "clickstream-data"
}
```

---

## Step 4: Visualization

OpenSearch Dashboards is used to visualize data:

- Clicks over time  
- Top pages  
- Browser distribution  
- Country distribution  

---

## Sample Dashboard

<img width="3250" height="1870" alt="image" src="https://github.com/user-attachments/assets/bf9e93b5-3c50-464a-975b-6ad8f08242d7" />


---



## Improvements / Future Work

- Add security with SASL/RBAC/ACL  
- Enhance schema validation  
  
