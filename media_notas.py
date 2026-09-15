#!/usr/bin/env python3
"""
Aplicação de linha de comando para calcular a média de notas
de provas dos alunos de uma faculdade.

Funcionalidades:
- Cadastrar alunos
- Lançar notas de provas para cada aluno
- Calcular a média individual de um aluno
- Calcular a média geral da turma
- Listar todos os alunos com suas médias
- Salvar/carregar dados em um arquivo JSON (persistência entre execuções)
"""

import json
import os
import sys

ARQUIVO_DADOS = "alunos.json"


def carregar_dados():
    """Carrega os dados dos alunos a partir do arquivo JSON, se existir."""
    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Aviso: não foi possível ler o arquivo de dados. Iniciando vazio.")
            return {}
    return {}


def salvar_dados(alunos):
    """Salva os dados dos alunos no arquivo JSON."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(alunos, f, ensure_ascii=False, indent=2)


def cadastrar_aluno(alunos):
    nome = input("Nome do aluno: ").strip()
    if not nome:
        print("Nome inválido.")
        return
    if nome in alunos:
        print(f"O aluno '{nome}' já está cadastrado.")
        return
    alunos[nome] = []
    salvar_dados(alunos)
    print(f"Aluno '{nome}' cadastrado com sucesso.")


def lancar_nota(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado ainda.")
        return

    nome = input("Nome do aluno: ").strip()
    if nome not in alunos:
        print(f"Aluno '{nome}' não encontrado.")
        return

    while True:
        entrada = input("Digite a nota (0 a 10): ").strip().replace(",", ".")
        try:
            nota = float(entrada)
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue

        if 0 <= nota <= 10:
            alunos[nome].append(nota)
            salvar_dados(alunos)
            print(f"Nota {nota:.2f} lançada para '{nome}'.")
            break
        else:
            print("A nota deve estar entre 0 e 10.")


def calcular_media(notas):
    """Retorna a média de uma lista de notas, ou None se não houver notas."""
    if not notas:
        return None
    return sum(notas) / len(notas)


def media_aluno(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado ainda.")
        return

    nome = input("Nome do aluno: ").strip()
    if nome not in alunos:
        print(f"Aluno '{nome}' não encontrado.")
        return

    notas = alunos[nome]
    media = calcular_media(notas)

    if media is None:
        print(f"'{nome}' ainda não possui notas lançadas.")
    else:
        situacao = "Aprovado" if media >= 6 else "Reprovado"
        print(f"\nAluno: {nome}")
        print(f"Notas: {', '.join(f'{n:.2f}' for n in notas)}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}\n")


def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado ainda.")
        return

    print("\n{:<25} {:<10} {:<12} {:<10}".format("Aluno", "Nº Notas", "Média", "Situação"))
    print("-" * 60)
    for nome, notas in alunos.items():
        media = calcular_media(notas)
        if media is None:
            media_str = "—"
            situacao = "—"
        else:
            media_str = f"{media:.2f}"
            situacao = "Aprovado" if media >= 6 else "Reprovado"
        print("{:<25} {:<10} {:<12} {:<10}".format(nome, len(notas), media_str, situacao))
    print()


def media_geral_turma(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado ainda.")
        return

    medias = [calcular_media(notas) for notas in alunos.values() if notas]
    if not medias:
        print("Nenhum aluno possui notas lançadas ainda.")
        return

    media_turma = sum(medias) / len(medias)
    print(f"\nMédia geral da turma (com base em {len(medias)} aluno(s) com notas): {media_turma:.2f}\n")


def remover_aluno(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado ainda.")
        return

    nome = input("Nome do aluno a remover: ").strip()
    if nome not in alunos:
        print(f"Aluno '{nome}' não encontrado.")
        return

    confirmacao = input(f"Tem certeza que deseja remover '{nome}'? (s/n): ").strip().lower()
    if confirmacao == "s":
        del alunos[nome]
        salvar_dados(alunos)
        print(f"Aluno '{nome}' removido.")
    else:
        print("Operação cancelada.")


def exibir_menu():
    print("=" * 45)
    print(" SISTEMA DE MÉDIA DE NOTAS - FACULDADE")
    print("=" * 45)
    print("1. Cadastrar aluno")
    print("2. Lançar nota de prova")
    print("3. Calcular média de um aluno")
    print("4. Listar todos os alunos")
    print("5. Calcular média geral da turma")
    print("6. Remover aluno")
    print("0. Sair")
    print("=" * 45)


def main():
    alunos = carregar_dados()

    opcoes = {
        "1": cadastrar_aluno,
        "2": lancar_nota,
        "3": media_aluno,
        "4": listar_alunos,
        "5": media_geral_turma,
        "6": remover_aluno,
    }

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "0":
            print("Encerrando o sistema. Até logo!")
            sys.exit(0)

        funcao = opcoes.get(escolha)
        if funcao:
            print()
            funcao(alunos)
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário.")
        sys.exit(0)
