import streamlit as st
import numpy as np
import pandas as pd
import joblib  # Import joblib for loading the model
import requests
from streamlit_lottie import st_lottie

# Load the .pkl model
with open('C:\\Users\\RIJU\\Downloads\\voting_clf_model.pkl\\voting_clf_model.pkl', 'rb') as f:
  model = joblib.load(f)

# Page configuration
st.set_page_config(page_title="Automated Fraud Detection System", layout='wide')

# Boilerplate to remove the Streamlit logo and footer
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Title and description
st.title("Automated Fraud Detection System Web App")
st.write("""
This app helps track transactions that lead to fraud. The dataset is collected and stored in this 
[Kaggle repository](https://www.kaggle.com/datasets/anidiptapal/fraud-detection-1000-rows), which contains 
historical information about fraudulent transactions to detect fraud in online payments.
""")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets8.lottiefiles.com/packages/lf20_yhTqG2.json"
lottie_hello = load_lottieurl(lottie_url)

# Navigation
page = st.radio("", ("Home", "Demo"), key="main_page", horizontal=True)

if page == "Home":
    st.header("Home")
    st.write("Welcome to the Automated Fraud Detection System.")
    
    # Detailed Project Summary
    st.subheader("Project Summary")
    st.write("""
    Fraud detection is crucial in the digital age, where millions of financial transactions occur daily. Our project, 
    **"Advanced Fraud Detection Using Machine Learning,"** tackles this challenge by developing a sophisticated and scalable 
    system tailored for financial institutions and e-commerce platforms.

    We began by analyzing a highly imbalanced dataset with 6.3 million transactions, only a fraction of which were fraudulent. 
    Our initial approach combined deep learning techniques—using CNN and LSTM models to capture intricate patterns in the data—with 
    a Random Forest Classifier for final classification. This method provided a solid foundation but highlighted the need for better 
    handling of data imbalance.

    To address this, we adopted advanced resampling techniques like SMOTE and ADASYN, which effectively balanced the dataset and 
    improved model performance. We then enhanced our model by integrating CatBoost and Random Forest in a voting classifier ensemble, 
    optimizing the system for higher accuracy and robustness.

    Our solution is brought to life with an intuitive interface developed using Streamlit, enhanced by Lottie animations for an engaging 
    user experience. Users can easily input transaction details and receive instant fraud risk assessments, supported by clear explanations 
    and interactive dashboards.

    Despite encountering challenges such as data imbalance and the complexity of model integration, our project demonstrates significant 
    promise in providing real-time, reliable fraud detection. Our focus on scalability ensures that our system can adapt to growing data 
    volumes and evolving fraud tactics, making it a vital tool in the fight against financial fraud.
    """)

    # Practical Uses of This Model
    st.subheader("Practical Uses of This Model")
    st.write("""
    This fraud detection system can be practically used in various scenarios, such as:
    """)
    st.markdown("""
    - **Banking Sector:** To monitor and analyze transactions in real-time, flagging suspicious activities and preventing fraudulent transactions.
    - **E-commerce Platforms:** To protect online retailers and their customers from fraudulent purchases and chargebacks.
    - **Payment Processors:** To ensure the security of digital payments and reduce fraud-related losses.
    - **Insurance Companies:** To detect and prevent fraudulent insurance claims by analyzing transaction patterns.
    - **Financial Services:** To enhance the security and trustworthiness of financial services by identifying potential frauds.
    - **Regulatory Compliance:** To help organizations comply with anti-fraud regulations and standards by providing robust fraud detection capabilities.
    """)

    # Sidebar for feature explanation
    with st.sidebar:
        st_lottie(lottie_hello, quality='high')

elif page == "Demo":
    st.header('Demo')
    st.write('Enter the transaction details below to predict if it is fraudulent.')

    # Sidebar for feature explanation
    with st.sidebar:
        st_lottie(lottie_hello, quality='high')
        st.sidebar.title('User Features Explanation')
        st.sidebar.markdown("**step**: represents a unit of time where 1 step equals 1 hour")
        st.sidebar.markdown("**type**: type of online transaction (CASH IN,  CASH OUT,  DEBIT,  PAYMENT,  TRANSFER)")
        st.sidebar.markdown('**amount**: the amount of the transaction')
        st.sidebar.markdown('**oldbalanceOrg**: balance before the transaction')
        st.sidebar.markdown('**newbalanceDest**: the new balance of recipient after the transaction')
        st.sidebar.markdown('**changebalanceOrg**: the change in balance of the origin after the transaction')

    def user_input_features():
        step = st.number_input('Step', min_value=0, max_value=5000, step=1)
        type_mapping = {"CASH IN": 0, "CASH OUT": 1, "DEBIT": 2, "PAYMENT": 3, "TRANSFER": 4}
        type = st.radio('Online Transaction Type', ("CASH IN", "CASH OUT", "DEBIT", "PAYMENT", "TRANSFER"), horizontal=True)
        amount = st.slider("Amount of the transaction (INR)", 0.0, 100000.0, step=100.0)

        col1, col2 = st.columns(2)
        with col1:
            oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, step=0.1)

        # Calculate newbalanceDest based on the type of transaction
        if type == "CASH IN":
            newbalanceDest_default = oldbalanceOrg + amount
        else:
            newbalanceDest_default = oldbalanceOrg - amount

        newbalanceDest_color = "green" if newbalanceDest_default >= 0 else "red"
        newbalanceDest_display = f"<p style='color:{newbalanceDest_color};'>{newbalanceDest_default}</p>"

        with col2:
            newbalanceDest = st.number_input("New Balance Destination", value=newbalanceDest_default, step=0.1)
            st.markdown(newbalanceDest_display, unsafe_allow_html=True)

        # Calculate changebalanceOrg
        changebalanceOrg = newbalanceDest - oldbalanceOrg

        type_num = type_mapping[type]
        if type_num != 0 and amount > oldbalanceOrg:
            st.error("Not Valid Transaction: Amount is greater than old balance for transaction types other than CASH IN.")
            st.stop()  # Stop further execution to prevent invalid predictions


        data = {
            'step': step,
            'type': type_mapping[type],
            'amount': amount,
            'oldbalanceOrg': oldbalanceOrg,
            'newbalanceDest': newbalanceDest,
            'changebalanceOrg': changebalanceOrg
        }
        features = pd.DataFrame(data, index=[0])
        return features

    df = user_input_features()

    if st.button("Predict"):
        # Make prediction
        y_preds = model.predict(df)  # Get the class predictions

        if y_preds[0] == 0:
            st.metric("Prediction", value="Transaction is not fraudulent")
        else:
            st.metric("Prediction", value="Transaction is fraudulent")