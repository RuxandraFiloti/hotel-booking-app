class SpaTicket():
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object
    def generate(self):
        content = f"""
    Thank you for you SPA reservation!
    Here are your spa booking details:
    Name: {self.customer_name}
    Hotel: {self.hotel_object.name}
    """
        return content