from flask import Flask, request, send_file
import segno
import tempfile
import base64
import os

app = Flask(__name__)

@app.route('/')
def generate_qr_code():
    text = request.args.get('text')
    if text:
        try:        
            qr = segno.make(text)
            temp_file = tempfile.NamedTemporaryFile(delete_on_close=False)
            tmp = temp_file.name + ".png"
            qr.save(tmp, scale=20)
            temp_file.close()

            with open(tmp, 'rb') as file:
                qr_data = file.read()
                base64_encoded = base64.b64encode(qr_data).decode('utf-8')

            return f'data:image/png;base64,{base64_encoded}"', 200, {'Cache-Control': 'max-age=31536000'}
        except:
            return "An error occurred while generating the QR code.", 500
    else:
        return "Please provide a 'text' query parameter.", 400

if __name__ == '__main__':
    app.run()