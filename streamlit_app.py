import streamlit as st

# Define page names and corresponding functions (replace with your actual pages)
page_names = ["Home", "Page 2", "Page 3"]
page_functions = [st.write("This is the Home page"), st.write("This is Page 2"), st.write("This is Page 3")]

# Custom CSS for styling (place in your main app file)
st.set_page_config(page_title="Your App Name", page_icon=":gear:", layout="wide")  # Set page title, icon, and wide layout

def add_style():
    """
    Adds custom CSS for the app's styling.
    """
    style = """
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #f0f2f5;  /* Light background for main content area */
        }

        .stApp {
            padding: 10px;  /* Adjust padding as needed for minimal top space */
        }

        .reportview-container .sidebar .sidebar-content {
            background-color: #000 !important;  /* Black sidebar background */
            color: #fff;  /* White text for sidebar */
            padding: 15px;  /* Add some padding for aesthetics */
        }

        .reportview-container .main .block-container {
            padding-top: 20px;  /* Increase padding for minimal top space in main content */
        }

        .reportview-container .main .block-container h1 {
            margin-top: 0;  /* Remove default top margin for heading */
        }

        .reportview-container .main .annotation {
            color: #333;  /* Adjust annotation text color */
        }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

add_style()  # Call the styling function

# Header with logo (replace with your logo image)
st.markdown(
    """
    <div style="display: flex; align-items: center; padding: 10px 20px; background-color: #000; color: #fff;">
        <img src="https://placeholdit.img/30x30" alt="Logo" style="margin-right: 10px;">
        <h1>Your App Name</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar navigation
selection = st.sidebar.selectbox("Select a page", page_names)

# Display the selected page content
for i, page_name in enumerate(page_names):
    if selection == page_name:
        page_functions[i]()
