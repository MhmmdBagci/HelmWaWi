from ShoppingCart.shoppingCart import shoppingCart

class user():
    def __init__(self, email, name, password, adresse, tel):
        self.shoppingCart = shoppingCart()
        self.email = email
        self.name = name
        self.password = password
        self.adresse = adresse
        self.tel = tel
