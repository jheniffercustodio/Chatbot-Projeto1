# Importações de bibliotecas externas
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download

# Baixar o modelo de linguagem do spacy
download("en_core_web_sm")

# Definir a classe de idioma para o spacy
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

# Configurar o chatbot
chatbot = ChatBot("CartorioBot", tagger_language=ENGSM)

# Definir as conversas para treinar o chatbot
conversacoes = [
    "Oi", "Olá! Como posso ajudar você com os serviços de cartório hoje?",
    "Quais serviços o software oferece?", "Nosso software oferece serviços como registro de imóveis, emissão de certidões, autenticação de documentos, entre outros. Como posso ajudar especificamente?",
    "Como faço para registrar um imóvel?", "Para registrar um imóvel, você deve acessar o módulo de Registro de Imóveis, preencher os dados necessários e anexar os documentos requeridos. Precisa de mais alguma informação sobre o registro?",
    "Como posso emitir uma certidão de nascimento?", "Para emitir uma certidão de nascimento, vá até o módulo de Certidões, selecione 'Certidão de Nascimento' e preencha os dados necessários",
    "Como autenticar documentos?", "Para autenticar documentos, acesse o módulo de Autenticação, selecione o tipo de documento e siga as instruções para anexar e validar o documento.",
    "Posso emitir uma certidão online?", "Sim, você pode emitir certidões online através do nosso software. Acesse o módulo de Certidões e escolha o tipo de certidão que deseja emitir.",
    "Como faço para consultar um registro de imóveis?", "Para consultar um registro de imóveis, vá até o módulo de Consulta de Registros, insira os dados do imóvel ou do proprietário e visualize as informações disponíveis.",
    "Preciso de ajuda com a emissão de certidão de casamento.", "Para emitir uma certidão de casamento, acesse o módulo de Certidões, selecione 'Certidão de Casamento' e preencha os dados necessários dos cônjuges.",
    "Como posso atualizar os dados de um registro?", "Para atualizar os dados de um registro, vá até o módulo de Atualização de Registros, selecione o registro que deseja atualizar e edite as informações necessárias.",
    "Quais são os documentos necessários para registro de um imóvel?", "Os documentos necessários incluem a escritura do imóvel, a guia de IPTU, certidão negativa de débitos e documento de identidade do proprietário.",
    "Posso verificar a autenticidade de uma certidão?", "Sim, você pode verificar a autenticidade de uma certidão através do módulo de Verificação de Certidões, inserindo o código da certidão para validar sua autenticidade.",
    "O software permite emitir certidões em segunda via?", "Sim, nosso software permite a emissão de segundas vias de certidões. Acesse o módulo de Certidões e escolha a opção para emissão de segunda via.",
    "Como cancelar um registro de imóvel?", "Para cancelar um registro de imóvel, acesse o módulo de Cancelamento de Registros, selecione o registro que deseja cancelar e siga as instruções para confirmar o cancelamento.",
    "Quais são as taxas para serviços de cartório?", "As taxas variam conforme o serviço solicitado. Você pode consultar a tabela de taxas no menu 'Tarifas e Serviços'.",
    "Como agendar uma consulta no cartório?", "Para agendar uma consulta, acesse o módulo de Agendamento, escolha o serviço desejado e selecione a data e horário disponíveis.",
    "Como acessar o histórico de transações?", "Você pode acessar o histórico de transações no módulo 'Histórico de Transações', onde é possível visualizar todas as atividades realizadas.",
    "Preciso de ajuda com a retificação de um registro.", "Para retificar um registro, acesse o módulo de Retificação de Registros, selecione o registro que deseja corrigir e faça as alterações necessárias. Alguma outra dúvida?",
    "Preciso de ajuda com a atualização do software.", "Para atualizar o software, vá até o menu 'Configurações' e clique em 'Verificar atualizações'. Siga as instruções na tela para completar a atualização. Precisa de mais alguma informação?"
]

# Treinar o chatbot com as conversas definidas
trainer = ListTrainer(chatbot)
trainer.train(conversacoes)

# Função principal para iniciar o chat
def iniciar_chat():
    print("Olá! Meu nome é CartorioBot, o assistente virtual da ASCIV!")
    print("Digite sua pergunta ou digite 'sair' para encerrar.")
    while True:
        mensagem = input("> ")
        if mensagem.lower() == "sair":
            print("Tchau! Foi bom conversar com você.")
            break
        resposta = chatbot.get_response(mensagem)
        print(resposta)
        if not perguntar_satisfacao():
            break  # Sai do loop de chat e retorna ao menu principal
    return True  # Retorna ao menu principal

# Função para perguntar se a resposta foi satisfatória
def perguntar_satisfacao():
    respostas_sim = ["sim", "s", "claro", "com certeza", "positivo", "é claro", "sem dúvida", "afirmativo"]
    respostas_nao = ["não", "nao", "na", "n", "negativo"]
    while True:
        feedback = input("A resposta foi satisfatória? (sim/não): ").strip().lower()
        if feedback in respostas_sim:
            return mais_alguma_ajuda()
        elif feedback in respostas_nao:
            print("Sinto muito que a resposta não tenha atendido sua necessidade.")
            return mostrar_opcoes_suporte_ou_chamado()
        else:
            print("Opção inválida. Por favor, responda 'sim' ou 'não'.")

# Função para perguntar se precisa de mais alguma ajuda
def mais_alguma_ajuda():
    respostas_sim = ["sim", "s", "claro", "com certeza", "positivo", "é claro", "sem dúvida", "afirmativo"]
    respostas_nao = ["não", "nao", "na", "n", "negativo"]
    while True:
        escolha = input("Você precisa de mais alguma ajuda? (sim/não): ").strip().lower()
        if escolha in respostas_sim:
            print("Retornando ao menu principal...\n")
            return True  # Indica que o usuário deseja voltar ao menu principal
        elif escolha in respostas_nao:
            print("Agradecemos pelo seu contato. Até logo!")
            return False
        else:
            print("Opção inválida. Por favor, responda 'sim' ou 'não'.")

# Função para abrir um chamado de suporte
def abrir_chamado():
    print("Vamos abrir um chamado de suporte.")
    nome = input("Por favor, informe seu nome: ")
    email = input("Por favor, informe seu email: ")
    descricao = input("Por favor, descreva o problema que está enfrentando: ")
    # Simulação do armazenamento do chamado
    print(f"Obrigado, {nome}. Seu chamado foi aberto e enviaremos um e-mail de confirmação para {email} em breve.")
    print("Descrição do problema: " + descricao)

# Função para mostrar opções de suporte ou abrir chamado
def mostrar_opcoes_suporte_ou_chamado():
    print("\nVocê pode:")
    print("1. Voltar ao menu principal")
    print("2. Abrir um chamado de suporte")
    print("3. Encerrar o atendimento")
    while True:
        escolha = input("Escolha uma das opções informadas: ")
        if escolha == "1":
            return True  # Indica que o usuário deseja voltar ao menu principal
        elif escolha == "2":
            abrir_chamado()
            return False
        elif escolha == "3":
            print("Espero ter ajudado. Até logo!")
            return False
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Função para mostrar opções de suporte
def mostrar_opcoes_suporte():
    print("\nOpções de Suporte:")
    print("1. Instalação do software")
    print("2. Recuperação de senha")
    print("3. Atualização do software")
    print("4. Outras dúvidas")
    print("5. Abrir um chamado")
    print("6. Sair")

# Função principal do programa
def main():
    print("Bem-vindo ao suporte ao cliente da ASCIV!")
    while True:
        mostrar_opcoes_suporte()
        escolha = input("Escolha uma das opções informadas: ")
        if escolha == "1":
            print("Você escolheu: Instalação do software")
            print("Para instalar o software, baixe o instalador do nosso site e siga as instruções na tela.")
        elif escolha == "2":
            print("Você escolheu: Recuperação de senha")
            print("Para recuperar a senha, clique em 'Esqueci minha senha' na tela de login e siga as instruções. Um email será enviado com os passos para redefinir sua senha.")
        elif escolha == "3":
            print("Você escolheu: Atualização do software")
            print("Para atualizar o software, vá até o menu 'Configurações' e clique em 'Verificar atualizações'. Siga as instruções na tela para completar a atualização.")
        elif escolha == "4":
            print("Você escolheu: Outras dúvidas")
            if iniciar_chat():  # Verifica se o usuário deseja voltar ao menu principal
                continue  # Volta ao início do loop principal
            else:
                break  # Sai do loop principal se o usuário não desejar mais assistência
        elif escolha == "5":
            print("Você escolheu: Abrir um chamado")
            abrir_chamado()
            if not perguntar_satisfacao():
                break  # Sai do loop principal se o usuário não desejar mais assistência
        elif escolha == "6":
            print("Espero ter ajudado. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
        
        # Perguntar se a resposta foi satisfatória após a escolha
        if not perguntar_satisfacao():
            break  # Sai do loop principal se o usuário não desejar mais assistência

# Executar a função principal quando o script é executado diretamente
if __name__ == "__main__":
    main()
