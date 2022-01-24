'''
This script will create a Flask application listening for commands from your custom Alexa Skill you created in your Amazon account.

Important Notes:

    1. This script is only HALF of what is required to make this work, you must also create a custom Alexa Skill in 
       your Amazon account at https://developer.amazon.com/alexa/console/ask.  This script is expecting your Alexa Skill 
       to have a custom Intent named "ShackPower" with an Intent Slot named "power_state" and provided value of either ON or OFF.
       
       There are many videos on YouTube covering how to create your own Alexa Skill - just remember that your skill will NOT be
       Alexa hosted, you will need to select "Provision your own" when asked to choose the method to host your still's backend resources.
       
    2. You will need to create a self-signed key pair to use with your Flask application and to upload to your custom Alexa skill.
       By default, this script is expecting these keys to be located at "/home/pi/cert.pem" and "/home/pi/key.pem", however this can be 
       changed on the last line of this script.
       
       To generate a self-signed key pair, run the following commands:
       "openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365"

    3. This Flask application will accept connections from ANYONE, which is INSECURE.  
       It is HIGHLY RECOMMENDED that you run this application behind a firewall which only allows connections from Amazon's servers.
'''

import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

STATUSON = ['on']
STATUSOFF = ['off']

 
@ask.launch
def launch():
    speech_text = 'Welcome to The Radio Gods Shack Power'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)


@ask.intent('ShackPower', mapping = {'power_state':'power_state'})
def shack_power(power_state,room):
    if power_state in STATUSON:
        os.system("python3 /home/pi/iot_power_control.py ON")
        return statement('turning {} the shack'.format(power_state))
    elif power_state in STATUSOFF:
        os.system("python3 /home/pi/iot_power_control.py OFF")
        return statement('turning {} the shack'.format(power_state))
    else:
        return statement('Sorry, I do not understand.  You can tell me to turn the shack power on or off')


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can tell me to turn the shack power on or off'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    # Note the paths for cert.pem and key.pem in the line below.  If the names or paths of your certs are different, they must be changed here
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=('/home/pi/cert.pem', '/home/pi/key.pem'))
