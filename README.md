# Real-Time Clickstream Analytics using Aiven Kafka and OpenSearch

## Overview

This project demonstrates how to build a real-time data pipeline using Aiven services to monitor and analyze website activity.

The pipeline simulates clickstream data, streams it through Aiven Kafka, and visualizes it using OpenSearch Dashboards.

---

## Architecture

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

## Step 1: Generate Clickstream Data

A Python script (`producer.py`) generates real-time clickstream events with fields such as:

- user_id  
- page  
- action  
- timestamp (ISO 8601 format)  
- device  
- country  

Run the producer:

---

## Step 2: Kafka Ingestion

Data is published to the `clickstream` topic in Aiven Kafka.

---

## Step 3: Stream Data to OpenSearch

Kafka Connect is used with the OpenSearch Sink Connector to push data into OpenSearch.

---

## Step 4: Visualization

OpenSearch Dashboards is used to visualize data:

- Clicks over time  
- Top pages  
- Device distribution  
- Country distribution  

---

## Sample Dashboard

(Add screenshots here)

---



## Improvements / Future Work

- Add security with SASL/RBAC/ACL  
- Enhance schema validation  
  
