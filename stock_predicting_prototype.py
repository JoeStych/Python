##@mainpage Stock predicting prototype
#Written by Joseph Steichen
#a stock predictor prototype that uses machine learning algorithms to predict stock market trends
#
#@author Joseph Steichen
#@date April 27, 2023

from sklearn.linear_model import LogisticRegression

##@class LogisticRegression
#@brief Class for the logistic regression machine learning algorithm.

##@class emptyclass
#@brief this is empty

from sklearn.model_selection import train_test_split, RandomizedSearchCV

##@class RandomizedSearchCV
#@brief Class used for the Random Forest Classifier Optimization Program
#@details This class is used for the RFC optimizer. It creates numerous random forests and check which one has the best parameters

##@brief Splits the data into 4 arrays. 2 are used for training and 2 for testing.
#@param X independent variables
#@param Y dependent variable
#@param test_size how much fo thed data is to be used for testing
#@param random_state the seed for the random number generator

from sklearn.metrics import f1_score, accuracy_score

##@brief Takes the array of predicted values and compares with array of actual values to determine an f1 score.
#@param y_true the true y variable values
#@param y_pred the predicted y variable values
#@return f1 score for model

##@brief Determines the accuracy of a model
#@param y_true the true values of the y variable
#@param y_pred the predicted values of the y variable
#@return the percentage of correct predictions


from sklearn.ensemble import RandomForestClassifier

##@class RandomForestClassifer
#@brief The class for the random forest classifier machine learning algorithm.
#@details This class can be used to predict a y variable based on x variables.

from sklearn.naive_bayes import BernoulliNB

##@class BernoulliNB
#@brief The class for the Bernoulli Naive Bayesian machine learning model
#@details This class can be used to predict a binary y variable based on x variables.

import numpy as np

##@class numpy
#@brief This class is a special kind of array with more advanced formatting options than the default python lists.

import pandas as pd

##@class pandas
#@brief This class is a special kind of array with more advanced formatting optiosn than the default python lists.

from datetime import datetime as dt
import yfinance as yf
from ta import add_all_ta_features

##@brief This function calculates technical indicators based on arrays of market data.
#@param df The array to calculate data on.
#@returns a dictionary with the calculated techinical indicators.

import os

##Constant list of stock symbols being tested.
SYMBOLLIST = ["GOOGL", "AMZN", "XOM", "GE", "AAPL", "CAT", "PG", "JPM", "WMT", "JNJ", "BTC-USD"]

##Constant list of technical indicators
INDICATORLIST = ["trend_macd", "momentum_rsi", "momentum_stoch", "trend_arron_ind", "trend_cci", "trend_adx", "volume_obv", "trend_adx_pos", "trend_adx_neg"]

##Start date for the data miner
start_date = "2004-01-01"

##end date for the data miner
end_date = "2023-04-10"

##Path the program searches for all files
PATH = "C:\\"

##Amount of days per row of the daily matrix
WINDOW_SIZE = 12


#program greeting
print("----Welcome to Joseph's Stock Predicting Prototype----\n")
print("Please consult the user's manuel for proper usage.")
print("The current path is set to", PATH)


#locating data files and checking for their existence
if os.path.isfile(PATH + "XOMdata.txt"):
    print("Market data detected.")
    ##Variable marking whether the program located market data
    market_d = True
else:
    print("WARNING: Unable to locate market data. Please consult the user's manual for help.")
    market_d = False

if os.path.isfile(PATH + "Google Data\\" + "XOMgoogledata.txt"):
    print("Google data located.")
    ##variable marking whether the program located market data
    google_d = True
else:
    print("WARNING: Could not find google data. Please consult the user's manual for help.")
    google_d = False

#Core program loop
while True:
    if google_d == False or market_d == False:
        print("WARNING: Unable to locate either market or google data. Please update the PATH or consult user's manual.")
    
    #main menu
    print("\n---MENU---\n")
    print("1. Gather data for each stock from Yahoo Finance")
    print("2. Run the daily predictor")
    print("3. Run the monthly predictor")
    print("4. Change the PATH temporarily")
    print("5. Run the Random Forest Classifier Optimization Program")
    print("6. Quit")
    print("")
    ##saving choices from the user
    choice = eval(input("Enter your choice and press enter: "))
    
    if choice == 1: #data mining
        print("Data mining initiated...")
        # Extract the opening, closing, volume for each day and write to a text file
        for stock in SYMBOLLIST:
            print("Gathering data for ", stock, "...", sep='')
            data = yf.download(stock, start=start_date, end=end_date)
            data = add_all_ta_features(data, open="Open", high="High", low="Low", close="Close", volume="Volume")
            with open(PATH + stock +"data.txt", "w") as f:
                for index, row in data.iterrows():
                    #Date, open, close, and volume
                    date = index.strftime("%Y-%m-%d %H:%M:%S")
                    open_price = row["Open"]
                    close_price = row["Close"]
                    volume = row["Volume"]
                    
                    #technical indicators
                    macd = row["trend_macd"]
                    rsi = row["momentum_rsi"]
                    stoch = row["momentum_stoch"]
                    arron = row["trend_aroon_ind"]
                    cci = row["trend_cci"]
                    adx = row["trend_adx"]
                    adx_pos = row["trend_adx_pos"]
                    adx_neg = row["trend_adx_neg"]
                    obv = row["volume_obv"]
                    
                    f.write(f"{date} {open_price} {close_price} {volume} {macd} {rsi} {stoch} {arron} {cci} {adx} {adx_pos} {adx_neg} {obv}\n")

        print("Data collection Successful.")
    
    
    if choice == 2:#Daily stock predictor
        while True:
            if google_d == False or market_d == False:
                print("WARNING: Cannot locate market or google data. The program will fail to run correctly unless this issue is resolved.")
                another = input("Are you sure you want to continue? (y/n): ")
            
                if another != 'y':
                    break
                
            print("---DAILY PREDICTOR---")
            #forming the stock list and getting the choice from the user
            j = 0
            print("Select stock to train data. Enter -1 to quit.")
            for stock in SYMBOLLIST:
                print(j, ". ", stock, sep='')
                j += 1

            choice = eval(input("Choice: "))
            if choice == -1:
                break

            #Setting the targetted symbol to the one chosen by the user
            SYMBOL = SYMBOLLIST[choice]

            ##change in price over the day
            x = [0]
            ##binary increase or decrease of a stock
            y = []
            ##volume of a stock
            z = [0]
            date_array = [0]
            #technical indictors
            d_macd = [0]
            d_rsi = [0]
            d_stoch = [0]
            d_aroon_ind = [0]
            d_cci = [0]
            d_adx = [0]
            d_adx_pos = [0]
            d_adx_neg = [0]
            d_obv = [0]
            entryNum = 0
            nan_entries = 0

            #Reading from file
            with open(PATH + SYMBOL + "data.txt") as file:
                print("Loading Array with information from " + SYMBOL)
                while True:
                    element = file.readline()
                    if element == '':
                        break;
                    else:
                        date, date_time, opening, closing, volume, macd, rsi, stoch, aroon_ind, cci, adx, adx_pos, adx_neg, obv = element.split()
                        date_array.append(dt.strptime(date, '%Y-%m-%d'))
                        change = float(opening) - float(closing)
                        opening = float(opening)
                        closing = float(closing)
                        volume = float(volume)
                        x.append(change)
                        z.append(volume)
                        if change > 0:
                            y.append(1)
                        else:
                            y.append(0)
                        
                        d_macd.append(float(macd))
                        d_rsi.append(float(rsi))
                        d_stoch.append(float(stoch))
                        d_aroon_ind.append(float(aroon_ind))
                        d_cci.append(float(cci))
                        d_adx.append(float(adx))
                        d_adx_pos.append(float(adx_pos))
                        d_adx_neg.append(float(adx_neg))
                        d_obv.append(float(obv))
                        entryNum += 1

            print("Number of data points:", len(x))
            
            
            #creating generic number list
            numberList = []
            for i in range(0, entryNum + 1):
                numberList.append(i)


            #converting python lists into numpy arrays
            data = np.column_stack((date_array, numberList, x, z, d_macd, d_rsi, d_stoch, d_aroon_ind, d_cci, d_adx, d_adx_pos, d_adx_neg, d_obv))
            y = np.array(y)
            
            #excluding data with 'nan' values
            df = pd.DataFrame(data)
            nan_entries = df.shape[0]
            df = df.dropna()
            data = df.values
            nan_entries -= df.shape[0]
            print("Excluding", nan_entries, "data points.")
            
            #retrieval of google trends data
            google_date = []
            interest_array = []
            with open(PATH + "Google Data\\" + SYMBOL + "googledata.txt") as f:
                while True:
                    element = f.readline()
                    if element == '':
                        break
                    else:
                        date, interest = element.split(',')
                        if interest == '<1\n':
                            interest = 0.5
                        date = dt.strptime(date, '%Y-%m')
                        google_date.append(date)
                        interest_array.append(interest)
            
            #turning google trend lists into numpy array
            google_data = np.column_stack((google_date, interest_array))
            
            #adding a row of zeros to insert google data, and deleting the empty first row of the matrix
            data = np.column_stack((data, np.zeros(data.shape[0])))
            data = np.delete(data, 0, axis=0)
            
            #inserting google data into main matrix
            for row in data:
                for otherRow in google_data:
                    if row[0].month == otherRow[0].month and row[0].year == otherRow[0].year:
                        row[6] = otherRow[1]
            
            #creating multiple matrices of WINDOW_SIZE day periods
            data_new = []
            for i in range(WINDOW_SIZE, len(data)):
                data_window = data[i - WINDOW_SIZE:i, 1:]
                data_new.append(data_window)
            data_new = np.array(data_new)
            n_windows = data_new.shape[0]
            window_size = data_new.shape[1]
            n_features = data_new.shape[2]
            data_new = data_new.reshape((n_windows, window_size * n_features))
            
            
            
            #split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(data_new[:, 1:], y[:((-1 * (nan_entries - 1)) - WINDOW_SIZE) - 1], test_size=0.1, random_state=42)




            #train the logistic regression model on the training set
            print("\n\nTraining Logistic Regression Model...")
            ir = LogisticRegression()
            ir.fit(X_train[:, :], y_train)

            #predict the labels for the testing set
            ir_y_pred = ir.predict(X_test[:, :])

            #print the results of the test
            print("Logistic Regrssion results\n-----------------")

            num_incorrect = sum(ir_y_pred != y_test)
            print("Model was wrong at predicting stock rise/fall", num_incorrect, "times out of", len(y_test), "attempts")

            print("Accuracy:", accuracy_score(y_test, ir_y_pred))
            f1 = f1_score(y_test, ir_y_pred)
            print("F1 Score:", f1)





            #random forest classifier model
            print("\n\nTraining Random Forest...")

            #declare the forest. Parameters come from random forest optimizer
            rf = RandomForestClassifier(n_estimators=1400, max_depth=10, min_samples_split=2, min_samples_leaf=1, max_features="sqrt")

            #Training the model
            rf.fit(X_train[:, :2], y_train)

            #predicting the test data
            rf_y_pred = rf.predict(X_test[:, :2])

            #print the results
            print("\nRandom Forest Results\n------------")

            num_incorrect = sum(rf_y_pred != y_test)
            print("Model was wrong at predicting stock rise/fall", num_incorrect, "times out of", len(y_test), "attempts")
            
            print("Accuracy:", accuracy_score(y_test, rf_y_pred))
            print("F1-score:", f1_score(y_test, rf_y_pred))




            #Naive Bayes Bernoulli Model
            print("\n\nTraining Bernoulli Naive Bayes Model...")
            bnb = BernoulliNB()

            #train the model with training data
            bnb.fit(X_train[:, :2], y_train)

            #run predictions on test data
            bnb_y_pred = bnb.predict(X_test[:, :2])

            #print the results
            print("\nBernoulli Naive Bayes Results\n---------")
            num_incorrect = sum(bnb_y_pred != y_test)
            print("Model was wrong at predicting stock rise/fall", num_incorrect, "times out of", len(y_test), "attempts")

            print("Accuracy:", accuracy_score(y_test, bnb_y_pred))
            print("F1-score:", f1_score(y_test, bnb_y_pred))

            
            #run another stock?
            print("\n\n")
            another = input("Run models on another stock? (y/n): ")
            
            if another == 'n':
                choice = 0
                break
    
    
    if choice == 3:#monthly predictor
        while True:
            #checking if data can be located
            if google_d == False or market_d == False:
                print("WARNING: Cannot locate market or google data. The program will fail to run correctly unless this issue is resolved.")
                another = input("Are you sure you want to continue? (y/n): ")
            
                if another != 'y':
                    break
            #printing the stock list and getting choice from user
            print("---MONTHLY PREDICTOR---")
            j = 0
            print("Select stock to train data. Enter -1 to quit.")
            for stock in SYMBOLLIST:
                print(j, ". ", stock, sep='')
                j += 1

            choice = eval(input("Choice: "))
            if choice == -1:
                break


            SYMBOL = SYMBOLLIST[choice]

            x = [0] #change in price over the day
            y = [] #binary increase or decrease
            z = [0] #volume
            date_array = [0]
            open_array = [0]
            close_array = [0]
            #technical indictors
            d_macd = [0]
            d_rsi = [0]
            d_stoch = [0]
            d_aroon_ind = [0]
            d_cci = [0]
            d_adx = [0]
            d_adx_pos = [0]
            d_adx_neg = [0]
            d_obv = [0]
            entryNum = 0
            nan_entries = 0

            #reading market data from file
            with open(PATH + SYMBOL + "data.txt") as file:
                print("Loading Array with information from " + SYMBOL)
                while True:
                    element = file.readline()
                    if element == '':
                        break;
                    else:
                        date, date_time, opening, closing, volume, macd, rsi, stoch, aroon_ind, cci, adx, adx_pos, adx_neg, obv = element.split()
                        date_array.append(dt.strptime(date, '%Y-%m-%d'))
                        change = float(opening) - float(closing)
                        opening = float(opening)
                        closing = float(closing)
                        volume = float(volume)
                        open_array.append(opening)
                        close_array.append(closing)
                        x.append(change)
                        z.append(volume)
                        if change > 0:
                            y.append(1)
                        else:
                            y.append(0)
                        
                        d_macd.append(float(macd))
                        d_rsi.append(float(rsi))
                        d_stoch.append(float(stoch))
                        d_aroon_ind.append(float(aroon_ind))
                        d_cci.append(float(cci))
                        d_adx.append(float(adx))
                        d_adx_pos.append(float(adx_pos))
                        d_adx_neg.append(float(adx_neg))
                        d_obv.append(float(obv))
                        entryNum += 1

            print("Number of data points:", len(x))
            
            
            #forming a generic number list
            numberList = []
            for i in range(0, entryNum + 1):
                numberList.append(i)


            #converting python lists into numpy arrays
            data = np.column_stack((date_array, numberList, x, z, open_array, close_array, d_rsi, d_macd))
            data = np.delete(data, 0, axis=0)
            y = np.array(y)
            
            #forming arrays for monthly data
            targetMonth = data[0][0].month
            monthlyOpen = [data[0][4]]
            monthlyClose = []
            monthlyDates = [data[0][0]]
            
            #getting monthly data from stored daily data
            for row in data:
                if row[0].month != targetMonth:
                    monthlyClose.append(row[4])
                    monthlyOpen.append(row[4])
                    monthlyDates.append(row[0])
                    targetMonth = row[0].month
            
            monthlyClose.append(data[data.shape[0] - 1][4])
            y = []
            
            #getting binary increase or decrease for each month
            for i in range(0, len(monthlyClose)):
                change = monthlyClose[i] - monthlyOpen[i]
                if change >= 0:
                    y.append(1)
                else:
                    y.append(0)
            
            #forming a new number list based on size of monthly data
            numberList = []
            for i in range(0, len(monthlyClose)):
                numberList.append(i)
            
            data = np.column_stack((monthlyDates, numberList, monthlyOpen, monthlyClose))
            
            #reading data from google trends
            google_date = []
            interest_array = []
            with open(PATH + "Google Data\\" + SYMBOL + "googledata.txt") as f:
                while True:
                    element = f.readline()
                    if element == '':
                        break
                    else:
                        date, interest = element.split(',')
                        if interest == '<1\n':
                            interest = 0.5
                        interest = float(interest)
                        date = dt.strptime(date, '%Y-%m')
                        google_date.append(date)
                        interest_array.append(interest)
            
            google_data = np.column_stack((google_date, interest_array))
                        
            data = np.column_stack((data, np.zeros(data.shape[0])))
            
            #matching google data to other stock data
            for row in data:
                for otherRow in google_data:
                    if row[0].month == otherRow[0].month and row[0].year == otherRow[0].year:
                        row[data.shape[1] - 1] = otherRow[1]
            
            #deleting the empty row
            y = np.delete(y, 0)
            
            #variables for finding the averages across multiple tests
            LR_fscore = 0
            RFC_fscore = 0
            BNB_fscore = 0
            LR_incorrect = 0
            RFC_incorrect = 0
            BNB_incorrect = 0
            
            #Run 10 tests to makeup for the fact there is less monthly data points
            for i in range(10, 19):
                #split the data into training and testing sets
                X_train, X_test, y_train, y_test = train_test_split(data[:-1, 1:], y, test_size=0.1, random_state=i)




                #train the logistic regression model on the training set
                print("\n\nTraining Logistic Regression Model...")
                ir = LogisticRegression()
                ir.fit(X_train[:, :], y_train)

                #predict the labels for the testing set
                ir_y_pred = ir.predict(X_test[:, :])

                #print the final results
                print("Logistic Regrssion results\n-----------------")

                num_incorrect = sum(ir_y_pred != y_test)
                LR_incorrect += num_incorrect
                print("Model was wrong at predicting stock rise/fall", num_incorrect, "times out of", len(y_test), "attempts")

                print("Accuracy:", accuracy_score(y_test, ir_y_pred))
                f1 = f1_score(y_test, ir_y_pred)
                print("F1 Score:", f1)
                
                LR_fscore += f1


                #Random forest training
                print("\n\nTraining Random Forest...")
                
                #declaring random forest using values from the optimizer
                rf = RandomForestClassifier(n_estimators=1000, max_depth=40, min_samples_split=2, min_samples_leaf=2, max_features="sqrt")

                #fitting model with training data
                rf.fit(X_train[:, :2], y_train)

                #testing the test data
                rf_y_pred = rf.predict(X_test[:, :2])

                #printing the results
                print("\nRandom Forest Results\n------------")

                num_incorrect = sum(rf_y_pred != y_test)
                RFC_incorrect += num_incorrect
                print("Model was wrong at predicting stock rise/fall", num_incorrect, "times out of", len(y_test), "attempts")
                
                print("Accuracy:", accuracy_score(y_test, rf_y_pred))
                print("F1-score:", f1_score(y_test, rf_y_pred))

                RFC_fscore += f1_score(y_test, rf_y_pred)


                #Naive Bayes Bernoulli model
                print("\n\nTraining Bernoulli Naive Bayes Model...")
                bnb = BernoulliNB()

                #fitting the model with training data
                bnb.fit(X_train[:, :2], y_train)

                #predicting the test data
                bnb_y_pred = bnb.predict(X_test[:, :2])

                #printing the results
                print("\nBernoulli Naive Bayes Results\n---------")
                num_incorrect = sum(bnb_y_pred != y_test)
                BNB_incorrect += num_incorrect
                print("Model was wrong at predicting stock rise/fall", num_incorrect, "times out of", len(y_test), "attempts")

                print("Accuracy:", accuracy_score(y_test, bnb_y_pred))
                print("F1-score:", f1_score(y_test, bnb_y_pred))
                BNB_fscore += f1_score(y_test, bnb_y_pred)

            #dividing all scores by 10 to get the average
            LR_fscore /= 10
            LR_incorrect /= 10
            RFC_fscore /= 10
            RFC_incorrect /= 10
            BNB_fscore /= 10
            BNB_incorrect /= 10


            #printing all the final results
            print("FINAL RESULTS\n----------\n")
            print("Logistic Regression...")
            print("Average Incorrect:", LR_incorrect, "/", len(y_test))
            print("Average Accuracy:", (len(y_test) - LR_incorrect) / len(y_test))
            print("Average F1 Score:", LR_fscore)
            
            print("\nRandom Forest Classifier...")
            print("Average Incorrect:", RFC_incorrect, "/", len(y_test))
            print("Average Accuracy:", (len(y_test) - RFC_incorrect) / len(y_test))
            print("Average F1 Score:", RFC_fscore)
            
            print("\nBernoulli Naive Bayesian...")
            print("Average Incorrect:", BNB_incorrect, "/", len(y_test))
            print("Average Accuracy:", (len(y_test) - BNB_incorrect) / len(y_test))
            print("Average F1 Score:", BNB_fscore)


            #prompting user for another run
            print("\n\n")
            another = input("Run models on another stock? (y/n): ")
            
            if another == 'n':
                choice = 0
                break
            
    
    
    if choice == 4:#updating the path
        while True:
            print("What would you like to change the path to?")
            print("NOTE: Changes to the PATH are lost after program termination. Consult user's manual to change permanently.")
            print("Remember to use double backslashes '\\' between directories.")
            PATH = input("Path = ")
            if os.path.isfile(PATH + "XOMdata.txt"):
                print("Market data detected.")
                market_d = True
            else:
                print("Unable to locate market data. Please consult the user's manual for help.")

            if os.path.isfile(PATH + "Google Data\\" + "XOMgoogledata.txt"):
                print("Google data located.")
                google_d = True
            else:
                print("Could not find google data. Please consult the user manual for help.")
                
            if google_d == True and market_d == True:
                print("Both market data and google data were detected.")
                break
            else:
                print("Failed to detect either market or google data.")
                another = input("Try updating the PATH again? (y/n): ")
                if another == 'n':
                    break
    
    
    if choice == 5:#RFC optimization program
        print("NOTE: The Random Forest Classifier Optimization Program is used to find the best parameters for the RFC.")
        print("It was used in the making of this program and it's benefits have already been realized.")
        print("The program has been included in this final version simply to show how the best parameters were found.")
        print("It is not required to be ran for the best parameters to be present. They have already been included.")
        print("(Press enter to continue)")
        input()
        
        print("Would you like the run the optimizer on daily or monthly data?\n")
        print("1. Daily")
        print("2. Monthly")
        print("3. Back to main menu")
        n = eval(input("\nChoice: "))
        
        if n == 1:
            while True:
                #stock list and getting input
                j = 0
                print("Select stock to train DAILY data. Enter -1 to quit.")
                for stock in SYMBOLLIST:
                    print(j, ". ", stock, sep='')
                    j += 1

                choice = eval(input("Choice: "))
                if choice == -1:
                    break


                SYMBOL = SYMBOLLIST[choice]


                x = [0]#change over a given day
                y = []#binary increase/decrease
                z = [0]#volume
                #technical indicators
                d_macd = [0]
                d_rsi = [0]
                d_stoch = [0]
                d_aroon_ind = [0]
                d_cci = [0]
                d_adx = [0]
                d_adx_pos = [0]
                d_adx_neg = [0]
                d_obv = [0]
                entryNum = 0
                nan_entries = 0

                #reading market data from file
                with open(PATH + SYMBOL + "data.txt") as file:
                    print("Loading Array with information from " + SYMBOL)
                    while True:
                        element = file.readline()
                        if element == '':
                            break;
                        else:
                            date, date_time, opening, closing, volume, macd, rsi, stoch, aroon_ind, cci, adx, adx_pos, adx_neg, obv = element.split()
                            change = float(opening) - float(closing)
                            opening = float(opening)
                            closing = float(closing)
                            volume = float(volume)
                            x.append(change)
                            z.append(volume)
                            if change > 0:
                                y.append(1)
                            else:
                                y.append(0)

                            d_macd.append(float(macd))
                            d_rsi.append(float(rsi))
                            d_stoch.append(float(stoch))
                            d_aroon_ind.append(float(aroon_ind))
                            d_cci.append(float(cci))
                            d_adx.append(float(adx))
                            d_adx_pos.append(float(adx_pos))
                            d_adx_neg.append(float(adx_neg))
                            d_obv.append(float(obv))
                            entryNum += 1

                print("Number of data points in file:", len(x))

                #creating generic number list
                numberList = []
                for i in range(0, entryNum + 1):
                    numberList.append(i)


                #convert python lists into numpy matrix
                data = np.column_stack((numberList, x, z))
                
                #excluding data with 'nan' values
                df = pd.DataFrame(data)
                nan_entries = df.shape[0]
                df = df.dropna()
                data = df.values
                nan_entries -= df.shape[0]
                print("Excluding", nan_entries, "nan data points.")
                
                #putting data into matrix of matrices containing WINDOW_SIZE day periods
                data_new = []
                for i in range(WINDOW_SIZE, len(data)):
                    data_window = data[i - WINDOW_SIZE:i]
                    data_new.append(data_window)
                data_new = np.array(data_new)
                n_windows = data_new.shape[0]
                window_size = data_new.shape[1]
                n_features = data_new.shape[2]
                data_new = data_new.reshape((n_windows, window_size * n_features))
                

                #Split the data into training and testing sets
                X_train, X_test, y_train, y_test = train_test_split(data[:-1, :], y, test_size=0.2, random_state=42)
                
                
                print("\nRunning the optimizer.\nWARNING: This will take a while.\n")
                rf = RandomForestClassifier()
                
                #setting parameters to be iterated through
                n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
                max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
                max_depth.append(None)
                min_samples_split = [2, 5, 10]
                min_samples_leaf = [1, 2, 4]
                
                #placing parameters into a grid
                random_grid = {'n_estimators': n_estimators,
                        'max_features': [1.0, 'sqrt'],
                        'max_depth': max_depth,
                        'min_samples_split': min_samples_split,
                        'min_samples_leaf': min_samples_leaf,
                        }
                
                #setting up the randomized search
                rf_random = RandomizedSearchCV(estimator=rf,
                                        param_distributions=random_grid,
                                        n_iter=100,
                                        cv=3,
                                        verbose=2,
                                        random_state=42,
                                        n_jobs=-1,
                                        scoring="accuracy")
                
                #running the test and printing the best tree's parameters and score
                rf_random.fit(X_train, y_train)
                print(rf_random.best_params_)
                print(rf_random.best_score_)
                
                print("\n\nTry another?")
                another = input("(y/n): ")
                if another == 'n':
                    choice = 0
                    break
                
        
        if n == 2:#monthly optimizer
            while True:
                j = 0
                print("Select stock to train MONTHLY data. Enter -1 to quit.")
                for stock in SYMBOLLIST:
                    print(j, ". ", stock, sep='')
                    j += 1

                choice = eval(input("Choice: "))
                if choice == -1:
                    break


                SYMBOL = SYMBOLLIST[choice]

                x = [0] #change in over the day
                y = [] #binary increase or decrease
                z = [0] #volume
                date_array = [0]
                open_array = [0]
                close_array = [0]
                #technical indictors
                d_macd = [0]
                d_rsi = [0]
                d_stoch = [0]
                d_aroon_ind = [0]
                d_cci = [0]
                d_adx = [0]
                d_adx_pos = [0]
                d_adx_neg = [0]
                d_obv = [0]
                entryNum = 0
                nan_entries = 0

                # reading market data from file
                with open(PATH + SYMBOL + "data.txt") as file:
                    print("Loading Array with information from " + SYMBOL)
                    while True:
                        element = file.readline()
                        if element == '':
                            break;
                        else:
                            date, date_time, opening, closing, volume, macd, rsi, stoch, aroon_ind, cci, adx, adx_pos, adx_neg, obv = element.split()
                            date_array.append(dt.strptime(date, '%Y-%m-%d'))
                            change = float(opening) - float(closing)
                            opening = float(opening)
                            closing = float(closing)
                            volume = float(volume)
                            open_array.append(opening)
                            close_array.append(closing)
                            x.append(change)
                            z.append(volume)
                            if change > 0:
                                y.append(1)
                            else:
                                y.append(0)
                            
                            d_macd.append(float(macd))
                            d_rsi.append(float(rsi))
                            d_stoch.append(float(stoch))
                            d_aroon_ind.append(float(aroon_ind))
                            d_cci.append(float(cci))
                            d_adx.append(float(adx))
                            d_adx_pos.append(float(adx_pos))
                            d_adx_neg.append(float(adx_neg))
                            d_obv.append(float(obv))
                            entryNum += 1
                
                

                numberList = []
                for i in range(0, entryNum + 1):
                    numberList.append(i)


                #converting python lists into numpy arrays
                data = np.column_stack((date_array, numberList, x, z, open_array, close_array, d_rsi, d_macd))
                data = np.delete(data, 0, axis=0)
                y = np.array(y)
                
                #converting daily data into monthly data
                targetMonth = data[0][0].month
                monthlyOpen = [data[0][4]]
                monthlyClose = []
                monthlyDates = [data[0][0]]
                for row in data:
                    if row[0].month != targetMonth:
                        monthlyClose.append(row[4])
                        monthlyOpen.append(row[4])
                        monthlyDates.append(row[0])
                        targetMonth = row[0].month
                
                monthlyClose.append(data[data.shape[0] - 1][4])
                y = []
                
                for i in range(0, len(monthlyClose)):
                    change = monthlyClose[i] - monthlyOpen[i]
                    if change >= 0:
                        y.append(1)
                    else:
                        y.append(0)
                
                #reforming the number list
                numberList = []
                for i in range(0, len(monthlyClose)):
                    numberList.append(i)
                
                data = np.column_stack((monthlyDates, numberList, monthlyOpen, monthlyClose))
                
                #reading google trends data
                google_date = []
                interest_array = []
                with open(PATH + "Google Data\\" + SYMBOL + "googledata.txt") as f:
                    while True:
                        element = f.readline()
                        if element == '':
                            break
                        else:
                            date, interest = element.split(',')
                            if interest == '<1\n':
                                interest = 0.5
                            interest = float(interest)
                            date = dt.strptime(date, '%Y-%m')
                            google_date.append(date)
                            interest_array.append(interest)
                
                #adding google trends data to main matrix
                google_data = np.column_stack((google_date, interest_array))
                
                data = np.column_stack((data, np.zeros(data.shape[0])))
                
                for row in data:
                    for otherRow in google_data:
                        if row[0].month == otherRow[0].month and row[0].year == otherRow[0].year:
                            row[data.shape[1] - 1] = otherRow[1]
                
                #deleting empty row
                y = np.delete(y, 0)
                
                print("Number of data points:", len(data))
                
                # Split the data into training and testing sets
                X_train, X_test, y_train, y_test = train_test_split(data[:-1, 1:], y, test_size=0.1, random_state=15)
                
                print("\nRunning the optimizer.\nWARNING: This will take a while.\n")
                rf = RandomForestClassifier()
                
                #setting parameters to be iterated through
                n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
                max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
                max_depth.append(None)
                min_samples_split = [2, 5, 10]
                min_samples_leaf = [1, 2, 4]
                
                random_grid = {'n_estimators': n_estimators,
                        'max_features': [1.0, 'sqrt'],
                        'max_depth': max_depth,
                        'min_samples_split': min_samples_split,
                        'min_samples_leaf': min_samples_leaf,
                        }
                
                #setting up the randomized search
                rf_random = RandomizedSearchCV(estimator=rf,
                                        param_distributions=random_grid,
                                        n_iter=100,
                                        cv=3,
                                        verbose=2,
                                        random_state=42,
                                        n_jobs=-1,
                                        scoring="accuracy")
                
                #running the test and printing the best tree's parameters and score
                rf_random.fit(X_train, y_train)
                print(rf_random.best_params_)
                print(rf_random.best_score_)
                
                print("\n\nTry another?")
                another = input("(y/n): ")
                if another == 'n':
                    choice = 0
                    break
    
    
    if choice == 6:#quit
        print("Goodbye.")
        break