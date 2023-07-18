# Sistema de Plotagem de Médias das Notas do ENEM

Este é um sistema simples de plotagem de gráficos que analisa as médias das notas do ENEM (Exame Nacional do Ensino Médio) para diferentes áreas de conhecimento ao longo dos anos de 2018 a 2022. O sistema utiliza a biblioteca pandas para importar os dados das notas de cada área e a biblioteca Matplotlib para plotar os gráficos.

## Requisitos

- Python 3.x instalado no sistema
- Bibliotecas pandas e matplotlib instaladas. Caso não estejam instaladas, você pode instalá-las utilizando o gerenciador de pacotes pip:

```
pip install pandas
pip install matplotlib
```

## Como utilizar o sistema

1. Baixe o código do sistema em seu computador.
2. Certifique-se de ter os arquivos de dados corretos nos caminhos definidos no código. Os arquivos contendo as notas de cada área devem estar no formato CSV.
3. Execute o código em um ambiente Python, como Jupyter Notebook, ou em um arquivo Python (.py).

O sistema importará as médias das notas de Ciências da Natureza, Ciências Humanas, Linguagens e Códigos, Matemática e Redação para os anos de 2018 a 2022 e plotará um gráfico de linha para cada área. As médias serão exibidas no eixo y, enquanto os anos serão exibidos no eixo x.

## Personalização

Você pode personalizar o sistema de acordo com suas necessidades:

- Altere os caminhos dos arquivos de dados (variáveis `cn18`, `cn19`, etc.) para apontar para os seus arquivos de notas específicos.
- Personalize os rótulos e cores dos gráficos modificando os parâmetros nas funções `plt.plot()`.
- Modifique o limite superior do eixo y para cada gráfico com `plt.ylim()` para melhorar a visualização dos dados.

## Salvar o Gráfico

O sistema salva o gráfico em formato PDF usando a função `plt.savefig()`. O arquivo PDF será salvo no diretório especificado pelo caminho fornecido. Se você preferir salvá-lo em outro formato, como PNG ou JPEG, pode modificar o parâmetro `format` na função `plt.savefig()`.

Espero que este sistema seja útil para analisar as médias das notas do ENEM em diferentes áreas de conhecimento ao longo dos anos. Se você tiver alguma dúvida ou precisar de mais informações, sinta-se à vontade para entrar em contato.

Divirta-se plotando seus gráficos!
