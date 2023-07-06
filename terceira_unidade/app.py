import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("Analisando renda dos responsáveis pelos domícilios por gênero de Natal - RN")

st.subheader("A Streamlit web app by Matheus Silva")

analise02 = pd.read_csv('terceira_unidade/data/analise02.csv')

lst1 = [12, 13, 20, 23, 28, 31, 34, 0, 1, 2, 6, 15, 16, 24, 29, 32, 33, 35, 36, 3, 7, 8, 9, 10, 11, 19, 21, 26, 30, 4, 5, 14, 18, 22, 25, 27]

# colocando em ordem para eixo x
analise02 = analise02.loc[lst1].reset_index(drop=True)

colors_orange = ['#FFBA08', '#FAA307', '#F48C06', '#E85D04', '#DC2F02', '#D00000', '#9D0208', '#6A040F', '#370617']
colors_blue = ['#8CF3F1', '#6EC8C6', '#60B2B1', '#519D9B', '#428786', '#337270', '#255C5B', '#164745', '#073130']

bar_men = px.bar(analise02, y='Nome_do_bairro', x=analise02.iloc[:, 4:13].columns,
             labels={'variable': '', 'value': '', 'Nome_do_bairro' : 'Nome do Bairro'},
             color_discrete_sequence=colors_orange,
             title='Renda dos homens responsáveis dos domícilios - Natal RN'
             )
bar_men.update_layout(
    width=1700,
    height=800  # Set the desired height in pixels
)
bar_men.update_yaxes(autorange="reversed")
st.plotly_chart(bar_men)

bar_women = px.bar(analise02, y='Nome_do_bairro', x=analise02.iloc[:, 13:22].columns,
              labels={'variable': '', 'value': '', 'Nome_do_bairro' : 'Nome do Bairro'},
              color_discrete_sequence=colors_blue,
              title='Renda das mulheres responsáveis dos domícilios - Natal RN', orientation='h'
             )
bar_women.update_layout(
    width=1700,
    height=800  # Set the desired height in pixels
)
bar_women.update_yaxes(autorange="reversed")
st.plotly_chart(bar_women)