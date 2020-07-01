import streamlit as st
import datetime
import pandas as pd
from PIL import Image
import time
st.sidebar.header('智慧政务系统')



# image = Image.open('image.jpg')
# st.sidebar.image(image, 
#           use_column_width=True)

option = st.sidebar.selectbox('请选择要进行的操作',('文本评价', '文本分类', '热点挖掘'),index = 0)
if option == '文本评价':
    st.title('问政回复评价系统')
    st.markdown('Government response evaluation system')

if option == '文本分类':
    st.title('问政文本分类系统')
    st.markdown('Message Text Classification System')


if option == '热点挖掘':
    st.title('问政热点挖掘系统')


