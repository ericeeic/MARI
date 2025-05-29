import streamlit as st
bi = st.button("HELLO")
if bi == True:
    st.image("IMG_1314.gif")
sb1 = st.selectbox("CHOOSE",("MARI ANGRY","MARI SAD","MARI HAPPY","LICK"),index=None, placeholder="Select contact method...",)
if sb1  == "MARI ANGRY":
    st.image("image0.jpg")
if sb1 == "MARI SAD":
    st.image("IMG_0728.jpg")
if sb1 == "MARI HAPPY":
    st.image("IMG_0977.jpg")
if sb1 == "LICK":
    st.image("IMG_1314.gif")
    
te = st.text_input("MARI?")
if te == "BREAK":
    st.image("imageh.jpg")
if te == "SHY":
    st.image("images.jpg")
if te == "CHM":
    st.image("imagefg.jpg")
if te == "THREE":
    st.image("imagth.jpg")
if te == "SLEEP":
    st.image("2023-06-13_194233.png")
if te == "FOOD":
    st.image("IMG_5390.jpg")
if te == "TAIL":
    st.image("IMG_2257.jpg")
if te == "LICK":
    st.image("IMG_1314.jpg")
