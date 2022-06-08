import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go # plotly graphical object

df = pd.read_csv('TexasTurbine.csv', encoding='latin-1')
print(df)
df.columns = ['data', 'pot_ativa', 'vel_vento', 'vel_dir', 'pressure', 'temperature','int_vel_vento','pot_teo']
print(df.data)
#Tratamento de dados
#--------------------------------------------------
#Transformando a coluna data em tipo de data
df['data'] = pd.to_datetime(df['data'])
df.set_index('data',inplace=True)
datas = df.index
print(datas)

#Extrair dia,mes e horas da variável data
print(datas)
horas = []
dia = []
mes = []
#Extrai apenas a porção hora do tipo data
for data in datas:
    horas.append(data.hour)
    dia.append(data.day)
    mes.append(data.month)

df['horas'] = horas
df['dias'] = dia
df['mes'] = mes

intervalo = np.arange(0,20,1)
media_vento = df.groupby(pd.cut(df['vel_vento'],intervalo)).mean()
media_vento_int = df.groupby(pd.cut(df['vel_vento'],intervalo)).mean()

plt.figure()
media_vento.pot_ativa.plot(rot=45,label="Potência ativa",style='.-')
media_vento_int.pot_teo.plot(label="Potência Teorica",color="blue",style='-')

plt.figure()
cont_vento = df.groupby(pd.cut(df['vel_vento'],intervalo)).count()
cont_vento.vel_vento.plot(kind = "bar",title='Average of Active Power of each Hours')

# plt.figure()
# ax = df.plot(x='vel_vento', y='pot_ativa',style="o")
# df.plot(ax=ax,x='vel_vento', y='pot_teo',style='.')
#Tratamento
# df2 = df[(df.pot_teo>0) & (df.vel_vento>=3.5)]

# ax2 = df2.plot(x='vel_vento',y='pot_teo',style='.')
# df2.plot(ax=ax2,x='vel_vento',y='pot_ativa',style='.')

        
# for i in range(len(df.pot_ativa)):
#     if (df.pot_ativa[i] > 0) & (df.vel_vento[i] <=3.5):
#         df.pot_ativa[i] = 0
#     elif ((df.pot_ativa[i] > 200) & (df.vel_vento[i] <=4.25) & (df.vel_vento[i] > 3.5)):
#         df.pot_ativa[i] = 0
#     else:
#         df.pot_ativa[i] = df.pot_ativa[i]

for i in range(len(df.pot_ativa)):
    if (df.pot_ativa[i] > 0) & (df.vel_vento[i] <=3.5):
        df.iloc[i,0] = 0
    elif ((df.pot_ativa[i] > 200) & (df.vel_vento[i] <=4.25) & (df.vel_vento[i] > 3.5)):
        df.iloc[i,0] = 0
    else:
        df.iloc[i,0] = df.pot_ativa[i]


print(df.loc[:,'vel_vento']) #refere-se o item (ver se na linha um numero corresponde ao n desejado) e a coluna desejada (nome da coluna)
print(df.iloc[1,1]) #refere-se a posição (linha) e coluna desejada (posição da coluna)
ax = df.plot(x='vel_vento', y='pot_ativa',style="o")
df.plot(ax=ax,x='vel_vento', y='pot_teo',style='.')

#Válido Somente valores onde Pot_teo>Pot_ativa
df2 = df[df.pot_ativa<df.pot_teo]
ax2 = df.plot(x='vel_vento', y='pot_ativa',style="o")

plt.figure()
media_vento_corr = df2.groupby(pd.cut(df2['vel_vento'],intervalo)).mean()
media_vento_corr.pot_ativa.plot(label="Potência Ativa Corrigida")
media_vento_corr.pot_teo.plot(label="Potência Teórica")
plt.legend()


print("-------------")
x = df.groupby(pd.cut(df['vel_vento'],intervalo)).count().vel_vento.index
x = np.arange(1,20,1)
y = df.groupby(pd.cut(df['vel_vento'],intervalo)).count().vel_vento.values
print(x)

# trace1 = go.Histogram(
#     x=x,
#     y = y,
#     name = "2011",
#     # marker=dict(color='rgba(171, 50, 96, 0.6)')
# )

# data = trace1
# layout = go.Layout(barmode='overlay',
#                    title=' pao',
#                    xaxis=dict(title='students-staff ratio'),
#                    yaxis=dict( title='Count'),
# )
# fig = go.Figure(data=data, layout=layout)
# fig.show()

plt.figure()
# plt.plot(x,y)
plt.bar(x = x, height = y)
plt.title('pao')
plt.show()