
def get_price_prediction_answer(card_id):
    answers = {
    "9312": "42000",
    "9313": "52000",
    "9314": "10000",
    "9315": "35000",
    "9316": "39000",
    "9317": "331000",
    "9318": "23000",
    "9319": "2560000",
    "9320": "434000",
    "9321": "117000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9302": "Alberto Giacometti",
    "9303": "Sanyu",
    "9304": "Roy Lichtenstein",
    "9305": "Salvador Dali",
    "9306": "Edgar Degas",
    "9307": "Chu Teh-Chun",
    "9308": "Marc Chagall",
    "9309": "Qi Baishi",
    "9310": "Qi Gong",
    "9311": "Amedeo Modigliani"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9292": "$1.8 billion",
    "9293": "$851.3 million",
    "9294": "$49.0 million",
    "9295": "$2.1 billion",
    "9296": "$659.8 million",
    "9297": "$249.4 million",
    "9298": "$152.9 million",
    "9299": "$344.7 million",
    "9300": "$7.8 billion",
    "9301": "$2.4 billion"
}
    return answers.get(str(card_id), None)
