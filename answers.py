
def get_price_prediction_answer(card_id):
    answers = {
    "10668": "30000",
    "10669": "33000",
    "10667": "5631000",
    "10663": "13000",
    "10666": "31000",
    "10671": "414000",
    "10662": "16000",
    "10664": "86000",
    "10665": "24000",
    "10670": "16000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10652": "Andy Warhol",
    "10653": "Lin Fengmian",
    "10656": "Georges Braque",
    "10655": "Sanyu",
    "10654": "Robert Combas",
    "10657": "Marc Chagall",
    "10658": "Fernando Botero",
    "10659": "Guan Liang",
    "10660": "Wu Changshuo",
    "10661": "Albert Oehlen"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10642": "$3.6 billion",
    "10646": "$205.6 million",
    "10643": "$550.9 million",
    "10645": "$1.5 billion",
    "10648": "$738.4 million",
    "10644": "$644.9 million",
    "10647": "$108.6 million",
    "10649": "$257.0 million",
    "10650": "$1.8 billion",
    "10651": "$1.0 billion"
}
    return answers.get(str(card_id), None)
