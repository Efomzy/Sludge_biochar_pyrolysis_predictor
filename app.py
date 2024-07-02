import streamlit as st
import pickle
import numpy as np
from xgboost import XGBRegressor
XGB1 = pickle.load(open('XGB1.pkl', 'rb'))
XGB2 = pickle.load(open('XGB2.pkl', 'rb'))
XGB3 = pickle.load(open('XGB3.pkl', 'rb'))
XGB4 = pickle.load(open('XGB4.pkl', 'rb'))
XGB5 = pickle.load(open('XGB5.pkl', 'rb'))
XGB6 = pickle.load(open('XGB6.pkl', 'rb'))
XGB7 = pickle.load(open('XGB7.pkl', 'rb'))
XGB8 = pickle.load(open('XGB8.pkl', 'rb'))
XGB9 = pickle.load(open('XGB9.pkl', 'rb'))
XGB10 = pickle.load(open('XGB10.pkl', 'rb'))


st.write('## Sludge biochar Pyrolysis Predictor')
st.subheader('(Ultimate and Proximate properties should be in dry basis)')

col1, col2, col3 = st.columns(3)

with col1:
  st.write(Ultimate properties)
  C = st.number_input("Carbon content (%)", 0.00,50.00)

with col2:
  st.write(Proximate properties)
  A = st.number_input("Ash content (%)", 0.00,80.00)
  
with col3:
  st.write(Pyrolysis conditions)
  HR = st.number_input("Heating Rate (°C/min)", 0.00,100.00)
  
  
with col1:
  H = st.number_input("Hydrogen content (%)", 0.00,15.00)

with col2:
  VM = st.number_input("Volatile Matter (%)", 0.00,75.00)
  
with col3:
  RT = st.number_input("Residence Time (min)", 0.00,300.00)
  
  
with col1:
  O = st.number_input("Oxygen content (%)", 0.00,40.00)

with col2:
  FC = st.number_input("Fixed Carbon (%)", 0.00,25.00)
  
with col3:
  T = st.number_input("Temperature (°C)", 250,1000)
  
  
with col1:
  N = st.number_input("Hydrogen content (%)", 0.00,15.00)
with col1:
  S = st.number_input("Hydrogen content (%)", 0.00,15.00)
 

if C+H+O+N+S+A >= 85 and C+H+O+N+S+A <= 115 and A+VM+FC >= 85 and A+VM+FC <= 115:

  Yield1 = XGB1.predict([[C, H, O, N, S, A, VM, FC, HR, RT, T]])
  Cb2 = XGB2.predict([[C, H, O, N, S, A, VM, FC, HR, RT, T]])
  Hb3 = XGB3.predict([[C, H, O, N, S, A, VM, FC, HR, RT, T]])
  Nb4 = XGB4.predict([[C, H, O, N, S, A, VM, FC, HR, RT, T]])
  Ab5 = XGB5.predict([[C, H, O, N, S, A, VM, FC, HR, RT, T]])
  pHb6 = XGB6.predict([[C, H, O, N, S, A, VM, FC, HR, RT, T]])
  H/Cb7 = XGB7.predict([[C, H, O, N, S, A, VM, FC, HR, RT, T]])
  O/Cb8 = XGB8.predict([[C, H, O, N, S, A, VM, FC, HR, RT, T]])
  EDR9 = XGB9.predict([[C, H, O, N, S, A, VM, FC, HR, RT, T]])
  HHV10 = XGB10.predict([[C, H, O, N, S, A, VM, FC, HR, RT, T]])
  
  
  Yield = round(Yield1[0], 2)
  Cb = round(Cb2[0], 2)
  Hb = round(Hb3[0], 2)
  Nb = round(Nb4[0], 2)
  Ab = round(Ab5[0], 2)
  pHb = round(pHb6[0], 2)
  H/Cb = round(H/Cb7[0], 2)
  O/Cb = round(O/Cb8[0], 2)
  EDR = round(EDR9[0], 2)
 HHV = round(HHV10[0], 2)

else:
  
  Yield = 'error in input data'
  Cb = 'error in input data'
  Hb = 'error in input data'
  Nb = 'error in input data'
  Ab = 'error in input data'
  pHb = 'error in input data'
  H/Cb = 'error in input data'
  O/Cb = 'error in input data'
  EDR = 'error in input data'
  HHV = 'error in input data'

if st.button('Click here to predict sludge biochar properties'):
  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
    st.write('Yield (wt.%)', Yield)
    
  with col2:
    st.write('Hb (wt.%)', Hb)
    
  with col3:
    st.write('Ab (wt.%)', Ab)
    
  with col4:
     st.write('H/Cb', H/Cb)
    
  with col5:
     st.write('EDR', EDR)

  
  with col1:
    st.write('Cb (wt.%)', Cb)
    
  with col2:
    st.write('Nb (wt.%)', Nb)
    
  with col3:
    st.write('pHb', pHb)
    
  with col4:
     st.write('O/Cb', O/Cb)
    
  with col5:
     st.write('HHV (MJ/kg)', HHV)
