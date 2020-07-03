from mycroft import intent_file_handler, MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context
import requests

class ListagemRespostas(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)
		
	@intent_file_handler('respostas.listagem.intent')
	def handle_respostas_listagem(self, message):

		r = requests.get('http://localhost:3000/respostas')
		rn = r.json()
		
		for ri in rn:

			self.speak_dialog('proxima.listagem')
			self.speak_dialog('texto_alternativa.listagem', data=ri)
			self.speak_dialog('texto_resposta.listagem', data=ri)
			self.speak_dialog('contagem.listagem', data=ri)
		


def create_skill():
	return ListagemRespostas()

