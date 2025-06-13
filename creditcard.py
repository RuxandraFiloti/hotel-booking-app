import pandas as pd

df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient='records') #convert to a list of dictionaries

class CreditCard:
    def __init__(self, number):
        self.number = number
    
    def validate(self, expiration_date, holder_name, cvc):
        card_data = {"number":self.number, 
                     "expiration_date": expiration_date, 
                     "holder_name": holder_name, 
                     "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False
