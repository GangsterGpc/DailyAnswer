
def get_price_prediction_answer(card_id):
    answers = {
    "9364": "205000",
    "9363": "125000",
    "9362": "512000",
    "9365": "43000",
    "9367": "370000",
    "9370": "34000",
    "9368": "29000",
    "9366": "41000",
    "9369": "800000",
    "9371": "13000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9352": "Chu Teh-Chun",
    "9355": "Kaws",
    "9353": "Zeng Fanzhi",
    "9354": "Pablo Picasso",
    "9359": "Lee Ufan",
    "9356": "Fernand Leger",
    "9360": "Pu Ru",
    "9357": "Andy Warhol",
    "9358": "Ernst Ludwig Kirchner",
    "9361": "Norman Rockwell"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9347": "$453.5 million",
    "9346": "$1.4 billion",
    "9345": "$759.7 million",
    "9348": "$1.2 billion",
    "9349": "$205.6 million",
    "9350": "$2.4 billion",
    "9351": "$1.2 billion",
    "9344": "$1.8 billion",
    "9342": "$3.1 billion",
    "9343": "$778.2 million"
}
    return answers.get(str(card_id), None)
