
def get_price_prediction_answer(card_id):
    answers = {
    "10562": "26000",
    "10563": "59000",
    "10565": "190000",
    "10564": "23000",
    "10567": "93000",
    "10566": "85000",
    "10568": "74000",
    "10569": "43000",
    "10570": "92000",
    "10571": "29000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10553": "Pablo Picasso",
    "10552": "Qi Gong",
    "10554": "Qi Baishi",
    "10555": "Camille Pissarro",
    "10559": "Marc Chagall",
    "10557": "Lee Ufan",
    "10556": "Lin Fengmian",
    "10558": "Alex Katz",
    "10560": "Paul Signac",
    "10561": "Andy Warhol"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10542": "$1.0 billion",
    "10543": "$1.8 billion",
    "10545": "$738.4 million",
    "10544": "$108.6 million",
    "10548": "$257.0 million",
    "10549": "$350.2 million",
    "10546": "$2.1 billion",
    "10550": "$3.2 billion",
    "10547": "$700.4 million",
    "10551": "$2.0 billion"
}
    return answers.get(str(card_id), None)
