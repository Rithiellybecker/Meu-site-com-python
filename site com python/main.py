from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Esse e meu 1° site"

@app.route("/contatos")
def contatos():
    return "<p>nossos contatos são:</p> <p>Email: rithiellybecker7@gmail.com</p> <p>Telefone: 45 999070796.</p> <P>Linkedin: link</p>"

if __name__ == "__main__":
    app.run(debug=True)