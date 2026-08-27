# 🖥️ GPU Scraper: Análise de Preço e Performance

Um projeto de web scraping em Python, desenvolvido e executado no **Google Colab**, que coleta dados de placas de vídeo (GPUs), converte os valores para Real Brasileiro (R$) e armazena as informações estruturadas em um banco de dados.

## 🎯 Objetivo
Automatizar a coleta de dados de performance (benchmarks) e preços de placas de vídeo, permitindo analisar o custo-benefício de cada modelo diretamente em moeda local.

## ✨ Funcionalidades
- **Web Scraping:** Extração automática de modelos de GPUs, pontuações de benchmark e preços em dólares (ou outra moeda de origem).
- **Conversão de Câmbio:** Conversão automática dos preços extraídos para Real Brasileiro (BRL) usando a cotação atual.
- **Armazenamento:** Salvamento dos dados limpos e processados em um banco de dados (SQLite) para consultas futuras.
- **Ambiente em Nuvem:** Feito para rodar diretamente no Google Colab, sem necessidade de configuração complexa de ambiente local.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** [Python 3](https://www.python.org/)
- **Ambiente:** [Google Colab](https://colab.research.google.com/)
- **Bibliotecas Principais:**
  - `requests` e `BeautifulSoup4` - Para coleta de dados nas páginas web.
  - `pandas` - Para manipulação, limpeza e organização dos dados.
