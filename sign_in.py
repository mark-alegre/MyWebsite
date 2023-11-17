import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re

DETA_KEY = 'c01xrwf27rc_LKFXSYWwzkWgaMvkvkpq8jqvx61nTVFH'

def sign_up():
    with st.form(key='signup', clear_on_submit=True):
        st.subheader(':green[Sign Up]')
        email = st.text_input('Email', placeholder='Enter Your Email')
        username = st.text_input('Username', placeholder='Enter Your Username')
        password1 = st.text_input('Password', placeholder='Enter Your Password', type='password')
        password2 = st.text_input('Password', placeholder='Conform Your Password', type='password')