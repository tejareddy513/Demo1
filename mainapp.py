# falsk is a frame work like tool create the path 
from flask import Flask
# This is used to route the  shop the routes
from routes.shop_routes import shop_routes
# Flask to create instance objects
app = Flask(__name__)

app.register_blueprint(shop_routes)

if __name__ == "__main__":
    app.run(debug=True)
