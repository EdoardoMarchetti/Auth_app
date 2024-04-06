import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.exceptions import (CredentialsError,
                                                          ForgotError,
                                                          LoginError,
                                                          RegisterError,
                                                          ResetError,
                                                          UpdateError) 

# # Loading config file
# with open('./config.yaml', 'r', encoding='utf-8') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# # Creating the authenticator object
# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['pre-authorized']
# )

credentials = dict(st.secrets['credentials'])

authenticator = stauth.Authenticate(
    credentials,
    st.secrets['cookie']['name'],
    st.secrets['cookie']['key'],
    st.secrets['cookie']['expiry_days'],
    st.secrets['pre-authorized']
)

print('-------------------------')
print('Chiavi sessione')
for k in st.session_state.keys():
    print(k)
print('-------------------------')

st.button('Ciao')


# Creating a login widget
#try:
#    authenticator.login()
#except LoginError as e:
#    st.error(e)



#if st.session_state["authentication_status"]:
#    authenticator.logout()
#    st.write(f'Welcome *{st.session_state["name"]}*')
#    st.title('Now you can visit the pages')
#elif st.session_state["authentication_status"] is False:
#    st.error('Username/password is incorrect')
#elif st.session_state["authentication_status"] is None:
#    st.warning('Please enter your username and password')
