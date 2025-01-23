
def get_price_prediction_answer(card_id):
    answers = {
    "9813": "46000",
    "9812": "17000",
    "9815": "59000",
    "9817": "33000",
    "9814": "38000",
    "9818": "15000",
    "9821": "24000",
    "9819": "352000",
    "9816": "31000",
    "9820": "146000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9802": "Andy Warhol",
    "9803": "Qi Baishi",
    "9807": "Paul Gauguin",
    "9804": "Zhang Daqian",
    "9805": "Edgar Degas",
    "9806": "Georges Braque",
    "9808": "Zeng Fanzhi",
    "9809": "Paul Signac",
    "9811": "Maurice de Vlaminck",
    "9810": "Sanyu"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9792": "$621.0 million",
    "9795": "$1.8 billion",
    "9793": "$276.5 million",
    "9794": "$2.1 billion",
    "9796": "$1.0 billion",
    "9797": "$205.6 million",
    "9800": "$760.0 million",
    "9798": "$257.0 million",
    "9799": "$5.3 billion",
    "9801": "$505.2 million"
}
    return answers.get(str(card_id), None)
