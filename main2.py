import pandas as pd
from abc import ABC, abstractmethod #abstract base class

df = pd.read_csv("hotels.csv", dtype={"id":str}) #dtype to ensure all data is read as strings

class Hotel:
    watermark = "The Real Estate Company" # class variable
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """"Book the hotel by changing its availability to no."""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """"Check if the hotel is available for booking."""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
        
    #class method 
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)
    
    #magcic method
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False
    
    #if i had price, I could do an adding
    # def __add__(self, other):
    #     total = self.price + other.price
    #     return total

#abstract class
class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass

class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object): 
        self.customer_name = customer_name #self.customer_name is for calling the customer name in another method
        self.hotel_object = hotel_object

    def generate(self): #self is like no input parameter for this method
        content = f"""
        Thank you for your reservation.
        Here are your booking data:
        Name: {self.the_customer_name}
        Hotel: {self.hotel_object.name}
"""
        return content
    
    #property
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name
    
    #static method
    @staticmethod
    def convert(amount):
        return amount * 1.2 #converts euro to usd

class DigitalTicket(Ticket):
    def generate(self):
        content = f"""
        Digital Ticket:
        Name: {self.the_customer_name}
        Hotel: {self.hotel_object.name}
"""
        return content
    
    def download(self):
        pass

# hotel1 = Hotel(hotel_id="188")
# hotel2 = Hotel(hotel_id="134")

# print(hotel1.name) #instance variable
# print(hotel2.name)

# print(hotel1.available()) #instance method

# print(hotel1.watermark) # class variable
# print(hotel2.watermark)

# print(Hotel.watermark) # class variable accessed through class name
# #print(Hotel.name) #error: 'type' object has no attribute 'name'

# print(Hotel.get_hotel_count(data=df)) # class method

# #calling property
# ticket = ReservationTicket(customer_name="john smith", hotel_object=hotel1)
# print(ticket.the_customer_name) # property method; it doesn't require parentheses
# print(ticket.generate()) # no arguments because of the 'self' 

# #calling static method
# converted = ReservationTicket.convert(100)
# print(converted)