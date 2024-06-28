from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import plotly.express as px

app = Flask(__name__)

# Load model
model = joblib.load("models/model.joblib")

# Load dataset for dropdown options
df = pd.read_csv("data/bengaluru_prices_preprocessed-100.csv")

# Load actual and predicted prices for display
results_df = pd.read_csv("data/results.csv")


@app.route("/")
def index():
    area_types = df["Area_type"].unique()
    locations = df["Location"].unique()
    return render_template("index.html", area_types=area_types, locations=locations)


@app.route("/predict", methods=["POST"])
def predict():
    area_type = request.form["area_type"]
    location = request.form["location"]
    total_sqft = float(request.form["total_sqft"])
    bathroom = int(request.form["bathroom"])
    balcony = int(request.form["balcony"])
    size = int(request.form["size"].split(" ")[0])

    # Prepare input data for prediction
    input_data = pd.DataFrame(
        [[area_type, location, total_sqft, bathroom, balcony, size]],
        columns=["Area_type", "Location", "Total_sqft", "Bathroom", "Balcony", "Size"],
    )

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Calculate sum of prices by area type
    sum_price_by_area = df.groupby("Area_type")["Price in lakhs"].sum().reset_index()

    # Sort by the sum of prices to ensure correct ordering in the chart
    sum_price_by_area = sum_price_by_area.sort_values(
        by="Price in lakhs", ascending=False
    )

    # Filter for selected area type
    selected_area_price = sum_price_by_area[
        sum_price_by_area["Area_type"] == area_type
    ]["Price in lakhs"].values[0]

    # Create the chart
    fig = px.bar(
        sum_price_by_area,
        x="Area_type",
        y="Price in lakhs",
        title="Sum of Prices by Area Type",
    )

    # Hide y-axis labels
    fig.update_yaxes(showticklabels=False)

    # Convert the plotly figure to JSON
    graph_json = fig.to_json()

    # Get top 10 actual and predicted prices for display along with Total_sqft
    top_results = results_df.head(10)

    return jsonify(
        {
            "prediction": prediction,
            "selected_area_price": selected_area_price,
            "sum_price_by_area": sum_price_by_area.to_dict(orient="records"),
            "graph": graph_json,
            "results": top_results.to_dict(orient="records"),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
