
def get_price_prediction_answer(card_id):
    answers = {
    "10162": "24000",
    "10163": "80000",
    "10164": "17000",
    "10165": "24000",
    "10168": "33000",
    "10166": "39000",
    "10167": "13000",
    "10169": "70000",
    "10171": "1580000",
    "10170": "40000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10153": "Lu Yanshao",
    "10152": "Pu Ru",
    "10155": "Li Keran",
    "10157": "Lin Fengmian",
    "10156": "Paul Gauguin",
    "10154": "Lee Ufan",
    "10158": "Maurice de Vlaminck",
    "10159": "Pablo Picasso",
    "10160": "Fernando Botero",
    "10161": "Chu Teh-Chun"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10151": "$205.6 million",
    "10142": "$107.7 million",
    "10143": "$2.5 billion",
    "10145": "$1.0 billion",
    "10144": "$257.0 million",
    "10147": "$13.0 billion",
    "10146": "$550.9 million",
    "10148": "$767.3 million",
    "10149": "$440.9 million",
    "10150": "$490.6 million"
}
    return answers.get(str(card_id), None)
