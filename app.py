from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample crop data (you would replace this with real data)
crop_data = {
    "crop1": {
        "weather_preference": "Sunny",
        "soil_preference": "Loam",
        "water_requirement": "Moderate",
    },
    "crop2": {
        "weather_preference": "Rainy",
        "soil_preference": "Clay",
        "water_requirement": "High",
    },
    # Add more crop data here
}


@app.route("/recommend_crop", methods=["POST"])
def recommend_crop():
    try:
        data = request.get_json()

        # Simulated recommendation logic based on input data
        weather = data.get("weather")
        soil_quality = data.get("soil_quality")
        water_availability = data.get("water_availability")

        recommended_crops = []

        for crop, preferences in crop_data.items():
            if (
                weather == preferences["weather_preference"]
                and soil_quality == preferences["soil_preference"]
                and water_availability == preferences["water_requirement"]
            ):
                recommended_crops.append(crop)

        return jsonify({"recommended_crops": recommended_crops})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
