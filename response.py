from flask import Flask, request
import csv

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    
    number = request.form['From']
    message_body = request.form['Body']

    response_file = open("response.csv", "a", encoding="utf8")
    csv_writer = csv.writer(response_file,)

    csv_writer.writerow([number, message_body])
    return
    
if __name__ == '__main__':
    app.run()