
# Pesquisa de preço com Webscraping

Objetivo deste projeto é fazer um robo que acessa o site de um marketplace especifico (nesse exemplo acessamos o americanas.com.br), procura pelos produtos definidos, comparar se o preço está menor que o estipulado e caso esteja retorna a URL desse produto.

## Stack utilizada

**Back-end:** Python;

**Bibliotecas:** Requests, BeutifulSoup, gzip, brotli, io.

### OBS

- Comentei cada etapa do código (um pouco na contra a mao de um clean code), pois, esse repositório foi criado para fins educativos. 

- O projeto surgiu de uma necessidade real e decide compartilhar o inicio do projeto (a lógica de como vai funcionar) para demonstrar um pouco do meu conhecimento e o que já desenvolvi.

- O algortimo final está o mais simples possível (só para testar se realmente está funcionando).


### Atenção

O BeatifulSoup está procurando os dados atráves de classes HTML do site especifico (americanas), ao passar do tempo se essas classes forem alteradas pelo site, o algoritmo não vai retornar dados. 

A solução é simples, basta inserir a classe correta na parte do BeautifulSoup.





