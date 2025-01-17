
def get_price_prediction_answer(card_id):
    answers = {
    "9468": "30000",
    "9470": "11000",
    "9462": "2600000",
    "9464": "48000",
    "9463": "6669000",
    "9465": "286000",
    "9471": "13000",
    "9467": "34000",
    "9469": "17000",
    "9466": "46000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9457": "Pierre Bonnard",
    "9458": "Qi Gong",
    "9453": "Yoshitomo Nara",
    "9459": "Zhou Chunya",
    "9461": "Huang Zhou",
    "9452": "Lin Fengmian",
    "9460": "Pu Ru",
    "9454": "Jean-Michel Basquiat",
    "9455": "Pablo Picasso",
    "9456": "Alexander Calder"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9451": "$1.2 billion",
    "9450": "$759.7 million",
    "9443": "$851.3 million",
    "9444": "$220.4 million",
    "9447": "$505.2 million",
    "9445": "$36.2 million",
    "9446": "$796.4 million",
    "9448": "$3.2 billion",
    "9442": "$205.6 million",
    "9449": "$840.9 million"
}
    return answers.get(str(card_id), None)
