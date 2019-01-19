import chatterbot
from chatterbot.trainers import ListTrainer
MyBot=chatterbot.ChatBot("Rebirthing")
conversation = [
"Hello",
"Hi there!",
"How are you doing?",
"What's good about this morning!!!",
"That is good to hear",
"Thank you.",
"You're welcome."
]
MyBot.set_trainer(ListTrainer)
MyBot.train(conversation)
response = MyBot.get_response("Hello!!!")
print(response)
