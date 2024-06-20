# import streamlit as st

# def setup_sidebar():
#     st.sidebar.title('CNAS Dashboard')
#     admin_info = st.sidebar.container()
#     with admin_info:
#         username = st.session_state.get('username', 'Unknown User')
#         role = st.session_state.get('role', 'Unknown Role')
#         email = st.session_state.get('Email', 'user@cnas.dz')
#         phone = st.session_state.get('Phone', '+213 555 666 777')
#         html_content = f"""
#         <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
#         <div style="text-align: center;">
#             <h2 style="color:#0072bb;">Admin Info</h2>
#             <span class="material-icons" style="font-size:50px;color:#0072bb;">person</span>
#             <p>{username}</p>
#             <p>{role}</p>
#             <p>Data Science Department</p>
#         </div>
#         """
#         st.sidebar.markdown(html_content, unsafe_allow_html=True)
#         st.sidebar.markdown('---')
#         st.sidebar.subheader('Contact Us')
#         st.sidebar.write(f'Email: {email}')
#         st.sidebar.write(f'Phone: {phone}')
#         st.sidebar.markdown('---')
#         if st.sidebar.button('Log out'):
#             st.session_state['logged_in'] = False
#         st.sidebar.subheader('About')
#         st.sidebar.write('This dashboard provides insights and analysis on fraud detection in the CNAS.')


# import streamlit as st

# def setup_sidebar():
#     st.sidebar.title('CNAS Dashboard')
#     admin_info = st.sidebar.container()
#     with admin_info:
#         username = st.session_state.get('username', 'Unknown User')
#         role = st.session_state.get('role', 'Unknown Role')
#         email = st.session_state.get('Email', 'user@cnas.dz')
#         phone = st.session_state.get('Phone', '+213 555 666 777')
#         html_content = f"""
#         <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
#         <div style="text-align: center;">
#             <h2 style="color:#0072bb;">Admin Info</h2>
#             <span class="material-icons" style="font-size:50px;color:#0072bb;">person</span>
#             <p>{username}</p>
#             <p>{role}</p>
#             <p>Data Science Department</p>
#         </div>
#         """
#         st.sidebar.markdown(html_content, unsafe_allow_html=True)
#         st.sidebar.markdown('---')
#         st.sidebar.subheader('Contact Us')
#         st.sidebar.write(f'📧 Email: {email}')
#         st.sidebar.write(f'📞 Phone: {phone}')
#         st.sidebar.markdown('---')
#         # logout button
#         if st.sidebar.button('Log out'):
#             st.session_state['logged_in'] = False

#         st.sidebar.subheader('About')
#         st.sidebar.write('This dashboard provides insights and analysis on fraud detection in the CNAS system.')


# import streamlit as st
# from datetime import datetime

# def setup_sidebar():
#     st.sidebar.title('CNAS Dashboard')
#     admin_info = st.sidebar.container()
#     with admin_info:
#         username = st.session_state.get('username', 'Unknown User')
#         role = st.session_state.get('role', 'Unknown Role')
#         email = st.session_state.get('Email', 'user@cnas.dz')
#         phone = st.session_state.get('Phone', '+213 555 666 777')
#         html_content = f"""
#         <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
#         <div style="text-align: center;">
#             <h2 style="color:#0072bb;">Admin Info</h2>
#             <span class="material-icons" style="font-size:50px;color:#0072bb;">person</span>
#             <p>{username}</p>
#             <p>{role}</p>
#             <p>Data Science Department</p>
#         </div>
#         """
#         st.sidebar.markdown(html_content, unsafe_allow_html=True)
#         st.sidebar.markdown('---')
#         st.sidebar.subheader('Contact Us')
#         st.sidebar.write(f'📧 Email: {email}')
#         st.sidebar.write(f'📞 Phone: {phone}')
#         st.sidebar.markdown('---')
#         # logout button
#         if st.sidebar.button('Log out'):
#             st.session_state['logged_in'] = False

#         st.sidebar.subheader('About')
#         st.sidebar.write('This dashboard provides insights and analysis on fraud detection in the CNAS system.')

#     st.sidebar.markdown('---')
#     st.sidebar.subheader('Data Filter')
#     filter_type = st.sidebar.radio("Filter Type", ["Month", "Trimester", "Date Range"])
#     month = None
#     trimester = None
#     start_date = None
#     end_date = None

#     if filter_type == "Month":
#         month = st.sidebar.number_input("Select Month", min_value=1, max_value=12, step=1)
#     elif filter_type == "Trimester":
#         trimester = st.sidebar.number_input("Select Trimester", min_value=1, max_value=4, step=1)
#     elif filter_type == "Date Range":
#         start_date = st.sidebar.date_input("Start Date", value=datetime(2023, 1, 1))
#         end_date = st.sidebar.date_input("End Date", value=datetime(2023, 6, 30))

#     return filter_type, month, trimester, start_date, end_date
# import streamlit as st
# from datetime import datetime

# def setup_sidebar():
#     st.sidebar.title('CNAS Dashboard')
#     admin_info = st.sidebar.container()
#     with admin_info:
#         username = st.session_state.get('username', 'Unknown User')
#         role = st.session_state.get('role', 'Unknown Role')
#         email = st.session_state.get('Email', 'user@cnas.dz')
#         phone = st.session_state.get('Phone', '+213 555 666 777')
#         html_content = f"""
#         <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
#         <div style="text-align: center;">
#             <h2 style="color:#0072bb;">Admin Info</h2>
#             <span class="material-icons" style="font-size:50px;color:#0072bb;">person</span>
#             <p>{username}</p>
#             <p>{role}</p>
#             <p>Data Science Department</p>
#         </div>
#         """
#         st.sidebar.markdown(html_content, unsafe_allow_html=True)
#         st.sidebar.markdown('---')

#     # Add the data filter options
#     st.sidebar.subheader('Data Filter')
#     filter_type = st.sidebar.radio("Filter Type", ["Month", "Trimester", "Date Range"])
#     month = None
#     trimester = None
#     start_date = None
#     end_date = None

#     if filter_type == "Month":
#         month = st.sidebar.number_input("Select Month", min_value=1, max_value=12, step=1)
#     elif filter_type == "Trimester":
#         trimester = st.sidebar.number_input("Select Trimester", min_value=1, max_value=4, step=1)
#     elif filter_type == "Date Range":
#         start_date = st.sidebar.date_input("Start Date", value=datetime(2023, 1, 1))
#         end_date = st.sidebar.date_input("End Date", value=datetime(2023, 6, 30))

#     st.sidebar.markdown('---')
#     st.sidebar.subheader('Contact Us')
#     st.sidebar.write(f'📧 Email: {email}')
#     st.sidebar.write(f'📞 Phone: {phone}')
#     st.sidebar.markdown('---')

#     # logout button
#     if st.sidebar.button('Log out'):
#         st.session_state['logged_in'] = False
#         st.experimental_rerun()  # Immediately rerun the app to show the login form

#     st.sidebar.subheader('About')
#     st.sidebar.write('This dashboard provides insights and analysis on fraud detection in the CNAS system.')

#     return filter_type, month, trimester, start_date, end_date
# import streamlit as st
# from datetime import datetime

# def setup_sidebar():
#     st.sidebar.title('CNAS Dashboard')
#     admin_info = st.sidebar.container()
#     with admin_info:
#         username = st.session_state.get('username', 'Unknown User')
#         role = st.session_state.get('role', 'Unknown Role')
#         email = st.session_state.get('Email', 'user@cnas.dz')
#         phone = st.session_state.get('Phone', '+213 555 666 777')
#         html_content = f"""
#         <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
#         <div style="text-align: center;">
#             <h2 style="color:#0072bb;">Admin Info</h2>
#             <span class="material-icons" style="font-size:50px;color:#0072bb;">person</span>
#             <p>{username}</p>
#             <p>{role}</p>
#             <p>Data Science Department</p>
#         </div>
#         """
#         st.sidebar.markdown(html_content, unsafe_allow_html=True)
#         st.sidebar.markdown('---')

#     # Add the data filter options
#     st.sidebar.subheader('Data Filter')
#     filter_type = st.sidebar.radio("Filter Type", ["Month", "Trimester", "Date Range"])
#     month = None
#     trimester = None
#     start_date = None
#     end_date = None

#     if filter_type == "Month":
#         month = st.sidebar.number_input("Select Month", min_value=1, max_value=12, step=1)
#     elif filter_type == "Trimester":
#         trimester = st.sidebar.number_input("Select Trimester", min_value=1, max_value=4, step=1)
#     elif filter_type == "Date Range":
#         start_date = st.sidebar.date_input("Start Date", value=datetime(2023, 1, 1))
#         end_date = st.sidebar.date_input("End Date", value=datetime(2023, 6, 30))

#     st.sidebar.markdown('---')
#     st.sidebar.subheader('Contact Us')
#     st.sidebar.write(f'📧 Email: {email}')
#     st.sidebar.write(f'📞 Phone: {phone}')
#     st.sidebar.markdown('---')

#     # logout button
#     if st.sidebar.button('Log out'):
#         st.session_state['logged_in'] = False
#         st.experimental_rerun()  # Immediately rerun the app to show the login form

#     st.sidebar.subheader('About')
#     st.sidebar.write('This dashboard provides insights and analysis on fraud detection in the CNAS system.')

#     return filter_type, month, trimester, start_date, end_date


import streamlit as st
from datetime import datetime

def setup_sidebar():
    st.sidebar.title('CNAS Dashboard')
    admin_info = st.sidebar.container()
    with admin_info:
        username = st.session_state.get('username', 'Unknown User')
        role = st.session_state.get('role', 'Unknown Role')
        email = st.session_state.get('Email', 'user@cnas.dz')
        phone = st.session_state.get('Phone', '+213 555 666 777')
        html_content = f"""
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <div style="text-align: center;">
            <h2 style="color:#0072bb;">User Info</h2>
            <span class="material-icons" style="font-size:50px;color:#0072bb;">person</span>
            <p>{username}</p>
            <p>{role}</p>
            <p>Data Science Department</p>
        </div>
        """
        st.sidebar.markdown(html_content, unsafe_allow_html=True)
        st.sidebar.markdown('---')

    # Add the data filter options
    st.sidebar.subheader('Data Filter')
    filter_type = st.sidebar.radio("Filter Type", ["Month", "Trimester", "Date Range"])
    month = None
    trimester = None
    start_date = None
    end_date = None

    if filter_type == "Month":
        month = st.sidebar.number_input("Select Month", min_value=1, max_value=12, step=1)
    elif filter_type == "Trimester":
        trimester = st.sidebar.number_input("Select Trimester", min_value=1, max_value=4, step=1)
    elif filter_type == "Date Range":
        start_date = st.sidebar.date_input("Start Date", value=datetime(2023, 1, 1))
        end_date = st.sidebar.date_input("End Date", value=datetime(2023, 6, 30))

    st.sidebar.markdown('---')
    st.sidebar.subheader('Contact Us')
    st.sidebar.write(f'📧 Email: {email}')
    st.sidebar.write(f'📞 Phone: {phone}')
    st.sidebar.markdown('---')

    # Logout button
    if st.sidebar.button('Log out'):
        st.session_state['logged_in'] = False
        st.experimental_rerun()  # Immediately rerun the app to show the login form

    st.sidebar.subheader('About')
    st.sidebar.write('This dashboard provides insights and analysis on fraud detection in the CNAS system.')

    return filter_type, month, trimester, start_date, end_date

def setup_admin_sidebar():
    st.sidebar.title('CNAS Dashboard')
    admin_info = st.sidebar.container()
    with admin_info:
        username = st.session_state.get('username', 'Unknown User')
        role = st.session_state.get('role', 'Admin')
        email = st.session_state.get('Email', 'user@cnas.dz')
        phone = st.session_state.get('Phone', '+213 555 666 777')
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

    st.sidebar.subheader('Contact Us')
    st.sidebar.write(f'📧 Email: {email}')
    st.sidebar.write(f'📞 Phone: {phone}')
    st.sidebar.markdown('---')
    
    # Logout button
    if st.sidebar.button('Log out'):
        st.session_state['logged_in'] = False
        st.experimental_rerun()  # Immediately rerun the app to show the login form

    st.sidebar.subheader('About')
    st.sidebar.write('This dashboard provides insights and analysis on fraud detection in the CNAS system.')
