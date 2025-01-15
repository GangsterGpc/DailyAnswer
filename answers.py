
def get_price_prediction_answer(card_id):
    answers = {
    "9412": "57000",
    "9413": "23000",
    "9414": "141000",
    "9418": "29000",
    "9415": "311000",
    "9417": "261000",
    "9420": "257000",
    "9416": "190000",
    "9421": "91000",
    "9419": "31000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9403": "Donald Judd",
    "9407": "Pablo Picasso",
    "9402": "Lucio Fontana",
    "9404": "Marc Chagall",
    "9409": "Yayoi Kusama",
    "9405": "Ren\u00e9 Magritte",
    "9406": "Wu Guanzhong",
    "9410": "Paul Gauguin",
    "9408": "Lee Ufan",
    "9411": "Joan Mitchell"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9392": "$1.8 billion",
    "9393": "$460.1 million",
    "9394": "$140.9 million",
    "9396": "$205.6 million",
    "9395": "$851.3 million",
    "9397": "$49.0 million",
    "9398": "$1.2 billion",
    "9399": "$350.2 million",
    "9400": "$1.2 billion",
    "9401": "$550.9 million"
}
    return answers.get(str(card_id), None)
