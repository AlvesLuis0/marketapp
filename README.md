# API de supermercado
Este é uma simples API desenvolvida em Python com Django. Com este app é possível cadastrar, apagar,
visualizar e apresentar todos os registros de produtos, funcionários e administradores.

## Tabelas
A seguir, a estrutura das tabelas que serão implementadas no Django.

### Produtos

```SQL
CREATE TABLE PRODUCT (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NAME CHAR(50),
	PRICE DECIMAL,
	QUANTITY INTEGER DEFAULT 0,
);
```

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
- [x] Tela de login;
- [x] Além do cliente, terá o funcionário e o administrador;
- [x] Cada cargo terá seu painel personalizado com suas respectivas permissões;
- [x] O cliente pode apenas ver os produtos cadastrados, e comprá-los;
- [x] O funcionário pode manipular o banco de dados (criar, alterar e deletar **produtos**);
- [x] O administrador pode adicionar e deletar **funcionários**, além das permissões anteriores.

## Aprendizado
Com a construção dessa aplicação, foi possível desenvolver novas lógicas e conceitos sobre o e-commerce,
funcionalidades que o Django possui que não sabíamos, como por exemplo o sistema de autenticação e de
sessões, além de detalhes mais estéticos. A formatação do HTML e CSS no Django foi algo que nos confundiu no
começo. Porém, nada que algumas horas de estudo a mais não resolvessem!

Trabalhar neste projeto nos ofereceu uma gama de novas possibilidades, tanto no quesito técnico, quanto na
colaboração, comunicação e trabalho em equipe.