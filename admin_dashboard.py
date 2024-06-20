import streamlit as st
import psycopg2
from datetime import datetime

# Context manager for database connection
class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conn.close()

# Function to fetch all users
def fetch_all_users(cursor):
    cursor.execute("SELECT username, role, date_created FROM credentials")
    return cursor.fetchall()

# Function to add a new user
def add_user(cursor, conn, username, password, role):
    cursor.execute("INSERT INTO credentials (username, password, role, date_created) VALUES (%s, %s, %s, NOW())", (username, password, role))
    conn.commit()

# Function to delete a user
def delete_user(cursor, conn, username):
    cursor.execute("DELETE FROM credentials WHERE username=%s", (username,))
    conn.commit()

# Function to update a user's role
def update_user_role(cursor, conn, username, new_role):
    cursor.execute("UPDATE credentials SET role=%s WHERE username=%s", (new_role, username))
    conn.commit()

# Function to fetch active sessions count
def fetch_active_sessions_count(cursor):
    cursor.execute("SELECT COUNT(*) FROM sessions WHERE is_active = TRUE")
    return cursor.fetchone()[0]

# Function to set today's date for existing users
def update_existing_users_date(cursor, conn):
    cursor.execute("UPDATE credentials SET date_created = NOW() WHERE date_created IS NULL")
    conn.commit()
def display_admin_dashboard(cursor, conn):
    st.markdown("""
        <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        .user-table {
            width: 100%;
            border-collapse: collapse;
            border-spacing: 0; /* Ensures no spacing between cells */
        }

        .user-table th, .user-table td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
            line-height: 1;
            height: 40px; /* Set a fixed height */
        }

        .user-table th {
            background-color: #0072bb;
            color: white;
            padding: 8px;
        }

        .user-table td {
            background-color: white;
        }

        .action-buttons {
            display: flex;
            gap: 5px;
        }
        .action-button {
            background-color: white;
            color: black;
            border: 1px solid #ddd;
            padding: 5px;
            cursor: pointer;
            font-size: 12px;
            width: 32px;
            height: 32px;
        }
        .action-button:hover {
            background-color: #f0f0f0;
        }
        </style>
        """, unsafe_allow_html=True)

    st.header("User Management")

    # Update existing users' date_created to today
    update_existing_users_date(cursor, conn)

    # Fetch and display users
    users = fetch_all_users(cursor)
    st.write("Manage users:")

    # Add button for adding new user
    if st.button('Add New User', key="add_user_button", help="Add new user"):
        st.session_state.show_add_user_form = True

    # Display user table header
    cols = st.columns([1, 2, 2, 2, 2])
    headers = ["#", "Name", "Date Created", "Role", "Action"]
    for col, header in zip(cols, headers):
        col.markdown(f"<div style='background-color: #0072bb; color: white; padding: 8px; border: 1px solid #ddd; height: 40px;'>{header}</div>", unsafe_allow_html=True)

    role_options = ["admin", "data scientist", "data analyst", "mlops"]

    for idx, user in enumerate(users, start=1):
        username = user[0]
        role = user[1]
        date_created = user[2].strftime('%Y-%m-%d') if user[2] else datetime.now().strftime('%Y-%m-%d')  # Default to today if date_created is None

        with st.form(key=f"form_{username}", clear_on_submit=True):
            cols = st.columns([1, 2, 2, 2, 2])
            cols[0].markdown(f"<div style='padding: 0px; border: 1px solid #ddd; background-color: white; height: 40px;'>{idx}</div>", unsafe_allow_html=True)
            cols[1].markdown(f"<div style='padding: 0px; border: 1px solid #ddd; background-color: white; height: 40px;'>{username}</div>", unsafe_allow_html=True)
            cols[2].markdown(f"<div style='padding: 0px; border: 1px solid #ddd; background-color: white; height: 40px;'>{date_created}</div>", unsafe_allow_html=True)
            new_role = cols[3].selectbox("", role_options, index=role_options.index(role), key=f"role_{username}")
            with cols[4]:
                save_button = st.form_submit_button("💾")
                delete_button = st.form_submit_button("❌")

            if save_button:
                update_user_role(cursor, conn, username, new_role)
                st.experimental_rerun()
            if delete_button:
                delete_user(cursor, conn, username)
                st.experimental_rerun()

    if st.session_state.get('show_add_user_form', False):
        with st.form(key='add_user_form'):
            st.write("Add New User")
            new_username = st.text_input("New Username")
            new_password = st.text_input("New Password", type="password")
            new_role = st.selectbox("New Role", role_options)
            add_user_button = st.form_submit_button("Add User")
            if add_user_button:
                if new_username and new_password:
                    add_user(cursor, conn, new_username, new_password, new_role)
                    st.success(f"User {new_username} added successfully")
                    st.experimental_rerun()
                else:
                    st.error("Username and password cannot be empty")

    # System Settings Section
    st.subheader("System Settings")
    st.text("Configure application settings here.")
    # Add your system settings controls here
    
    # Notifications and Alerts Section
    st.subheader("Settings for Notifications and Alerts")
    st.text("Configure notifications and alert settings here.")
    # Add your notifications and alerts controls here

    # Additional Configuration Options Section
    st.subheader("Additional Configuration Options")
    st.text("Additional configuration options here.")
    # Add your additional configuration options here

    # High-Level KPIs Section
    st.subheader("High-Level KPIs")
    st.text("Overview of key performance indicators.")
    st.metric(label="Total Users", value=len(users))
    
    active_sessions = fetch_active_sessions_count(cursor)
    st.metric(label="Active Sessions", value=active_sessions)  # Use real data
    
    st.metric(label="System Uptime", value="99.9%")

# Streamlit configuration
st.set_page_config(page_title="Admin Dashboard", layout="wide")

# Main execution
if __name__ == "__main__":
    with DatabaseConnection(host='localhost', user='postgres', password='Postgres123', database='FraudDetection') as db:
        display_admin_dashboard(db.cursor, db.conn)

# import streamlit as st
# import pandas as pd
# import psycopg2
# from datetime import datetime

# # Context manager for database connection
# class DatabaseConnection:
#     def __init__(self, host, user, password, database):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.database = database
#         self.conn = None
#         self.cursor = None

#     def __enter__(self):
#         self.conn = psycopg2.connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database
#         )
#         self.cursor = self.conn.cursor()
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.cursor.close()
#         self.conn.close()

# # Function to fetch all users
# def fetch_all_users_df(cursor):
#     cursor.execute("SELECT username, role, date_created FROM credentials")
#     rows = cursor.fetchall()
#     return pd.DataFrame(rows, columns=["Name", "Role", "Date Created"])

# # Function to add a new user
# def add_user(cursor, conn, username, password, role):
#     cursor.execute("INSERT INTO credentials (username, password, role, date_created) VALUES (%s, %s, %s, NOW())", (username, password, role))
#     conn.commit()

# # Function to delete a user
# def delete_user(cursor, conn, username):
#     cursor.execute("DELETE FROM credentials WHERE username=%s", (username,))
#     conn.commit()

# # Function to update a user's role
# def update_user_role(cursor, conn, username, new_role):
#     cursor.execute("UPDATE credentials SET role=%s WHERE username=%s", (new_role, username))
#     conn.commit()

# # Function to fetch active sessions count
# def fetch_active_sessions_count(cursor):
#     cursor.execute("SELECT COUNT(*) FROM sessions WHERE is_active = TRUE")
#     return cursor.fetchone()[0]

# # Function to set today's date for existing users
# def update_existing_users_date(cursor, conn):
#     cursor.execute("UPDATE credentials SET date_created = NOW() WHERE date_created IS NULL")
#     conn.commit()

# # Function to display admin dashboard
# def display_admin_dashboard(cursor, conn):
#     st.header("User Management")

#     # Update existing users' date_created to today
#     update_existing_users_date(cursor, conn)

#     # Fetch and display users
#     users_df = fetch_all_users_df(cursor)
#     users_df['Date Created'] = users_df['Date Created'].apply(lambda x: x.strftime('%Y-%m-%d') if x else datetime.now().strftime('%Y-%m-%d'))

#     role_options = ["admin", "data scientist", "data analyst", "mlops"]

#     def get_table_download_link(df):
#         """Generates a link allowing the data in a given panda dataframe to be downloaded
#         in:  dataframe
#         out: href string
#         """
#         csv = df.to_csv(index=False)
#         b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
#         href = f'<a href="data:file/csv;base64,{b64}" download="users.csv">Download csv file</a>'
#         return href

#     def render_html_table(users_df):
#         # Generate HTML table
#         table_html = """
#         <table class="user-table">
#             <thead>
#                 <tr>
#                     <th>#</th>
#                     <th>Name</th>
#                     <th>Date Created</th>
#                     <th>Role</th>
#                     <th>Actions</th>
#                 </tr>
#             </thead>
#             <tbody>
#         """
#         for idx, row in users_df.iterrows():
#             table_html += f"""
#                 <tr>
#                     <td>{idx + 1}</td>
#                     <td>{row['Name']}</td>
#                     <td>{row['Date Created']}</td>
#                     <td>{row['Role']}</td>
#                     <td>
#                         <button onclick="window.location.href = '?edit={row['Name']}'">✏️</button>
#                         <button onclick="window.location.href = '?delete={row['Name']}'">🗑️</button>
#                     </td>
#                 </tr>
#             """
#         table_html += """
#             </tbody>
#         </table>
#         <style>
#         .user-table {
#             width: 100%;
#             border-collapse: collapse;
#             border-spacing: 0;
#         }
#         .user-table th, .user-table td {
#             border: 1px solid #ddd;
#             padding: 8px;
#             text-align: left;
#             line-height: 1;
#         }
#         .user-table th {
#             background-color: #0072bb;
#             color: white;
#         }
#         .user-table td {
#             background-color: white;
#         }
#         .user-table button {
#             background-color: white;
#             color: black;
#             border: 1px solid #ddd;
#             padding: 5px;
#             cursor: pointer;
#             font-size: 12px;
#             width: 32px;
#             height: 32px;
#         }
#         .user-table button:hover {
#             background-color: #f0f0f0;
#         }
#         </style>
#         """
#         return table_html

#     # Add new user form
#     if st.button('Add New User', key="add_user_button"):
#         st.session_state.show_add_user_form = True

#     if st.session_state.get('show_add_user_form', False):
#         with st.form(key='add_user_form'):
#             st.write("Add New User")
#             new_username = st.text_input("New Username")
#             new_password = st.text_input("New Password", type="password")
#             new_role = st.selectbox("New Role", role_options)
#             add_user_button = st.form_submit_button("Add User")
#             if add_user_button:
#                 if new_username and new_password:
#                     add_user(cursor, conn, new_username, new_password, new_role)
#                     st.success(f"User {new_username} added successfully")
#                     st.experimental_rerun()
#                 else:
#                     st.error("Username and password cannot be empty")

#     # Handle edit and delete actions
#     query_params = st.experimental_get_query_params()
#     if 'edit' in query_params:
#         username_to_edit = query_params['edit'][0]
#         new_role = st.selectbox("Select new role", role_options, index=role_options.index(users_df.loc[users_df['Name'] == username_to_edit, 'Role'].values[0]))
#         if st.button("Save Changes"):
#             update_user_role(cursor, conn, username_to_edit, new_role)
#             st.success(f"User {username_to_edit} role updated to {new_role}")
#             st.experimental_rerun()
#     elif 'delete' in query_params:
#         username_to_delete = query_params['delete'][0]
#         if st.button("Confirm Delete"):
#             delete_user(cursor, conn, username_to_delete)
#             st.success(f"User {username_to_delete} deleted")
#             st.experimental_rerun()

#     # Display the table
#     st.markdown(render_html_table(users_df), unsafe_allow_html=True)

#     # System Settings Section
#     st.subheader("System Settings")
#     st.text("Configure application settings here.")
#     # Add your system settings controls here

#     # Notifications and Alerts Section
#     st.subheader("Settings for Notifications and Alerts")
#     st.text("Configure notifications and alert settings here.")
#     # Add your notifications and alerts controls here

#     # Additional Configuration Options Section
#     st.subheader("Additional Configuration Options")
#     st.text("Additional configuration options here.")
#     # Add your additional configuration options here

#     # High-Level KPIs Section
#     st.subheader("High-Level KPIs")
#     st.text("Overview of key performance indicators.")
#     st.metric(label="Total Users", value=len(users_df))

#     active_sessions = fetch_active_sessions_count(cursor)
#     st.metric(label="Active Sessions", value=active_sessions)  # Use real data

#     st.metric(label="System Uptime", value="99.9%")

# # Streamlit configuration
# st.set_page_config(page_title="Admin Dashboard", layout="wide")

# # Main execution
# if __name__ == "__main__":
#     with DatabaseConnection(host='localhost', user='postgres', password='Postgres123', database='FraudDetection') as db:
#         display_admin_dashboard(db.cursor, db.conn)
