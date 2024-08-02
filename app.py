from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pyqrcode
import io
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json
    url = data.get('url')
    title = data.get('title')

    qr = pyqrcode.create(url)
    buffer = io.BytesIO()
    qr.png(buffer, scale=6)
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='qr_code.png')

if __name__ == '__main__':
    from waitress import serve
    port = int(os.environ.get("PORT", 5000))
    serve(app, host='0.0.0.0', port=port)
