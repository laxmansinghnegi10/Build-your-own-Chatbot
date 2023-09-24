import random

responses = {
    "hello": ["Hello!", "Hi there!", "Hey!", "Hi! How can I assist you?"],
    "bye": ["Goodbye!", "See you later!", "Bye now!", "Have a great day!"],
    "howare": ["I'm good, thanks!", "I'm doing well, how about you?", "Feeling great!"],
    "name": ["You can call me TVC bot.", "I go by TVC bot.", "I'm TVC bot, nice to meet you!"],
    "menu": ["We have a variety of apples available.", "Our menu features a selection of apples."],
    "hours": ["We are open from 7am to 4pm, Monday to Friday."],
    "default": ["I'm not sure how to respond to that.", "Can you please rephrase that?", "I'm still learning!"]
}

def get_response(user_input):
    user_input = user_input.lower()

    for key, value in responses.items():
        if user_input in key:
            return random.choice(value)

    return random.choice(responses["default"])

print("*******************************************************\n")

while True:
    user_input = input('User said - ')
    
    if user_input.lower() == 'exit':
        print("Bot said - Goodbye!")
        break

    response = get_response(user_input)
    print(f'Bot said - {response}\n')
