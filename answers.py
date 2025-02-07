
def get_price_prediction_answer(card_id):
    answers = {
    "10512": "326000",
    "10514": "40000",
    "10513": "62000",
    "10515": "22000",
    "10516": "17000",
    "10517": "918000",
    "10519": "14000",
    "10520": "1115000",
    "10518": "57000",
    "10521": "37000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10503": "Andy Warhol",
    "10502": "Joan Mir\u00f3",
    "10505": "Pu Ru",
    "10504": "Gerhard Richter",
    "10508": "Xu Beihong",
    "10506": "Wu Changshuo",
    "10507": "Keith Haring",
    "10511": "Qi Baishi",
    "10509": "Lee Ufan",
    "10510": "Jean Dubuffet"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10492": "$1.0 billion",
    "10493": "$3.2 billion",
    "10494": "$550.9 million",
    "10495": "$2.4 billion",
    "10497": "$1.0 billion",
    "10496": "$257.0 million",
    "10498": "$13.0 billion",
    "10499": "$2.0 billion",
    "10500": "$472.5 million",
    "10501": "$1.8 billion"
}
    return answers.get(str(card_id), None)
