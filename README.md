
# Web Scraping

Este projeto realiza web scraping do site Kabum.com.br para extrair informações sobre placas de vídeo (VGA), incluindo nomes dos produtos e preços. Os dados coletados são armazenados em um arquivo CSV e exibidos em formato de tabela no console.
## Pré-requisitos

Antes de executar o script, certifique-se de ter instalado os seguintes componentes:
- Python 3:
- Selenium: Biblioteca para automação web
````
pip install selenium

````
- Pandas: Biblioteca para manipulação de dados
````
pip install pandas

````
- Tabulate: Biblioteca para formatação de tabelas
````
pip install tabulate

````
- WebDriver do Chrome: O script utiliza o ChromeDriver, que deve ser compatível com sua versão do Chrome

    Verifique sua versão do Chrome em chrome://settings/help

    Baixe o ChromeDriver correspondente em ChromeDriver Downloads

    Coloque o chromedriver.exe no PATH ou especifique seu local no código
## Como Executar

- Clone o repositório ou copie o código para um arquivo Python (ex: scraper.py)
- Instale as dependências conforme listado acima
- Execute o script:
````
python scraper.py
````
## Funcionamento do Código

O script realiza as seguintes operações:

- Configuração do Navegador:

    Inicializa o ChromeDriver com opções padrão

    Acessa a URL específica de placas de vídeo no Kabum

- Coleta de Dados:

    Localiza e extrai os nomes dos produtos (elementos com classe nameCard)

    Localiza e extrai os preços (elementos com classe priceCard)

    Navega por todas as páginas disponíveis (através do botão "Próxima")

- Processamento dos Dados:

    Gera um arquivo CSV chamado placas.csv com os dados coletados

    Exibe os dados formatados em tabela no console usando a biblioteca Tabulate
