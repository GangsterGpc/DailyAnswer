
def get_price_prediction_answer(card_id):
    answers = {
    "9121": "34000",
    "9112": "60000",
    "9115": "48000",
    "9113": "100000",
    "9114": "13000",
    "9117": "11000",
    "9116": "26000",
    "9119": "23000",
    "9118": "14000",
    "9120": "12000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9102": "Qi Baishi",
    "9103": "Lin Fengmian",
    "9105": "Damien Hirst",
    "9104": "Pu Ru",
    "9106": "Alex Katz",
    "9107": "Takashi Murakami",
    "9108": "Gerhard Richter",
    "9110": "Richard Prince",
    "9109": "Jeff Koons",
    "9111": "Kaws"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9092": "$851.3 million",
    "9093": "$205.6 million",
    "9094": "$552.6 million",
    "9095": "$460.1 million",
    "9096": "$96.5 million",
    "9097": "$545.1 million",
    "9099": "$254.1 million",
    "9098": "$252.8 million",
    "9100": "$177.3 million",
    "9101": "$937.8 million"
}
    return answers.get(str(card_id), None)
