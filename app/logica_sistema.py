from models.aluno import Aluno
from models.curso import Curso

CURSOS = {}
ALUNOS = {}

#Se  a função esta fora de uma classe não precisa do self
def cadastrar_aluno(nome, nascimento, nome_curso=None):
    if not nome or not nascimento:
        return "Parametros inválidos"
    c = None
    aluno_objeto = Aluno(nome, nascimento)

    if nome_curso:
        c = CURSOS.get(nome_curso)
        c.alunos[aluno_objeto.matricula] = aluno_objeto

    ALUNOS[aluno_objeto.matricula] = aluno_objeto

    return {
        "nome_aluno": aluno_objeto.nome,
        "matricula": aluno_objeto.matricula,
        "curso": c.nome or None
    }

def listar_alunos():
    resposta = ""
    for aluno in ALUNOS.values():
        resposta += (f"Nome: {aluno.nome} \n"
                    f"Matricula: {aluno.matricula} \n"
                    f"Curso: {aluno.curso.nome if aluno.curso else "Sem curso no momento"} \n"
                    f"------------------------ \n")

    return resposta

def detalhar_aluno(matricula):
    if not matricula:
        return "Parametros Inválidos"

    aluno = ALUNOS.get(matricula)

    return (f"Nome: {aluno.nome} \n"
            f"Matricula: {aluno.matricula} \n"
            f"Data de nascimeto: {aluno.nascimento} \n"
            f"Data de ingresso: {aluno.ingresso} \n"
            f"Curso: {aluno.curso.nome if aluno.curso else "Sem curso no momento"} \n"
            f"Notas: {aluno.notas}")


def deletar_aluno(matricula):
    if not matricula:
        return "Paramentros Inválidos"

    aluno = ALUNOS.get(matricula)

    if not aluno:
        return "Este aluno não esta cadastrado"

    if aluno.curso:
        curso = CURSOS.get(aluno.curso.nome)
        curso.alunos.pop(matricula)

    ALUNOS.pop(matricula)

    return "Aluno excluido com  sucesso"


