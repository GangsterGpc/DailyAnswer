
def get_price_prediction_answer(card_id):
    answers = {
    "9563": "31000",
    "9568": "50000",
    "9562": "28000",
    "9565": "23000",
    "9564": "177000",
    "9566": "45000",
    "9567": "63000",
    "9569": "151000",
    "9571": "332000",
    "9570": "266000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9557": "Henry Moore",
    "9553": "Guan Liang",
    "9554": "Camille Pissarro",
    "9552": "Edgar Degas",
    "9555": "Yoshitomo Nara",
    "9556": "Sean Scully",
    "9561": "Zhang Daqian",
    "9558": "Pierre-Auguste Renoir",
    "9559": "Yves Klein",
    "9560": "Banksy"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9542": "$3.2 billion",
    "9543": "$5.3 billion",
    "9544": "$203.8 million",
    "9545": "$276.5 million",
    "9546": "$561.8 million",
    "9548": "$2.7 billion",
    "9549": "$1.3 billion",
    "9551": "$1.8 billion",
    "9547": "$851.3 million",
    "9550": "$3.1 billion"
}
    return answers.get(str(card_id), None)
