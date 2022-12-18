
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import streamlit as st
import plotly.figure_factory as ff

from streamlit.web import cli as stcli
import plotly.express as px
import sys
import io
import sys
import time



###########################################selenium################################################

import selenium
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
#browser = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
#browser.get("https://tmp.ineos-crm.ma/")
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


#####################################DATA_CLEANING############################################

df = pd.read_csv(r"Opportunities (2).csv")
df[' "Solution"'] = df[' "Solution"'].str.replace("Services::::", "")
df[' "Partenaire"'] = df[' "Partenaire"'].str.replace("Vendors::::", "")
df[' "Assigned To"'] = df[' "Assigned To"'].str.replace("@ineos.ma", "")
df[' "Organization Name"'] = df[' "Organization Name"'].str.replace("Accounts::::", " ")
df[' "Campaign Source"'] = df[' "Campaign Source"'].str.replace("Campaigns::::", " ")
df[' "Last Modified By"'] = df[' "Last Modified By"'].str.replace("@ineos.ma", "")
df[' "Last Modified By"'] = df[' "Last Modified By"'].str.replace(".", " ")


#########################################STREAMLIT_TEXT_HEADLINES###################################



st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
st.dataframe(df)

################################ADD_FILTERS######################################

# ---- SIDEBAR CREATION----
# Create a sidebar with a dropdown menu

#########Filtrer en fonction de assigned to & Entité

st.sidebar.header("Filtrer en fonction de assigned to & Entité:")

filter1_value = st.sidebar.text_input("Entrer le nom de la personne:")
filter2_value = st.sidebar.text_input("Choisissez l'organisation :")


filtered_df = df[(df[' "Assigned To"'] == filter1_value) & (df[' "Entité"'] == filter2_value)]

#TOSHOW_DATA
st.dataframe(filtered_df)

st.sidebar.header("Filtrer en fonction de 'assigned to':")
#

filter3_value = st.sidebar.text_input("Entrer le nom de la personne :")
# Filter the dataset based on the filter value and display the results
filtered_df2 = df[(df[' "Assigned To"'] == filter3_value)]

#TOSHOW_DATA
st.dataframe(filtered_df2)

# Calculate the sum of the column
sum_value = df[' "Amount"'].sum()

# Display the sum value
st.write("Total Amount:", sum_value, format= 'plain')



#############################################GRAPHES_CREATION#######################################
######FIRST
l1 = []
for x in df['Rappel du partenaire technologique']:
    if x not in l1:
        l1.append(x)
l2 = []
v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0
v6 = 0
v7 = 0
v8 = 0
v9 = 0
v10 = 0
v11 = 0
v12 = 0
v13 = 0
v14 = 0
v15 = 0
v16 = 0
v17 = 0
for i in range(len(df['Rappel du partenaire technologique'])):
    if df['Rappel du partenaire technologique'][i] == 'DELL EMC':
        v1 = v1 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'NaN':
        V2 = v2 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'VEEAM':
        v3 = v3 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'HUAWEI':
        v4 = v4 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'JIRA':
        v5 = v5 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'IPC':
        v6 = v6 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'CISCO':
        v7 = v7 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'FORTINET':
        v8 = v8 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'CHECK POINT':
        v9 = v9 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Symantec':
        v10 = v10 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Trend Micro':
        v11 = v11 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Beyondtrust':
        v12 = v12 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Dynatrace':
        v13 = v13 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Dell':
        v14 = v14 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Microsoft':
        v15 = v15 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Solarwinds':
        v16 = v16 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'DELL EMC':
        v17 = v17 + df[' "Amount"'][i]

l2.append(v1)
l2.append(v2)
l2.append(v3)
l2.append(v4)
l2.append(v5)
l2.append(v6)
l2.append(v7)
l2.append(v8)
l2.append(v9)
l2.append(v10)
l2.append(v11)
l2.append(v12)
l2.append(v13)
l2.append(v14)
l2.append(v15)
l2.append(v16)
l2.append(v17)

d = []

for i in range(len(l1)):
    d.append([l1[i], l2[i]])

###SECOND:

m1=[]
for x in df[' "Solution"']:
  if x not in m1 :
    m1.append(x)
m2=[]
w1 = 0
w2= 0
w3 = 0
w4 = 0
w5 = 0
w6 = 0
w7 = 0
w8 = 0
w9 = 0
w10 = 0
w11 = 0
w12 = 0
w13 = 0
for i in range(len(df[' "Solution"'])):
  if df[' "Solution"'][i] == 'Cloud':
    w1 = w1 + df[' "Amount"'][i]
  if df[' "Solution"'][i] == 'Postes de trawail':
    w2 = w2 + df[' "Amount"'][i]
  if df[' "Solution"'][i] == 'Réseau':
    w3 = w3 + df[' "Amount"'][i]
  if df[' "Solution"'][i] == 'Régie INEOS':
     w4 = w4 + df[' "Amount"'][i]
  if df[' "Solution"'][i] == 'Sécurité':
    w5 = w5 + df[' "Amount"'][i]
  if df[' "Solution"'][i] == 'Firewalling':
    w6 = w6 + df[' "Amount"'][i]
  if df[' "Solution"'][i] == 'Régie Cyberforce':
    w7 = w7 + df[' "Amount"'][i]
  if df[' "Solution"'][i] == 'Sécurité Poste de Travail':
    w8 = w8 + df[' "Amount"'][i]
  if df[' "Solution"'][i] == 'Audit et conseil':
    w9 = w9 + df[' "Amount"'][i]
  if df[' "Solution"'][i] == 'SOC':
    w10 = w10 + df[' "Amount"'][i]
  if df[' "Solution"'][i] == 'Maintenance':
    w11 = w11 + df[' "Amount"'][i]
  if df[' "Solution"'][i] == 'DevOps':
    w12 = w12 + df[' "Amount"'][i]
  if df[' "Solution"'][i] == 'NaN':
    w13 = w13 + df[' "Amount"'][i]
m2.append(w1)
m2.append(w2)
m2.append(w3)
m2.append(w4)
m2.append(w5)
m2.append(w6)
m2.append(w7)
m2.append(w8)
m2.append(w9)
m2.append(w10)
m2.append(w11)
m2.append(w12)
m2.append(w13)

z=[]
for i in range(len(m1)):
  z.append([m1[i],m2[i]])
st.header("BI APP TEST")
st.write("VERSION BETA DE L'APP")

######THIRD

b1=[]
for x in df[' "Assigned To"']:
  if x not in b1 :
    b1.append(x)
b2=[]
u1 = 0
u2= 0
u3 = 0
u4 = 0
u5 = 0
u6 = 0
for i in range(len(df[' "Assigned To"'])):
  if df[' "Assigned To"'][i] == 'reda bakkali' :
    u1 = u1 + df[' "Amount"'][i]
  if df[' "Assigned To"'][i] ==  'amine nemrouch' :
    u2 = u2 + df[' "Amount"'][i]
  if df[' "Assigned To"'][i] == 'mohamed ikniouen':
    u3 = u3 + df[' "Amount"'][i]
  if df[' "Assigned To"'][i] == 'iidriss zaamoun':
    u4 = u4 + df[' "Amount"'][i]
  if df[' "Assigned To"'][i] == 'hamida benlemlih':
    u5 = u5 + df[' "Amount"'][i]
  if df[' "Assigned To"'][i] ==  'yahya ajbali':
    u6 = u6 + df[' "Amount"'][i]

b2.append(u1)
b2.append(u2)
b2.append(u3)
b2.append(u4)
b2.append(u5)
b2.append(u6)

c=[]

for i in range(len(b1)):
  c.append([b1[i],b2[i]])

######FOURTH:

Subject = ['Qualification', 'Closed Won', 'Nouveau', 'Closed Lost', 'Proposition', 'Abandonnée']
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0
a9=0
a10=0
a11=0
a12=0
for i in range(len(df[' "Entité"'])):
  if df[' "Entité"'][i] == 'Ineos' and df[' "Sales Stage"'][i] == 'Qualification':
    a1 = a1 + df[' "Amount"'][i]
  if df[' "Entité"'][i] == 'Cyberforce' and df[' "Sales Stage"'][i] == 'Qualification':
    a2 = a2 + df[' "Amount"'][i]
  if df[' "Entité"'][i] == 'Ineos' and df[' "Sales Stage"'][i] == 'Closed Won':
    a3 = a3 + df[' "Amount"'][i]
  if df[' "Entité"'][i] == 'Cyberforce' and df[' "Sales Stage"'][i] == 'Closed Won':
    a4 = a4 + df[' "Amount"'][i]
  if df[' "Entité"'][i] == 'Ineos' and df[' "Sales Stage"'][i] == 'Nouveau':
    a5 = a5 + df[' "Amount"'][i]
  if df[' "Entité"'][i] == 'Cyberforce' and df[' "Sales Stage"'][i] == 'Nouveau':
    a6 = a6 + df[' "Amount"'][i]
  if df[' "Entité"'][i] == 'Ineos' and df[' "Sales Stage"'][i] == 'Closed Lost':
    a7 = a7 + df[' "Amount"'][i]
  if df[' "Entité"'][i] == 'Cyberforce' and df[' "Sales Stage"'][i] == 'Closed Lost':
    a8 = a8 + df[' "Amount"'][i]
  if df[' "Entité"'][i] == 'Ineos' and df[' "Sales Stage"'][i] == 'Proposition':
    a9 = a9 + df[' "Amount"'][i]
  if df[' "Entité"'][i] == 'Cyberforce' and df[' "Sales Stage"'][i] == 'Proposition':
    a10 = a10 + df[' "Amount"'][i]
  if df[' "Entité"'][i] == 'Ineos' and df[' "Sales Stage"'][i] == 'Abandonnée':
    a11 = a11 + df[' "Amount"'][i]
  if df[' "Entité"'][i] == 'Cyberforce' and df[' "Sales Stage"'][i] == 'Abandonnée':
    a12 = a12 + df[' "Amount"'][i]

# Create the pandas DataFrame
df = pd.DataFrame([['Qualification', 'Ineos',a1],['Qualification', 'Cyberforce',a2],['Closed Won', 'Ineos',a3],['Closed Won', 'Cyberforce',a4],
                   ['Nouveau', 'Ineos',a5],['Nouveau', 'Cyberforce',a6],['Closed Lost', 'Ineos',a7],['Closed Lost', 'Cyberforce',a8],
                   ['Proposition', 'Ineos',a9],['Proposition', 'Cyberforce',a10],['Abandonnée', 'Ineos',a11],['Abandonnée', 'Cyberforce',a12]
                   ], columns = ['Opportunities', 'Entité','Sales'])
fig = px.bar(df, x="Opportunities", y="Sales", color="Entité",barmode='group')
fig.show()


####################################GRAPHES_PLOTTING############################

t1 = pd.DataFrame(d, columns=['Rappel du partenaire technologique', 'Amount'])
t2=pd.DataFrame(z,columns=['Solution','Amount'])
t3=pd.DataFrame(c,columns=['Assigned To','Amount'])

st.bar_chart(t1, x='Rappel du partenaire technologique', y='Amount')
st.bar_chart(t2, x='Solution', y='Amount')
st.bar_chart(t3, x='Assigned To', y='Amount')

