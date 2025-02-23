# Bot para extrair a cotação do Euro (EUR-BRL)
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime


def formatar_cotacao(cotacao):
    cotacao_sem_milhar = cotacao.replace('.', '')   
    return float(cotacao_sem_milhar.replace(',', '.'))

# Função para extrair a cotação do Euro
def extrair_cotacao_euro():
    url = 'https://www.google.com/finance/quote/EUR-BRL'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    cotacao_elemento = soup.find('div', class_='YMlKec fxKbKc')
    if not cotacao_elemento:
        raise ValueError("Não foi possível encontrar a cotação do Euro.")

    cotacao = cotacao_elemento.text.strip()
    return cotacao

# Função principal
def main():
    try:
        # Extrair a cotação do Euro
        cotacao = extrair_cotacao_euro()
        print(f'Cotação atual do Euro (EUR-BRL): R$ {cotacao}')
        cotacao_float = formatar_cotacao(cotacao)

        # Salvar resultados em CSV
        with open('cotacoes_EUR_BRL.csv', 'a') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([datetime.now().strftime('%d/%m/%Y'), cotacao_float])

        if cotacao_float > 6.0:
            print("A cotação do Euro ultrapassou R$ 6.0! Enviando alerta...")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()