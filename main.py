import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from src.pythonREPL import execute_python, install_package
import src.services as services

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').strip()
    isPythonCode = False
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg.startswith('#!python3'):
        code = incoming_msg.lstrip('#!python3')
        output = execute_python(code)
        msg.body(output)
        isPythonCode = True

    elif incoming_msg.startswith('!pip install'):
        package = incoming_msg.split()[-1]
        output = install_package(package)
        msg.body(output)
        isPythonCode = True

    if isPythonCode:
        return str(resp)

    incoming_msg = incoming_msg.lower()

    if 'your name' in incoming_msg:
        output = "I am alfred, alfred at you service"

    if 'who are you' in incoming_msg:
        output = "I am alfred, alfred at you service"

    elif 'hey' in incoming_msg:
        output = "hello sir! alfred at you service"

    elif 'heya' in incoming_msg:
        output = "hello sir! alfred at you service"

    elif 'hello' in incoming_msg:
        output = "hello sir! alfred at you service"

    elif 'hi' in incoming_msg:
        output = "hello sir! alfred at you service"

    elif 'hola' in incoming_msg:
        output = "hello sir! alfred at you service"

    elif 'help' in incoming_msg:
        output = "How may i help you sir ? Please eleborate.🙂"

    elif 'bye' in incoming_msg:
        output = "Goodbye Sir !! Have a nice day.🙂"

    elif 'date' in incoming_msg:
        output = services.get_date()

    elif 'today' in incoming_msg:
        output = services.get_day()

    elif 'day' in incoming_msg:
        output = services.get_day()

    elif 'time' in incoming_msg:
        output = services.get_time()

    elif 'joke' in incoming_msg:
        output = services.get_joke()

    elif 'quote' in incoming_msg:
        output = services.get_quote()

    else:
        api_key = services.fetch_apikey('wolfram-alpha')

        if api_key == None:
            output = 'Wolfram alpha api key needed, check docs'
        else:
            output = services.chatbot(api_key, incoming_msg)

    msg.body(output)
    return str(resp)


if __name__ == '__main__':
    app.run()
