# API de supermercado
Este é uma simples API desenvolvida em Python com Django. Com este app é possível cadastrar, apagar,
visualizar e apresentar todos os registros de clientes e produtos.

## Tabelas

### Clientes

```SQL
CREATE TABLE CLIENT (
	CPF CHAR(14) PRIMARY KEY,
	NAME CHAR(50) NOT NULL,
	REGISTERED DATE NOT NULL
);
```

### Produtos

```SQL
CREATE TABLE PRODUCT (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NAME CHAR(50) NOT NULL,
	PRICE REAL NOT NULL,
	QUANTITY INTEGER DEFAULT 0 NOT NULL,
	REGISTERED DATE NOT NULL
);
```

## Urls
- [ ] `/` -> Página inicial _(Leva para a visualização e cadastro de clientes e produtos)_;

- [ ] `/client/get` -> Tabela de clientes;
- [ ] `/client/get/<int>` -> Informações de um cliente específico;
- [ ] `/client/post` -> Formulário para cadastrar cliente;
- [ ] `/client/delete` -> Endpoint para deletar registro de um cliente;

- [ ] `/product/get` -> Tabela de produtos;
- [ ] `/product/get/<int>` -> Informações de um produto específico;
- [ ] `/product/post` -> Formulário para cadastrar produto;
- [ ] `/product/delete` -> Endpoint para deletar registro de um produto.