
# def salvar_carro(marca, modelo, ano, placa):
#     # salva carro no banco de dados...
#     print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
# salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
# salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})


def gravar_pessoa(nome, idade, genero, contato):
    # Grava pessoa na base de dados
    print(f"Nome: {nome} / Idade: {idade} / Género: {genero} / Contacto: {contato}")

gravar_pessoa("Ivan", 45, "Masculino", "ivan.almeida1979@gmail.com")
gravar_pessoa(nome = "Carolina", idade = 1, genero = "Feminino", contato = "carolina.almeida@gmail.com")
gravar_pessoa(**{"nome": "Noémia", "idade": 45, "genero": "Feminino", "contato": "noemia.figueiredo@gmail.com"})
