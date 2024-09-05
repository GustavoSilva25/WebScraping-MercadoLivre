# WebScraping-MercadoLivre

Este projeto realiza a busca de produtos no Mercado Livre, extrai informações como nome, preço e link do produto, e salva os resultados em uma planilha Excel.

## Funcionalidades

- Busca automatizada de produtos no Mercado Livre.
- Extração de informações: título, preço e link do produto.
- Geração de arquivo Excel com os resultados da busca.

## Tecnologias Utilizadas

- **Python 3**
- **BeautifulSoup** para a extração de dados do HTML.
- **requests** para fazer requisições HTTP.
- **openpyxl** para manipulação de arquivos Excel.

## Como Utilizar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/WebScraping-MercadoLivre.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd WebScraping-MercadoLivre
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute o script:
    ```bash
    python main.py
    ```

5. Digite o nome do produto que deseja buscar quando solicitado:
    ```bash
    >> "Nome do Produto"
    ```

6. O script irá processar os resultados e salvar a lista de produtos em um arquivo Excel na pasta do projeto.

## Exemplo de Saída

Após a execução, será gerado um arquivo Excel com o nome do produto buscado e a data/hora do download, por exemplo:
```bash
  nome_do_produto_05092024_183045.xlsx
```


## Estrutura do Projeto

- `main.py`: Script principal que realiza o web scraping e salva os resultados.
- `requirements.txt`: Arquivo contendo as bibliotecas necessárias para o projeto.

## Considerações Legais

Este projeto é para fins educacionais e de pesquisa. O uso de web scraping deve estar em conformidade com os termos de serviço do site Mercado Livre. Respeite as regras do site e evite sobrecarregar os servidores.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

