from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Main class
chatbot = ChatBot('First ChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
print(chatbot.get_response("hi"))
