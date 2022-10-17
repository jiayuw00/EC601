# Project2 Twitter Analyzer

## Run the code
Firstly, open twitter.py. Replace the consumer_key, consumer_secret, access_token, access_token_secret with your own keys;

```
consumer_key ='Your API key/consumer key'
consumer_secret = 'Your secret API key/ consumer key'
access_token = 'Your access token'
access_token_secret = 'Your secret access token'
```

Run ``` $ python twitter.py;```

Set up Google environment and install Google API(https://github.com/googleapis/google-api-python-client);

Wait for the process to be done. You should see a new folder named "result" created containing 25 text files titled with city names;

After the folder is successfully created, run ```$ python nlp.py;```

Finally, you will get a text file named "result.txt" containing a list of 10 cities.


## Product mission

This project aims to get the most welcome cities in the US for a short trip by analyzing the tweets. I list cities ranked from the most positive to the least in the overall sentiment of all related text tweet content.

## MVP

The project retrieves user tweets and performs sentiment analysis. It provides the top 10 favorite US cities for a short trip using google sentiment analysis on the popular and real-time related Tweets.

## User stories

I, as a user, want to know what are the most welcome cities in the US for a short trip to get the best experience.

I, as a travelling agnecy, want to know the popularity rank of the tourist destinations, so that I can arrange tourism products accordingly.