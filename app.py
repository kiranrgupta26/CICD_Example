from flask import Flask

from shopping_cart import ShoppingCart

app = Flask(__name__)

@app.route('/')
def hello_world():
    cart = ShoppingCart()
    result = cart.get_hello_world()
    return result

if __name__=='__main__':
    app.run(debug=True)




