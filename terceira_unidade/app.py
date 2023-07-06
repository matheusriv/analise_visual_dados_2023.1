import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("Analisando renda dos responsáveis pelos domícilios por gênero de Natal - RN")

st.subheader("A Streamlit web app by Matheus Silva")

analise02 = pd.read_csv('terceira_unidade/data/analise02.csv')

lst1 = [12,13,19,22,27,30,33,0,1,2,6,15,16,23,28,31,32,34,35,3,7,8,9,10,11,18,20,25,29,4,5,14,17,21,24,26]

# colocando em ordem para eixo x
analise02 = analise02.loc[lst1].reset_index(drop=True)

colors_orange = ['#FFBA08', '#FAA307', '#F48C06', '#E85D04', '#DC2F02', '#D00000', '#9D0208', '#6A040F', '#370617']
colors_blue = ['#8CF3F1', '#6EC8C6', '#60B2B1', '#519D9B', '#428786', '#337270', '#255C5B', '#164745', '#073130']

st.write("Vendo só a quantidade de responsáveis, comparando homens e mulheres: ")

qtd_homens_mulheres = go.Figure(
    data = [
        go.Bar(
            name="Homens",
            x=analise02["Pessoas responsáveis masculino"],
            y=analise02["Nome_do_bairro"],
            orientation='h',
            offsetgroup=0,
        ),
        go.Bar(
            name="Mulheres",
            x=analise02["Pessoas responsáveis feminino"],
            y=analise02["Nome_do_bairro"],
            orientation='h',
            offsetgroup=1,
        ),
    ],
    layout=go.Layout(
        title="Pessoas responsáveis dos domícilios por gênero- Natal RN",
        yaxis_title="Nome do bairro"
    ),
)
qtd_homens_mulheres.data[0].marker.color = ('#F48C06')
qtd_homens_mulheres.data[1].marker.color = ('#60B2B1')
qtd_homens_mulheres.update_layout(
    width=1600,
    height=1000  # Set the desired height in pixels
)
qtd_homens_mulheres.update_yaxes(autorange="reversed") # Reverse the y-axis values
st.plotly_chart(qtd_homens_mulheres)

################### 

st.write("Gráfico final com linhas e barras: ")

grafico_final = make_subplots(rows=1, cols=2, horizontal_spacing=0.004, shared_yaxes=True, subplot_titles=("Homens", "Mulheres", "Total"))

i = 0
for column_name in analise02.iloc[:, 4:13].columns:
  grafico_final.add_trace(go.Scatter(y=analise02['Nome_do_bairro'], x=analise02[column_name], name=column_name,
                           line=dict(color=colors_orange[i], width=2), mode='lines+markers', marker=dict(size=5, symbol="square"),
                           legendgroup="group",  # this can be any string, not just "group"
                           legendgrouptitle_text="Responsáveis - Homens"),
                row=1, col=1, secondary_y=False)
  i+=1

i = 0
for column_name in analise02.iloc[:, 13:22].columns:
  grafico_final.add_trace(go.Scatter(y=analise02['Nome_do_bairro'], x=analise02[column_name], name=column_name,
                           line=dict(color=colors_blue[i], width=2), mode='lines+markers', marker=dict(size=5, symbol="circle"),
                           legendgroup="group2",  # this can be any string, not just "group"
                           legendgrouptitle_text="Responsáveis - Mulheres"),
                row=1, col=2, secondary_y=False)
  i+=1

grafico_final.add_trace(go.Bar(x=analise02["Pessoas responsáveis masculino"], y=analise02["Nome_do_bairro"],
                     name='Homens', orientation='h', marker=dict(color=colors_orange[3], opacity=0.4),
                     legendgroup="group3",  # this can be any string, not just "group"
                     legendgrouptitle_text="Total"),
              row=1, col=1, secondary_y=False)

grafico_final.add_trace(go.Bar(x=analise02["Pessoas responsáveis feminino"], y=analise02["Nome_do_bairro"],
                     name='Mulheres', orientation='h', marker=dict(color=colors_blue[2], opacity=0.4)),
              row=1, col=2, secondary_y=False)

grafico_final.update_layout(
    width=1900,
    height=1000,
    title=dict(text='Renda dos responsáveis dos domicílios de Natal - RN', font=dict(size=20)),
    yaxis=dict(title='Nome do Bairro'),
    title_y=0.99, # Sets the title position along the y-axis (0-1 range)
    xaxis1=dict(title='Quantidade', title_standoff=30),
    xaxis2=dict(range=[-200, 14200], title='Quantidade', title_standoff=30),
    legend=dict(groupclick="toggleitem")
)

grafico_final.update_xaxes(range=[14200, -200], row=1, col=1) # Reverse the x-axis values for the first chart
grafico_final.update_yaxes(autorange="reversed") # Reverse the y-axis values

st.plotly_chart(grafico_final)

################### 

st.write("Gráfico alternativo com barras: ")

import plotly.express as px
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2, horizontal_spacing=0.008, subplot_titles=("Homens", "Mulheres"), shared_yaxes=True)

# Create the first bar chart
fig1 = px.bar(
    analise02,
    y='Nome_do_bairro',
    x=analise02.iloc[:, 4:13].columns,
    labels={'variable': '', 'value': '', 'Nome_do_bairro': 'Nome do Bairro'},
    orientation='h',
    color_discrete_sequence=colors_orange
)

# Create the second bar chart
fig2 = px.bar(
    analise02,
    y='Nome_do_bairro',
    x=analise02.iloc[:, 13:22].columns,
    labels={'variable': '', 'value': '', 'Nome_do_bairro': 'Nome do Bairro'},
    orientation='h',
    color_discrete_sequence=colors_blue
)
fig2.update_yaxes(showticklabels=False)

# Add the first bar chart to the subplot grid
for trace in fig1.data:
    fig.add_trace(trace, row=1, col=1)

# Add the second bar chart to the subplot grid
for trace in fig2.data:
    fig.add_trace(trace, row=1, col=2)

fig.update_layout(
    barmode='stack',
    width=1600,
    height=850,  # Set the desired height in pixels
    title=dict(text='Renda dos responsáveis dos domicílios por gênero - Natal RN', font=dict(size=20)),
    yaxis=dict(title='Nome do Bairro'),
    xaxis1=dict(range=[0, 15000], title='Quantidade'),  # Set x-axis range for the first subplot
    xaxis2=dict(range=[0, 15000], title='Quantidade')
)

fig.update_xaxes(autorange="reversed", row=1, col=1) # Reverse the x-axis values for the first chart
#fig.update_yaxes(ticktext=[''] * len(analise02), tickvals=analise02['Nome_do_bairro'], row=1, col=2) # Remove y-axis values for the second chart
fig.update_yaxes(autorange="reversed") # Reverse the y-axis values

st.plotly_chart(fig)
