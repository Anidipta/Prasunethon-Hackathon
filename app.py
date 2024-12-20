import streamlit as st
import numpy as np
import pandas as pd
import joblib
import requests
from streamlit_lottie import st_lottie

# Load the model
with open('models/voting_clf_model.pt', 'rb') as f:
    model = joblib.load(f)

# Enhanced page configuration
st.set_page_config(
    page_title="Risk Sense",
    page_icon="🛡️",
    layout='wide',
    initial_sidebar_state="expanded"
)

# Custom CSS with modern styling and animations
st.markdown("""
<style>
    /* Modern dark theme color scheme */
    :root {
        --primary-color: #4CAF50;
        --secondary-color: #2196F3;
        --background-color: #1e1e1e;
        --text-color: #f0f2f6;
        --card-background-color: #2a2a2a;
        --button-hover-color: #3b3b3b;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom container styling */
    .stApp {
        background-color: var(--background-color);
    }
    
    /* Enhanced header styling */
    h1 {
        color: var(--text-color);
        font-size: 3rem !important;
        font-weight: 700 !important;
        text-align: center;
        margin-bottom: 2rem !important;
        background: linear-gradient(45deg, #4CAF50, #2196F3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient 3s ease infinite;
    }
    
    /* Subheader styling */
    h2 {
        color: var(--text-color);
        font-weight: 600 !important;
        margin-top: 2rem !important;
    }
    
    /* Card-like containers */
    .css-1r6slb0 {
        background-color: var(--card-background-color);
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    
    .css-1r6slb0:hover {
        transform: translateY(-5px);
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(45deg, #4CAF50, #2196F3) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.5rem 2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton button:hover {
        background-color: var(--button-hover-color) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Radio button styling */
    .stRadio > label {
        font-weight: 600 !important;
        color: var(--text-color) !important;
    }
    
    /* Metric styling */
    .css-1xarl3l {
        background-color: var(--card-background-color);
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
    }
    
    /* Add pulse animation for fraud detection */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .fraud-alert {
        animation: pulse 2s infinite;
        background: #ff4444;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    
    .safe-transaction {
        background: #00C851;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    
    .rect-button {
            display: inline-block;
            padding: 10px 30px;
            margin: 10px;
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-align: center;
            text-decoration: none;
            background: linear-gradient(45deg, #4CAF50, #2196F3);
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s, transform 0.2s;
        }
        .rect-button:hover {
            background: #3b3b3b;
            transform: translateY(-2px);
        }
        
</style>
""", unsafe_allow_html=True)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Updated Lottie animation URL for a more modern look
lottie_url = "https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json"
lottie_hello = load_lottieurl(lottie_url)

col1, col2 = st.sidebar.columns(2)
with col1:
    home = st.button("🏠 Home", key="home_button")
with col2:
    demo = st.button("🎮 Demo", key="demo_button")

# Manage page navigation with session state
if "page" not in st.session_state:
    st.session_state.page = "home"  # Default page is home

if home:
    st.session_state.page = "home"
    
if demo:
    st.session_state.page = "demo"
    
# Page navigation based on button clicks
if st.session_state.page == "home":
    st.title("Risk Sense : Next-Gen Fraud Predictor 🛡️")
    
    
    with st.sidebar:
        st_lottie(lottie_hello, quality='high', key="home_animation")
        st.markdown("""
        ### 🎯 Our Mission
        Protecting your transactions with cutting-edge AI technology.
        
        ### 🚀 Key Features
        - **Real-time Detection** ⚡
        - **Advanced AI Models** 🤖
        - **99.9% Accuracy** ✨
        - **24/7 Monitoring** 🕒
        """)
        
        st.markdown("""
        ### 💡 How It Works
        1. **Input Transaction** 📝
        2. **AI Analysis** 🔍
        3. **Instant Results** ⚡
        4. **Secure Decision** 🔒
        """)
        

elif st.session_state.page == "demo":
    st.title("Risk Sense : Demo 🔍")
    
    with st.sidebar:
        st_lottie(lottie_hello, quality='high', key="demo_animation")
        st.sidebar.title('📊 Feature Guide')
        st.sidebar.markdown("""
        - ⏱️ **Step**: Time unit (1 step = 1 hour)
        - 💳 **Type**: Transaction category
        - 💰 **Amount**: Transaction value
        - 📊 **Balance**: Account status
        """)

    def user_input_features():
        st.markdown("### 📝 Transaction Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            step = st.number_input('⏱️ Step', min_value=0, max_value=5000, step=1)
            amount = st.slider("💰 Amount (INR)", 0.0, 100000.0, step=100.0)
            
        with col2:
            type_mapping = {"CASH IN": 0, "CASH OUT": 1, "DEBIT": 2, "PAYMENT": 3, "TRANSFER": 4}
            type = st.radio('💳 Transaction Type', type_mapping.keys(), horizontal=True)
            oldbalanceOrg = st.number_input("📊 Old Balance", min_value=0.0, step=0.1)

        # Calculate newbalanceDest
        if type == "CASH IN":
            newbalanceDest_default = oldbalanceOrg + amount
        else:
            newbalanceDest_default = oldbalanceOrg - amount

        st.markdown("### 📈 Calculated Values")
        col3, col4 = st.columns(2)
        
        with col3:
            newbalanceDest = st.number_input("New Balance", value=newbalanceDest_default, step=0.1)
        
        with col4:
            changebalanceOrg = newbalanceDest - oldbalanceOrg
            st.metric("Balance Change", f"₹{changebalanceOrg:,.2f}", 
                     delta=f"{'+' if changebalanceOrg >= 0 else ''}{changebalanceOrg:,.2f}")

        if type_mapping[type] != 0 and amount > oldbalanceOrg:
            st.error("⚠️ Invalid Transaction: Amount exceeds available balance!")
            st.stop()

        return pd.DataFrame({
            'step': [step],
            'type': [type_mapping[type]],
            'amount': [amount],
            'oldbalanceOrg': [oldbalanceOrg],
            'newbalanceDest': [newbalanceDest],
            'changebalanceOrg': [changebalanceOrg]
        })

    df = user_input_features()

    if st.button("🔍 Analyze Transaction"):
        with st.spinner("🔄 Analyzing transaction..."):
            y_preds = model.predict(df)
            
            if y_preds[0] == 0:
                st.markdown("""
                <div class="safe-transaction">
                    <h2>✅ Safe Transaction</h2>
                    <p>This transaction appears to be legitimate.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="fraud-alert">
                    <h2>🚨 Fraud Alert!</h2>
                    <p>This transaction has been flagged as potentially fraudulent.</p>
                </div>
                """, unsafe_allow_html=True)
                
                
