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
        /* Reset Streamlit's default background */
        body {
            background-color: #f0f0f0;
        }
        
        /* Style for sidebar */
        .sidebar .sidebar-content {
            background-color: #000000;
            color: white;
            padding-top: 0;
            padding-bottom: 0;
        }
        
        /* Style for sidebar logo and app name */
        .sidebar .sidebar-content .sidebar-section .stMarkdown {
            color: white;
        }
        
        /* Style for top panel */
        .toppanel {
            background-color: #2a4b7c;
            color: white;
            padding: 0.5rem;
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
        }
        
        /* Style for feature list in top panel */
        .toppanel ul {
            display: inline;
            padding: 0;
            margin: 0;
        }
        
        /* Style for sidebar navigation links */
        .sidebar .sidebar-content .sidebar-section .sidebar-list {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }
        
        .sidebar .sidebar-content .sidebar-section .sidebar-list li {
            padding: 0.5rem 1rem;
        }
        
        /* Style for logo in sidebar */
        .sidebar .sidebar-content .sidebar-section .sidebar-logo img {
            max-width: 100%;
            height: auto;
            filter: brightness(0) invert(1); /* Invert color for white logos */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create the sidebar navigation with logo and app name
    st.sidebar.markdown(
        """
        <div class="sidebar-section">
            <div class="sidebar-logo">
                <img src="https://yourcompanylogo.png" alt="Company Logo" width=50>
                <h1 style="margin-left: 1rem; color: #ffffff;">Your App Name</h1>
            </div>
            <ul class="sidebar-list">
                <li><a href="#section-home" style="color: white;">Home</a></li>
                <li><a href="#section-page1" style="color: white;">Page 1</a></li>
                <li><a href="#section-page2" style="color: white;">Page 2</a></li>
                <li><a href="#section-page3" style="color: white;">Page 3</a></li>
            </ul>
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

    # Display different sections based on sidebar selection
    st.markdown("<h2 id='section-home'>Home Section</h2>", unsafe_allow_html=True)
    st.write("Welcome to the home section!")

    st.markdown("<h2 id='section-page1'>Page 1 Section</h2>", unsafe_allow_html=True)
    st.write("Content of Page 1 goes here.")

    st.markdown("<h2 id='section-page2'>Page 2 Section</h2>", unsafe_allow_html=True)
    st.write("Content of Page 2 goes here.")

    st.markdown("<h2 id='section-page3'>Page 3 Section</h2>", unsafe_allow_html=True)
    st.write("Content of Page 3 goes here.")

if __name__ == "__main__":
    main()
