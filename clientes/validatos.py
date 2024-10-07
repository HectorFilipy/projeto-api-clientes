import re
from validate_docbr import CPF

def cpf_valido(valide_cpf):
    cpf = CPF()
    return cpf.validate(valide_cpf)
    
def rg_valido(rg):
    return len(rg) == 9

def nome_valido(nome):
    return not nome.isalpha()

def celular_valido(celular):
    """ Verifica se o celular é valido (84 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta