from django.shortcuts import render
from django.http import HttpResponse

from textblob import TextBlob

text1 = TextBlob("Today is a great day, but it is boring")
sentiments = text1.sentiment.polarity

def index(request):
    return HttpResponse("Today is a great day, but it is boring\n"+str(sentiments))
