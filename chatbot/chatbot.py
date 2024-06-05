from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Main class
chatbot = ChatBot('First ChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train('chatterbot.corpus.english')

# Use loop to continue conversation
while True:
	user_input = input('Toi: ')

	# To stop the conversation
	if user_input.lower() == 'au rivoir':
		break
	# Get a response to an input statement
	response = chatbot.get_response(user_input)

	print('Moi:', response)