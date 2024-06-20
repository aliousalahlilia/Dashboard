# import streamlit as st

# def display_kpis(fraud_data):
#     kpi1, kpi2, kpi3, kpi4 = st.columns(4)

#     kpi1.metric(
#         label="Total Fraudulent Claims 🔍",
#         value=(fraud_data['predictions'] == 1).sum(),
#     )
    
#     kpi2.metric(
#         label="Female Suspects 👩‍⚕️",
#         value=((fraud_data['predictions'] == 1) & (fraud_data['SEXE_F'] == 1)).sum(),
#     )
    
#     kpi3.metric(
#         label="Male Suspects 👨‍⚕️",
#         value=((fraud_data['predictions'] == 1) & (fraud_data['SEXE_M'] == 1)).sum(),
#     )

#     kpi4.metric(
#         label="Medications Involved 💊",
#         value=fraud_data['NUM_ENR'].nunique(),
#     )

import streamlit as st

def display_kpis(fraud_data):
    if fraud_data is None or fraud_data.empty:
        st.error("No data available to display KPIs.")
        return

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    kpi1.metric(
        label="Total Fraudulent Claims 🔍",
        value=fraud_data['fraud_cases'].sum(),
    )
    
    kpi2.metric(
        label="Female Suspects 👩‍⚕️",
        value=fraud_data['female_fraud_cases'].sum(),
    )
    
    kpi3.metric(
        label="Male Suspects 👨‍⚕️",
        value=fraud_data['male_fraud_cases'].sum(),
    )

    kpi4.metric(
        label="Medications Involved 💊",
        value=fraud_data['NUM_ENR'].nunique(),
    )
