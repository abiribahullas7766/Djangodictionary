from multiprocessing import context
from django.shortcuts import render
from PyDictionary import PyDictionary

import dictionary
# Create your views here.

def homeView(request):
    return render(request,'dictionary/index.html')


def searchView(request):
    #capturing the word from the form via the name search

    word=request.GET.get('search')
    #creating a dictionary object
    dictionary=PyDictionary()
    #passing a word to the dictionary object
    meanings=dictionary.meaning(word)

    #getting a synonym and antonym
    synonyms=dictionary.synonym(word)
    antonyms=dictionary.antonym(word)

    #building all the variable in the context
    context={
        'word':word,
        'meanings':meanings,
        'synonyms':synonyms,
        'antonyms':antonyms
    }



    return render(request,'dictionary/search.html',context)