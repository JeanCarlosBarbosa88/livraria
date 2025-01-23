class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
     
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        
class Pedido:
    def __init__(self, cliente_id,
                 livro_id, quantidade, data_pedido):
        self.cliente_id = cliente_id   
        self.livro_id = livro_id
        self.quantidade = quantidade
        self.data_pedido = data_pedido
    
import sqlite3

def conectar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao 

def criar_tabelas(conexao):
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Livros(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      titulo TEXT NOT NULL,
                      autor TEXT NOT NULL,
                      preco REAL NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      EMAIL textnot null)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      cliente_id INTEGER NOT NULL,
                      livro_id INTEGER NOT NULL,
                      quantidade INTEGER NOT NULL,
                      data_pedido TEXT NOT NULL,
                      FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                      FOREIGN KEY (livro_id) REFERENCES Livros(id))''')
    
    conexao.commit()
    cursor.close()
    
def inserir_dados(conexao):
    cursor = conexao.cursor()
    
    livro = [Livro('Python para iniciantes', 'John Doe', 39.99),
             Livro('Algoritmos e Estruturas de Dados', 'Jane Smith', 78.65),
             Livro('inteligência Artificial', 'Alan Turing', 58.89)]
    
    clientes = [Cliente('Ravi', 'ravi@exemple.com'),
                Cliente('Luana', 'luana@exemple.com'),
                Cliente('Jean', 'jean@exemple.com'),]
    
    pedidos = [Pedido(1, 2, 4, '2021-08-25'),
               Pedido(2, 1, 6, '2021-04-13'),
               Pedido(1, 1, 2, '2024-11-15')]
    
    for livro in livro:
        cursor.execute('INSERT INTO Livros (titulo, autor, preco) VALUES (:titulo, :autor, :preco)', vars(livro))
    
    for cliente in clientes:
        cursor.execute('INSERT INTO Clientes (nome, email) VALUES (:nome, :email)', vars(cliente))  
          
    for pedido in pedidos:
        cursor.execute('INSERT INTO Pedidos (cliente_id, livro_id, quantidade, data_pedido) VALUES (:cliente_id, :livro_id, :quantidade, :data_pedido)', vars(pedido))    
    conexao.commit()
    cursor.close()
        
def exibir_pedidos(conexao):
    cursor = conexao.cursor()   
    query = '''    
    SELECT Pedidos.id, Clientes.nome, Livros.titulo, Pedidos.quantidade, Pedidos.data_pedido
    FROM Pedidos
    JOIN Clientes ON Pedidos.cliente_id = Clientes.id
    JOIN Livros ON Pedidos.livro_id = Livros.id
    '''    
    cursor.execute(query)
    pedidos = cursor.fetchall()    
    print('Pedidos:')

    for pedido in pedidos:        
        print(pedido)        
               
if __name__ == '__main__':
    conexao = conectar_banco('livraria.db')
    criar_tabelas(conexao)
    inserir_dados(conexao)
    exibir_pedidos(conexao)
    conexao.close()               
            