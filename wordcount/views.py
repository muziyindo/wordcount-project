#We must include this, it allows us return response via http
from django.http import HttpResponse

#import this module to be able to render an html page
from django.shortcuts import render


#we must put a request parameter in every function defined in djangoproject
def home(request):
    return render(request,'home.html',{'hithere':'this is me'}) #must parse thr request arguement

'''
def eggs(request):
    return HttpResponse('Eggs are great')
'''

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split() #split text into word list i.e array

    worddictonary = {} #declaring an empty dictionary

    for word in wordlist:
        if word in worddictonary:
            #increase
            worddictonary[word] += 1
        else:
            worddictonary[word] = 1

    #print (wordlist) #to show in command prompt
    #worddictonary.items() returns a sequence of tuple e.g ((james,2),(friend,3))
    return render(request,'count.html',{'fulltext_':fulltext,'count':len(wordlist),'worddictionary_':worddictonary.items()}) #pARSING FULL TEXT TO html page again

def about(request):
    return render(request,'about.html',{'title':'Welcome To About Page'})
