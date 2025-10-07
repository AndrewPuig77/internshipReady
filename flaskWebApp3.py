from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("starbucks_drinkMenu_expanded.csv")
#print(df.head)
#
@app.route("/")
def index():
    return jsonify({
        "routes":{
            "/drinks": "First 10 rows of all drinks",
            "/drinks/types": "List of all unique drink types",
            "/drinks/sizes": "List of all unique drink sizes",
            "/drinks/prices": "First 10 rows showing drink names and prices" 

        }
    })

@app.route("/cars")
def cars():
    return jsonify(df.head(10).to_dict('records'))

@app.route("/car/bodies")
def car_bodies():
    return jsonify(df["carbody"].unique().tolist())

@app.route("/car/prices")
def car_prices():
    return jsonify(df[["carname", "price"]].head(10).to_dict(orient ='records'))


if __name__ == "__main__":
    app.run(debug=True, port=5050)