import streamlit as st

def main():
    # Set page title and favicon
    st.set_page_config(
        page_title="Your App Name",
        page_icon=":rocket:",
        layout="wide"
    )

    # Define the layout of the app
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #2a4b7c;
            color: white;
        }
        .reportview-container .main .block-container {
            max-width: 1200px;
            padding-top: 2rem;
        }
        .toppanel {
            background-color: #2a4b7c;
            padding: 0.5rem;
            margin-bottom: 2rem;
            color: white;
        }
        .logo {
            display: flex;
            align-items: center;
            padding-left: 1rem;
            padding-top: 1rem;
        }
        .logo img {
            max-width: 100%;
            height: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create the top panel with company logo and feature names
    st.markdown(
        """
        <div class="toppanel">
            <div class="logo">
                <img src="https://yourcompanylogo.png" alt="Company Logo" width=100>
                <h1 style="margin-left: 1rem;">Your App Name</h1>
            </div>
            <h3>Features:</h3>
            <ul>
                <li><a href="#section-1">Feature 1</a></li>
                <li><a href="#section-2">Feature 2</a></li>
                <li><a href="#section-3">Feature 3</a></li>
                <!-- Add more features as needed -->
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Create the sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        ("Home", "Page 1", "Page 2", "Page 3")
    )

    # Display different pages based on sidebar selection
    if page == "Home":
        st.header("Home Page")
        st.write("Welcome to the home page!")

    elif page == "Page 1":
        st.header("Page 1")
        st.write("Content of Page 1 goes here.")

    elif page == "Page 2":
        st.header("Page 2")
        st.write("Content of Page 2 goes here.")

    elif page == "Page 3":
        st.header("Page 3")
        st.write("Content of Page 3 goes here.")

if __name__ == "__main__":
    main()
