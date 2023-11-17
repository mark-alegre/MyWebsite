import streamlit as st

from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
from dependancies import sign_up, fetch_users





try:
    users = fetch_users()
    emails = []
    usernames = []
    passwords = []

    for user in users:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])

    credentials = {'usernames': {}}
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4)

    email, authentication_status, username = Authenticator.login(':green[Login]', 'main')

    info, info1 = st.columns(2)

    if not authentication_status:
        sign_up()

    if username:
        if username in usernames:
            if authentication_status:
                # let User see app
                st.sidebar.subheader(f'Welcome {username}')
                Authenticator.logout('Log Out', 'sidebar')

                import home, trending, test, your_posts, about
                

                class MultiApp:

                    def __init__(self):
                        self.apps = []

                    def add_app(self, title, func):

                        self.apps.append({
                            "title": title,
                            "function": func
                        })

                    def run():
                        # app = st.sidebar(
                        with st.sidebar:        
                            app = option_menu(
                                menu_title='StarHaze',
                                options=['Home','Account','Trending','Your Posts','about'],
                                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                                menu_icon='chat-text-fill',
                                default_index=1,
                                styles={
                                    "container": {"padding": "5!important","background-color":'black'},
                        "icon": {"color": "white", "font-size": "23px"}, 
                        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                        "nav-link-selected": {"background-color": "#02ab21"},}
                                
                                )

                        
                        if app == "Home":
                            home.app()
                        if app == "Account":
                            test.app()    
                        if app == "Trending":
                            trending.app()        
                        if app == 'Your Posts':
                            your_posts.app()
                        if app == 'about':
                            about.app()    
                            
                        
                            
                    run()            
  

            elif not authentication_status:
                with info:
                    st.error('Incorrect Password or username')
            else:
                with info:
                    st.warning('Please feed in your credentials')
        else:
            with info:
                st.warning('Username does not exist, Please Sign up')


except:
    st.success('Refresh Page')

       