
def get_price_prediction_answer(card_id):
    answers = {
    "10313": "10000",
    "10317": "31000",
    "10318": "11000",
    "10315": "35000",
    "10314": "666000",
    "10319": "116000",
    "10321": "48000",
    "10316": "53000",
    "10320": "189000",
    "10312": "446000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10303": "Pierre Soulages",
    "10305": "Pablo Picasso",
    "10304": "Georges Braque",
    "10302": "Qi Baishi",
    "10306": "Andy Warhol",
    "10310": "Zhang Daqian",
    "10309": "Sanyu",
    "10311": "Wu Hufan",
    "10307": "Pu Ru",
    "10308": "Zao Wou-Ki"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10292": "$13.0 billion",
    "10293": "$205.6 million",
    "10295": "$893.7 million",
    "10294": "$550.9 million",
    "10301": "$603.8 million",
    "10297": "$562.2 million",
    "10296": "$767.3 million",
    "10298": "$229.6 million",
    "10299": "$1.0 billion",
    "10300": "$1.2 billion"
}
    return answers.get(str(card_id), None)
