import streamlit as st
from st_pages import Page, show_pages, add_page_title, Section
from streamlit_extras.stylable_container import stylable_container
from foundry.transforms import Dataset
import pandas as pd
add_page_title()
from datetime import datetime, timedelta
import base64
# logo image
logo_path = "logo.jpg"
with open('logo.jpg', 'rb') as f:
    image_data = f.read()
encoded_string = base64.b64encode(image_data).decode()
data_url = f'data:image/jpeg;base64,{encoded_string}'
st.markdown(f"""
    <style>
    .header-logo {{
        position: absolute;
        top: 10px; /* Adjust this value as needed */
        right: 10px; /* Adjust this value as needed */
        width: 100px;
        height: 40px;
    }}
    </style>
    <div>
        <img src="{data_url}" class="header-logo">
    </div>
    """, unsafe_allow_html=True)
from streamlit_extras.bottom_container import bottom
with bottom():
    st.markdown("---")
    st.write("Version: 0.0.1")



# Create a layout with three columns
col1, col2, col3 = st.columns(3)
 
# Add content to each column with headings and containers
with col1:
    container1 = st.container(border = True)
    with container1:
        st.header("A&E")
        # Add two columns within container A
        sub_col1, sub_col2 = st.columns(2)
        # Add bar charts to the first nested column
        with sub_col1:
            st.area_chart(pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c']))
        # Add bar charts to the second nested column
        with sub_col2:
            st.area_chart(pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c']))
 
with col2:
    container2 = st.container(border = True)
    with container2:
        st.header("Ambulance")
        # Add two columns within container B
        sub_col1, sub_col2 = st.columns(2)
        # Add bar charts to the first nested column
        with sub_col1:
            st.area_chart(pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c']))
        # Add bar charts to the second nested column
        with sub_col2:
            st.area_chart(pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c']))
 
with col3:
    container3 = st.container(border = True)
    with container3:
        st.header("111")
        # Add two columns within container C
        sub_col1, sub_col2 = st.columns(2)
        # Add bar charts to the first nested column
        with sub_col1:
            st.area_chart(pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c']))
        # Add bar charts to the second nested column
        with sub_col2:
            st.area_chart(pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c']))
