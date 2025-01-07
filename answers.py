
def get_price_prediction_answer(card_id):
    answers = {
    "8962": "17000",
    "8967": "19000",
    "8963": "483000",
    "8964": "18000",
    "8965": "113000",
    "8969": "3355000",
    "8966": "45000",
    "8968": "20000",
    "8970": "34000",
    "8971": "14000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8959": "Gerhard Richter",
    "8952": "Qi Baishi",
    "8954": "Lucio Fontana",
    "8953": "Pu Ru",
    "8960": "Ed Ruscha",
    "8955": "Damien Hirst",
    "8956": "Alex Katz",
    "8957": "Kaws",
    "8958": "Jeff Koons",
    "8961": "Jonas Wood"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8945": "$545.1 million",
    "8949": "$203.8 million",
    "8947": "$937.8 million",
    "8943": "$851.3 million",
    "8950": "$453.4 million",
    "8942": "$205.6 million",
    "8946": "$252.8 million",
    "8948": "$254.1 million",
    "8944": "$460.1 million",
    "8951": "$822.6 million"
}
    return answers.get(str(card_id), None)