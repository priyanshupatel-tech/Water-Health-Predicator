import streamlit as st
import pickle
import warnings
warnings.filterwarnings("ignore")
st.title("Water Health Predicator!!!")
ph=st.number_input("Enter Water pH")
hn=st.number_input("Enter the hardnness of water")
sd=st.number_input("Enter water solid")
clm=st.number_input("Enter  water chloromines")
sf=st.number_input("Enter Water Sulfate")
cuv=st.number_input("Enter Water Conductvity")
orgc=st.number_input("Enter amount of Oragnic Carban in Water")
tm=st.number_input("Enter Trihalomethanes in water")
tbdt=st.number_input("Enter Water Turbidity")
btn=st.button("Predict Water Health")

if btn:
    model=pickle.load(open("wh.pkl","rb"))
    result=model.predict([[ph,hn,sd,clm,sf,cuv,orgc,tm,tbdt]])[0]
    if result==1:
        st.success("Your water health is good and you can drink your water")
    else:
        st.success("Your water health is bad and you can't drink your water")
