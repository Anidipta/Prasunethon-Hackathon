### **📊 Dataset Description: Fraud Detection Dataset**

**Dataset Overview:**
This extensive dataset comprises transactional data, specifically designed for developing and evaluating fraud detection models. With a robust dataset of 6.3 million rows, it provides a comprehensive basis for rigorous analysis and model training.

**Columns:**
1. **⏳ `step`**: Represents a unit of time where 1 step equals 1 hour.
2. **💳 `type`**: Type of transaction, including 'CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', and 'TRANSFER'.
3. **💰 `amount`**: The monetary value of the transaction.
4. **🏦 `oldbalanceOrg`**: The initial balance of the origin account before the transaction.
5. **🏦 `newbalanceOrig`**: The new balance of the origin account after the transaction.
6. **🏦 `oldbalanceDest`**: The initial balance of the destination account before the transaction.
7. **🏦 `newbalanceDest`**: The new balance of the destination account after the transaction.
8. **🔄 `changebalanceOrg`**: The change in balance for the origin account following the transaction.
9. **🚨 `isFraud`**: Binary indicator (0 or 1), where 1 denotes a fraudulent transaction.

**Summary:**
- **📈 Total Rows**: 6,300,000
- **📊 Total Columns**: 9

Dataset can be accessed [here](https://www.kaggle.com/datasets/anidiptapal/fraud-detection-1000-rows).

### **Key Characteristics:**
- **🔢 Transaction Types**: Includes various transaction types, providing diverse scenarios for model training.
- **💳 Balance Changes**: Records balances before and after transactions for both origin and destination accounts, facilitating anomaly detection.
- **🚨 Fraud Indicator**: A binary fraud indicator essential for supervised learning in fraud detection.

### **Potential Use Cases:**
1. **🔍 Supervised Learning for Fraud Detection**: Train models to predict the likelihood of fraudulent transactions.
2. **📉 Pattern Analysis**: Study transactional patterns and behaviors indicative of fraud.
3. **🛠️ Feature Engineering**: Create new features from the dataset to boost model performance.

### **How to Run:**
Access our final model [here](https://drive.google.com/file/d/1P2HRWjud5vZ3E5PRUhqvywu9UHo8xttO/view?usp=sharing).

### **Data Source and Collection Method:**
The dataset is a simulated representation of real-world transactions. Each row depicts a single transaction, mirroring typical financial operations. This simulation ensures a realistic mix of fraudulent and non-fraudulent transactions.

### **Challenges and Considerations:**
- **⚖️ Class Imbalance**: With fraudulent transactions being significantly fewer than non-fraudulent ones, addressing class imbalance is crucial. Techniques like SMOTE, ADASYN, or ensemble methods can help mitigate this issue.
- **🔒 Data Privacy**: Although simulated, the dataset reflects real-world scenarios, allowing for significant insights while safeguarding sensitive information.

**Conclusion:**
This fraud detection dataset is a vital resource for developing and assessing fraud detection algorithms. Its size and detailed transactional records offer ample opportunities for thorough analysis, feature engineering, and model evaluation.

---

### **Python 3.9+**

**Python Requirements:**
```
catboost
streamlit
pandas
numpy
joblib
streamlit_lottie
scikit-learn
```

### **🎥 Demo Video:**

Watch the demo video [here](https://youtu.be/qHkBchgEdTg?si=mCmb0Dm8TBo88reV).

---


## **Author**

| **Name** | **Year** | **Position** |
|--|--|--|
| **Anidipta Pal** | 1st | Data Engineer, Data Analyst, ML Engineer |
| **Sagnik Basak** | 1st | Full Stack Developer |
