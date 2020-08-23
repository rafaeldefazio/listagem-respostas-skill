from mycroft import intent_file_handler, MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context
import requests

class ListagemRespostas(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)
		
	@intent_file_handler('respostas.listagem.intent')
	def handle_respostas_listagem(self, message):

		ipAPI = 'http://177.21.53.138:3000'


		payload = {'user':'publico','password':'123'}
		getToken = requests.post(ipAPI + "/login", data=payload)


		myToken = getToken.content;
		headers = {'x-access-token': myToken}


		r = requests.get(ipAPI + '/respostas', headers=headers)

		self.speak(r.status_code);


		if r.status_code != 200:
			self.speak('Ocorreu algum problema ao me conectar ao servidor de dados. Por favor, verifique as credenciais e tente novamente.')

		else:
			rn = r.json()

			for ri in rn:

				self.speak_dialog('proxima.listagem')
				self.speak_dialog('texto_alternativa.listagem', data=ri)
				self.speak_dialog('texto_resposta.listagem', data=ri)
				self.speak_dialog('contagem.listagem', data=ri)
		


def create_skill():
	return ListagemRespostas()

