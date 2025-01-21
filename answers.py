
def get_price_prediction_answer(card_id):
    answers = {
    "9713": "24000",
    "9714": "229000",
    "9712": "12000",
    "9716": "264000",
    "9715": "90000",
    "9718": "127000",
    "9719": "48000",
    "9717": "13000",
    "9720": "489000",
    "9721": "63000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9702": "Pablo Picasso",
    "9703": "Kaws",
    "9705": "Maurice de Vlaminck",
    "9704": "Pierre Soulages",
    "9708": "Paul Gauguin",
    "9706": "Norman Rockwell",
    "9707": "Kim WhanKi",
    "9709": "Damien Hirst",
    "9710": "Giorgio Morandi",
    "9711": "Tom Wesselmann"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9696": "$474.3 million",
    "9692": "$796.4 million",
    "9693": "$350.2 million",
    "9694": "$460.1 million",
    "9695": "$13.0 billion",
    "9697": "$257.0 million",
    "9698": "$2.1 billion",
    "9701": "$167.8 million",
    "9699": "$2.5 billion",
    "9700": "$385.5 million"
}
    return answers.get(str(card_id), None)
