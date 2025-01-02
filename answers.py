
def get_price_prediction_answer(card_id):
    answers = {
    "8762": "86000",
    "8763": "169000",
    "8765": "12000",
    "8766": "18000",
    "8768": "66000",
    "8764": "16000",
    "8767": "4154000",
    "8770": "16000",
    "8769": "11000",
    "8771": "36000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8752": "Pu Ru",
    "8760": "Dana Schutz",
    "8753": "Qi Baishi",
    "8754": "Damien Hirst",
    "8757": "George Condo",
    "8755": "Alex Katz",
    "8758": "Jeff Koons",
    "8756": "David Hockney",
    "8759": "Andy Warhol",
    "8761": "Jonas Wood"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8743": "$205.6 million",
    "8742": "$851.3 million",
    "8744": "$460.1 million",
    "8748": "$202.1 million",
    "8749": "$1.0 billion",
    "8745": "$545.1 million",
    "8746": "$256.9 million",
    "8747": "$505.2 million",
    "8750": "$134.7 million",
    "8751": "$1.6 billion"
}
    return answers.get(str(card_id), None)
