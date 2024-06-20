import streamlit as st
# from pyspark.sql import SparkSession
import pandas as pd
import numpy as np
# import time
from PIL import Image
import matplotlib.pyplot as plt
# import streamlit_extras as stx
# import streamlit_shadcn_ui as shcn
# import streamlit_elements as elements
from data import load_fraud_data
from auth import login

# Streamlit configuration
st.set_page_config(
    page_title="CNAS Fraud Detection Dashboard",
    page_icon=Image.open(r"C:\Users\DELL\OneDrive\Documents\memoire1\Streamlit-Fraud-Dashboard\assets\favicon.ico"),
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load the data
fraud_data = load_fraud_data()

# Check if user is logged in
if login():
    
    
    st.title('📊 CNAS Fraud/Abuse Detection in medication consumption Dashboard')
    # Sidebar with Admin Info and Navigation
    st.sidebar.title('CNAS Dashboard')
    admin_info = st.sidebar.container()
    with admin_info:
        username = st.session_state.get('username', 'Unknown User')
        role = st.session_state.get('role', 'Unknown Role')
        email=st.session_state.get('Emial', 'user@cnas.dz')
        phone=st.session_state.get('Phone', '+213 555 666 777')
        html_content = f"""
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <div style="text-align: center;">
            <h2 style="color:#0072bb;">Admin Info</h2>
            <span class="material-icons" style="font-size:50px;color:#0072bb;">person</span>
            <p>{username}</p>
            <p>{role}</p>
            <p>Data Science Department</p>
        </div>
        """
        st.sidebar.markdown(html_content, unsafe_allow_html=True)
        st.sidebar.markdown('---')
        
        st.sidebar.markdown('---')
        st.sidebar.subheader('Contact Us')
        st.sidebar.write('Email: {Email}')
        st.sidebar.write('Phone: {Phone}')
        st.sidebar.markdown('---')
        # logout button
        if st.sidebar.button('Log out'):
            st.session_state['logged_in'] = False

        st.sidebar.subheader('About')
        st.sidebar.write('This dashboard provides insights and analysis on fraud detection in the CNAS system.')

    # Placeholder for the KPIs
    placeholder = st.empty()
    with placeholder.container():
        # Create four columns for KPIs
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)

        # Fill in those four columns with respective metrics or KPIs
        kpi1.metric(
            label="Total Fraudulent Claims 🔍",
            value=(fraud_data['fraud_label'] == 1).sum(),
        )
        
        kpi2.metric(
            label="Female Suspects 👩‍⚕️",
            # count of fraud_label=1 and SEXE_F=1
            value=((fraud_data['fraud_label'] == 1) & (fraud_data['SEXE_F'] == 1)).sum(),
        )
        
        kpi3.metric(
            label="Male Suspects 👨‍⚕️",
            value=((fraud_data['fraud_label'] == 1) & (fraud_data['SEXE_M'] == 1)).sum(),
        )

        kpi4.metric(
            label="Medications Involved 💊",
            # count medications involved
            value=fraud_data['NUM_ENR'].nunique(),
        )

    # Horizontal line to separate the KPIs from the rest of the content
    st.markdown('---')

    # Define tabs
    tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

    # Tab 1 content
    with tab1:
        tab1_col1, tab1_col2 = st.columns(2)
        with tab1_col1:
            st.write('**Daily Fraudulent Claims**')
            fraud_data['Days'] = pd.to_datetime(fraud_data['DATE_PAIEMENT']).dt.day
            fraud_label_count = fraud_data[fraud_data['fraud_label'] == 1].groupby('Days').size()
            fraud_label_chart = st.line_chart(fraud_label_count)

            # Bar chart of count of fraud_label=1 per tranche_age
            st.write('**Count of Fraudulent Claims per Age Group**')
            fraud_label_count_age = fraud_data[fraud_data['fraud_label'] == 1].groupby('TRANCHE_AGE_BENEF').size()
            fig, ax = plt.subplots()
            ax.bar(fraud_label_count_age.index, fraud_label_count_age.values, color='#0072bb')
            ax.set_xlabel('Age Group')
            ax.set_ylabel('Count')
            st.pyplot(fig)

            #sum of mt_medic per days with fraud_label=1
            st.write('**Total Cost of Fraudulent Claims per Day**')
            fraud_label_sum = fraud_data[fraud_data['fraud_label'] == 1].groupby('Days')['MT_MEDIC'].sum()
            fig, ax = plt.subplots()
            ax.plot(fraud_label_sum.index, fraud_label_sum.values, color='#FF5733')
            ax.set_xlabel('Days')
            ax.set_ylabel('Total Cost in DZD')
            st.pyplot(fig)
            




        with tab1_col2:
            st.write('**Count of Fraudulent Claims per Gender**')
            fraud_label_count_gender = fraud_data[fraud_data['fraud_label'] == 1].groupby(['SEXE_F']).size()
            fig, ax = plt.subplots()
            ax.bar(fraud_label_count_gender.index, fraud_label_count_gender.values, color=['#FF5733', '#0072bb'])
            ax.set_xlabel('Gender')
            ax.set_ylabel('Count')
            st.pyplot(fig)
            
            st.write('**Count of Fraudulent Claims per TS**')
            fraud_label_count_ts = fraud_data[fraud_data['fraud_label'] == 1].groupby(['TS_O']).size()
            fig, ax = plt.subplots()
            ax.bar(fraud_label_count_ts.index, fraud_label_count_ts.values, color=['#0072bb', '#FF5733'])
            ax.set_xlabel('TS')
            ax.set_ylabel('Count')
            st.pyplot(fig)

    # Tab 2 content
    with tab2:
        tab2_col1, tab2_col2 = st.columns(2)
        with tab2_col1:
            st.write('**Top 10 Most Frequent Pharmacies Susceptible to Fraud**')
            # List of top 10 most frequent code_ps with fraud_label=1
            top_10_code_ps = fraud_data[fraud_data['fraud_label'] == 1]['CODEPS'].value_counts().head(10).index.tolist()
            # Convert top_10_code_ps to a dataframe
            top_10_code_ps_df = pd.DataFrame({'CODEPS': top_10_code_ps})
            # Display the data in a dataframe
            st.dataframe(top_10_code_ps_df)

            st.write('**Top 10 Medications Most Susceptible  to Fraud**')
            # List of top 10 most frequent NUM_ENR with fraud_label=1
            top_10_num_enr = fraud_data[fraud_data['fraud_label'] == 1]['NUM_ENR'].value_counts().head(10).index.tolist()
            # Convert top_10_num_enr to a dataframe
            top_10_num_enr_df = pd.DataFrame({'NUM_ENR': top_10_num_enr})
            st.dataframe(top_10_num_enr_df)
            


        with tab2_col2:
            st.write('**Recent Fraudulent Claims**')
            # # Display the most recent 50 rows of the dataset where fraud_label=1
            # st.dataframe(fraud_data[fraud_data['fraud_label'] == 1][['ID', 'NUM_ENR', 'NO_DOSSIER_NAT', 'DATE_PAIEMENT', 'QUANTITE_MED', 'CODEPS', 'MT_MEDIC']].tail(50))
            # #add a column for the fraud label : if =1 : fraud if 0 not fraud if 2 suspicious

            def apply_color(val):
                if val == 'fraud':
                    color = 'red'
                elif val == 'not fraud':
                    color = 'green'
                else:
                    color = 'yellow'
                return f'color: {color}'

            fraud_data['Fraud_Label'] = np.where(fraud_data['fraud_label'] == 1, 'fraud', np.where(fraud_data['fraud_label'] == 0, 'not fraud', 'suspicious'))
            # if fraud then color cell in red if not fraud color cell in green if suspicious color cell in yellow
            fraud_data.style.applymap(lambda x: 'color: red' if x == 1 else 'color: green' if x == 0 else 'color: yellow')
            styled_data = fraud_data[['ID', 'NUM_ENR', 'NO_DOSSIER_NAT', 'DATE_PAIEMENT', 'QUANTITE_MED', 'CODEPS', 'MT_MEDIC','Fraud_Label']].tail(50).style.applymap(apply_color, subset=['Fraud_Label'])
            st.dataframe(styled_data)
