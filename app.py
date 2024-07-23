from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "ABW1"

if __name__ == '__main__':
  print("Inside the if")
  app.run(host='0.0.0.0',debug=True)
  