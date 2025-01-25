
def get_price_prediction_answer(card_id):
    answers = {
    "9913": "2529000",
    "9912": "43000",
    "9914": "82000",
    "9918": "40000",
    "9915": "11000",
    "9916": "22000",
    "9917": "28000",
    "9920": "16000",
    "9921": "29000",
    "9919": "24000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9903": "Guan Liang",
    "9902": "Qi Gong",
    "9904": "Ernst Ludwig Kirchner",
    "9905": "Pablo Picasso",
    "9906": "David Hockney",
    "9911": "Qi Baishi",
    "9907": "Paul Gauguin",
    "9910": "Xu Beihong",
    "9908": "Balthus",
    "9909": "Louise Bourgeois"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9893": "$550.9 million",
    "9897": "$840.9 million",
    "9892": "$2.1 billion",
    "9894": "$3.1 billion",
    "9895": "$603.8 million",
    "9899": "$205.6 million",
    "9896": "$108.6 million",
    "9898": "$257.0 million",
    "9900": "$3.4 billion",
    "9901": "$203.8 million"
}
    return answers.get(str(card_id), None)
