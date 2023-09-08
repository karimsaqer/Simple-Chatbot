import json
from difflib import get_close_matches

#load questions and answers from json file
def load_data(filepath: str)-> dict:
    with open(filepath, 'r') as file:
        data: dict = json.load(file)
    return data

# save questions and answers to json file
def save_data(data: dict, filepath: str):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=2)

# find best match for user input in questions list
def find_best_match(user_input: str, questions: list[str]) -> str or None:
    print('Hello')
    best_match = get_close_matches(user_input, questions, n=1, cutoff=0.8)
    return best_match[0] if best_match else None
    
# get answer for the question
def get_answer(question: str, data: dict) -> str or None:
    for q in data["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None
    
# Chat Bot
def chatbot():
    # load data
    data: dict = load_data('questions.json')

    # chat bot
    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'exit':
            break
        
        else:
            # find best match for user input in questions list
            best_match: str = find_best_match(user_input,[q["question"] for q in data["questions"]])
            
            if best_match:
                # get answer for the question
                answer: str = get_answer(best_match, data)
                print('Bot:', answer)
            else:
                print('Bot: Sorry, I do not understand. Please teach me.')
                new_answer: str = input('Type your answer or type "skip" to skip: ')
                if new_answer.lower() != 'skip':
                    data["questions"].append({"question": user_input, "answer": new_answer})
                    save_data(data, 'questions.json')
                    print('Bot: Thanks for teaching me.')


if __name__ == '__main__':
    chatbot()