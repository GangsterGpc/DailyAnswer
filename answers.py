
def get_price_prediction_answer(card_id):
    answers = {
    "10964": "1158000",
    "10962": "13000",
    "10963": "41000",
    "10965": "63000",
    "10967": "32000",
    "10966": "3539000",
    "10968": "19000",
    "10969": "13000",
    "10970": "18000",
    "10971": "16000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10953": "Sanyu",
    "10959": "Chu Teh-Chun",
    "10954": "Xu Beihong",
    "10952": "Huang Binhong",
    "10955": "Zhang Daqian",
    "10956": "Lee Ufan",
    "10960": "Qi Baishi",
    "10957": "Pu Ru",
    "10958": "Marc Chagall",
    "10961": "Auguste Rodin"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10942": "$1.0 billion",
    "10949": "$3.1 billion",
    "10943": "$767.3 million",
    "10946": "$7.6 billion",
    "10944": "$664.3 million",
    "10945": "$205.6 million",
    "10948": "$257.0 million",
    "10947": "$1.8 billion",
    "10950": "$453.5 million",
    "10951": "$3.2 billion"
}
    return answers.get(str(card_id), None)
