class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name #self.customer_name is for calling the customer name in another method
        self.hotel_object = hotel_object

    def generate(self):   
        content = f"""
        Thank you for your reservation.
        Here are your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel_object.name}
"""
        return content