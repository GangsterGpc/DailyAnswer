
def get_price_prediction_answer(card_id):
    answers = {
    "9213": "1058000",
    "9214": "108000",
    "9216": "11000",
    "9212": "141000",
    "9219": "44000",
    "9218": "72000",
    "9215": "11000",
    "9217": "13000",
    "9220": "18000",
    "9221": "379000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9206": "Qi Gong",
    "9202": "Qi Baishi",
    "9207": "Damien Hirst",
    "9203": "Pu Ru",
    "9204": "Li Keran",
    "9205": "Bernard Buffet",
    "9208": "Kaws",
    "9209": "Gerhard Richter",
    "9210": "Takashi Murakami",
    "9211": "Ed Ruscha"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9192": "$205.6 million",
    "9198": "$48.8 million",
    "9200": "$937.8 million",
    "9193": "$851.3 million",
    "9197": "$142.2 million",
    "9196": "$96.5 million",
    "9194": "$1.2 billion",
    "9195": "$900.5 million",
    "9199": "$545.1 million",
    "9201": "$170.2 million"
}
    return answers.get(str(card_id), None)
