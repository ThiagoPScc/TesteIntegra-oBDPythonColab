from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from dataclasses import dataclass, asdict

#Código com objetivo de pegar dados de placas de vídeos e permitir pesquisas e graficos sobre seus dados e posteriormente permitir a exportação do arquivo para JSON, CSV e TXT.
@dataclass
class PlacaDeVideo:
    nome:str #nome da placa
    tipo:str  #se é para servidor ou desktop
    desempenho:float #nota geral de desempenho
    preco:float #preço da placa
    ano:int #ano de lançamento da placa

#site de onde vem os dados
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
NOME_DA_TABELA = "Placas"
URL = "https://technical.city/pt/video/best-price-to-performance"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

dados = soup.findAll('td')

def converter_dados_site_para_vetor(dadosBruto):
    dados_individuais = []
    for dado in dadosBruto:
      dadoLimpo = dado.text
      dadoLimpo = dadoLimpo.replace("\n","").replace("\t","").replace("\r","")
      if dadoLimpo != "":
        dados_individuais.append(dadoLimpo)
    print("V1C")
    return dados_individuais

def converter_dados_vetor_para_dataBase(dados):
  qntPlacas = len(dados)
  #chunking, separando os dados do vetor maior em 7 para criação de intervalos de dados de cada placa
  # aqui colocamos uma variavel que vai receber os dados de i que será contado no loop até i +7, que é o valor do intervalo, isso na quantidade certa de loops usando os parametros do in range
  dadosSeparados = [dados[i : i + 7] for i in range(0, len(dados), 7)]
  return dadosSeparados
  print(dadosSeparados)



def converter_moeda(dados):
  dadosConvertidos = []
  for dado in dados:
    dado[4] = dado[4].split(' ')
    dado[4] = dado[4][0]
    dado[4] = float(dado[4])
    dado[4] = dado[4] * 5.35

    dado.append(dado[4])
    dadosConvertidos.append(dado)
  return dadosConvertidos


def criar_dataBase(dados):
  listaDePlacasGeral = []
  for dado in dados:
    placa_atual = PlacaDeVideo(
    nome = dado[1],
    tipo = dado[2],
    desempenho = dado[5],
    preco = dado[4],
    ano = dado[6]
  )

    listaDePlacasGeral.append(placa_atual)

  return listaDePlacasGeral


#print(dados)
dadosVetor = converter_dados_site_para_vetor(dados)
dadosDataBase = converter_dados_vetor_para_dataBase(dadosVetor)
valorReais = converter_moeda(dadosDataBase)
#print(len(dadosDataBase))
#print(criar_dataBase(dadosDataBase))

listDB = criar_dataBase(dadosDataBase)


DT = pd.DataFrame(listDB)
print("-----------------------")
#print(DT)
dados_para_enviar = DT.to_dict(orient='records')
print(dados_para_enviar)

url_para_inserir = f"{NEXT_PUBLIC_SUPABASE_URL}/rest/v1/{NOME_DA_TABELA}"

headers = {
    "apikey": NEXT_PUBLIC_SUPABASE_ANON_KEY,
    "Authorization": f"Bearer {NEXT_PUBLIC_SUPABASE_ANON_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

try:
    response = requests.post(url_para_inserir, json=dados_para_enviar, headers=headers)


    if response.status_code == 201:
        print(f"Sucesso! {len(dados_para_enviar)} linhas inseridas no Supabase.")
    else:
        print(f"Erro ao inserir. Status: {response.status_code}")
        print(response.text) 

except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}")
