from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)

CORS(app)

# BREVO_API_KEY = "xsmtpsib-df0113930c4ca87d38c3ab80a82b20ef9766caf572be51336b3b2fece0e5f02c-tpD6M81WtIoJICtt"



@app.route("/")
def home():
    return "OTP API Running"


@app.route("/send-otp", methods=["POST"])
def send_otp():

    try:

        data = request.json

        email = data.get("email")
        otp = data.get("otp")

        payload = {

            "sender": {
                "name": "OTP Service",
                "email": "jsrnbank.nlass74@gmail.com"
            },

            "to": [
                {
                    "email": email
                }
            ],

            "subject": "Your OTP",

            "htmlContent":
                f"<h2>Your OTP is {otp}</h2>"
        }

        headers = {
            "accept": "application/json",
            "api-key":  "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",
            "content-type": "application/json"
        }

        response = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            json=payload,
            headers=headers
        )

        return jsonify({
            "status_code": response.status_code,
            "response": response.json()
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
