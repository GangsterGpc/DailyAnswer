
def get_price_prediction_answer(card_id):
    answers = {
    "9764": "16000",
    "9762": "59000",
    "9769": "11000",
    "9763": "23000",
    "9765": "104000",
    "9766": "24000",
    "9767": "29000",
    "9768": "362000",
    "9770": "109000",
    "9771": "85000"
}
    return answers.get(str(card_id), None)

def get_who_is_the_artist_answer(card_id):
    answers = {
    "9758": "Pierre-Auguste Renoir",
    "9752": "Fernando Botero",
    "9754": "Lee Ufan",
    "9757": "Maurice de Vlaminck",
    "9753": "Guan Liang",
    "9759": "Banksy",
    "9755": "Salvador Dali",
    "9760": "Andy Warhol",
    "9761": "Edgar Degas",
    "9756": "Bernard Buffet"
}
    return answers.get(str(card_id), None)

def get_artist_market_value_answer(card_id):
    answers = {
    "9743": "$2.5 billion",
    "9747": "$725.3 million",
    "9742": "$13.0 billion",
    "9744": "$840.9 million",
    "9745": "$453.5 million",
    "9746": "$134.7 million",
    "9751": "$205.6 million",
    "9748": "$7.6 billion",
    "9749": "$49.0 million",
    "9750": "$1.0 billion"
}
    return answers.get(str(card_id), None)
