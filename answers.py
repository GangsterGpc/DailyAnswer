
def get_price_prediction_answer(card_id):
    answers = {
    "10013": "29000",
    "10015": "176000",
    "10012": "49000",
    "10016": "370000",
    "10014": "371000",
    "10017": "112000",
    "10021": "538000",
    "10019": "1999000",
    "10020": "15000",
    "10018": "125000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10002": "Yoshitomo Nara",
    "10007": "Francis Picabia",
    "10006": "Salvador Dali",
    "10003": "Ren\u00e9 Magritte",
    "10005": "Marc Chagall",
    "10004": "Pablo Picasso",
    "10009": "Andy Warhol",
    "10008": "Kim WhanKi",
    "10010": "David Hockney",
    "10011": "Qi Baishi"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9992": "$2.5 billion",
    "9993": "$1.3 billion",
    "9994": "$13.0 billion",
    "9995": "$2.5 billion",
    "9996": "$2.1 billion",
    "9998": "$1.4 billion",
    "9997": "$709.5 million",
    "10001": "$350.2 million",
    "9999": "$510.8 million",
    "10000": "$218.8 million"
}
    return answers.get(str(card_id), None)
