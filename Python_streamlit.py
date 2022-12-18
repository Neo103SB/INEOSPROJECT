import requests
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
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

import time

import glob
import os

browser = webdriver.Chrome(executable_path='chromedriver.exe')
browser.get("https://tmp.ineos-crm.ma/")
file = open(r"config.txt")
line = file.readlines()
username = line[0]
password = line[1]

elementID = browser.find_element(By.ID, 'username')
elementID.send_keys(username)
elementID = browser.find_element(By.ID, 'password')
elementID.send_keys(password)
elementID.submit()

# Set the path where you want to save the file
browser.get('https://tmp.ineos-crm.ma/index.php?module=Potentials&view=List&app=SALES')
browser.find_element(by=By.CLASS_NAME, value='caret').click()
time.sleep(5)
browser.find_element(by=By.ID, value='Potentials_listView_advancedAction_LBL_EXPORT').click()
time.sleep(5)
browser.find_element(by=By.XPATH, value='//*[@id="exportForm"]/div[3]/div/div/div/button').click()
time.sleep(5)
browser.close()
######
# Get a list of all files matching the pattern
csv_files = glob.glob(r"C:\Users\HP\Downloads\Opportunities*.csv")

# Sort the list by modification time
csv_files.sort(key=os.path.getmtime)

# Process the last file in the sorted list
latest_file = csv_files[-1]
# Set the file path and name
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://github.com/login")
username_field = driver.find_element(By.ID, "login_field")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys("hamza.sbiti@centrale-casablanca.ma")
password_field.send_keys("Hamza2002Hamza_")
login_button = driver.find_element(By.NAME, "commit")
login_button.click()
driver.get("https://github.com/Neo103SB/INEOSPROJECT/upload/master")
file_input = driver.find_element(By.XPATH, value='//*[@id="upload-manifest-files-input"]')
time.sleep(3)
file_input.send_keys(str(latest_file))
time.sleep(3)
upload_button = driver.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/form/button')
time.sleep(3)
upload_button.click()
time.sleep(3)
driver.close()

#####################################DATA_CLEANING############################################

df = pd.read_csv(str(latest_file))
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

# TOSHOW_DATA
st.dataframe(filtered_df)

st.sidebar.header("Filtrer en fonction de 'assigned to':")
#

filter3_value = st.sidebar.text_input("Entrer le nom de la personne :")
# Filter the dataset based on the filter value and display the results
filtered_df2 = df[(df[' "Assigned To"'] == filter3_value)]

# TOSHOW_DATA
st.dataframe(filtered_df2)

# Calculate the sum of the column
sum_value = df[' "Amount"'].sum()

# Display the sum value
st.write("Total Amount:", sum_value, format='plain')

#############################################GRAPHES_CREATION#######################################
######FIRST
########graphe 1 :
Subject = ['Qualification', 'Closed Won', 'Nouveau', 'Closed Lost', 'Proposition', 'Abandonnée']
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
a8 = 0
a9 = 0
a10 = 0
a11 = 0
a12 = 0
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
df2 = pd.DataFrame([['Qualification', 'Ineos', a1], ['Qualification', 'Cyberforce', a2], ['Closed Won', 'Ineos', a3],
                    ['Closed Won', 'Cyberforce', a4],
                    ['Nouveau', 'Ineos', a5], ['Nouveau', 'Cyberforce', a6], ['Closed Lost', 'Ineos', a7],
                    ['Closed Lost', 'Cyberforce', a8],
                    ['Proposition', 'Ineos', a9], ['Proposition', 'Cyberforce', a10], ['Abandonnée', 'Ineos', a11],
                    ['Abandonnée', 'Cyberforce', a12]
                    ], columns=['Opportunities', 'Entité', 'Sales'])
fig1 = px.bar(df2, x="Opportunities", y="Sales", color="Entité", barmode='group')
st.plotly_chart(fig1)

###############graphe 2 :
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0

b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0

m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0
m6 = 0

i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0

h1 = 0
h2 = 0
h3 = 0
h4 = 0
h5 = 0
h6 = 0

y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0
y6 = 0

for j in range(len(df[' "Assigned To"'])):
    if df[' "Assigned To"'][j] == 'reda.bakkali' and df[' "Sales Stage"'][j] == 'Qualification' and df[' "Amount"'][
        j] != 0:
        r1 = r1 + 1
    if df[' "Assigned To"'][j] == 'reda.bakkali' and df[' "Sales Stage"'][j] == 'Closed Won' and df[' "Amount"'][
        j] != 0:
        r2 = r2 + 1
    if df[' "Assigned To"'][j] == 'reda.bakkali' and df[' "Sales Stage"'][j] == 'Nouveau' and df[' "Amount"'][j] != 0:
        r3 = r3 + 1
    if df[' "Assigned To"'][j] == 'reda.bakkali' and df[' "Sales Stage"'][j] == 'Closed Lost' and df[' "Amount"'][
        j] != 0:
        r4 = r4 + 1
    if df[' "Assigned To"'][j] == 'reda.bakkali' and df[' "Sales Stage"'][j] == 'Proposition' and df[' "Amount"'][
        j] != 0:
        r5 = r5 + 1
    if df[' "Assigned To"'][j] == 'reda.bakkali' and df[' "Sales Stage"'][j] == 'Abandonnée' and df[' "Amount"'][
        j] != 0:
        r6 = r6 + 1

    if df[' "Assigned To"'][j] == 'amine.nemrouch' and df[' "Sales Stage"'][j] == 'Qualification' and df[' "Amount"'][
        j] != 0:
        b1 = b1 + 1
    if df[' "Assigned To"'][j] == 'amine.nemrouch' and df[' "Sales Stage"'][j] == 'Closed Won' and df[' "Amount"'][
        j] != 0:
        b2 = b2 + 1
    if df[' "Assigned To"'][j] == 'amine.nemrouch' and df[' "Sales Stage"'][j] == 'Nouveau' and df[' "Amount"'][j] != 0:
        b3 = b3 + 1
    if df[' "Assigned To"'][j] == 'amine.nemrouch' and df[' "Sales Stage"'][j] == 'Closed Lost' and df[' "Amount"'][
        j] != 0:
        b4 = b4 + 1
    if df[' "Assigned To"'][j] == 'amine.nemrouch' and df[' "Sales Stage"'][j] == 'Proposition' and df[' "Amount"'][
        j] != 0:
        b5 = b5 + 1
    if df[' "Assigned To"'][j] == 'amine.nemrouch' and df[' "Sales Stage"'][j] == 'Abandonnée' and df[' "Amount"'][
        j] != 0:
        b6 = b6 + 1

    if df[' "Assigned To"'][j] == 'mohamed.ikniouen' and df[' "Sales Stage"'][j] == 'Qualification' and df[' "Amount"'][
        j] != 0:
        m1 = m1 + 1
    if df[' "Assigned To"'][j] == 'mohamed.ikniouen' and df[' "Sales Stage"'][j] == 'Closed Won' and df[' "Amount"'][
        j] != 0:
        m2 = m2 + 1
    if df[' "Assigned To"'][j] == 'mohamed.ikniouen' and df[' "Sales Stage"'][j] == 'Nouveau' and df[' "Amount"'][
        j] != 0:
        m3 = m3 + 1
    if df[' "Assigned To"'][j] == 'mohamed.ikniouen' and df[' "Sales Stage"'][j] == 'Closed Lost' and df[' "Amount"'][
        j] != 0:
        m4 = m4 + 1
    if df[' "Assigned To"'][j] == 'mohamed.ikniouen' and df[' "Sales Stage"'][j] == 'Proposition' and df[' "Amount"'][
        j] != 0:
        m5 = m5 + 1
    if df[' "Assigned To"'][j] == 'mohamed.ikniouen' and df[' "Sales Stage"'][j] == 'Abandonnée' and df[' "Amount"'][
        j] != 0:
        m6 = m6 + 1

    if df[' "Assigned To"'][j] == 'iidriss.zaamoun' and df[' "Sales Stage"'][j] == 'Qualification' and df[' "Amount"'][
        j] != 0:
        i1 = i1 + 1
    if df[' "Assigned To"'][j] == 'iidriss.zaamoun' and df[' "Sales Stage"'][j] == 'Closed Won' and df[' "Amount"'][
        j] != 0:
        i2 = i2 + 1
    if df[' "Assigned To"'][j] == 'iidriss.zaamoun' and df[' "Sales Stage"'][j] == 'Nouveau' and df[' "Amount"'][
        j] != 0:
        i3 = i3 + 1
    if df[' "Assigned To"'][j] == 'iidriss.zaamoun' and df[' "Sales Stage"'][j] == 'Closed Lost' and df[' "Amount"'][
        j] != 0:
        i4 = i4 + 1
    if df[' "Assigned To"'][j] == 'iidriss.zaamoun' and df[' "Sales Stage"'][j] == 'Proposition' and df[' "Amount"'][
        j] != 0:
        i5 = i5 + 1
    if df[' "Assigned To"'][j] == 'iidriss.zaamoun' and df[' "Sales Stage"'][j] == 'Abandonnée' and df[' "Amount"'][
        j] != 0:
        i6 = i6 + 1

    if df[' "Assigned To"'][j] == 'hamida.benlemlih' and df[' "Sales Stage"'][j] == 'Qualification' and df[' "Amount"'][
        j] != 0:
        h1 = h1 + 1
    if df[' "Assigned To"'][j] == 'hamida.benlemlih' and df[' "Sales Stage"'][j] == 'Closed Won' and df[' "Amount"'][
        j] != 0:
        h2 = h2 + 1
    if df[' "Assigned To"'][j] == 'hamida.benlemlih' and df[' "Sales Stage"'][j] == 'Nouveau' and df[' "Amount"'][
        j] != 0:
        h3 = h3 + 1
    if df[' "Assigned To"'][j] == 'hamida.benlemlih' and df[' "Sales Stage"'][j] == 'Closed Lost' and df[' "Amount"'][
        j] != 0:
        h4 = h4 + 1
    if df[' "Assigned To"'][j] == 'hamida.benlemlih' and df[' "Sales Stage"'][j] == 'Proposition' and df[' "Amount"'][
        j] != 0:
        h5 = h5 + 1
    if df[' "Assigned To"'][j] == 'hamida.benlemlih' and df[' "Sales Stage"'][j] == 'Abandonnée' and df[' "Amount"'][
        j] != 0:
        h6 = h6 + 1

    if df[' "Assigned To"'][j] == 'yahya.ajbali' and df[' "Sales Stage"'][j] == 'Qualification' and df[' "Amount"'][
        j] != 0:
        y1 = y1 + 1
    if df[' "Assigned To"'][j] == 'yahya.ajbali' and df[' "Sales Stage"'][j] == 'Closed Won' and df[' "Amount"'][
        j] != 0:
        y2 = y2 + 1
    if df[' "Assigned To"'][j] == 'yahya.ajbali' and df[' "Sales Stage"'][j] == 'Nouveau' and df[' "Amount"'][j] != 0:
        y3 = y3 + 1
    if df[' "Assigned To"'][j] == 'yahya.ajbali' and df[' "Sales Stage"'][j] == 'Closed Lost' and df[' "Amount"'][
        j] != 0:
        y4 = y4 + 1
    if df[' "Assigned To"'][j] == 'yahya.ajbali' and df[' "Sales Stage"'][j] == 'Proposition' and df[' "Amount"'][
        j] != 0:
        y5 = y5 + 1
    if df[' "Assigned To"'][j] == 'yahya.ajbali' and df[' "Sales Stage"'][j] == 'Abandonnée' and df[' "Amount"'][
        j] != 0:
        y6 = y6 + 1

df3 = pd.DataFrame(
    [['Qualification', 'reda.bakkali', r1], ['Closed Won', 'reda.bakkali', r2], ['Nouveau', 'reda.bakkali', r3],
     ['Closed Lost', 'reda.bakkali', r4], ['Proposition', 'reda.bakkali', r5], ['Abandonnée', 'reda.bakkali', r6],
     ['Qualification', 'amine.nemrouch', b1], ['Closed Won', 'amine.nemrouch', b2], ['Nouveau', 'amine.nemrouch', b3],
     ['Closed Lost', 'amine.nemrouch', b4], ['Proposition', 'amine.nemrouch', b5], ['Abandonnée', 'amine.nemrouch', b6],
     ['Qualification', 'mohamed.ikniouen', m1], ['Closed Won', 'mohamed.ikniouen', m2],
     ['Nouveau', 'mohamed.ikniouen', m3], ['Closed Lost', 'mohamed.ikniouen', m4],
     ['Proposition', 'mohamed.ikniouen', m5], ['Abandonnée', 'mohamed.ikniouen', m6],
     ['Qualification', 'iidriss.zaamoun', i1], ['Closed Won', 'iidriss.zaamoun', i2],
     ['Nouveau', 'iidriss.zaamoun', i3], ['Closed Lost', 'iidriss.zaamoun', i4], ['Proposition', 'iidriss.zaamoun', i5],
     ['Abandonnée', 'iidriss.zaamoun', i6],
     ['Qualification', 'hamida.benlemlih', h1], ['Closed Won', 'hamida.benlemlih', h2],
     ['Nouveau', 'hamida.benlemlih', h3], ['Closed Lost', 'hamida.benlemlih', h4],
     ['Proposition', 'hamida.benlemlih', h5], ['Abandonnée', 'hamida.benlemlih', h6],
     ['Qualification', 'yahya.ajbali', y1], ['Closed Won', 'yahya.ajbali', y2], ['Nouveau', 'yahya.ajbali', y3],
     ['Closed Lost', 'yahya.ajbali', y4], ['Proposition', 'yahya.ajbali', y5], ['Abandonnée', 'yahya.ajbali', y6]
     ], columns=['Sales Stage', 'Manager', 'Sales'])

fig2 = px.bar(df3, x='Sales Stage', y="Sales", color='Manager', barmode='group')
st.plotly_chart(fig2)

#############graphe 3 :
v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0
v6 = 0
for i in range(len(df[' "Assigned To"'])):
    if df[' "Assigned To"'][i] == 'reda.bakkali':
        v1 = v1 + df[' "Amount"'][i]
    if df[' "Assigned To"'][i] == 'amine.nemrouch':
        v2 = v2 + df[' "Amount"'][i]
    if df[' "Assigned To"'][i] == 'mohamed.ikniouen':
        v3 = v3 + df[' "Amount"'][i]
    if df[' "Assigned To"'][i] == 'iidriss.zaamoun':
        v4 = v4 + df[' "Amount"'][i]
    if df[' "Assigned To"'][i] == 'hamida.benlemlih':
        v5 = v5 + df[' "Amount"'][i]
    if df[' "Assigned To"'][i] == 'yahya.ajbali':
        v6 = v6 + df[' "Amount"'][i]

df4 = pd.DataFrame([['reda bakkali', v1], ['amine nemrouch', v2], ['mohamed ikniouen', v3], ['iidriss zaamoun', v4],
                    ['hamida benlemlih', v5], ['yahya ajbali', v6],
                    ], columns=['Manager', 'Sales'])
fig3 = px.bar(df4, x="Manager", y="Sales")
st.plotly_chart(fig3)

################graphe 4 :
w1 = 0
w2 = 0
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
w14 = 0
w15 = 0
w16 = 0
w17 = 0
for i in range(len(df['Rappel du partenaire technologique'])):
    if df['Rappel du partenaire technologique'][i] == 'DELL EMC':
        w1 = w1 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'NaN':
        w2 = w2 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'VEEAM':
        w3 = w3 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'HUAWEI':
        w4 = w4 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'JIRA':
        w5 = w5 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'IPC':
        w6 = w6 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'CISCO':
        w7 = w7 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'FORTINET':
        w8 = w8 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'CHECK POINT':
        w9 = w9 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Symantec':
        w10 = w10 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Trend Micro':
        w11 = w11 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Beyondtrust':
        w12 = w12 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Dynatrace':
        w13 = w13 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Dell':
        w14 = w14 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Microsoft':
        w15 = w15 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Solarwinds':
        w16 = w16 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'DELL EMC':
        w17 = w17 + df[' "Amount"'][i]

df5 = pd.DataFrame(
    [['DELL EMC', w1], ['NaN', w2], ['VEEAM', w3], ['HUAWEI', w4], ['JIRA', w5], ['IPC', w6], ['CISCO', w7],
     ['FORTINET', w8],
     ['CHECK POINT', w9], ['Symantec', w10], ['Trend Micro', w11], ['Beyondtrust', w12], ['Dynatrace', w12],
     ['Dell', w13], ['Microsoft', w14], ['Solarwinds', w15],
     ['DELL EMC', w16]
     ], columns=['partenaire technologique', 'Sales'])
fig4 = px.bar(df5, x="partenaire technologique", y="Sales")
st.plotly_chart(fig4)

############graphe 5 :
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0
s10 = 0
s11 = 0
s12 = 0
s13 = 0
for i in range(len(df[' "Solution"'])):
    if df[' "Solution"'][i] == 'Cloud':
        s1 = s1 + df[' "Amount"'][i]
    if df[' "Solution"'][i] == 'Postes de travail':
        s2 = s2 + df[' "Amount"'][i]
    if df[' "Solution"'][i] == 'Réseau':
        s3 = s3 + df[' "Amount"'][i]
    if df[' "Solution"'][i] == 'Régie INEOS':
        s4 = s4 + df[' "Amount"'][i]
    if df[' "Solution"'][i] == 'Sécurité':
        s5 = s5 + df[' "Amount"'][i]
    if df[' "Solution"'][i] == 'Firewalling':
        s6 = s6 + df[' "Amount"'][i]
    if df[' "Solution"'][i] == 'Régie Cyberforce':
        s7 = s7 + df[' "Amount"'][i]
    if df[' "Solution"'][i] == 'Sécurité Poste de Travail':
        s8 = s8 + df[' "Amount"'][i]
    if df[' "Solution"'][i] == 'Audit et conseil':
        s9 = s9 + df[' "Amount"'][i]
    if df[' "Solution"'][i] == 'SOC':
        s10 = s10 + df[' "Amount"'][i]
    if df[' "Solution"'][i] == 'Maintenance':
        s11 = s11 + df[' "Amount"'][i]
    if df[' "Solution"'][i] == 'DevOps':
        s12 = s12 + df[' "Amount"'][i]
    if df[' "Solution"'][i] == 'NaN':
        s13 = s13 + df[' "Amount"'][i]
df6 = pd.DataFrame([['Cloud', s1], ['Postes de travail', s2], ['Réseau', s3], ['Régie INEOS', s4], ['Sécurité', s5],
                    ['Firewalling', s6], ['Régie Cyberforce', s7], ['Sécurité Poste de Travail', s8],
                    ['Audit et conseil', s9], ['SOC', s10], ['Maintenance', s11], ['DevOps', s12], ['NaN', s13]
                    ], columns=['Solution', 'Sales'])
fig5 = px.bar(df6, x="Solution", y="Sales")
st.plotly_chart(fig5)

####################################GRAPHES_PLOTTING############################

t1 = pd.DataFrame(d, columns=['Rappel du partenaire technologique', 'Amount'])
t2 = pd.DataFrame(z, columns=['Solution', 'Amount'])
t3 = pd.DataFrame(c, columns=['Assigned To', 'Amount'])

st.bar_chart(t1, x='Rappel du partenaire technologique', y='Amount')
st.bar_chart(t2, x='Solution', y='Amount')
st.bar_chart(t3, x='Assigned To', y='Amount')

