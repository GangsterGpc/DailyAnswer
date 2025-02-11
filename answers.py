
def get_price_prediction_answer(card_id):
    answers = {
    "10762": "43000",
    "10766": "19000",
    "10763": "44000",
    "10764": "88000",
    "10765": "8416000",
    "10767": "22000",
    "10768": "20000",
    "10769": "1009000",
    "10770": "34000",
    "10771": "226000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10752": "Henri Matisse",
    "10754": "Xu Beihong",
    "10753": "Qi Baishi",
    "10761": "Wu Changshuo",
    "10755": "Pu Ru",
    "10756": "Robert Combas",
    "10757": "Sanyu",
    "10758": "Marc Chagall",
    "10759": "Andy Warhol",
    "10760": "G\u00fcnther F\u00f6rg"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10743": "$254.1 million",
    "10744": "$760.0 million",
    "10742": "$330.0 million",
    "10747": "$344.7 million",
    "10745": "$276.5 million",
    "10746": "$205.6 million",
    "10749": "$350.2 million",
    "10748": "$603.5 million",
    "10750": "$210.2 million",
    "10751": "$3.6 billion"
}
    return answers.get(str(card_id), None)
