from creditcard import CreditCard
import pandas as pd


df_secure_cards = pd.read_csv("card_security.csv", dtype=str)

class SecureCreditCard(CreditCard): # Inherit from CreditCard class
    
    def authenticate(self, given_password):
        password = df_secure_cards.loc[df_secure_cards["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False

