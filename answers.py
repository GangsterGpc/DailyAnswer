
def get_price_prediction_answer(card_id):
    answers = {
    "10617": "142000",
    "10614": "309000",
    "10612": "85000",
    "10616": "25000",
    "10613": "32000",
    "10615": "15000",
    "10618": "22000",
    "10620": "36000",
    "10619": "30000",
    "10621": "28000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10602": "Auguste Rodin",
    "10603": "Alberto Giacometti",
    "10604": "Pablo Picasso",
    "10606": "Pu Ru",
    "10605": "Takashi Murakami",
    "10607": "Mark Tansey",
    "10608": "Guan Liang",
    "10609": "Salvador Dali",
    "10610": "Qi Baishi",
    "10611": "Lee Ufan"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10592": "$550.9 million",
    "10593": "$205.6 million",
    "10594": "$1.0 billion",
    "10595": "$767.3 million",
    "10596": "$3.1 billion",
    "10597": "$13.0 billion",
    "10598": "$330.8 million",
    "10601": "$252.8 million",
    "10599": "$1.2 billion",
    "10600": "$2.1 billion"
}
    return answers.get(str(card_id), None)
