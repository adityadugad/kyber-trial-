import os
from flask import Flask, jsonify
import oqs

# Make sure liboqs C library can be found
os.environ["LD_LIBRARY_PATH"] = "/usr/local/lib"
os.environ["OQS_INSTALL_PATH"] = "/usr/local"

app = Flask(__name__)

@app.route("/")
def home():
    return "OQS KEM test running!"

@app.route("/kem")
def kem_test():
    kem = oqs.KeyEncapsulation("Kyber512")
    public_key = kem.generate_keypair()
    ciphertext, secret_enc = kem.encap_secret(public_key)
    secret_dec = kem.decap_secret(ciphertext)

    return jsonify({
        "algorithm": "Kyber512",
        "match": secret_enc == secret_dec,
        "public_key_length": len(public_key),
        "ciphertext_length": len(ciphertext)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
