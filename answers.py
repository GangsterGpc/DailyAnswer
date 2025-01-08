
def get_price_prediction_answer(card_id):
    answers = {
    "9066": "13000",
    "9063": "33000",
    "9062": "46000",
    "9067": "438000",
    "9065": "21000",
    "9064": "13000",
    "9071": "12000",
    "9069": "567000",
    "9068": "19000",
    "9070": "30000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9052": "Pu Ru",
    "9053": "Qi Baishi",
    "9059": "George Condo",
    "9055": "Alex Katz",
    "9058": "Anish Kapoor",
    "9054": "Damien Hirst",
    "9061": "Jeff Koons",
    "9056": "Peter Doig",
    "9057": "Kaws",
    "9060": "Gerhard Richter"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9044": "$460.1 million",
    "9042": "$851.3 million",
    "9043": "$205.6 million",
    "9045": "$545.1 million",
    "9046": "$252.8 million",
    "9047": "$2.1 billion",
    "9049": "$254.1 million",
    "9051": "$603.8 million",
    "9048": "$203.8 million",
    "9050": "$505.2 million"
}
    return answers.get(str(card_id), None)
