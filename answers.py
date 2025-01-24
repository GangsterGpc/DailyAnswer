
def get_price_prediction_answer(card_id):
    answers = {
    "9862": "28000",
    "9864": "36000",
    "9863": "51000",
    "9865": "33000",
    "9866": "13000",
    "9867": "319000",
    "9869": "23000",
    "9868": "34000",
    "9870": "66000",
    "9871": "246000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9852": "Pu Ru",
    "9853": "Sanyu",
    "9854": "Brice Marden",
    "9858": "Huang Binhong",
    "9855": "Banksy",
    "9857": "Lin Fengmian",
    "9856": "Roy Lichtenstein",
    "9859": "Pablo Picasso",
    "9860": "Qi Baishi",
    "9861": "Lee Ufan"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9842": "$1.4 billion",
    "9843": "$3.4 billion",
    "9845": "$550.9 million",
    "9844": "$603.8 million",
    "9846": "$3.1 billion",
    "9847": "$336.0 million",
    "9848": "$330.8 million",
    "9849": "$2.1 billion",
    "9850": "$1.2 billion",
    "9851": "$205.6 million"
}
    return answers.get(str(card_id), None)
