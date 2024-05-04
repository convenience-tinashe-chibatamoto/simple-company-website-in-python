import streamlit as st
import pandas

# Set webpage layout to wide
st.set_page_config(layout="wide")

# Add a header and some other text
st.header("Initech Software Company")
st.write("""
Initech is a leading software development company specializing in the design, development, and delivery of innovative technology solutions. With a team of experienced professionals and a passion for innovation, we help businesses of all sizes navigate the complexities of the digital landscape and achieve their goals efficiently and effectively.

Why Choose Us: At Initech we are dedicated to delivering exceptional service and support to our clients. We take the time to understand their unique needs and goals, and work closely with them to develop tailored solutions that meet their specific requirements. Our commitment to innovation, collaboration, and excellence sets us apart from other software development companies, and we are proud to have earned a reputation as a trusted partner for businesses seeking to leverage technology for success.""")
st.subheader("Our Team")

# Prepare the columns
col1, col2, col3 = st.columns(3)

# Make a dataframe with the company members
df = pandas.read_csv("data.csv")

# Add content to the first column
with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the second column
with col2:
    # Iterate over rows 4 to 7
    for index, row in df[4:8].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])


with col3:
    # Iterate over rows 4 to 7
    for index, row in df[8:].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])




