from mycroft import MycroftSkill, intent_file_handler


class ListagemRespostas(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('respostas.listagem.intent')
    def handle_respostas_listagem(self, message):
        self.speak_dialog('respostas.listagem')


def create_skill():
    return ListagemRespostas()

