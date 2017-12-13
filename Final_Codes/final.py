from tkinter import *
# Import the required packages
import pandas as pd
import numpy as np
from pymongo import MongoClient

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LogisticRegression


#initiate request to MongoDB
client = MongoClient('mongodb://cavu17:Hello1234@ds111476.mlab.com:11476/final_project')
db = client.get_database('final_project')

#import dataset
df = pd.read_csv('glassdoor_linkedin_final2.csv', encoding='iso-8859-1')

#remove rows with null or zero values
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
df2 = df2[np.isfinite(df['diversity'])]
df2 = df2[df.diversity != 0]

#drop features that are not important
df2 = df2.drop('ceo_names',1)
df2 = df2.drop('ceo_pctDisapprove',1)
df2 = df2.drop('company_name',1)
df2 = df2.drop('HQ_City',1)
df2 = df2.drop('HQ_State',1)
df2 = df2.drop('Growth',1)
df2 = df2.drop('compensation_rating',1)
df2 = df2.drop('ceo_names.1',1)
df2 = df2.drop('overallRating',1) #Direct correspond with the classification
df2 = df2.drop('seniorLeadershipRating',1)
df2 = df2.drop('workLifeBalanceRating',1)
df2 = df2.drop('ceo_pctApprove',1)
df2 = df2.drop('population',1)
df2 = df2.drop('ratingDescription',1)
df2 = df2.drop('diversity',1)

#set threshold for recommend or not recommend
df2.loc[df2['recommendToFriendRating'] < 60, 'recommendToFriendRating'] = 0
df2.loc[df2['recommendToFriendRating'] > 59, 'recommendToFriendRating'] = 1

#training and test sets
training_data = df2.tail(700)
test_data = df2.head(157)

#x_values(features) and y_values(output)
y_train = training_data['recommendToFriendRating'].values
y_test = test_data['recommendToFriendRating'].values
x_train = training_data.drop('recommendToFriendRating',1)
x_test = test_data.drop('recommendToFriendRating',1)



# fit the model using the dataset
clf2 = RandomForestClassifier()
clf5 = LogisticRegression()
eclf = VotingClassifier(estimators=[ ('rf', clf2),('lr',clf5)],voting='soft')

param_grid = {
            'rf__n_estimators': [2, 4, 8, 16],
              'rf__min_samples_leaf':[50,100, 500,128,250,400],
              'weights': [[7,3],[2,5],[3,4],[5,3],[4,2],[2,3]]
            }
eclf = RandomizedSearchCV(estimator=eclf, param_distributions=param_grid, cv=10, scoring = 'accuracy')

#fit model
eclf.fit(x_train, y_train)


def show_answer():
    """Receives culture rating, city, and state inputs. Gather commute, crime, rainfall, and snowfall data for these inputs.
    Returns recommendations one whether or not the employees are happy with the job in term of recommendations. It also outputs
    probability of "yes" and "no".
    """

    #Extract city and state input
    x = num2.get()
    y = num3.get()

    # initiate plot
    fig = plt.figure(1)
    plt.ion()
    plt.gcf().clear()

    blank.delete(0, END)#clear previous input values

    answer = '' #output answer

    #Loads commute data based on city and state. Returns error if city/state combination is not found.
    try:
        commute = db.city_commute.find_one({'city': x, 'state': y}, {'commute_time_mins_est': True})['commute_time_mins_est']
    except:
        blank.delete(0, END)
        blank.insert(0,"City/State does not exist in database")


    #Loads rainfall data based on state. Returns error if state is not found
    try:
        inches_rain = db.state_rainfall.find_one({'Abbreviation': y}, {'Inches': True})['Inches']
    except:
        blank.delete(0, END)
        blank.insert(0, "City/State does not exist in database")


    #Loads snowfall data based on state. Returns error if state is not found
    try:
        inches_snow = db.snowfall_data.find_one({'Abbreviation': y}, {'inches': True})['inches']
    except:
        blank.delete(0, END)
        blank.insert(0, "City/State does not exist in database")

    # Loads crime data based on city and state. Returns error if city/state combination is not found.
    try:
        crime = db.crime_data.find_one({'City': x, 'abbreviation': y}, {'crime_rate': True})['crime_rate']
    except:
        blank.delete(0, END)
        blank.insert(0, "City/State does not exist in database")

    # Process culture rating input. Returns error if culture rating is not in the correct syntax
    try:
        culture=float(num1.get())
    except:
        blank.delete(0, END)
        blank.insert(0, "Enter culture rating with correct syntax")

    #organize input data into a data frame and insert into trained model
    x_t = {'culture_rating': [culture],
        'Annual_Rainfall': [inches_rain],
        'Annual_Snowfall': [inches_snow],
       'Avg_Commute_work': [commute],
        'crime_rate_per_1000': [crime]}
    x_t = pd.DataFrame(data=x_t)
    x_t = x_t.reindex_axis(['culture_rating', 'Annual_Rainfall', 'Annual_Snowfall', 'Avg_Commute_work', 'crime_rate_per_1000'], axis=1)

    try:
        probas = eclf.predict_proba(x_t)
        probas2 = eclf.predict(x_t)
    except:
        blank.delete(0, END)
        blank.insert(0, "City/State does not exist in database")


    #Generate output
    if culture <= 5 and culture >= 1:
        if probas2[0] == 0:
            answer = "No, I don't recommend it!"
            blank.insert(0,answer)
        else:
            answer = "Yes. Go for it!"
            blank.insert(0, answer)
    else:
        blank.insert(0, "Enter culture rating in range 1-5")


    #generate probability chart
    if answer == "No, I don't recommend it!" or answer == "Yes. Go for it!":
        x = [1, 2]
        labels = ['No', 'Yes']
        plt.bar(x, probas[0], align='center')
        plt.xticks(x, labels)
        canvas = FigureCanvasTkAgg(fig, main)
        plot_widget = canvas.get_tk_widget()
        plot_widget.grid(row=5, columnspan=2)

#initiation UI
main = Tk()

#Labels for text box
Label(main, text = "Culture Rating:").grid(row=0,sticky='e')
Label(main, text = "City:").grid(row=1,sticky='e')
Label(main, text = "State:").grid(row=2,sticky='e')
Label(main, text = "Result").grid(row=3,sticky='e')

#Text boxes
num1 = Entry(main,width=30)
num2 = Entry(main,width=30)
num3 = Entry(main,width=30)
blank = Entry(main,width=30)
num1.insert(END, '3.5 (Scale 1-5)')
num2.insert(END, 'Tacoma')
num3.insert(END, 'WA')


#Insert text box
num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
num3.grid(row=2, column=1)
blank.grid(row=3, column=1)

#Buttons for quit and run 
Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W, pady=4)
Button(main, text='Run', command=show_answer).grid(row=4, column=1, sticky=W, pady=4)

mainloop()