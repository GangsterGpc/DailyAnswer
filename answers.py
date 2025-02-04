
def get_price_prediction_answer(card_id):
    answers = {
    "10364": "30000",
    "10363": "49000",
    "10366": "15000",
    "10365": "13000",
    "10367": "154000",
    "10370": "13000",
    "10369": "201000",
    "10368": "30000",
    "10371": "29000",
    "10362": "153000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10354": "Wayne Thiebaud",
    "10352": "Rudolf Stingel",
    "10357": "Lee Ufan",
    "10355": "Xu Beihong",
    "10353": "Qi Baishi",
    "10359": "Henry Moore",
    "10358": "Pu Ru",
    "10356": "Li Keran",
    "10360": "Huang Zhou",
    "10361": "Ren\u00e9 Magritte"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10342": "$107.7 million",
    "10343": "$815.6 million",
    "10344": "$1.0 billion",
    "10347": "$560.3 million",
    "10346": "$257.0 million",
    "10345": "$3.1 billion",
    "10351": "$510.8 million",
    "10349": "$205.6 million",
    "10348": "$2.4 billion",
    "10350": "$7.6 billion"
}
    return answers.get(str(card_id), None)
