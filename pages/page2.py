import streamlit as st
import time
import numpy as np
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.exceptions import (CredentialsError,
                                                          ForgotError,
                                                          LoginError,
                                                          RegisterError,
                                                          ResetError,
                                                          UpdateError) 
import yaml
from yaml.loader import SafeLoader


# # Loading config file
# with open('./config.yaml', 'r', encoding='utf-8') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# Creating the authenticator object
authenticator = stauth.Authenticate(
    dict(st.secrets['credentials']),
    st.secrets['cookie']['name'],
    st.secrets['cookie']['key'],
    st.secrets['cookie']['expiry_days'],
    st.secrets['pre-authorized']
)

if st.session_state["authentication_status"]:
    authenticator.logout()
    #st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Page 2')
    st.markdown('unlocked')
else: 
    st.error('Please come back to main page and login')
