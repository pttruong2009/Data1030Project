import time
from slackclient import SlackClient
from slacker import Slacker
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from pymongo import MongoClient
import matplotlib
import matplotlib.pyplot as plt

# starterbot's ID as an environment variable
BOT_ID = 'U8D759XB8'

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "company"


# instantiate Slack clients
slack_client = SlackClient('xoxb-285243337382-trQ8Ywc88dCdCdjHedSg5IBH')
slack = Slacker("xoxb-285636270311-HqQMMkAum8wl4FCbSPVUqBs9")

matplotlib.use('TkAgg')

#training and creating the model

#loading the data set
df = pd.read_csv('glassdoor_linkedin_final2.csv', encoding='iso-8859-1')

#removing rows with zero or null values
df2 = df[np.isfinite(df['Avg_Commute_work'])]
df2 = df2[df.Avg_Commute_work != 0]
df2 = df2[np.isfinite(df['ceo_pctApprove'])]
df2 = df2[df.ceo_pctApprove != 0]
df2 = df2[np.isfinite(df['compensation_rating'])]
df2 = df2[df.compensation_rating != 0]
df2 = df2[np.isfinite(df['culture_rating'])]
df2 = df2[df.culture_rating != 0]
df2 = df2[np.isfinite(df['overallRating'])]
df2 = df2[df.overallRating != 0]
df2 = df2[np.isfinite(df['recommendToFriendRating'])]
df2 = df2[df.recommendToFriendRating != 0]
df2 = df2[np.isfinite(df['seniorLeadershipRating'])]
df2 = df2[df.seniorLeadershipRating != 0]
df2 = df2[np.isfinite(df['workLifeBalanceRating'])]
df2 = df2[df.workLifeBalanceRating != 0]
df2 = df2[np.isfinite(df['population'])]
df2 = df2[df.population != 0]
df2 = df2[np.isfinite(df['crime_rate_per_1000'])]
df2 = df2[df.crime_rate_per_1000 != 0]

#remove variables that are not important
df2 = df2.drop('ceo_names', 1)
df2 = df2.drop('ceo_names.1', 1)
df2 = df2.drop('ceo_pctDisapprove', 1)
df2 = df2.drop('company_name', 1)
df2 = df2.drop('HQ_City', 1)
df2 = df2.drop('HQ_State', 1)
df2 = df2.drop('Growth', 1)
df2 = df2.drop('compensation_rating', 1)
df2 = df2.drop('overallRating', 1)  # Directly correspond with the classification (1 to 1)
df2 = df2.drop('seniorLeadershipRating', 1)
df2 = df2.drop('workLifeBalanceRating', 1)
df2 = df2.drop('ceo_pctApprove', 1)
df2 = df2.drop('population', 1)
df2 = df2.drop('ratingDescription', 1)
df2 = df2.drop('diversity',1)
df2.loc[df2['recommendToFriendRating'] < 60, 'recommendToFriendRating'] = 0
df2.loc[df2['recommendToFriendRating'] > 59, 'recommendToFriendRating'] = 1

#separating training and test
training_data = df2.tail(680)
test_data = df2.head(177)

# x_values and y_values
y_train = training_data['recommendToFriendRating'].values
y_test = test_data['recommendToFriendRating'].values

x_train = training_data.drop('recommendToFriendRating', 1)
x_test = test_data.drop('recommendToFriendRating', 1)

# training the model
clf2 = RandomForestClassifier()
clf5 = LogisticRegression()
eclf = VotingClassifier(estimators=[('rf', clf2), ('lr', clf5)], voting='soft')

param_grid = {
    'rf__n_estimators': [2, 4, 8, 16],
    'rf__min_samples_leaf': [50, 100, 500, 128, 250, 400],
    'weights': [[7, 3], [2, 5], [3, 4], [5, 3], [4, 2], [2, 3]]
}
eclf = RandomizedSearchCV(estimator=eclf, param_distributions=param_grid, cv=10, scoring='accuracy')

#fitting the model
eclf.fit(x_train, y_train)

#loading data from MongoDB
client = MongoClient('mongodb://cavu17:Hello1234@ds111476.mlab.com:11476/final_project')
db = client.get_database('final_project')

#data tables containing information about city and state
commute_df = pd.DataFrame.from_records(db.city_commute.find())
rain_df = pd.DataFrame.from_records(db.state_rainfall.find())
snow_df = pd.DataFrame.from_records(db.snowfall_data.find())
crime_df = pd.DataFrame.from_records(db.crime_data.find())

#reconstruct city and state field
commute_df["city-state"] = commute_df["city"] + "-" + commute_df["state"]
crime_df["city-state"] = crime_df["City"] + "-" + crime_df["abbreviation"]


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands to output a recommendation. If not,
        returns back what it needs for clarification.
    """

    com = command.split() #parsing command values

    #parsing city and state values
    if len(com)>=4:
        if len(com)==4:
            city = com[2].title()
        else:
            city_pre = com[2:len(com) - 1]
            city = city_pre[0].title()
            for i in range(1, len(city_pre)):
                city = city + " " + city_pre[i].title()
        state = com[len(com)-1].upper()
        city_state = city + "-"+state
    else:
        response = "You are missing some values. Use the *" + EXAMPLE_COMMAND + \
                   "* command with format: " + EXAMPLE_COMMAND +" culture_rating city state."

    # search in data set for commute, rain, snow, crime, and culture rating for company, city and state


    if (command.startswith(EXAMPLE_COMMAND) and len(com)>=4):
        if (any(commute_df['city-state'] == city_state)):
            commute_pre = commute_df[(commute_df['city-state'] == city_state)]
            commute = commute_pre['commute_time_mins_est'].values[0]
            if (any(rain_df['Abbreviation'] == state)):
                rain_pre = rain_df[(rain_df['Abbreviation'] == state)]
                inches_rain = rain_pre['Inches'].values[0]
                if (any(snow_df['Abbreviation'] == state)):
                    snow_pre = snow_df[(snow_df['Abbreviation'] == state)]
                    inches_snow = snow_pre['inches'].values[0]
                    if (any(crime_df["city-state"]==city_state)):
                        crime_pre = crime_df[(crime_df['city-state']==city_state)]
                        crime = crime_pre['crime_rate'].values[0]
                        try:
                            culture = float(com[1])
                            if culture <= 5 and culture >= 1:
                                #feed data into model
                                x_t = {'culture_rating': [culture],
                                        'Annual_Rainfall': [inches_rain],
                                        'Annual_Snowfall': [inches_snow],
                                        'Avg_Commute_work': [commute],
                                        'crime_rate_per_1000': [crime],}
                                x_t = pd.DataFrame(data=x_t)
                                x_t = x_t.reindex_axis(
                                        ['culture_rating', 'Annual_Rainfall', 'Annual_Snowfall', 'Avg_Commute_work',
                                        'crime_rate_per_1000'], axis=1)
                                probas = eclf.predict_proba(x_t)
                                probas2 = eclf.predict(x_t)

                                #constructing bot response
                                if probas2[0] == 0:
                                    response = "No, I don't recommend it!"

                                else:
                                    response = "Yes. Go for it!"
                                plt.gcf().clear()
                                x = [1, 2]
                                labels = ['No', 'Yes']
                                plt.bar(x, probas[0], align='center')
                                plt.xticks(x, labels)
                                plt.savefig("botfig.png")
                            else:
                                #Error for when user input incorrect values for culture rating
                                response = "Enter culture rating in range 1-5"
                        except:
                            # Error for when user input incorrect values for culture rating
                            response = "Enter culture rating with correct syntax"
                    else:
                        # Error for when the script cannot find city and state combination in database
                        response = "City/State does not exist in database"
                else:
                    # Error for when the script cannot find city and state combination in database
                    response = "City/State does not exist in database"
            else:
                # Error for when the script cannot find city and state combination in database
                response = "City/State does not exist in database"
        else:
            # Error for when the script cannot find city and state combination in database
            response = "City/State does not exist in database"
    else:
        # Error for when user input an incorrect command
        response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
                   "* command with format: " + EXAMPLE_COMMAND +" culture_rating city state.  Example: @friend-bot company 3.3 Tacoma WA"

    # Error for when user input an incorrect command structure

    if command =="whats up?":
        response = "What's up team? Heard you have a presentation today."
    elif command == "yup it is today.":
        response = "Good luck!"
    elif command == "we need your help!":
        response = "of course, how can I help?"

    # Sending bot response to channel
    slack_client.api_call("chat.postMessage", channel='G8E2KGF8W',
                          text=response, as_user=True)
    if (response == "No, I don't recommend it!") or (response == "Yes. Go for it!"):
        slack.files.upload("botfig.png", channels="G8E2KGF8W")



def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            print(output)
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace remove
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


#initiate the bot connnection
if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")