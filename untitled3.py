import streamlit as st 
bi = st.button("HELLO")
if bi == True:
    st.image(r"C:\MARI\IMG_1314.gif")
sb1 = st.selectbox("CHOOSE",("MARI ANGRY","MARI SAD","MARI HAPPY","LICK"),index=None, placeholder="Select contact method...",)
if sb1  == "MARI ANGRY":
    st.image(r"C:\MARI\image0.jpg")
if sb1 == "MARI SAD":
    st.image(r"C:\MARI\IMG_0728.jpg")
if sb1 == "MARI HAPPY":
    st.image(r"C:\MARI\IMG_0977.jpg")
if sb1 == "LICK":
    st.image(r"C:\MARI\IMG_1314.gif")
    
te = st.text_input("MARI?")
if te == "BREAK":
    st.image(r"C:\MARI\imageh.jpg")
if te == "SHY":
    st.image(r"C:\MARI\images.jpg")
if te == "CHM":
    st.image(r"C:\MARI\imagefg.jpg")
if te == "THREE":
    st.image(r"C:\MARI\imagth.jpg")
if te == "SLEEP":
    st.image(r"C:\MARI\2023-06-13_194233.png")
if te == "FOOD":
    st.image(r"C:\MARI\IMG_5390.jpg")
if te == "TAIL":
    st.image(r"C:\MARI\IMG_2257.jpg")
if te == "LICK":
    st.image(r"C:\MARI\IMG_1314.gif")