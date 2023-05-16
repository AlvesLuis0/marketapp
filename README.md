# API de supermercado
Este é uma simples API desenvolvida em Python com Django. Com este app é possível cadastrar, apagar,
visualizar e apresentar todos os registros de clientes e produtos.

## Tabelas
A seguir, a estrutura das tabelas dos clientes e produtos, que serão implementadas no Django.

### Clientes

```SQL
CREATE TABLE CLIENT (
	CPF CHAR(11) PRIMARY KEY,
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
- [x] `/` -> Página inicial _(Leva para a visualização e cadastro de clientes e produtos)_;
- [x] `/client/get` -> Tabela de clientes;
- [x] `/client/post` -> Formulário para cadastrar cliente;
- [x] `/product/get` -> Tabela de produtos;
- [x] `/product/post` -> Formulário para cadastrar produto.

## Extras de desenvolvimento
A seguir, alguns scripts para auxiliar no desenvolvimento do projeto, mas antes, você deve executar os seguintes comandos para dar permissão de execução de arquivos:
```console
chmod +x build.sh
chmod +x clear.sh
```

### Construir o Banco de Dados
Execute o comando `./build.sh` para criar o banco de dados, incluindo clientes, produtos e usuários do
painel de admin.

### Resetar o Banco de Dados
Execute o comando `./clear.sh` para limpar todo o banco de dados, incluindo clientes, produtos e usuários
do painel de admin.

## Futuras implementações
- [ ] Tela de login;
- [ ] Além do cliente, terá o funcionário e o administrador;
- [ ] Cada cargo terá seu painel personalizado com suas respectivas permissões;
- [ ] O cliente pode apenas ver os produtos cadastrados, e comprá-los;
- [ ] O funcionário pode manipular o banco de dados (criar, alterar e deletar **produtos**);
- [ ] O administrador pode adicionar e deletar **funcionários**, além das permissões anteriores.