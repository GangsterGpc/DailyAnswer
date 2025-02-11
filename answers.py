
def get_price_prediction_answer(card_id):
    answers = {
    "10713": "92000",
    "10712": "128000",
    "10716": "17000",
    "10714": "30000",
    "10715": "2854000",
    "10717": "641000",
    "10718": "464000",
    "10719": "23000",
    "10720": "28000",
    "10721": "27000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "10702": "Yoshitomo Nara",
    "10704": "Sanyu",
    "10705": "Robert Motherwell",
    "10703": "Lin Fengmian",
    "10706": "Maurice de Vlaminck",
    "10709": "Pablo Picasso",
    "10707": "Paul Gauguin",
    "10710": "Robert Combas",
    "10708": "Andy Warhol",
    "10711": "Pu Ru"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "10692": "$13.0 billion",
    "10693": "$550.9 million",
    "10694": "$2.5 billion",
    "10695": "$603.5 million",
    "10696": "$1.8 billion",
    "10697": "$760.0 million",
    "10701": "$108.6 million",
    "10698": "$3.6 billion",
    "10699": "$1.3 billion",
    "10700": "$567.8 million"
}
    return answers.get(str(card_id), None)
