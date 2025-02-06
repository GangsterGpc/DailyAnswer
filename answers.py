
def get_price_prediction_answer(card_id):
    answers = {
    "10464": "48000",
    "10467": "23000",
    "10466": "178000",
    "10469": "31000",
    "10471": "107000",
    "10470": "27000",
    "10462": "44000",
    "10463": "34000",
    "10465": "263000",
    "10468": "27000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10452": "Zhang Daqian",
    "10457": "Alexander Calder",
    "10453": "Pablo Picasso",
    "10454": "Takashi Murakami",
    "10455": "Sanyu",
    "10456": "George Condo",
    "10459": "Li Keran",
    "10461": "Wu Changshuo",
    "10458": "Henry Moore",
    "10460": "Pu Ru"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10442": "$3.2 billion",
    "10443": "$205.6 million",
    "10445": "$427.2 million",
    "10444": "$900.0 million",
    "10446": "$1.8 billion",
    "10447": "$1.0 billion",
    "10448": "$3.6 billion",
    "10449": "$893.7 million",
    "10450": "$330.8 million",
    "10451": "$13.0 billion"
}
    return answers.get(str(card_id), None)
