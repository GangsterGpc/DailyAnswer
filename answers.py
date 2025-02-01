
def get_price_prediction_answer(card_id):
    answers = {
    "10213": "29000",
    "10212": "36000",
    "10214": "19000",
    "10220": "22000",
    "10216": "36000",
    "10215": "74000",
    "10218": "96000",
    "10219": "15000",
    "10217": "26000",
    "10221": "78000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10202": "Huang Binhong",
    "10203": "Andy Warhol",
    "10205": "Sam Francis",
    "10204": "Guan Liang",
    "10206": "Qi Baishi",
    "10207": "Sanyu",
    "10210": "Robert Combas",
    "10208": "Wu Guanzhong",
    "10209": "Lin Fengmian"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10196": "$3.1 billion",
    "10192": "$228.2 million",
    "10193": "$2.5 billion",
    "10194": "$705.6 million",
    "10197": "$205.6 million",
    "10195": "$603.8 million",
    "10201": "$7.6 billion",
    "10200": "$3.2 billion",
    "10198": "$427.2 million",
    "10199": "$108.6 million"
}
    return answers.get(str(card_id), None)
