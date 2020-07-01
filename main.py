import streamlit as st
import datetime
import pandas as pd
from PIL import Image
import time
import sys
sys.path.append('fenlei/code')
sys.path.append('hot_mining')
sys.path.append('evaluation')
from getLabel_new import getLabel
from hot import getHot
from Q3 import test
st.sidebar.header('智慧政务系统')



# image = Image.open('image.jpg')
# st.sidebar.image(image, 
#           use_column_width=True)

option = st.sidebar.selectbox('请选择要进行的操作',('文本评价', '文本分类', '热点挖掘'),index = 0)
if option == '文本评价':
    st.title('问政回复评价系统')
    st.markdown('Government response evaluation system')
    text = st.text_area('请输入需要评价的文本')
    d1 = st.date_input('留言时间',datetime.date(2019, 7, 6))
    d2 = st.date_input('回复时间',datetime.date(2019, 7, 6))
    if st.button('开始评价'):
        st.write('评分为', test(text,d1,d2))

if option == '文本分类':
    st.title('问政文本分类系统')
    st.markdown('Message Text Classification System')
    text = st.text_area('请输入需要分类的文本')
    if st.button('开始分类'):
        st.write('类别为', getLabel(text))


if option == '热点挖掘':
    st.title('问政热点挖掘系统')
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)
        if st.button('开始挖掘热点'):
            '聚类中请稍后...'
            df = getHot(data, 0.6, 10)
            # Add a placeholder
            st.write('聚类完成！')
            st.write(df)


