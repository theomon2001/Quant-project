# import altair as alt
import streamlit as st
from functions import *
# filepath = 


onglet = st.sidebar.radio("pricer", ["Call", "Put"])
if onglet == "Call":
    st.markdown(
        '''
        <style>
        .subheader-text {
            color: White; 
            font-size: 32px;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )
    st.markdown("<h1 class='subheader-text'>Call price</h1>", unsafe_allow_html=True)
    with st.form(key='form_1'):
        S = st.number_input("Underlying asset price", value=100)
        K = st.number_input("Strike", value=100)
        sig = st.number_input("Volatility", value=1)
        T = st.number_input("Time to maturity", value=1)
        r = st.number_input ("Interest rate", value=0.05)
        submit_button = st.form_submit_button(label='Price')

    if submit_button :
        P = pricer(S, K,sig,T,r)
        call_price = P.call()
        delta = P.delta_call()
        gamma = P.gamma()
        vega = P.vega()
        st.write(f"Call price: {call_price}")
        st.write(f"Delta : {delta}")
        st.write(f"Gamma : {gamma}")
        st.write(f"Vega : {vega}")        


if onglet == "Put":
    st.markdown(
        '''
        <style>
        .subheader-text {
            color: White; 
            font-size: 32px;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )
    st.markdown("<h1 class='subheader-text'>Put price</h1>", unsafe_allow_html=True)
    with st.form(key='form_1'):
        S = st.number_input("Underlying asset price", value=100)
        K = st.number_input("Strike", value=100)
        sig = st.number_input("Volatility", value=1)
        T = st.number_input("Time to maturity", value=1)
        r = st.number_input ("Interest rate", value=0.05)
        submit_button = st.form_submit_button(label='Price')

    if submit_button :
        P = pricer(S, K,sig,T,r)
        call_price = P.put()
        delta = P.delta_put()
        gamma = P.gamma()
        vega = P.vega()
        st.write(f"Call price: {call_price}")
        st.write(f"Delta : {delta}")
        st.write(f"Gamma : {gamma}")
        st.write(f"Vega : {vega}")  
