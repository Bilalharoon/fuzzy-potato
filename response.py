from flask import Flask, request
import csv
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    
    number = request.form['From']
    message_body = request.form['Body']

    resp = MessagingResponse()

    resp.message("Thank you for your message. Inshallah we will get back to you shortly")

    response_file = open("Data/response.csv", "a", encoding="utf8")
    csv_writer = csv.writer(response_file,)

    csv_writer.writerow([number, message_body])
    return str(resp)
    
if __name__ == '__main__':
    app.run()