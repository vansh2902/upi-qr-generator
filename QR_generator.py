import qrcode

upi_id = input("enter your upi ID = ")

upi_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
upi_qr = qrcode.make(upi_url)
upi_qr.save('phonepe_qr.png')
upi_qr.show()