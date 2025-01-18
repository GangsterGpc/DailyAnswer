
def get_price_prediction_answer(card_id):
    answers = {
    "9513": "29000",
    "9512": "28000",
    "9514": "538000",
    "9517": "120000",
    "9515": "33000",
    "9516": "92000",
    "9520": "342000",
    "9518": "166000",
    "9519": "12000",
    "9521": "61000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9511": "Huang Zhou",
    "9502": "Qi Gong",
    "9503": "Henri Matisse",
    "9504": "Lee Ufan",
    "9505": "Zhang Daqian",
    "9508": "Joan Mitchell",
    "9507": "Wassily Kandinsky",
    "9506": "David Hockney",
    "9510": "Sanyu",
    "9509": "Guan Liang"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9492": "$205.6 million",
    "9494": "$385.5 million",
    "9493": "$49.0 million",
    "9496": "$13.0 billion",
    "9495": "$545.1 million",
    "9497": "$107.7 million",
    "9498": "$1.0 billion",
    "9500": "$2.1 billion",
    "9499": "$350.2 million",
    "9501": "$2.4 billion"
}
    return answers.get(str(card_id), None)
