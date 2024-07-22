import streamlit as st

# Define function to render sidebar
def render_sidebar():
    st.sidebar.title('Company Name')
    st.sidebar.image('path_to_logo.png', use_column_width=True)
    st.sidebar.markdown('[Page 1](#/page1)\n[Page 2](#/page2)\n[Page 3](#/page3)')

# Define function to render top panel
def render_top_panel(page_name):
    st.markdown(f'<h1 style="color:navy;">{page_name}</h1>', unsafe_allow_html=True)

# Main function to run the app
def main():
    st.set_page_config(page_title='Streamlit Web App')
    
    render_sidebar()

    # Determine which page to show based on URL hash
    page = st.experimental_get_query_params().get('page', ['page1'])[0]

    # Render the top panel with page name
    if page == 'page1':
        render_top_panel('Page 1')
        st.write('This is Page 1.')
    elif page == 'page2':
        render_top_panel('Page 2')
        st.write('This is Page 2.')
    elif page == 'page3':
        render_top_panel('Page 3')
        st.write('This is Page 3.')
    else:
        st.error('Page not found')

if __name__ == "__main__":
    main()
