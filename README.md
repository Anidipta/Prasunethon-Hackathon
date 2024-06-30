### **Dataset Description: Fraud Detection Dataset**

**Dataset Overview:**
This dataset contains transactional data, specifically curated to aid in the development and evaluation of fraud detection models. With a total of 6.3 million rows, it offers a substantial volume of data for robust analysis and model training. 

**Columns:**
1. **step**: Represents a unit of time where 1 step equals 1 hour of time.
2. **type**: Type of transaction, such as 'CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', and 'TRANSFER'.
3. **amount**: The amount of money involved in the transaction.
4. **oldbalanceOrg**: The initial balance before the transaction for the origin account.
5. **newbalanceOrig**: The new balance after the transaction for the origin account.
6. **oldbalanceDest**: The initial balance before the transaction for the destination account.
7. **newbalanceDest**: The new balance after the transaction for the destination account.
8. **changebalanceOrg**: The change in balance for the origin account after the transaction.
9. **isFraud**: Binary indicator (0 or 1) where 1 represents a fraudulent transaction.

**Summary:**
- **Total Rows**: 6,300,000
- **Total Columns**: 9

Dataset can be access from [here](https://www.kaggle.com/datasets/anidiptapal/fraud-detection-1000-rows)

### **Key Characteristics:**
- **Transaction Types**: Various types of transactions are included, providing diverse scenarios for model training.
- **Balance Changes**: Both origin and destination account balances are recorded before and after transactions, facilitating the detection of unusual patterns.
- **Fraud Indicator**: The dataset includes a binary fraud indicator, crucial for supervised learning approaches in fraud detection.

### **Potential Use Cases:**
1. **Supervised Learning for Fraud Detection**: Train machine learning models to predict the likelihood of fraud in transactions.
2. **Pattern Analysis**: Analyze transactional patterns and behaviors that are indicative of fraud.
3. **Feature Engineering**: Develop new features based on the provided data to enhance model performance.


### How to run?
the link to access our final model is [here](https://drive.google.com/file/d/1P2HRWjud5vZ3E5PRUhqvywu9UHo8xttO/view?usp=sharing)


### **Data Source and Collection Method:**
The dataset is a simulated representation of real-world transactional data. Each row represents a single transaction, and the data is generated to reflect typical patterns found in financial operations. This ensures a realistic distribution of both fraudulent and non-fraudulent transactions.

### **Challenges and Considerations:**
- **Class Imbalance**: Fraudulent transactions are significantly fewer compared to non-fraudulent ones, posing a challenge for model training. Techniques such as resampling (e.g., SMOTE, ADASYN) or advanced algorithms (e.g., ensemble methods) can be employed to address this.
- **Data Privacy**: Although the data is simulated, it mirrors real-world scenarios, allowing for meaningful insights without compromising sensitive information.

**Conclusion:**
This fraud detection dataset is a valuable resource for developing and evaluating fraud detection algorithms. Its extensive size and detailed transactional records provide ample opportunities for rigorous analysis, feature engineering, and model testing.

---

- Python 3.9+ 

- Python requirements
```
joblib==1.0.0
kaggle==1.5.12
numpy==1.19.5
pandas==1.1.2
regex==2020.7.14
scikit-learn==0.22.1
scipy==1.5.4
auto-sklearn==0.14.7
dask==2022.8.1
```

### Visualization


### Conclusion


### Author
| Name | Year | Position |
|--|--|--|
|ANIDIPTA PAL| 1st|Data Engineer , Data Analyst , ML Engineer|
|SAGNIK BASAK|1st|Full Stack Developer|
