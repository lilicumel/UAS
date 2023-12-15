# app.py
from flask import Flask, render_template, request
from affine_cipher import encrypt, decrypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_text():
    text = request.form['text']
    key_a = int(request.form['key_a'])
    key_b = int(request.form['key_b'])
    encrypted_text = encrypt(text, key_a, key_b)
    return render_template('index.html', text=text, key_a=key_a, key_b=key_b, result=encrypted_text, operation='Encrypt')

@app.route('/decrypt', methods=['POST'])
def decrypt_text():
    text = request.form['text']
    key_a = int(request.form['key_a'])
    key_b = int(request.form['key_b'])
    decrypted_text = decrypt(text, key_a, key_b)
    return render_template('index.html', text=text, key_a=key_a, key_b=key_b, result=decrypted_text, operation='Decrypt')

if __name__ == '__main__':
    app.run(debug=True)
