questions = [
    "What is your name?",
    "How old are you",
    "what is your favorite color?",
    "what is your favorite animal?",
    "what is your favorite food?"
]

responses = [
    "My name is AI_chatbot. Nice to meet you!",
    "I am AI_chatbot, so i don't age.",
    "My favorite color is Red",
    "My favorite animal is Lion",
    "My favorite food is Samosa"
]


def get_input():
    return input("What is your Question? :").lower()

def is_question(input_text):
    return input_text.endswith("?")

def contains_keyword(input_text,keyword):
    return keyword in input_text

def get_response(input_text):
    if is_question(input_text):
        for i in range(len(questions)):
            if contains_keyword(input_text,questions[i].lower()):
                return responses[i]
    return "I'm sorry, I didn't understand your Question!"

while True:
    user_input = get_input()

    if user_input == "exit":
        break

    responses = get_response(user_input)

    print(responses)

