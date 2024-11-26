import random #biblioteca para randomizar os caracteres
import string #biblioteca que os caracteres

def gerar_senha(complex,compri):
    '''
    função que gera uma string de senha de acordo com os argumentos complexidade e comprimento
    '''
    if (complex == 'Baixa'):
        caracteres = string.ascii_letters
    elif (complex == 'Média' or complex == 'Media'):
        caracteres = string.ascii_letters + string.digits
    elif (complex == 'Alta'):
        caracteres = string.ascii_letters + string.digits + string.punctuation
    
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha
    
if __name__ == '__main__':
    print('Bem vindo ao programa de geração de senhas.')
    #loop de verificação de inserção valores correta
    while True:
        complexidade = input('Digite o nível de complexidade esperado: Baixa, Media ou Alta: ').capitalize()
        if complexidade in ['Baixa', 'Média','Media', 'Alta']:
            break
        else:
            print('Erro: Digite uma complexidade válida.')
    
    #loop de verificaçao de inserção de valores correta
    while True:
        try:
            comprimento = int(input('Digite quantos caracteres você quer que sua senha tenha: '))
            break
        except ValueError:
            print('Erro: Digite um número inteiro.')
        
    #chamar a função gerar_senha
    senha_gerada = gerar_senha(complexidade,comprimento)
    print(f'A senha gerada é: {senha_gerada}')
    
    
    