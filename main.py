import pandas as pd
import matplotlib.pyplot as plt

# Importando as medianas do DataFrame das notas de Ciências da Natureza da prova do ENEM de 2018 a 2022
cn22 = pd.read_csv(r"df_notasCNatureza18a22\df_notaCN22.csv")['NU_NOTA_CN'].dropna().median() # Nota de 2022
cn21 = pd.read_csv(r"df_notasCNatureza18a22\df_notaCN21.csv")['NU_NOTA_CN'].dropna().median() # Nota de 2021
cn20 = pd.read_csv(r"df_notasCNatureza18a22\df_notaCN20.csv")['NU_NOTA_CN'].dropna().median() # Nota de 2020
cn19 = pd.read_csv(r"df_notasCNatureza18a22\df_notaCN19.csv")['NU_NOTA_CN'].dropna().median() # Nota de 2019
cn18 = pd.read_csv(r"df_notasCNatureza18a22\df_notaCN18.csv")['NU_NOTA_CN'].dropna().median() # Nota de 2018

# Importando as medianas do DataFrame das notas de Ciências Humanas da prova do ENEM de 2018 a 2022
ch22 = pd.read_csv(r"df_notasCHumanas18a22\df_notaCH22.csv")['NU_NOTA_CH'].dropna().median() # Nota de 2022
ch21 = pd.read_csv(r"df_notasCHumanas18a22\df_notaCH21.csv")['NU_NOTA_CH'].dropna().median() # Nota de 2021
ch20 = pd.read_csv(r"df_notasCHumanas18a22\df_notaCH20.csv")['NU_NOTA_CH'].dropna().median() # Nota de 2020
ch19 = pd.read_csv(r"df_notasCHumanas18a22\df_notaCH19.csv")['NU_NOTA_CH'].dropna().median() # Nota de 2019
ch18 = pd.read_csv(r"df_notasCHumanas18a22\df_notaCH18.csv")['NU_NOTA_CH'].dropna().median() # Nota de 2018

# Importando as medianas do DataFrame das notas de Linguagens e Códigos da prova do ENEM de 2018 a 2022
lc22 = pd.read_csv(r"df_notasLCodigos18a22\df_notaLC22.csv")['NU_NOTA_LC'].dropna().median() # Nota de 2022
lc21 = pd.read_csv(r"df_notasLCodigos18a22\df_notaLC21.csv")['NU_NOTA_LC'].dropna().median() # Nota de 2021
lc20 = pd.read_csv(r"df_notasLCodigos18a22\df_notaLC20.csv")['NU_NOTA_LC'].dropna().median() # Nota de 2020
lc19 = pd.read_csv(r"df_notasLCodigos18a22\df_notaLC19.csv")['NU_NOTA_LC'].dropna().median() # Nota de 2019
lc18 = pd.read_csv(r"df_notasLCodigos18a22\df_notaLC18.csv")['NU_NOTA_LC'].dropna().median() # Nota de 2018

# Importando as medianas do DataFrame das notas de Matemática da prova do ENEM de 2018 a 2022
mt22 = pd.read_csv(r"df_notasMatematica18a22\df_notaMT22.csv")['NU_NOTA_MT'].dropna().median() # Nota de 2022
mt21 = pd.read_csv(r"df_notasMatematica18a22\df_notaMT21.csv")['NU_NOTA_MT'].dropna().median() # Nota de 2021
mt20 = pd.read_csv(r"df_notasMatematica18a22\df_notaMT20.csv")['NU_NOTA_MT'].dropna().median() # Nota de 2020
mt19 = pd.read_csv(r"df_notasMatematica18a22\df_notaMT19.csv")['NU_NOTA_MT'].dropna().median() # Nota de 2019
mt18 = pd.read_csv(r"df_notasMatematica18a22\df_notaMT18.csv")['NU_NOTA_MT'].dropna().median() # Nota de 2018

# Importando as medianas do DataFrame das notas de Redação da prova do ENEM de 2018 a 2022
redacao22 = pd.read_csv(r"df_notasRedacao18a22\df_notaRedacao22.csv")['NU_NOTA_REDACAO'].dropna().median() # Nota de 2022
redacao21 = pd.read_csv(r"df_notasRedacao18a22\df_notaRedacao21.csv")['NU_NOTA_REDACAO'].dropna().median() # Nota de 2021
redacao20 = pd.read_csv(r"df_notasRedacao18a22\df_notaRedacao20.csv")['NU_NOTA_REDACAO'].dropna().median() # Nota de 2020
redacao19 = pd.read_csv(r"df_notasRedacao18a22\df_notaRedacao19.csv")['NU_NOTA_REDACAO'].dropna().median() # Nota de 2019
redacao18 = pd.read_csv(r"df_notasRedacao18a22\df_notaRedacao18.csv")['NU_NOTA_REDACAO'].dropna().median() # Nota de 2018

# Criando as listas com as medianas e os rótulos
labels = ['2018', '2019', '2020', '2021', '2022']
medianas_cn = [cn18, cn19, cn20, cn21, cn22]
medianas_ch = [ch18, ch19, ch20, ch21, ch22]
medianas_lc = [lc18, lc19, lc20, lc21, lc22]
medianas_mt = [mt18, mt19, mt20, mt21, mt22]
medianas_redacao = [redacao18, redacao19, redacao20, redacao21, redacao22]

# Plotando os gráficos
plt.plot(labels, medianas_cn, label='Ciências da Natureza', marker='o')
plt.plot(labels, medianas_ch, label='Ciências Humanas', marker='o')
plt.plot(labels, medianas_lc, label='Linguagens e Códigos', marker='o')
plt.plot(labels, medianas_mt, label='Matemática', marker='o')
plt.plot(labels, medianas_redacao, label='Redação', marker='o')

# Definindo o limite do eixo y
plt.ylim([450, 650])

# Adicionando título e legendas
plt.title('Medianas das Notas do ENEM por Área de Conhecimento')
plt.xlabel('Ano')
plt.ylabel('Mediana da Nota')

# Exibindo a legenda
plt.legend()

# Salvando o gráfico em PDF
plt.savefig('grafico_notas18a22.pdf', format='pdf')

# Exibindo o gráfico
plt.show()
