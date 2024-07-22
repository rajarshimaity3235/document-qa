import streamlit as st

# Function to display page content based on sidebar selection
def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ('Home', 'Page 1', 'Page 2'))

    if page == 'Home':
        st.title('Home Page')
        st.write('Welcome to the Home Page.')

    elif page == 'Page 1':
        st.title('Page 1')
        st.write('Welcome to Page 1.')

    elif page == 'Page 2':
        st.title('Page 2')
        st.write('Welcome to Page 2.')

# Sidebar configuration
st.sidebar.markdown(
    """
    <style>
    .sidebar-content {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Top panel configuration
st.markdown(
    """
    <style>
    .reportview-container .main .block-container {
        padding-top: 0px !important;
        background-color: navy;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo and company name
#st.image('your_logo.png', width=200)
st.markdown('# Your Company Name')

# Main content display
main()
