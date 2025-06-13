from creditcard import CreditCard
from hotel import Hotel
from reservationTicket import ReservationTicket
import pandas as pd
from secureCreditCard import SecureCreditCard
from spaHotel import SpaHotel
from spaTicket import SpaTicket

df = pd.read_csv("hotels.csv", dtype={"id": str})  # Ensure all data is read as strings
print(df)

# Create a hotel instance and check availability
hotel_ID = input("Enter a hotel: ")
#hotel = Hotel(hotel_ID)
hotel = SpaHotel(hotel_ID)  # Assuming SpaHotel inherits from Hotel

# check hotel availability
if hotel.available():
    credit_card = CreditCard(number=input("Enter your credit card number: "))

    #check validation of credit card
    if credit_card.validate(expiration_date=input("Enter expiration date (MM/YY): "),
                           holder_name=input("Enter cardholder name: "),
                           cvc=input("Enter CVC: ")):
        
        # Use SecureCreditCard for authentication
        if credit_card.authenticate(given_password=input("Enter your password: ")):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
            # Ask if the customer wants to book a spa package
            spa = input ("Do you want to book a spa package? (yes/no): ")
            if spa == "yes":
                hotel.book_spa_package()
                spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                print(spa_ticket.generate())
        else:
            print("Authentication failed. Invalid password.")
    else:
        print("Invalid credit card details. Booking cannot be completed.")
else:
    print("Hotel is not available for booking.")






