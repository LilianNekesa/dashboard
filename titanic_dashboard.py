import streamlit as st 
import pandas as pd 
import plotly.express as px 

st.title("Titanic Data Analysis")
st.write("This app analyses Titanic Dataset from different points and displays various visualizations. I have dropped some colum such as the cabin column. I have also done some feature engineering and included two more columns. My main aim was to find data for those who travelled as a family or were alone. So, I have added the Family Size and PersonIsAlone column for that.")

@st.cache_resource
def load_data():
     url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
     data = pd.read_csv(url)
     data['Age'].fillna(data['Age'].median(), inplace=True)
     data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
     data.drop('Cabin', axis=1, inplace=True)
     data['FamilySize']=data['SibSp']+ data['Parch']+1
     data['PersonIsAlone'] = data['FamilySize'].apply(lambda x: 1 if x == 1 else 0)
     return data

data = load_data()
#display the data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)

st.header('Visualizations Using Plotly')
st.header('Survival Rate By Gender')

gender_survival=data.groupby('Sex')['Survived'].mean(). reset_index()
fig= px.bar(gender_survival, x='Sex', y='Survived', title='Titanic Survivors Rate by Gender')
st.plotly_chart(fig)


st.header('Survival Rate by Passenger Class')
pclass_survival=data.groupby('Pclass')['Survived'].mean().reset_index()

fig=px.bar(pclass_survival, x='Pclass', y='Survived', title='Survival Rate According to Passenger Class')
st.plotly_chart(fig)

st.header('Survival Rate According to Age')
age_survival=data.groupby('Age')['Survived'].sum().reset_index()

fig=px.line(age_survival, x='Age', y='Survived', title='Survival Rate According to Age')
st.plotly_chart(fig)

st.header('Survival Rate According to Family Size')
pclass_survival=data.groupby('FamilySize')['Survived'].sum().reset_index()

fig=px.bar(pclass_survival, x='FamilySize', y='Survived', title='Survival Rate According to Passenger Ticket')
st.plotly_chart(fig)

st.header('Age Distribution of Passengers by Survival Status')
fig=px.histogram(data, x='Age', nbins=50, title='Age Distribution of Passengers')
st.plotly_chart(fig)
