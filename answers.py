
def get_price_prediction_answer(card_id):
    answers = {
    "8813": "56000",
    "8815": "1299000",
    "8812": "47000",
    "8816": "14000",
    "8814": "18000",
    "8818": "30000",
    "8821": "26000",
    "8819": "31000",
    "8820": "18000",
    "8817": "59000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8802": "Pu Ru",
    "8804": "Chu Teh-Chun",
    "8803": "Qi Baishi",
    "8806": "Alex Katz",
    "8805": "Damien Hirst",
    "8807": "Jeff Koons",
    "8808": "Takashi Murakami",
    "8809": "David Hockney",
    "8811": "Ed Ruscha",
    "8810": "Fernando Botero"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8792": "$205.6 million",
    "8793": "$851.3 million",
    "8795": "$460.1 million",
    "8796": "$545.1 million",
    "8794": "$2.5 billion",
    "8797": "$256.9 million",
    "8801": "$1.6 billion",
    "8799": "$143.7 million",
    "8798": "$1.0 billion",
    "8800": "$202.1 million"
}
    return answers.get(str(card_id), None)
