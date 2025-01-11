
def get_price_prediction_answer(card_id):
    answers = {
    "9162": "19000",
    "9164": "18000",
    "9166": "12000",
    "9168": "24000",
    "9163": "39000",
    "9165": "24000",
    "9170": "17000",
    "9167": "17000",
    "9169": "16000",
    "9171": "896000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9152": "Pu Ru",
    "9153": "Qi Baishi",
    "9155": "Jeff Koons",
    "9160": "Zeng Fanzhi",
    "9159": "Lee Ufan",
    "9154": "Damien Hirst",
    "9156": "Dana Schutz",
    "9157": "Gerhard Richter",
    "9158": "Antony Gormley",
    "9161": "George Condo"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9150": "$134.7 million",
    "9143": "$205.6 million",
    "9142": "$851.3 million",
    "9145": "$552.6 million",
    "9144": "$453.4 million",
    "9146": "$545.1 million",
    "9147": "$937.8 million",
    "9148": "$252.8 million",
    "9149": "$5.5 billion",
    "9151": "$822.6 million"
}
    return answers.get(str(card_id), None)
