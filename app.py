from flask import Flask, request
import qrcode

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    qr_image = None

    if request.method == "POST":
        upi_id = request.form["upi_id"]

        upi_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

        upi_qr = qrcode.make(upi_url)

        upi_qr.save("static/upi_qr.png")

        qr_image = "/static/upi_qr.png"

    return f"""
        <h1>UPI QR Code Generator</h1>

        <form method="POST">
            <input type="text" name="upi_id" placeholder="Enter UPI ID">
            <button type="submit">Generate QR</button>
        </form>

        {"<img src='" + qr_image + "' width='300'>" if qr_image else ""}
    """


app.run(debug=True)