Este projeto implementa um sistema simples de gerenciamento de uma livraria utilizando Python junto com o SQLite.
Permitindo o cadatro de livros, clientes e pedidos, e também exibi os pedidos realizados.

1. Classes de Modelo
Livro: Representa um livro na livraria.

Atributos:

titulo: Título do livro.

autor: Autor do livro.

preco: Preço do livro.

Cliente: Representa um cliente da livraria.

Atributos:

nome: Nome do cliente.

email: E-mail do cliente.

Pedido: Representa um pedido realizado por um cliente.

Atributos:

cliente_id: ID do cliente que realizou o pedido.

livro_id: ID do livro solicitado.

quantidade: Quantidade do livro solicitada.

data_pedido: Data em que o pedido foi realizado.

2. Funções de Banco de Dados
conectar_banco(nome_banco): Estabelece uma conexão com o banco de dados SQLite especificado por nome_banco.

criar_tabelas(conexao): Cria as tabelas Livros, Clientes e Pedidos no banco de dados, caso ainda não existam. As tabelas possuem os seguintes campos:

Livros: id, titulo, autor, preco.

Clientes: id, nome, email.

Pedidos: id, cliente_id, livro_id, quantidade, data_pedido.

inserir_dados(conexao): Insere dados de exemplo nas tabelas Livros, Clientes e Pedidos.

exibir_pedidos(conexao): Exibe todos os pedidos realizados, incluindo o nome do cliente e o título do livro.

3. Fluxo Principal
No bloco principal (if __name__ == '__main__':), o código executa as seguintes etapas:

Conecta-se ao banco de dados livraria.db.

Cria as tabelas no banco de dados.

Insere dados de exemplo nas tabelas.

Exibe todos os pedidos realizados.

Banco de Dados SQLite
O banco de dados é gerenciado utilizando o módulo sqlite3 do Python, que oferece uma interface DB-API 2.0 para interação com bancos de dados SQLite.

Observações
O código utiliza chaves estrangeiras (FOREIGN KEY) para estabelecer relacionamentos entre as tabelas Pedidos, Clientes e Livros, garantindo a integridade referencial dos dados.

As operações de inserção e consulta são realizadas utilizando instruções SQL executadas através de cursores (cursor).

O banco de dados é armazenado em um arquivo local (livraria.db), facilitando o acesso e a persistência dos dados.

Como Executar
Clone este repositório em sua máquina local.

Certifique-se de ter o Python 3.x instalado.

Execute o script Python:
terminal: python nome_do_arquivo.py
Substitua nome_do_arquivo.py pelo nome do arquivo que contém o código.
O sistema criará o banco de dados livraria.db e exibirá os pedidos realizados.
