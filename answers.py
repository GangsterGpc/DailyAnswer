
def get_price_prediction_answer(card_id):
    answers = {
    "9663": "582000",
    "9662": "131000",
    "9665": "106000",
    "9667": "85000",
    "9664": "39000",
    "9666": "28000",
    "9669": "17000",
    "9668": "24000",
    "9671": "64000",
    "9670": "31000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9653": "Qi Baishi",
    "9652": "Zhang Daqian",
    "9655": "Qi Gong",
    "9654": "Auguste Rodin",
    "9656": "Huang Binhong",
    "9657": "Wu Changshuo",
    "9658": "Georges Braque",
    "9659": "Andy Warhol",
    "9660": "Wu Hufan",
    "9661": "Pierre-Auguste Renoir"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9642": "$1.0 billion",
    "9646": "$1.8 billion",
    "9643": "$330.8 million",
    "9644": "$7.8 billion",
    "9645": "$2.1 billion",
    "9649": "$2.4 billion",
    "9648": "$1.4 billion",
    "9647": "$336.0 million",
    "9650": "$440.9 million",
    "9651": "$257.0 million"
}
    return answers.get(str(card_id), None)