# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# def display_tab1(fraud_data):
#     tab1_col1, tab1_col2 = st.columns(2)
#     with tab1_col1:
#         st.write('**Daily Fraudulent Claims**')
#         fraud_data['Days'] = pd.to_datetime(fraud_data['DATE_PAIEMENT']).dt.day
#         fraud_label_count = fraud_data[fraud_data['predictions'] == 1].groupby('Days').size()
#         st.line_chart(fraud_label_count)

#         st.write('**Count of Fraudulent Claims per Age Group**')
#         fraud_label_count_age = fraud_data[fraud_data['predictions'] == 1].groupby('TRANCHE_AGE_BENEF').size()
#         fig, ax = plt.subplots()
#         ax.bar(fraud_label_count_age.index, fraud_label_count_age.values, color='#0072bb')
#         ax.set_xlabel('Age Group')
#         ax.set_ylabel('Count')
#         st.pyplot(fig)

#         st.write('**Total Cost of Fraudulent Claims per Day**')
#         fraud_label_sum = fraud_data[fraud_data['predictions'] == 1].groupby('Days')['MT_MEDIC'].sum()
#         fig, ax = plt.subplots()
#         ax.plot(fraud_label_sum.index, fraud_label_sum.values, color='#FF5733')
#         ax.set_xlabel('Days')
#         ax.set_ylabel('Total Cost in DZD')
#         st.pyplot(fig)

#     with tab1_col2:
#         st.write('**Count of Fraudulent Claims per Gender**')
#         fraud_label_count_gender = fraud_data[fraud_data['predictions'] == 1].groupby(['SEXE_F']).size()
#         fig, ax = plt.subplots()
#         ax.bar(fraud_label_count_gender.index, fraud_label_count_gender.values, color=['#FF5733', '#0072bb'])
#         ax.set_xlabel('Gender')
#         ax.set_ylabel('Count')
#         st.pyplot(fig)
        
#         st.write('**Count of Fraudulent Claims per TS**')
#         fraud_label_count_ts = fraud_data[fraud_data['predictions'] == 1].groupby(['TS_O']).size()
#         fig, ax = plt.subplots()
#         ax.bar(fraud_label_count_ts.index, fraud_label_count_ts.values, color=['#0072bb', '#FF5733'])
#         ax.set_xlabel('TS')
#         ax.set_ylabel('Count')
#         st.pyplot(fig)

# def display_tab2(fraud_data):
#     tab2_col1, tab2_col2 = st.columns(2)
#     with tab2_col1:
#         # display the top 10 medications most susceptible to fraud in pie chart
#         st.write('**Representation of Top 10 Medications Most Susceptible  to Fraud**')
#         top_10_num_enr_count = fraud_data[fraud_data['predictions'] == 1]['NUM_ENR'].value_counts().head(10)
#         fig, ax = plt.subplots()
#         ax.pie(top_10_num_enr_count, labels=top_10_num_enr_count.index, autopct='%1.1f%%', startangle=90)
#         ax.axis('equal')
#         st.pyplot(fig)

        

#         # # display the top 10 most frequent pharmacies susceptible to fraud in a horizontal bar chart based on count of fraud label==1 
#         # top_10_code_ps_count = fraud_data[fraud_data['fraud_label'] == 1]['CODEPS'].value_counts().head(10)
#         # fig, ax = plt.subplots()
#         # ax.barh(top_10_code_ps_count.index, top_10_code_ps_count.values, color='#FF5733')
#         # ax.set_xlabel('Count')
#         # ax.set_ylabel('Pharmacy Code')
#         # st.pyplot(fig)

#         st.write('**List of Top 10 Medications Most Susceptible  to Fraud**')
#         top_10_num_enr = fraud_data[fraud_data['predictions'] == 1]['NUM_ENR'].value_counts().head(10).index.tolist()
#         top_10_num_enr_df = pd.DataFrame({'NUM_ENR': top_10_num_enr})
#         st.dataframe(top_10_num_enr_df)

        


#     with tab2_col2:
#         st.write('**List of Top 10 Most Frequent Pharmacies Susceptible to Fraud**')
#         top_10_code_ps = fraud_data[fraud_data['predictions'] == 1]['CODEPS'].value_counts().head(10).index.tolist()
#         top_10_code_ps_df = pd.DataFrame({'CODEPS': top_10_code_ps})
#         st.dataframe(top_10_code_ps_df)
        
#         st.write('**Recent Fraudulent Claims**')
#         def apply_color(val):
#             if val == 'fraud':
#                 color = 'red'
#             elif val == 'not fraud':
#                 color = 'green'
#             else:
#                 color = 'yellow'
#             return f'color: {color}'

#         fraud_data['predictions'] = np.where(fraud_data['predictions'] == 1, 'fraud', np.where(fraud_data['predictions'] == 0, 'not fraud', 'suspicious'))
#         styled_data = fraud_data[['ID', 'NUM_ENR', 'NO_DOSSIER_NAT', 'DATE_PAIEMENT', 'QUANTITE_MED', 'CODEPS', 'MT_MEDIC','predictions']].tail(50).style.applymap(apply_color, subset=['predictions'])
#         st.dataframe(styled_data) 
       

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# def display_tab1(fraud_data):
#     if fraud_data is None or fraud_data.empty:
#         st.error("No data available for plotting.")
#         return

#     if 'week' not in fraud_data.columns:
#         st.error("'week' column is missing from the data.")
#         print(f"Columns available: {fraud_data.columns}")
#         return

#     tab1_col1, tab1_col2 = st.columns(2)
#     with tab1_col1:
#         st.write('**Weekly Fraudulent Claims**')
#         st.line_chart(fraud_data.set_index('week')['fraud_cases'])

#         st.write('**Count of Fraudulent Claims per Age Group**')
#         fraud_label_count_age = fraud_data[fraud_data['fraud_cases'] > 0].groupby('TRANCHE_AGE_BENEF').size()
#         fig, ax = plt.subplots()
#         ax.bar(fraud_label_count_age.index, fraud_label_count_age.values, color='#0072bb')
#         ax.set_xlabel('Age Group')
#         ax.set_ylabel('Count')
#         st.pyplot(fig)

#         st.write('**Total Cost of Fraudulent Claims per Week**')
#         fig, ax = plt.subplots()
#         ax.plot(fraud_data['week'], fraud_data['total_cost'], color='#FF5733')
#         ax.set_xlabel('Weeks')
#         ax.set_ylabel('Total Cost in DZD')
#         st.pyplot(fig)

#     with tab1_col2:
#         st.write('**Count of Fraudulent Claims per Gender**')
#         fraud_label_count_gender = fraud_data[fraud_data['fraud_cases'] > 0].groupby(['SEXE_F']).size()
#         fig, ax = plt.subplots()
#         ax.bar(fraud_label_count_gender.index, fraud_label_count_gender.values, color=['#FF5733', '#0072bb'])
#         ax.set_xlabel('Gender')
#         ax.set_ylabel('Count')
#         st.pyplot(fig)
        
#         st.write('**Count of Fraudulent Claims per TS (O)**')
#         fraud_label_count_ts = fraud_data[fraud_data['fraud_cases'] > 0].groupby(['TS_O']).size()
#         fig, ax = plt.subplots()
#         ax.bar(fraud_label_count_ts.index, fraud_label_count_ts.values, color=['#0072bb', '#FF5733'])
#         ax.set_xlabel('TS_O')
#         ax.set_ylabel('Count')
#         st.pyplot(fig)

#         st.write('**Count of Fraudulent Claims per TS (N)**')
#         fraud_label_count_ts_n = fraud_data[fraud_data['fraud_cases'] > 0].groupby(['TS_N']).size()
#         fig, ax = plt.subplots()
#         ax.bar(fraud_label_count_ts_n.index, fraud_label_count_ts_n.values, color=['#0072bb', '#FF5733'])
#         ax.set_xlabel('TS_N')
#         ax.set_ylabel('Count')
#         st.pyplot(fig)

# def display_tab2(fraud_data):
#     if fraud_data is None or fraud_data.empty:
#         st.error("No data available for plotting.")
#         return

#     tab2_col1, tab2_col2 = st.columns(2)
#     with tab2_col1:
#         st.write('**Representation of Top 10 Medications Most Susceptible to Fraud**')
#         top_10_num_enr_count = fraud_data[fraud_data['fraud_cases'] > 0]['NUM_ENR'].value_counts().head(10)
#         fig, ax = plt.subplots()
#         ax.pie(top_10_num_enr_count, labels=top_10_num_enr_count.index, autopct='%1.1f%%', startangle=90)
#         ax.axis('equal')
#         st.pyplot(fig)

#         st.write('**List of Top 10 Medications Most Susceptible to Fraud**')
#         top_10_num_enr = fraud_data[fraud_data['fraud_cases'] > 0]['NUM_ENR'].value_counts().head(10).index.tolist()
#         top_10_num_enr_df = pd.DataFrame({'NUM_ENR': top_10_num_enr})
#         st.dataframe(top_10_num_enr_df)

#     with tab2_col2:
#         st.write('**List of Top 10 Most Frequent Pharmacies Susceptible to Fraud**')
#         top_10_code_ps = fraud_data[fraud_data['fraud_cases'] > 0]['CODEPS'].value_counts().head(10).index.tolist()
#         top_10_code_ps_df = pd.DataFrame({'CODEPS': top_10_code_ps})
#         st.dataframe(top_10_code_ps_df)
        
#         st.write('**Recent Fraudulent Claims**')
#         def apply_color(val):
#             if val == 'fraud':
#                 color = 'red'
#             elif val == 'not fraud':
#                 color = 'green'
#             else:
#                 color = 'yellow'
#             return f'color: {color}'

#         fraud_data['predictions'] = np.where(fraud_data['fraud_cases'] > 0, 'fraud', 'not fraud')
#         styled_data = fraud_data[['ID', 'NUM_ENR', 'NO_DOSSIER_NAT', 'DATE_PAIEMENT', 'QUANTITE_MED', 'CODEPS', 'total_cost', 'predictions']].tail(50).style.applymap(apply_color, subset=['predictions'])
#         st.dataframe(styled_data)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def display_tab1(fraud_data):
    if fraud_data is None or fraud_data.empty:
        st.error("No data available for plotting.")
        return

    tab1_col1, tab1_col2 = st.columns(2)
    with tab1_col1:
        st.write('**Weekly Fraudulent Claims**')
        if 'week' in fraud_data.columns:
            weekly_fraud_cases = fraud_data.groupby('week')['fraud_cases'].sum().reset_index()
            fig, ax = plt.subplots()
            ax.plot(weekly_fraud_cases['week'], weekly_fraud_cases['fraud_cases'], marker='o', linestyle='-')
            ax.set_xlabel('Weeks')
            ax.set_ylabel('Number of Fraudulent Claims')
            ax.set_title('Weekly Fraudulent Claims')
            st.pyplot(fig)
        elif 'month' in fraud_data.columns:
            monthly_fraud_cases = fraud_data.groupby('month')['fraud_cases'].sum().reset_index()
            fig, ax = plt.subplots()
            ax.plot(monthly_fraud_cases['month'], monthly_fraud_cases['fraud_cases'], marker='o', linestyle='-')
            ax.set_xlabel('Months')
            ax.set_ylabel('Number of Fraudulent Claims')
            ax.set_title('Monthly Fraudulent Claims')
            st.pyplot(fig)
        elif 'trimester' in fraud_data.columns:
            trimester_fraud_cases = fraud_data.groupby('trimester')['fraud_cases'].sum().reset_index()
            fig, ax = plt.subplots()
            ax.plot(trimester_fraud_cases['trimester'], trimester_fraud_cases['fraud_cases'], marker='o', linestyle='-')
            ax.set_xlabel('Trimesters')
            ax.set_ylabel('Number of Fraudulent Claims')
            ax.set_title('Trimester Fraudulent Claims')
            st.pyplot(fig)

        st.write('**Count of Fraudulent Claims per Age Group**')
        fraud_label_count_age = fraud_data[fraud_data['fraud_cases'] > 0].groupby('TRANCHE_AGE_BENEF').size()
        fig, ax = plt.subplots()
        ax.bar(fraud_label_count_age.index, fraud_label_count_age.values, color='#0072bb')
        ax.set_xlabel('Age Group')
        ax.set_ylabel('Count')
        st.pyplot(fig)

        st.write('**Total Cost of Fraudulent Claims**')
        fig, ax = plt.subplots()
        if 'week' in fraud_data.columns:
            weekly_total_cost = fraud_data.groupby('week')['total_cost'].sum().reset_index()
            ax.plot(weekly_total_cost['week'], weekly_total_cost['total_cost'], marker='o', linestyle='-')
            ax.set_xlabel('Weeks')
        elif 'month' in fraud_data.columns:
            monthly_total_cost = fraud_data.groupby('month')['total_cost'].sum().reset_index()
            ax.plot(monthly_total_cost['month'], monthly_total_cost['total_cost'], marker='o', linestyle='-')
            ax.set_xlabel('Months')
        elif 'trimester' in fraud_data.columns:
            trimester_total_cost = fraud_data.groupby('trimester')['total_cost'].sum().reset_index()
            ax.plot(trimester_total_cost['trimester'], trimester_total_cost['total_cost'], marker='o', linestyle='-')
            ax.set_xlabel('Trimesters')
        ax.set_ylabel('Total Cost in DZD')
        ax.set_title('Total Cost of Fraudulent Claims')
        st.pyplot(fig)

    with tab1_col2:
        st.write('**Count of Fraudulent Claims per Gender**')
        fraud_label_count_gender = fraud_data[fraud_data['fraud_cases'] > 0].groupby(['SEXE_F']).size()
        fig, ax = plt.subplots()
        ax.bar(fraud_label_count_gender.index, fraud_label_count_gender.values, color=['#FF5733', '#0072bb'])
        ax.set_xlabel('Gender')
        ax.set_ylabel('Count')
        st.pyplot(fig)
        
        st.write('**Count of Fraudulent Claims per TS**')
        fraud_label_count_ts = fraud_data[fraud_data['fraud_cases'] > 0].groupby(['TS_O', 'TS_N']).size().unstack().fillna(0)
        fig, ax = plt.subplots()
        fraud_label_count_ts.plot(kind='bar', stacked=True, ax=ax, color=['#0072bb', '#FF5733'])
        ax.set_xlabel('TS')
        ax.set_ylabel('Count')
        st.pyplot(fig)

def display_tab2(fraud_data):
    if fraud_data is None or fraud_data.empty:
        st.error("No data available for plotting.")
        return

    tab2_col1, tab2_col2 = st.columns(2)
    with tab2_col1:
        st.write('**Representation of Top 10 Medications Most Susceptible to Fraud**')
        top_10_num_enr_count = fraud_data[fraud_data['fraud_cases'] > 0]['NUM_ENR'].value_counts().head(10)
        fig, ax = plt.subplots()
        ax.pie(top_10_num_enr_count, labels=top_10_num_enr_count.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

        st.write('**List of Top 10 Medications Most Susceptible to Fraud**')
        top_10_num_enr = fraud_data[fraud_data['fraud_cases'] > 0]['NUM_ENR'].value_counts().head(10).index.tolist()
        top_10_num_enr_df = pd.DataFrame({'NUM_ENR': top_10_num_enr})
        st.dataframe(top_10_num_enr_df)

    with tab2_col2:
        st.write('**List of Top 10 Most Frequent Pharmacies Susceptible to Fraud**')
        top_10_code_ps = fraud_data[fraud_data['fraud_cases'] > 0]['CODEPS'].value_counts().head(10).index.tolist()
        top_10_code_ps_df = pd.DataFrame({'CODEPS': top_10_code_ps})
        st.dataframe(top_10_code_ps_df)
        
        st.write('**Recent Fraudulent Claims**')
        def apply_color(val):
            if val == 'fraud':
                color = 'red'
            elif val == 'not fraud':
                color = 'green'
            else:
                color = 'yellow'
            return f'color: {color}'

        fraud_data['predictions'] = np.where(fraud_data['fraud_cases'] > 0, 'fraud', 'not fraud')
        styled_data = fraud_data[['ID', 'NUM_ENR', 'NO_DOSSIER_NAT', 'DATE_PAIEMENT', 'QUANTITE_MED', 'CODEPS', 'total_cost', 'predictions']].tail(50).style.applymap(apply_color, subset=['predictions'])
        st.dataframe(styled_data)
