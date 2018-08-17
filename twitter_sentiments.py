#CEM TORUN
#HERE IS MY CODE!

#-------------------------------------
#DEFINING VARIABLES AND FUNCTIONS

listOfKeywords = [] #Setting an empty list for keywords
listOfPrimaryScoreValues = [] #Setting an empty list for scores

#list of all happiness values for each tweet
pacificTimeZoneListHapScoreTotal = []
mountainTimeZoneListHapScoreTotal = []
centralTimeZoneListHapScoreTotal = []
easternTimeZoneListHapScoreTotal = []

#number of tweets in timezone list
pacificTimeZoneListNumberTweets = []
mountainTimeZoneListNumberTweets = []
centralTimeZoneListNumberTweets = []
easternTimeZoneListNumberTweets = []

#sum of happiness values before division
pacificTimeZoneHappinessScoreFinal = 0
mountainTimeZoneHappinessScoreFinal = 0
centralTimeZoneHappinessScoreFinal = 0
easternTimeZoneHappinessScoreFinal = 0

punctuation=["(", ")", "?", ":", ";", ",", "!", "/", "'", '"', "#"] #list of punctuation that will be removed

#This function below returns the longitude value that would have already been split within the list and makes it so
#it is cleaned up only such that it is only the numerial value (ex: 41.00021201 instead of ["41.34141"],
def cleanUpLongitude(lineSplit):
    return str(lineSplit[1].replace("]",""))

def cleanUpLatitude(lineSplit):
    placeHolder = lineSplit[0].replace("[","")
    return placeHolder.replace(",","")

#This function checks the value of the longitude of the tweet and appends the value that coincides with the keyword
#to a list. This is the case for each and every timezone what of which each have their own respective lists.
def longitudeValueCheck(longitudeValue,latitudeValue):
    if longitudeValue >= -87.518395 and longitudeValue <= -67.444574 and latitudeValue < 49.189787 and latitudeValue > 24.660845:
        hapValueCurrent = (listOfPrimaryScoreValues[counter - 1])
        easternTimeZoneListHapScoreTotal.append((listOfPrimaryScoreValues[counter - 1]))
        return hapValueCurrent
    elif longitudeValue >= -101.998892 and longitudeValue < -87.518395 and latitudeValue < 49.189787 and latitudeValue > 24.660845:
        hapValueCurrent = (listOfPrimaryScoreValues[counter - 1])
        centralTimeZoneListHapScoreTotal.append((listOfPrimaryScoreValues[counter - 1]))
        return hapValueCurrent
    elif longitudeValue >= -115.236428 and longitudeValue < -101.99889 and latitudeValue < 49.189787 and latitudeValue > 24.660845:
        hapValueCurrent = (listOfPrimaryScoreValues[counter - 1])
        mountainTimeZoneListHapScoreTotal.append((listOfPrimaryScoreValues[counter - 1]))
        return hapValueCurrent
    elif longitudeValue >= -125.242264 and longitudeValue < -115.236428 and latitudeValue < 49.189787 and latitudeValue > 24.660845:
        hapValueCurrent = (listOfPrimaryScoreValues[counter - 1])
        pacificTimeZoneListHapScoreTotal.append((listOfPrimaryScoreValues[counter - 1]))
        return hapValueCurrent
    else:
        hapValueCurrent = 0
        return hapValueCurrent

#function to check for the number of tweets in a region, this is segmented from the function above b/c this runs a
#check to see
def numberOfTweetInRegionCheckAndHapScoreTotalCalc(longitudeValue,latitudeValue):
    if longitudeValue >= -87.518395 and longitudeValue <= -67.444574 and latitudeValue < 49.189787 and latitudeValue > 24.660845:
        easternTimeZoneListNumberTweets.append(1)
    elif longitudeValue >= -101.998892 and longitudeValue < -87.518395 and latitudeValue < 49.189787 and latitudeValue > 24.660845:
        centralTimeZoneListNumberTweets.append(1)
    elif longitudeValue >= -115.236428 and longitudeValue < -101.99889 and latitudeValue < 49.189787 and latitudeValue > 24.660845:
        mountainTimeZoneListNumberTweets.append(1)
    elif longitudeValue >= -125.242264 and longitudeValue < -115.236428 and latitudeValue < 49.189787 and latitudeValue > 24.660845:
        pacificTimeZoneListNumberTweets.append(1)

#this function checks the name of the file and to see if it is the keywords file
def inputCheckKeywords (filename):
    try:
        openKeywords = open(filename, "r")
    except IOError as e:
            print(e.strerror)
            exit()
#this function checks the name of the file and to see if it is the tweets file
def inputCheckTweets (filename):
    try:
        openTweets = open(filename, "r")
    except IOError as e:
            print(e.strerror)
            exit()

#--------------------------------------------------------------------------------------------------
#FILE CHECK AND OPEN

#asks user for input and runs a function to verify it the file name is correct
userInputKeywords = input("Please enter the name of the file containing the keywords.")
inputCheckKeywords(userInputKeywords)#runs function to check file name

userInputTweets = input("Please enter the name of the file containing the tweets.")
inputCheckTweets(userInputTweets)#runs function to check file name

#I chose to calculate everything after receiving the files because it made the code cleaner.

#learned about this method of opening files after creating most of the code, thats why the format is different
#than in the code. this is checks for the number of lines in the tweet file
with open('tweets.txt') as f:
   sizeTweets=sum(1 for _ in f)

with open('keywords.txt') as f:
   sizeKeywords=sum(1 for _ in f)

#opens the files the boring way
openKeywords = open("keywords.txt", "r")
openTweets = open("tweets.txt", "r") # Assign a variable to be able to call the tweet txt file.

#------------------------------------------------------------------------------------------------
#PREPARING KEYWORDS AND LATITUDE/LONGITUDE VALUES
for keywordsLine in openKeywords:
    keywordAndNumberSplit = keywordsLine.split(",") #Splits the keywords and the number
    keyWord = keywordAndNumberSplit[0] #The first element of the keyword and number is the keyword
    keyNumber = keywordAndNumberSplit[1] #The second element of the keyword and number is the number
    listOfKeywords.append(keyWord) #Adds the keyword to a one list
    listOfPrimaryScoreValues.append(keyNumber) #Adds the number to another list

#With the above, I have the one list for all my keywords and one list for all my primary values and at index one
#in both lists the keyword is matched with its value.

#---------------------------------------------------
#DATA COLLECTION

#main loops that collects data
for i in range(sizeTweets):
    #this sequence below reads the line, splits it, makes it all lower case, and removes any puncutation
    line = openTweets.readline()
    lineSplitIntial = line.split()
    lineSplit = [x.lower() for x in lineSplitIntial]
    lineSplit = [''.join(c for c in s if c not in punctuation) for s in lineSplit]

    #values that get reset for each loops, otherwise answers would be compounded
    keyWordsInATweet = 0
    counter = 0
    hapValueListTotal = 0
    happinessScoreSingleStorage = 0
    hapValueCurrent = 0

    #this loops splits the keywords and checks which zone it belongs and adds the number of tweets with a
    #happiness score greater than 0 for each region
    for i in range(sizeKeywords): # this case covers all 53 keywords
        if listOfKeywords[i] in lineSplit: #checks to see if the first keyword is in the first line and reiterates
            counter = counter + 1
            hapValueCurrent = longitudeValueCheck((float(cleanUpLongitude(lineSplit))),(float(cleanUpLatitude((lineSplit)))))
            keyWordsInATweet = keyWordsInATweet + 1
            hapValueListTotal = int(hapValueListTotal) + int(hapValueCurrent)
        else:
            counter = counter + 1

    #this checks b/c a divisible by 0 error occurs that means that keywords in a tweet was 0.
    #this if here also makes sure to see if the tweet has 0 keywords then list(third line does that)
    #also checks to see if theres 1 keyword that has a score of 1, which should be counted and is
    if keyWordsInATweet != 0 or keyWordsInATweet == 1:
        happinessScoreSingleStorage = hapValueListTotal/keyWordsInATweet
        numberOfTweetInRegionCheckAndHapScoreTotalCalc((float(cleanUpLongitude(lineSplit))),(float(cleanUpLatitude((lineSplit)))))
#---------------------------------------------------
#PROCESSING COLLECTED DATA

#one tweet represents one index so I find the length of the list
pacificTimeZoneTweetsFinal = len(pacificTimeZoneListNumberTweets)
mountainTimeZoneTweetsFinal = len(mountainTimeZoneListNumberTweets)
centralTimeZoneTweetsFinal = len(centralTimeZoneListNumberTweets)
easternTimeZoneTweetsFinal = len(easternTimeZoneListNumberTweets)

#removes \n from the list
pacificTimeZoneHappinessScorePreFinal = [(el.strip()) for el in pacificTimeZoneListHapScoreTotal]
mountainTimeZoneHappinessScorePreFinal = [(el.strip()) for el in mountainTimeZoneListHapScoreTotal]
centralTimeZoneHappinessScorePreFinal = [(el.strip()) for el in centralTimeZoneListHapScoreTotal]
easternTimeZoneHappinessScorePreFinal = [(el.strip()) for el in easternTimeZoneListHapScoreTotal]

#adds all happiness scores of each and every single tweet that has one and that is in the given region
for k in range(len(pacificTimeZoneHappinessScorePreFinal)):
    pacificTimeZoneHappinessScoreFinal = int(pacificTimeZoneHappinessScorePreFinal[k]) + pacificTimeZoneHappinessScoreFinal

for k in range(len(mountainTimeZoneHappinessScorePreFinal)):
    mountainTimeZoneHappinessScoreFinal = int(mountainTimeZoneHappinessScorePreFinal[k]) + mountainTimeZoneHappinessScoreFinal

for k in range(len(centralTimeZoneHappinessScorePreFinal)):
    centralTimeZoneHappinessScoreFinal = int(centralTimeZoneHappinessScorePreFinal[k]) + centralTimeZoneHappinessScoreFinal

for k in range(len(easternTimeZoneHappinessScorePreFinal)):
    easternTimeZoneHappinessScoreFinal = int(easternTimeZoneHappinessScorePreFinal[k]) + easternTimeZoneHappinessScoreFinal

#rounds the happiness score for each region to 3 decimal places as required
pacificTimeZoneHappinessScoreFinal = round(pacificTimeZoneHappinessScoreFinal/(len(pacificTimeZoneHappinessScorePreFinal)),3)
mountainTimeZoneHappinessScoreFinal = round(mountainTimeZoneHappinessScoreFinal/(len(mountainTimeZoneHappinessScorePreFinal)),3)
centralTimeZoneHappinessScoreFinal = round(centralTimeZoneHappinessScoreFinal/(len(centralTimeZoneHappinessScorePreFinal)),3)
easternTimeZoneHappinessScoreFinal = round(easternTimeZoneHappinessScoreFinal/(len(easternTimeZoneHappinessScorePreFinal)),3)

#------------
#DISPLAYING OUTPUT

print("The average happiness score per tweet in the pacific timezone was {} and there were {} total tweets in this region.".format(pacificTimeZoneHappinessScoreFinal,pacificTimeZoneTweetsFinal))
print("The average happiness score per tweet in the mountain timezone was {} and there were {} total tweets in this region.".format(mountainTimeZoneHappinessScoreFinal,mountainTimeZoneTweetsFinal))
print("The average happiness score per tweet in the central timezone was {} and there were {} total tweets in this region.".format(centralTimeZoneHappinessScoreFinal,centralTimeZoneTweetsFinal))
print("The average happiness score per tweet in the eastern timezone was {} and there were {} total tweets in this region.".format(easternTimeZoneHappinessScoreFinal,easternTimeZoneTweetsFinal))

#closing the files
openTweets.close()
openKeywords.close()

#------------------
#GRAPHICS

from happy_histogram import drawSimpleHistogram

drawSimpleHistogram(easternTimeZoneHappinessScoreFinal,centralTimeZoneHappinessScoreFinal,mountainTimeZoneHappinessScoreFinal,pacificTimeZoneHappinessScoreFinal)
#values given in order of eastern, central, mountain, and pacific and specified.
#--------------

#THE END!


