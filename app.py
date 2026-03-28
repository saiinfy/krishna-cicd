from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>DAST Integrated Scanning</p>"

if __name__ == '__main__':
    # Run the app on a specific port, for example, 8000
    app.run(debug=True, host= "0.0.0.0",port=8000)

