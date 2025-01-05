
def get_price_prediction_answer(card_id):
    answers = {
    "8912": "258000",
    "8914": "20000",
    "8913": "87000",
    "8915": "13000",
    "8916": "19000",
    "8917": "19000",
    "8918": "10000",
    "8919": "949000",
    "8920": "15000",
    "8921": "415000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "8904": "Yves Klein",
    "8903": "Pu Ru",
    "8902": "Qi Baishi",
    "8905": "Damien Hirst",
    "8906": "Alex Katz",
    "8908": "Gerhard Richter",
    "8907": "Jeff Koons",
    "8909": "Takashi Murakami",
    "8910": "Salvador Dali",
    "8911": "Yayoi Kusama"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8896": "$256.9 million",
    "8894": "$460.1 million",
    "8892": "$205.6 million",
    "8893": "$851.3 million",
    "8895": "$545.1 million",
    "8898": "$202.1 million",
    "8897": "$1.0 billion",
    "8899": "$5.4 billion",
    "8900": "$453.4 million",
    "8901": "$134.7 million"
}
    return answers.get(str(card_id), None)
