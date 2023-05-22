# Integrantes do Grupo
Arthur de Brito Bonifácio - 2019006370

Heitor de Paula Santos Damasceno - 2019006671

Thiago Henrique Moreira Santos - 2019007074

# Tecnologias Utilizadas

<img src="https://www.tshirtgeek.com.br/wp-content/uploads/2021/03/com001.jpg" width=250 height=250>
<img src="https://media.trustradius.com/product-logos/Ou/HU/R8JW30GR5ELU-180x180.PNG" width=250 height=250>

Python é uma linguagem de programação interpretada que vem se tornado muito popular pela facilidade de utilização e grande quantidade de bibliotecas.

SQLite é uma biblioteca lightweight de python que permite operações em um banco de dado SQL, que na prática salva o banco em um arquivo .db.


# O que é
Uma implementação de um sistema de controle de bibliotecas. O sistema possui três grandes entidades e duas delas representam papéis que podem ser assumidos:

* Administradores
* Cliente
* Livros

Os dois papéis mencionados possuem os seguintes **casos de uso**:
* Cliente
    - Como cliente eu gostaria de alugar livros
    - Como cliente eu gostaria de visualizar as informações de um livro
    - Como cliente eu gostaria de ver meus livros alugados
    - Como cliente eu gostaria de renovar o aluguel de um dos livros
    - Como cliente eu gostaria de devolver um livro
    - Como cliente eu gostaria de consultar multas pendentes

* Admnistrador
    - Como administrador eu gostaria de adicionar, remover e editar livros
    - Como administrador eu gostaria de adicionar, remover e editar usuários
    - Como administrador de registrar a devolução de um livro
    - Como administrador eu gostaria de registrar a quitação de uma multa

# Como utilizar
A interface da aplicação é o próprio terminal, portanto, seguem as instruções para uso:

```
python3 main.py
```
O comando acima executa o código principal da aplicação permitindo que seja realizada as diversas operações mencionadas anteriormente.

