# UPI QR Generator (Python) 💳

A small Python script that turns a UPI ID into a scannable payment QR code
and saves it as a PNG image.

## How it works
1. Run the script and enter your UPI ID
2. It builds a `upi://pay` payment link
3. It saves the QR as `phonepe_qr.png` and opens it

## Setup
```bash
pip install qrcode[pil]
python QR_generator.py
```

## Tech
- Python 3
- `qrcode` library (with Pillow for image output)
