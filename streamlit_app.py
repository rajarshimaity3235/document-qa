import streamlit as st

# Function to render different pages based on user selection
def render_page(page):
    if page == "Page 1":
        render_page1()
    elif page == "Page 2":
        render_page2()
    elif page == "Page 3":
        render_page3()

# Function to render Page 1 content
def render_page1():
    st.title("Page 1")
    st.write("Welcome to Page 1")

# Function to render Page 2 content
def render_page2():
    st.title("Page 2")
    st.write("Welcome to Page 2")

# Function to render Page 3 content
def render_page3():
    st.title("Page 3")
    st.write("Welcome to Page 3")

# Sidebar with navigation links
st.sidebar.title('Navigation')
pages = ["Page 1", "Page 2", "Page 3"]
selection = st.sidebar.radio("Go to", pages)

# Top panel with logo, company name, and title
st.markdown(
    """
    <div style="background-color: navy; padding: 0.1px; color: white;">
        <h1 style="color: white; text-align: center;">Company Name</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Render the selected page
render_page(selection)
