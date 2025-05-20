from app.logica_sistema import cadastrar_aluno, listar_alunos, detalhar_aluno, deletar_aluno

comando = ""
#while funciona até que peça para sair
while comando != "sair":
    comando = input("Escolha uma opção: \n"
                    f"1) Cadastrar Aluno \n"
                    f"2) Listar Alunos \n"
                    f"3) Detalhar Matricula \n"
                    f"4) Deletar Aluno \n"
                    f"5) Cadastrar Curso \n"
                    f"6) Listar Cursos \n"
                    f"7) Detalhar Curso \n"
                    f"8) Deletar Curso \n"
                    f"9) Listar Alunos Aprovados \n"
                    f"10) Inserir um Aluno em Curso \n"
                    f"Digite 'sair' para sair do sistema \n")

    match comando:
        case "1":
            nome = input("Informe o nome do aluno:")
            nascimento = input("Informe a data de nascimento do aluno:")
            curso = input("Informe o curso do aluno se tiver, se não deixe vazio")

            print(cadastrar_aluno(nome,nascimento,curso))

        case "2":
            print(listar_alunos())

        case "3":
            matricula = input("Informe a matricula do aluno")

            print(detalhar_aluno(matricula))

        case "4":
            matricula = input("Informe a matricula do aluno")

            print(deletar_aluno(matricula))

        case "5":
            nome_curso = input("Informe o nome do curso: ")

            print(cadastrar_curso(nome_curso))

        case "6":
            print(listar_cursos())

        case "7":
            nome_curso = input("Informe o nome do curso: ")

            print(detalhar_curso(nome_curso))

        case "8":
            nome_curso = input("Informe o nome do curso: ")

            print(deletar_curso(nome_curso))

        case "9":
            nome_curso = input("Informe o nome do curso: ")

            print(listar_alunos_aprovados(nome_curso))

        case "10":
            matricula = input("Informe o nome do aluno: ")
            nome_curso = input("Informe o nome do curso: ")

            print(inserir_aluno_no_curso(matricula, nome_curso))

        case "sair":
            print("Saindo do sistema")