
def get_price_prediction_answer(card_id):
    answers = {
    "10064": "200000",
    "10062": "46000",
    "10063": "30000",
    "10065": "74000",
    "10068": "1359000",
    "10066": "148000",
    "10067": "192000",
    "10069": "256000",
    "10070": "26000",
    "10071": "225000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10052": "Yves Klein",
    "10053": "Keith Haring",
    "10054": "Alexander Calder",
    "10055": "Henri Matisse",
    "10056": "Maurice de Vlaminck",
    "10057": "Robert Combas",
    "10058": "Auguste Rodin",
    "10059": "Zhang Daqian",
    "10061": "Paul Signac",
    "10060": "David Hockney"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10044": "$550.9 million",
    "10042": "$349.3 million",
    "10043": "$2.1 billion",
    "10045": "$3.6 billion",
    "10046": "$102.6 million",
    "10047": "$205.6 million",
    "10048": "$1.4 billion",
    "10049": "$1.8 billion",
    "10050": "$2.1 billion",
    "10051": "$13.0 billion"
}
    return answers.get(str(card_id), None)
