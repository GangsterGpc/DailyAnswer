
def get_price_prediction_answer(card_id):
    answers = {
    "9613": "70000",
    "9615": "15000",
    "9612": "23000",
    "9614": "45000",
    "9616": "17000",
    "9617": "23000",
    "9621": "132000",
    "9618": "22000",
    "9619": "68000",
    "9620": "14000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9603": "Fernand Leger",
    "9604": "Kaws",
    "9602": "Pablo Picasso",
    "9605": "Francois-Xavier Lalanne",
    "9610": "Qi Baishi",
    "9607": "Liu Ye",
    "9608": "Edgar Degas",
    "9609": "Alex Katz",
    "9606": "Andy Warhol",
    "9611": "Sam Francis"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9596": "$1.8 billion",
    "9593": "$453.5 million",
    "9594": "$13.0 billion",
    "9592": "$517.9 million",
    "9595": "$256.9 million",
    "9601": "$330.8 million",
    "9598": "$1.3 billion",
    "9599": "$550.9 million",
    "9597": "$3.2 billion",
    "9600": "$7.8 billion"
}
    return answers.get(str(card_id), None)
