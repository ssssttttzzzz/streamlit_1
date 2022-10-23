import streamlit as st
import pandas as pd
import random as rd

st.set_page_config(page_icon="📈", page_title="play")
def get_mycard():
  my_card = [None]*3
  i = 0
  hsk = ["♥️","♠️","♦️","♣️"]
  paik = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
  while not my_card[2]:
    hs = rd.randint(0,3)
    pai = rd.randint(0,12)
    creat_card = hsk[hs]+paik[pai]
    if creat_card not in my_card:
      my_card[i]=creat_card
      i+=1
  return my_card
if st.button("发牌！"):
  my_card = get_mycard()    
  st.title(my_card[0])
  st.title(my_card[1])
  st.title(my_card[2])
