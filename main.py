
# import streamlit as st
# from config import setup_page
# from data import load_fraud_data
# from auth import login
# from sidebar import setup_sidebar
# from kpi_display import display_kpis
# from plots import display_tab1, display_tab2

# # Streamlit configuration
# setup_page()  # This must be the first Streamlit command

# if login():
    
#         st.title('📊 CNAS Fraud/Abuse Detection in medication consumption Dashboard')
                 
#         # Setup sidebar and get the selected filter type and filters
#         filter_type, month, trimester, start_date, end_date = setup_sidebar()
        
#         # Load the data based on the selected filters
#         fraud_data = load_fraud_data(filter_type,month=month, trimester=trimester, start_date=start_date, end_date=end_date)
        
#         if fraud_data is not None and not fraud_data.empty:
#             print(fraud_data.columns)  # Log the columns of the loaded data
#             print(fraud_data.head())   # Log the first few rows of the loaded data
#             # Placeholder for the KPIs
#             placeholder = st.empty()
#             with placeholder.container():
#                 display_kpis(fraud_data)

#             # Horizontal line to separate the KPIs from the rest of the content
#             st.markdown('---')

#             # Define tabs
#             tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

#             # Tab 1 content
#             with tab1:
#                 display_tab1(fraud_data)

#             # Tab 2 content
#             with tab2:
#                 display_tab2(fraud_data)
#         else:
#             st.error("Failed to load data. Please check your database connection or query.")
#             print("Failed to load data. Please check your database connection or query.")
import streamlit as st
from config import setup_page
from data import load_fraud_data
from auth import login
from sidebar import setup_sidebar, setup_admin_sidebar
from kpi_display import display_kpis
from plots import display_tab1, display_tab2
import admin_dashboard

# Streamlit configuration - this must be the first Streamlit command
setup_page()
if login():
    st.title('📊 CNAS Fraud/Abuse Detection in Medication Consumption Dashboard')
    
    # Check user role and display the appropriate dashboard
    if st.session_state['role'] in ['data scientist', 'data analyst']:
        # Setup sidebar and get the selected filter type and filters
        filter_type, month, trimester, start_date, end_date = setup_sidebar()
        
        # Load the data based on the selected filters
        fraud_data = load_fraud_data(filter_type, month=month, trimester=trimester, start_date=start_date, end_date=end_date)
        
        if fraud_data is not None and not fraud_data.empty:
            print(fraud_data.columns)  # Log the columns of the loaded data
            print(fraud_data.head())   # Log the first few rows of the loaded data
            
            # Placeholder for the KPIs
            placeholder = st.empty()
            with placeholder.container():
                display_kpis(fraud_data)

            # Horizontal line to separate the KPIs from the rest of the content
            st.markdown('---')

            # Define tabs
            tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

            # Tab 1 content
            with tab1:
                display_tab1(fraud_data)

            # Tab 2 content
            with tab2:
                display_tab2(fraud_data)
        else:
            st.error("Failed to load data. Please check your database connection or query.")
            print("Failed to load data. Please check your database connection or query.")
    elif st.session_state['role'] == 'admin':
        # Setup the admin sidebar
        setup_admin_sidebar()
        
        # Display the admin dashboard
        with admin_dashboard.DatabaseConnection(
            host='localhost',
            user='postgres',
            password='Postgres123',
            database='FraudDetection'
        ) as db:
            admin_dashboard.display_admin_dashboard(db.cursor, db.conn)
    else:
        st.error("You do not have permission to view this dashboard.")
