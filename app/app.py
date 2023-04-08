import streamlit as st

# Set page title
st.set_page_config(page_title="My Awesome Streamlit App")

# Add title and subtitle to the app
st.title("Welcome to my Streamlit app!")
st.subheader("Here's some things you can do:")

# Add a checkbox to show/hide content
if st.checkbox("Show some text"):
    st.write("You can add some text here.")

# Add a selectbox for options
option = st.selectbox("Choose an option:", ("Option 1", "Option 2", "Option 3"))

# Show the selected option
st.write("You selected:", option)

# Add a slider to the sidebar
add_slider = st.sidebar.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0)
)
st.sidebar.write("You selected:", add_slider)

# Add a button
if st.button("Click me"):
    st.write("You clicked the button!")

# Add code block
with st.beta_expander("See the code"):
    st.code("""
        import pandas as pd
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': [4, 5, 6]
        })
        st.dataframe(df)
    """)

# Add footer text
footer = """
Made with ❤️ by [Your Name](https://your-website.com)
"""
st.markdown(footer, unsafe_allow_html=True)