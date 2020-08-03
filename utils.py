from models import Pessoas

# Insere dados na tabela pessoas
def insere_pessoas():
    pessoa = Pessoas(nome='Miguel', idade=4)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoas
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome = 'Jailton').first()
    print(pessoa.nome, pessoa.idade)


# Realiza alteração na tabela pessoas
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(id=2).first()
    #pessoa.idade = 30
    pessoa.nome = 'Miguel'
    pessoa.save()

# Realiza exclusão na tabela pessoas
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Miguel').first()
    pessoa.delete()

if __name__ == '__main__':
    insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    consulta_pessoas()
