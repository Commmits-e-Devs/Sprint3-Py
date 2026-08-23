funcionalidades = {
    "Detecção de Contexto": "A câmera analisa o que está na tela e identifica se é uma lousa/texto, "
    "uma pessoa ou uma paisagem.",
    "Calibração Automática": "Ajusta sozinha parâmetros como ISO, nitidez e iluminação de acordo com o contexto "
    "(por exemplo, força o contraste se for texto ou suaviza a luz se for um retrato).",
    "Filtro de Legibilidade (Lousa)": "Trata a imagem do quadro para remover reflexos e sombras, "
    "destacando o texto escrito para garantir leitura fácil.",
    "Categorização Automática no Disparo": "No momento da captura, a câmera aplica uma etiqueta na foto "
    "para enviá-la direto para a pasta certa (como Estudos, Lazer ou Pessoas).",
    "Captura Rápida (<1s)": "Executa o ajuste de imagem e o salvamento em segundo plano sem travar a navegação do usuário."
}

galeria = {
    "Estudos": [],
    "Lazer": [],
    "Pessoas": []
}

def mostrar_menu():
    print("""
---------------MENU DE FUNCIONALIDADES---------------
    1 - Detecção de contexto
    2 - Calibração automática
    3 - Filtro de Legibilidade
    4 - Categorização automática no Disparo
    5 - Captura rápida (<1s)
    6 - Visualizar galeria
    0 - Sair
    """)

def detectar_contexto(funcionalidades):
    print(funcionalidades["Detecção de Contexto"])
    print("""
    1 - Lousa/Texto
    2 - Paisagem
    3 - Retrato
    4 - Selfie
        """)
    try:
        opc_contexto = int(input("Informe o contexto atual para foto: "))
    except ValueError:
        print("Digite apenas números.")
        return None

    if opc_contexto == 1:
        contexto =  "Lousa/Texto"
    elif opc_contexto == 2:
        contexto = "Paisagem"
    elif opc_contexto == 3:
        contexto = "Retrato"
    elif opc_contexto == 4:
        contexto = "Selfie"
    else:
        print("Contexto inválido")
        return None
    return contexto

def calibracao_automatica(funcionalidades, contexto):
    print(funcionalidades["Calibração Automática"])
    if contexto == "Lousa/Texto":
        print("""
        -----AJUSTES PADRÕES-----
        Calibração aplicada: Lousa/Texto
        ISO: 200
        Nitidez: Alta
        Contraste: Alto
        Iluminação: Ajustada para destacar o texto
        """)
    elif contexto == "Paisagem":
        print("""
        -----AJUSTES PADRÕES-----
        Calibração aplicada: Paisagem
        ISO: 100
        Nitidez: Alta
        Contraste: Médio
        Iluminação: Natural
        """)
    elif contexto == "Retrato" or contexto == "Selfie":
        print("""
        -----AJUSTES PADRÕES-----
        Calibração aplicada: Retrato/Selfie
        ISO: 200
        Nitidez: Média
        Contraste: Suave
        Iluminação: Suavizada para o rosto
        """)

def filtro_legibilidade(funcionalidades, contexto):
    print(funcionalidades["Filtro de Legibilidade (Lousa)"])
    if contexto == "Lousa/Texto":
        print("""
        -----AJUSTES PADRÕES-----
        Filtro aplicado: Lousa
        Reflexos removidos
        Sombras reduzidas
        Contraste aumentado
        Texto destacado
        """)
    else:
        print("Filtro de Legibilidade apenas para lousas/textos.")

def categorizacao_automatica(funcionalidades, contexto, galeria):
    print(funcionalidades["Categorização Automática no Disparo"])
    nome_foto = input("Informe o nome da foto: ").strip()
    while nome_foto == "":
        print("O nome da foto não pode estar vazio.")
        nome_foto = input("Informe o nome da foto: ").strip()
    if contexto == "Lousa/Texto":
        categoria = "Estudos"
        galeria[categoria].append(nome_foto)
        print(f"Foto salva automaticamente na categoria: {categoria}")

    elif contexto == "Paisagem":
        categoria = "Lazer"
        galeria[categoria].append(nome_foto)
        print(f"Foto salva automaticamente na categoria: {categoria}")

    elif contexto == "Retrato" or contexto == "Selfie":
        categoria = "Pessoas"
        galeria[categoria].append(nome_foto)
        print(f"Foto salva automaticamente na categoria: {categoria}")

def captura_rapida(funcionalidades, galeria):
    print(funcionalidades["Captura Rápida (<1s)"])
    contexto = detectar_contexto(funcionalidades)

    if contexto is not None:
        calibracao_automatica(funcionalidades, contexto)
        if contexto == "Lousa/Texto":
            filtro_legibilidade(funcionalidades, contexto)
        categorizacao_automatica(funcionalidades, contexto, galeria)
        print("Captura realizada e salva com sucesso em menos de 1 segundo.")

def visualizar_galeria(galeria):
    print("\n-----GALERIA-----")

    for categoria, fotos in galeria.items():
        print(f"\n{categoria}:")

        if len(fotos) == 0:
            print("Nenhuma foto.")

        else:
            for foto in fotos:
                print(f"- {foto}")

def executar_sistema(funcionalidades, galeria):
    opc = -1
    contexto = None
    while opc != 0:
        mostrar_menu()

        try:
            opc = int(input("Escolha uma opção: "))
            if opc == 1:
                contexto = detectar_contexto(funcionalidades)

            elif opc == 2:
                if contexto is not None:
                    calibracao_automatica(funcionalidades, contexto)
                else:
                    print("Primeiro realize a detecção de contexto.")

            elif opc == 3:
                if contexto is not None:
                    filtro_legibilidade(funcionalidades, contexto)
                else:
                    print("Primeiro realize a detecção de contexto.")

            elif opc == 4:
                if contexto is not None:
                    categorizacao_automatica(funcionalidades, contexto, galeria)
                else:
                    print("Primeiro realize a detecção de contexto.")

            elif opc == 5:
                captura_rapida(funcionalidades, galeria)

            elif opc == 6:
                visualizar_galeria(galeria)

            elif opc == 0:
                print("Encerrando o sistema...")
            else:
                print("Opção inválida...\nTente novamente.")

        except ValueError:
            print("Digite apenas números.")

executar_sistema(funcionalidades, galeria)