import streamlit as st

# Define the function to display each page
def page_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def page_about():
    st.title("About Page")
    st.write("This is the About Page.")

def page_contact():
    st.title("Contact Page")
    st.write("You can contact us here.")

# Upload your logo image
logo = st.sidebar.file_uploader("Upload Logo", type=["png", "jpg", "jpeg"])

# Create the sidebar with links to different pages and logo display
st.sidebar.image(logo, use_column_width=True) if logo else None
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "About", "Contact"))

# Display the selected page based on user selection
if page == "Home":
    page_home()
elif page == "About":
    page_about()
elif page == "Contact":
    page_contact()

# Customizing the appearance of the app
st.markdown(
    """
    <style>
    .st-bw {
        background-color: black !important;
    }
    .css-1vupu7s {
        padding-top: 0px !important;
    }
    .css-1y9fo8r {
        background-color: #001F3F !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
