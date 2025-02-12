
def get_price_prediction_answer(card_id):
    answers = {
    "10812": "14000",
    "10814": "28000",
    "10815": "23000",
    "10813": "27000",
    "10816": "148000",
    "10817": "47000",
    "10818": "14000",
    "10819": "61000",
    "10820": "12000",
    "10821": "203000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10806": "Henri Matisse",
    "10802": "Edgar Degas",
    "10804": "Maurice de Vlaminck",
    "10805": "Yves Klein",
    "10803": "Paul Signac",
    "10808": "Wu Guanzhong",
    "10810": "Zhang Daqian",
    "10807": "Pablo Picasso",
    "10809": "Pu Ru",
    "10811": "Yoshitomo Nara"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10792": "$749.1 million",
    "10794": "$1.2 billion",
    "10793": "$49.0 million",
    "10795": "$1.0 billion",
    "10798": "$2.4 billion",
    "10799": "$3.2 billion",
    "10796": "$108.6 million",
    "10800": "$7.6 billion",
    "10801": "$460.1 million",
    "10797": "$230.3 million"
}
    return answers.get(str(card_id), None)
