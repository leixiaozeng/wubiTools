#此脚本用于输入一个文字来查询此文字在五笔输入法中的拆字方法
import re
import requests
import streamlit as st

def get_bianma():#获取编码
    url = f'https://search.cidianwang.com/?m=0&y=0&q={zi}&t=3'
    heds = {
        'Referer':'https://www.cidianwang.com/',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    html = requests.get(url=url,headers=heds)
    html.close()
    html = html.text
    recp = re.compile(r'<div class="stitle"><a href="(.*?)" target="_blank" >')
    data = re.findall(recp,html)
    if data[0] != '': 
        # print('第一阶段完成：'+data[0])
        get_jiegou(url=data[0])

def get_jiegou(url):#获取结果
    heds = {
        'Referer':'https://www.cidianwang.com/',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    html = requests.get(url=url,headers=heds)
    html.close()
    html.encoding = 'utf-8'
    html = html.text
    recp = re.compile(r'的五笔编码</h2><p align="left"><span class="fgreen">(.*?)</span></p><h2>')
    data = re.findall(recp,html)
    if data[0] != '':
        st.info(f'{zi}的五笔编码：'+data[0])
        st.image(f"https://c.cidianwang.com/file/wubi/{zi}.gif")
try:
    menu_dic = {
        "Get Help":None,
        "Report a bug":None,
        "About":"测试版本0.1",
    }
    st.set_page_config(page_title="五笔查询小工具",page_icon=":book:",menu_items=menu_dic)
    st.info("### :book:五笔查询小工具")
    with st.form("table_1"):
        zi = st.text_input(label='输入要查询的文字（只能输入一个字，就算你输入多个也只查询第一个字)',max_chars=6,help='请只输入“一个”字。')
        if st.form_submit_button('查询'):
            get_bianma()
except:
    st.info('出错了！！')