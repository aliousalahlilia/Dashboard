
# import streamlit as st
# import psycopg2

# def check_credentials(username, password):
#     conn = psycopg2.connect(
#         host='localhost',
#         user='postgres',
#         password='Postgres123',
#         database='FraudDetection'
#     )
#     cursor = conn.cursor()
#     cursor.execute("SELECT password, role, Email, Phone FROM credentials WHERE Username=%s", (username,))
#     row = cursor.fetchone()
#     conn.close()
    
#     if row and row[0] == password:
#         st.session_state['role'] = row[1]
#         st.session_state['Email'] = row[2]
#         st.session_state['Phone'] = row[3]
#         return True
#     return False

# def login():
#     if 'logged_in' not in st.session_state:
#         st.session_state['logged_in'] = False

#     if not st.session_state['logged_in']:
#         st.title('🔒 Login')
#         st.write('Welcome to CNAS Fraud Detection Dashboard!')
        
#         with st.form(key='login_form'):
#             username = st.text_input('👤 Username', key='login_username')
#             password = st.text_input('🔒 Password', type='password', key='login_password')
#             login_button = st.form_submit_button('Login')

#             if login_button:
#                 if check_credentials(username, password):
#                     st.session_state['logged_in'] = True
#                     st.experimental_rerun()  # Rerun the app to load the dashboard
#                 else:
#                     st.error('The username or password you entered is incorrect')
#                     st.session_state['logged_in'] = False
#     return st.session_state['logged_in']

import streamlit as st
import psycopg2

def check_credentials(username, password):
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Postgres123',
        database='FraudDetection'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT password, role, Email, Phone FROM credentials WHERE username=%s", (username,))
    row = cursor.fetchone()
    conn.close()
    
    if row and row[0] == password:
        st.session_state['username'] = username  # Save username in session state
        st.session_state['role'] = row[1]
        st.session_state['Email'] = row[2]
        st.session_state['Phone'] = row[3]
        return True
    return False

def login():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        st.title('🔒 Login')
        st.write('Welcome to CNAS Fraud Detection Dashboard!')
        
        with st.form(key='login_form'):
            username = st.text_input('👤 Username', key='login_username')
            password = st.text_input('🔒 Password', type='password', key='login_password')
            login_button = st.form_submit_button('Login')

            if login_button:
                if check_credentials(username, password):
                    st.session_state['logged_in'] = True
                    st.experimental_rerun()  # Rerun the app to load the dashboard
                else:
                    st.error('The username or password you entered is incorrect')
                    st.session_state['logged_in'] = False
    return st.session_state['logged_in']
