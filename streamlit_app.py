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
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
        )        
        .reportview-container .main .block-container {
            max-width: 1200px;
            padding-top: 2rem;
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
            filter: brightness(0) invert(1); /* Invert color for white logos */
        }
        .sidebar .sidebar-content .sidebar-section {
            margin-bottom: 2rem;
        }
        .sidebar .sidebar-content .sidebar-section .sidebar-title {
            padding: 0.5rem 1rem;
            margin-bottom: 0.5rem;
        }
        .sidebar .sidebar-content .sidebar-section ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }
        .sidebar .sidebar-content .sidebar-section ul li {
            padding: 0.5rem 1rem;
        }
        .toppanel {
            background-color: #2a4b7c;
            padding: 0.5rem;
            margin-bottom: 2rem;
            color: white;
        }
        .toppanel h3 {
            display: inline;
            margin-right: 1rem;
        }
        .toppanel ul {
            display: inline;
            padding: 0;
            margin: 0;
        }
        .toppanel ul li {
            display: inline;
            margin-right: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create the sidebar navigation with logo
    st.sidebar.markdown(
        """
        <div class="logo">
            <img src="https://yourcompanylogo.png" alt="Company Logo" width=50>
            <h1 style="margin-left: 1rem; color: #ffffff;">Your App Name</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Create the top panel with feature names
    st.markdown(
        """
        <div class="toppanel">
            <h3>Features:</h3>
            <ul>
                <li>Feature 1</li>
                <li>Feature 2</li>
                <li>Feature 3</li>
                <!-- Add more features as needed -->
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Create the sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "",
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
