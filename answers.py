
def get_price_prediction_answer(card_id):
    answers = {
    "9270": "1309000",
    "9271": "34000",
    "9269": "15000",
    "9262": "35000",
    "9264": "15000",
    "9267": "11000",
    "9263": "21000",
    "9265": "23000",
    "9268": "1865000",
    "9266": "39000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9253": "Qi Baishi",
    "9257": "Jeff Koons",
    "9252": "Pu Ru",
    "9254": "Damien Hirst",
    "9255": "Kaws",
    "9256": "Cecily Brown",
    "9258": "Gerhard Richter",
    "9259": "Alex Katz",
    "9260": "Wayne Thiebaud",
    "9261": "Jonas Wood"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9245": "$545.1 million",
    "9244": "$1.2 billion",
    "9248": "$252.8 million",
    "9249": "$254.1 million",
    "9251": "$2.5 billion",
    "9242": "$205.6 million",
    "9243": "$851.3 million",
    "9246": "$5.5 billion",
    "9250": "$937.8 million",
    "9247": "$203.8 million"
}
    return answers.get(str(card_id), None)
