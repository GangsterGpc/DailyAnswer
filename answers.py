
def get_price_prediction_answer(card_id):
    answers = {
    "10112": "470000",
    "10113": "38000",
    "10116": "27000",
    "10114": "38000",
    "10115": "33000",
    "10119": "1132000",
    "10117": "300000",
    "10118": "38000",
    "10120": "37000",
    "10121": "12000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10102": "Xu Beihong",
    "10103": "Lin Fengmian",
    "10104": "Pierre-Auguste Renoir",
    "10107": "Fernand Leger",
    "10110": "Chen Yifei",
    "10106": "Kaws",
    "10111": "Yoshitomo Nara",
    "10108": "Li Keran",
    "10109": "Paul Signac",
    "10105": "Henry Moore"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10093": "$2.2 billion",
    "10098": "$276.5 million",
    "10099": "$2.1 billion",
    "10092": "$1.0 billion",
    "10096": "$517.7 million",
    "10094": "$796.4 million",
    "10097": "$1.8 billion",
    "10095": "$142.4 million",
    "10100": "$767.3 million",
    "10101": "$5.4 billion"
}
    return answers.get(str(card_id), None)
