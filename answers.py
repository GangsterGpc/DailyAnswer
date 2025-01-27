
def get_price_prediction_answer(card_id):
    answers = {
    "9962": "108000",
    "9965": "74000",
    "9967": "19000",
    "9964": "132000",
    "9963": "13000",
    "9968": "60000",
    "9966": "21000",
    "9971": "25000",
    "9970": "533000",
    "9969": "11000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9953": "Henry Moore",
    "9952": "Pablo Picasso",
    "9958": "Zhang Daqian",
    "9954": "Antony Gormley",
    "9955": "Andy Warhol",
    "9956": "Ren\u00e9 Magritte",
    "9960": "Lee Ufan",
    "9961": "Georg Baselitz",
    "9957": "Robert Rauschenberg",
    "9959": "Alex Katz"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9944": "$760.0 million",
    "9947": "$366.3 million",
    "9946": "$550.9 million",
    "9943": "$640.4 million",
    "9945": "$1.1 billion",
    "9942": "$8.0 billion",
    "9948": "$108.6 million",
    "9950": "$257.0 million",
    "9949": "$49.0 million",
    "9951": "$1.0 billion"
}
    return answers.get(str(card_id), None)
