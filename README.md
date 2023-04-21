# API de supermercado
Este é uma simples API desenvolvida em Python com Django. Com este app é possível cadastrar, apagar,
visualizar e apresentar todos os registros de clientes e produtos.

## Tabelas

### Clientes

```SQL
CREATE TABLE CLIENT (
	CPF INTEGER PRIMARY KEY,
	NAME CHAR(50),
	PHONE CHAR(22),
	REGISTERED DATE
);
```

### Produtos

```SQL
CREATE TABLE PRODUCT (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NAME CHAR(50),
	PRICE DECIMAL,
	QUANTITY INTEGER DEFAULT 0,
	REGISTERED DATE
);
```

## Urls
- [ ] `/` -> Página inicial _(Leva para a visualização e cadastro de clientes e produtos)_;

- [ ] `/client/get` -> Tabela de clientes;
- [ ] `/client/post` -> Formulário para cadastrar cliente;
- [ ] `/client/delete/<int>` -> Endpoint para deletar registro de um cliente;

- [ ] `/product/get` -> Tabela de produtos;
- [ ] `/product/post` -> Formulário para cadastrar produto;
- [ ] `/product/delete/<int>` -> Endpoint para deletar registro de um produto.