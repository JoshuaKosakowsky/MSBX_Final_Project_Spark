# Fraud Detection in Large-Scale Financial Transactions

---

## Background & Problem Statement

Fraud in financial transactions creates challenges beyond detection, leading to:

- Direct monetary losses (reimbursements, lost fees, interest revenue)  
- Operational and merchant-side costs (chargebacks, unrecoverable goods, labor-intensive investigations)  
- Loss of customer trust due to fraud incidents or false declines  

As digital payments continue to scale, institutions must process large volumes of transactions efficiently while minimizing these risks.

This project aims to analyze large-scale credit card transaction data to identify patterns associated with fraudulent activity and evaluate how fraud impacts financial loss, operational costs, and customer trust.

---

## Dataset

We evaluated multiple datasets based on size, computational feasibility, and suitability for distributed processing using PySpark, ultimately deciding with the following:

- **Credit Card Transactions Dataset (Priyam Choksi)**  
  - ~1.3 million transactions  
  - Real world data (Anonymized)
  - Descriptive column data
  - Ground Truth column "is_fraud"  

Current working dataset:  
[Credit Card Transactions Dataset](https://www.kaggle.com/datasets/priyamchoksi/credit-card-transactions-dataset)

---

## Methodology

The project will be implemented using **PySpark with Docker and on AWS EMR**, with data stored **Locally and in Amazon S3**.

### Data Ingestion
- Host locally in "data/raw" folder
- Upload dataset to S3  
- Load into Spark DataFrames  

### Data Cleaning & Preparation
- Handle missing values  
- Filter invalid records  
- Feature engineering:
  - Transaction time features  
  - Amount categories  
  - Behavioral indicators  

### Exploratory Analysis
- Analyze fraud rates across:
  - Transaction types  
  - Transaction amounts  
  - Time patterns  
- Identify anomalies between fraudulent and legitimate transactions  

### Modeling
- Implement a baseline classification model:
  - Logistic Regression (Spark ML) 
  - Random Forest 
- Address class imbalance using:
  - Oversampling / undersampling  
  - Class weighting  

### Distributed Performance Evaluation
- Compare runtime performance across:
  - Dataset sizes  
  - Cluster configurations  

---

## Expected Outcomes

- Identification of key fraud patterns  
- Insights into how fraud varies across transaction characteristics  
- Demonstration of how **distributed computing improves efficiency**  
- Understanding of business implications related to:
  - Reducing financial loss  
  - Lowering operational costs  
  - Preserving customer trust  

These insights aim to support more effective and scalable fraud detection strategies.