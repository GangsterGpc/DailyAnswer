
def get_price_prediction_answer(card_id):
    answers = {
    "9014": "18000",
    "9018": "10333000",
    "9012": "67000",
    "9015": "54000",
    "9017": "64000",
    "9013": "26000",
    "9016": "14000",
    "9021": "18000",
    "9019": "16000",
    "9020": "62000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9002": "Pu Ru",
    "9009": "Tomoo Gokita",
    "9008": "Zhou Chunya",
    "9011": "David Hockney",
    "9004": "Damien Hirst",
    "9003": "Qi Baishi",
    "9005": "Alex Katz",
    "9006": "Gerhard Richter",
    "9010": "Kaws",
    "9007": "Julie Mehretu"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "8992": "$851.3 million",
    "8999": "$5.5 billion",
    "8993": "$205.6 million",
    "8994": "$460.1 million",
    "8995": "$545.1 million",
    "8997": "$203.8 million",
    "8998": "$937.8 million",
    "8996": "$252.8 million",
    "9000": "$254.1 million",
    "9001": "$822.6 million"
}
    return answers.get(str(card_id), None)
