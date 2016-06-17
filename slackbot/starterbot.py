import requests
import time
from config_file_stamates import *
from slackclient import SlackClient

API_URL = "https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?language=eng&apikey=" + \
            HPE_HAVEN_API_KEY

BOT_ID = GP_HOA_STARTERBOT_ID

# constants
AT_BOT = "<@" + BOT_ID + ">:"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient(GP_HOA_STARTERBOT_TOKEN)

def score_response(score):
    response = ""
    if score < -0.9:
        response = "Whoa, whoa!  You're making baby Jesus cry.  Let's try to be more positive!"
    elif score < -0.7:
        response = "Someone seems a little cranky... no you need a nap?  Maybe some juice?"
    elif score < 0:
        pass
    elif score < 0.7:
        pass
    elif score < 0.9:
        response = "Someone's in a chipper mood!"
    else:
        response = "Wow!  The cup isn't half full, it's 4 smaller cups that are overflowing isn't it?!"
    return response

def handle_command(atbot, command, channel, score):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = score_response(score)
    if atbot:
        if command.startswith(EXAMPLE_COMMAND):
            response = "Sure...write some more code then I can do that!"
        else:
            response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
                        "* command with numbers, delimited by spaces."
    if response != "":
        if score < -0.91: # Remove offensive message
            pass # Remove message
        slack_client.api_call("chat.postMessage", channel=channel,
                              text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    score = 0
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and output['user'] != BOT_ID:
                url = API_URL + "&text=" + output['text']
                sentiment = requests.get(url).json() # Receives sentiment results from HPE Haven API
                try:
                    score = sentiment['aggregate']['score']
                    print score
                except:
                    pass
                if AT_BOT in output['text']:
                    # return text after the @ mention, whitespace removed
                    return True, output['text'].split(AT_BOT)[1].strip().lower(), \
                           output['channel'], score
                else:
                    return False, output['text'], output['channel'], score
    return False, None, None, score

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            atbot, command, channel, score = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(atbot, command, channel, score)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
