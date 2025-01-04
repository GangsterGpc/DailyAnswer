
def get_price_prediction_answer(card_id):
    answers = {
    "8870": "107000",
    "8871": "28000",
    "8866": "40000",
    "8862": "198000",
    "8863": "77000",
    "8865": "12000",
    "8864": "17000",
    "8869": "109000",
    "8867": "86000",
    "8868": "669000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8852": "Pu Ru",
    "8855": "Damien Hirst",
    "8856": "Alex Katz",
    "8860": "Yoshitomo Nara",
    "8854": "Norman Rockwell",
    "8853": "Qi Baishi",
    "8857": "Jeff Koons",
    "8858": "Kaws",
    "8859": "Cecily Brown",
    "8861": "Zhou Chunya"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8843": "$205.6 million",
    "8847": "$256.9 million",
    "8842": "$851.3 million",
    "8844": "$460.1 million",
    "8845": "$1.2 billion",
    "8846": "$545.1 million",
    "8848": "$1.0 billion",
    "8849": "$202.1 million",
    "8850": "$180.1 million",
    "8851": "$2.1 billion"
}
    return answers.get(str(card_id), None)
