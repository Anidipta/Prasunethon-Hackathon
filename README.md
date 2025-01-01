# 📊 **Risk Sense : Next-Gen Fraud Predictor**

## **Dataset Overview**
This dataset is specifically designed for developing and evaluating machine learning models focused on **fraud detection** in financial transactions. It contains **6.3 million** rows of simulated transactional data, offering a comprehensive foundation for building and testing models to detect fraudulent activities.

## **Columns in the Dataset:**

1. **⏳ `step`**: Represents a unit of time where 1 step equals **1 hour**.
2. **💳 `type`**: The **type** of transaction, including the following categories:
   - `CASH_IN`
   - `CASH_OUT`
   - `DEBIT`
   - `PAYMENT`
   - `TRANSFER`
3. **💰 `amount`**: The **monetary value** of the transaction.
4. **🏦 `oldbalanceOrg`**: The initial **balance of the origin account** before the transaction.
5. **🏦 `newbalanceOrig`**: The updated **balance of the origin account** after the transaction.
6. **🏦 `oldbalanceDest`**: The initial **balance of the destination account** before the transaction.
7. **🏦 `newbalanceDest`**: The updated **balance of the destination account** after the transaction.
8. **🔄 `changebalanceOrg`**: The **change in balance** for the origin account following the transaction.
9. **🚨 `isFraud`**: A **binary indicator** (0 or 1) where:
   - `1`: Fraudulent transaction
   - `0`: Non-fraudulent transaction

---

## **Dataset Summary:**

- **📈 Total Rows**: 6,300,000
- **📊 Total Columns**: 9

### **Key Features:**
- **🔢 Transaction Types**: A variety of transaction types, making the dataset suitable for modeling different fraud scenarios.
- **💳 Balance Changes**: Tracks balance changes before and after transactions for both origin and destination accounts.
- **🚨 Fraud Indicator**: Essential for supervised learning, helping models identify fraudulent behavior.

---

## Flow-Case

![Flowchart](https://github.com/Anidipta/Risk-Sense/blob/main/Images%20Model/Flow.png)

---


## **Potential Use Cases:**

1. **🔍 Supervised Learning for Fraud Detection**: 
   - Train models to predict the likelihood of fraudulent transactions.
   - Develop predictive models using **binary classification** techniques such as decision trees, XGBoost, or neural networks.

2. **📉 Pattern Analysis**: 
   - Analyze transaction patterns that indicate potential fraud.
   - Discover features such as **unusual amounts** or rapid **balance changes** that could suggest fraudulent activities.

3. **🛠️ Feature Engineering**: 
   - Create new features to improve the performance of models, such as:
     - Transaction frequency over time.
     - Account balance changes relative to previous transactions.
     - Time-based behavior patterns for accounts.

---

## **How to Run:**

Access our **final fraud detection model** [here](https://drive.google.com/file/d/1P2HRWjud5vZ3E5PRUhqvywu9UHo8xttO/view?usp=sharing).

### **Live Demo**: 
No download is needed! **Try the fraud detection model live** at [Risk Sense](https://risksense.streamlit.app/).

---

## **Data Source & Collection Method:**

The dataset is a **simulated representation** of real-world financial transactions. Each row represents a transaction with attributes designed to mimic actual banking behavior. The simulation includes both **fraudulent** and **non-fraudulent transactions**, providing a diverse environment for model training and evaluation.

---

## **Challenges and Considerations:**

- **⚖️ Class Imbalance**: 
  Fraudulent transactions are significantly fewer than non-fraudulent ones, which could result in **model bias** towards predicting non-fraudulent transactions. This can be mitigated by:
  - **Resampling techniques** such as **SMOTE** or **ADASYN**.
  - Using **ensemble models** that can better handle imbalance, like **Random Forest** or **XGBoost**.

- **🔒 Data Privacy**: 
  While this dataset is simulated, it mimics the structure of real-world transactional data, which can still be useful for creating privacy-preserving algorithms for **real-time fraud detection** systems.

---

## **Conclusion:**

This **Fraud Detection Dataset** is a comprehensive resource for developing robust fraud detection models. With a variety of features capturing transaction behavior and the fraud indicator, it provides ample opportunities for **pattern recognition**, **anomaly detection**, and **predictive modeling**. This dataset is ideal for both **academic research** and **industry applications** aiming to enhance financial security through automated fraud detection.

---

## **Dependencies:**

Ensure you have the following Python libraries installed:

```bash
catboost
streamlit
pandas
numpy
joblib
streamlit_lottie
scikit-learn
```

---

## **Demo Video**: 
For an introduction to the fraud detection system, watch the demo video [here](https://youtu.be/qHkBchgEdTg?si=mCmb0Dm8TBo88reV).

---

## **Author Information**

| **Name** | **Year** | **Position** |
|:---:|:---:|:---:|
| **Anidipta Pal** | 1st | Data Engineer, Data Analyst, ML Engineer |
| **Sagnik Basak** | 1st | Full Stack Developer |
