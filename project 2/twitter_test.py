from TwitterSearch.TwitterSearch import *
import time
import os
import csv
import pytest

consumer_key = "***************"
consumer_secret = "************"
access_token = "***************"
access_token_secret = "********"

# check to see if input file is valid
def test_connect_file():
    f = open("USCities.txt", "r")
    cities = f.read().splitlines()
    if cities is not None:
        print("Valid input file")
    else:
        print("INVALID input file")


def test_retrieve():
    assert retrieve() is not None


def retrieve():
    tso = TwitterSearchOrder()
    tso.set_keywords(["#travel", "#holiday", "#vacation"], or_operator=True)
    tso.add_keyword("boston")
    tso.set_language("en")
    tso.set_count(100)
    tso.set_result_type("mixed")
    tso.set_include_entities(False)

    ts = TwitterSearch(consumer_key, consumer_secret, access_token, access_token_secret)

    return ts


def test_error():
    try:
        tso = TwitterSearchOrder()
        tso.set_keywords(["#travel", "#holiday", "#vacation"], or_operator=True)
        tso.add_keyword("Cambridge")
        tso.set_language("en")
        tso.set_count(100)
        tso.set_result_type("mixed")
        tso.set_include_entities(False)

        ts = TwitterSearch(consumer_key, consumer_secret, access_token, access_token_secret)
    except (TwitterSearchException(ts.exceptions[400])) as e:
        raise TwitterSearchException(ts.exceptions[400].message)