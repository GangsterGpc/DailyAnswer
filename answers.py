
def get_price_prediction_answer(card_id):
    answers = {
    "8712": "22000",
    "8714": "16000",
    "8713": "150000",
    "8720": "168000",
    "8717": "36000",
    "8715": "38000",
    "8716": "14000",
    "8718": "48000",
    "8721": "41000",
    "8719": "292000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8702": "Qi Baishi",
    "8704": "Damien Hirst",
    "8703": "Pu Ru",
    "8709": "Ed Ruscha",
    "8707": "Jeff Koons",
    "8708": "Kaws",
    "8710": "Andy Warhol",
    "8705": "Alex Katz",
    "8706": "David Hockney",
    "8711": "Antony Gormley"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8697": "$1.0 billion",
    "8694": "$453.4 million",
    "8695": "$460.1 million",
    "8692": "$205.6 million",
    "8696": "$545.1 million",
    "8693": "$851.3 million",
    "8699": "$202.1 million",
    "8698": "$603.8 million",
    "8701": "$2.1 billion",
    "8700": "$344.7 million"
}
    return answers.get(str(card_id), None)
