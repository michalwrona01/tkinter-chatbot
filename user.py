import random


def send_welcome():
    welcomes_list = []
    with open("bot_welcome.txt", "r", encoding="UTF-8") as file:
        for line in file:
            welcomes_list.append(line.strip())
        return "• User: " + random.choice(welcomes_list)


def send_answer():
    answer_list = []
    with open("bot_answers.txt", "r", encoding="UTF-8") as file:
        for line in file:
            answer_list.append(line.strip())
        return "• User: " + random.choice(answer_list)


def send_question():
    question_list = []
    with open("bot_questions.txt", "r", encoding="UTF-8") as file:
        for line in file:
            question_list.append(line.strip())
        return "• User: " + random.choice(question_list)


def send_good_bay():
    good_bay_list = []
    with open("bot_good_bay.txt", "r", encoding="UTF-8") as file:
        for line in file:
            good_bay_list.append(line.strip())
        return "• User: " + random.choice(good_bay_list)
