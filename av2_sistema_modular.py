# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2sistemamodular.py
# Nome do Aluno: Ane Rafaelle
# Data:18/09/2026
# TEMA: Biblioteca Comunitária - Sistema de Cadastro de Leitores
# ==============================================================================

dados_brutos = [
    "  Anilca Pereira;estudante;11988887777  ",
    "  Sophia de Jesus;professor;21977776666  ",
    "  Ana Lyvia;comunidade;31966665555  ",
    "  Luiz Miguel;pesquisador;4795554444  "
]


def limpar_e_formatar_texto(texto):
    
    texto_limpo = texto.strip()
    texto_formatado = texto_limpo.upper()
    return texto_formatado


def extrair_codigo_ou_ddd(dado):
    
    dado_limpo = dado.strip()
    ddd = dado_limpo[0:2]
    return ddd


def gerar_matricula(nome_completo, posicao):
   
    partes_do_nome = nome_completo.strip().lower().split()

    primeiro_nome = partes_do_nome[0]
    ultimo_sobrenome = partes_do_nome[-1]

    sigla = primeiro_nome[0:3] + ultimo_sobrenome[0:3]

    return f"BIB-{sigla.upper()}-{posicao:03d}"


def processar_e_exibir_cadastros(lista_dados):
   
    total = 0

    for cadastro in lista_dados:
        partes = cadastro.split(";")

        nome = limpar_e_formatar_texto(partes[0])
        categoria = limpar_e_formatar_texto(partes[1])
        telefone = partes[2].strip()

        ddd = extrair_codigo_ou_ddd(telefone)
        matricula = gerar_matricula(partes[0], total + 1)

        print(f"Matrícula: {matricula}")
        print(f"Leitor: {nome}")
        print(f"Categoria: {categoria}")
        print(f"DDD: ({ddd})")
        print(f"Telefone: {telefone}")
        print("-" * 50)

        total = total + 1

    return total


def main():
    print("==================================================")
    print("   BIBLIOTECA COMUNITÁRIA - CADASTRO DE LEITORES  ")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    total_processado = processar_e_exibir_cadastros(dados_brutos)

    print(f"\nTotal de leitores cadastrados: {total_processado} registro(s).")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO              ")
    print("==================================================")


if __name__ == "__main__":
    main()
