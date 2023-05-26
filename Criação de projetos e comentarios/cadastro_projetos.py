from dataclasses import dataclass, asdict
import json

@dataclass
class Projeto:
    nome: str
    curso: str
    resumo: str
    comentario: str

def cadastra_projeto():
    nome = input("Qual o nome do seu projeto?: ")
    curso = input("O seu projeto é de que curso?: ")
    resumo = input("Descreva seu projeto brevemente: ")
    conf = input("Quer comentar sobre o projeto?: ") .lower()
    if conf == "sim" :
        comentario = input("Comentario: ")
        return Projeto(nome, curso, resumo,comentario)
    else:
        comentario = None
        return Projeto(nome, curso, resumo,comentario)
             

        



projeto_obj = [
    cadastra_projeto()
]


with open('banco_projetos.json', 'w') as arquivo:
        projeto_dict = list(map(asdict, projeto_obj))
        projeto_json = json.dumps(projeto_dict, indent=4)
        arquivo.write(projeto_json)

def criar_projeto(d):
    return Projeto(**d)
    
projeto_json = json.dumps(projeto_dict,sort_keys=True)
