import streamlit as st
bi = st.button("HELLO")
if bi == True:
    st.image("images/IMG_1314.gif")
sb1 = st.selectbox("CHOOSE",("MARI ANGRY","MARI SAD","MARI HAPPY","LICK"),index=None, placeholder="Select contact method...",)
if sb1  == "MARI ANGRY":
    st.image("images/image0.jpg")
if sb1 == "MARI SAD":
    st.image("images/IMG_0728.jpg")
if sb1 == "MARI HAPPY":
    st.image("images/IMG_0977.jpg")
if sb1 == "LICK":
    st.image("images/IMG_1314.gif")
    
te = st.text_input("MARI?")
if te == "BREAK":
    st.image("images/imageh.jpg")
if te == "SHY":
    st.image("images/images.jpg")
if te == "CHM":
    st.image("images/imagefg.jpg")
if te == "THREE":
    st.image("images/imagth.jpg")
if te == "SLEEP":
    st.image("images/2023-06-13_194233.png")
if te == "FOOD":
    st.image("images/IMG_5390.jpg")
if te == "TAIL":
    st.image("images/IMG_2257.jpg")
if te == "LICK":
    st.image("images/IMG_1314.jpg")
