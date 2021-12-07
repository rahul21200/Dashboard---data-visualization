'''
RAHUL KAPOOR
3CO20
101903508

NOTE: To run this file type 'streamlit run dashboard.py' in the terminal
'''

import pandas as pd                     #library used for data manipulation and analysis
import streamlit as st                  #library used to make frontend of website
import plotly.express as px             #library used for data visualization

st.markdown(                            #used for formating the app layout
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 100%;
        padding-top: 0rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 0rem;
    }}
</style>
""", unsafe_allow_html=True,)
    
st.title('Heart Disease Analysis')

histogram,piechart= st.columns(2)                #divides into 2 container seperated vertically

@st.cache                                        #writing code under 'cache' means that this code won't rerun again
def load_data():                                 #function to load dataset
    data= pd.read_csv('heart.csv')               #converts csv format data into pandas.Dataframe format
    data_true= data[data['HeartDisease']==1]     #data of patients with heart disease 
    return data,data_true

df,dft=load_data()
# st.write(df.head(len(df)))


with histogram:                                  #function to display histograms

    st.subheader('Effect of various festures on Heart Disease ')
    feature=st.selectbox('Select Feauture: ',options=['Age','Resting ECG','Chest Pain Type'],index=0)  #dropdown option
    s=feature.split()
    feature="".join(s)                           #converting features names to the form they are present in the csv file

    fig = px.histogram(df, x = feature , color = "HeartDisease")        #plots histogram
    fig.update_layout(bargroupgap=0.1)
    newnames = {'0':'No', '1': 'Yes'}
    fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))     #rename legends from 0 and 1 to 'NO' and 'Yes' respectively

    st.write(fig)                                #display figure


with piechart:                                   #function to display piecharts

    st.subheader('Feature distribution among patients with Heart Disease ')
    feature=st.selectbox('Select Feauture: ',options=['Sex','Resting ECG','Chest Pain Type','Exercise Angina'],index=0)     #dropdown
    s=feature.split()
    feature="".join(s)                           #converting features names to the form they are present in the csv file

    value_count=dft[feature].value_counts()      #extracting parameters for plotting piecharts
    names=value_count.keys()
    fig1=px.pie(values=value_count,names=names)

    fig1.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=20,marker=dict( line=dict(color='#000000', width=0.5)))
    fig1.update_layout(margin=dict(t=60, b=60, l=60, r=60))

    st.write(fig1)                               #display figure