from hotel import Hotel
from reservationTicket import ReservationTicket
import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})  # Ensure all data is read as strings
print(df)

# Create a hotel instance and check availability
hotel_ID = input("Enter a hotel: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not available for booking.")






