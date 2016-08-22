__author__ = 'Alex'

import time
import os
import webbrowser
import speech_recognition as sr
import copy
import feedparser
import linecache

global function, Arg, userenter
global Lastsentence




runfunctlist = {"v"}

#ASCII ART
def Titlecard():

    print("FFFFFFFFFFF  RRRRRRRRRR   IIIIIIIIII  DDDDDDDDD       AAAAAAAA    YY       YY")
    print("F            R         R      II      D        D     A        A    YY     YY")
    print("F            R         R      II      D         D   A          A    YY   YY")
    print("FFFFFFFFF    RRRRRRRRRR       II      D          D  A          A      YYY")
    print("F            RR RRR           II      D          D  AAAAAAAAAAAA       Y")
    print("F            RR   RR          II      D         D  A            A      Y")
    print("F            RR    RR         II      D        D   A            A      Y")
    print("F            RR     RR    IIIIIIIIII  DDDDDDDDD    A            A      Y\n")


#PROCESSING/DEBUG FUNCTIONS
def expand(term):
  if term=="Q":
      return "Question"

  if term=="C":
      return "Command"

  if term=="S":
      return "Statement"

def fetchtype(word):
    firstletter=word[0]
    #print(word,"--  Word lookup failed. I am too beta rn\n")


#FRIDAY SPECIAL FUNCTIONS

def Google(Arg):
    webbrowser.open_new_tab("http://www.google.com/search?q=" + Arg)
    print("Webpage Opened")
    return 0

def Friday(Arg):
    print("Hi guys")


def Voice(Arg):
    Voiceinput()


functionList = {"Google": Google, "Friday": Friday, "v": Voice}


#Main Task FUNCTIONS




def Command(sentence):
    print("OMG a command!!")
    firsttwo=sentence[0]+sentence[1]

    if sentence[0]=="Search" or sentence[0]=="search":
        print("Im doing a  web search m8")
        websearch(sentence)
    if sentence[0]+sentence[1]=="look up":
        print("Doing a lookup")


def KATRSScheck(RSS):

    d = feedparser.parse(RSS)


    print("Latest entry\n",d["entries"][0]["title"],"-",d["entries"][0]["link"])

    lastdate=linecache.getline("DCWEEKRSS.txt", 1)
    lastdate=lastdate[:-1]
    #print(lastdate)



    if str(d.entries[0].updated)!=lastdate:
        print("New entry, adding torrent")
        with open('DCWEEKRSS.txt', 'w') as file:
            file.writelines(d.entries[0].updated)
        magnet=d.entries[0].torrent_magneturi
        webbrowser.open_new_tab(magnet)





def websearch(sentence):
    searchsites={"Google", "KAT", "Kickasstorrents","The pirate bay","Iso hunt","Amazon"}
    searchtypes=["pictures","torrent","torrents","videos","Videos"]
    ran=False


    key=copy.copy(sentence)
    contype="Null"
    site="Null"
    backways=False

    ###############################################################################################FIND SITE
    if sentence[1].title() in searchsites:    ##In list??
        Type=1
        site=sentence[1]
        print("website supported")
        supported=True

    elif sentence[-1].title() in searchsites:         ##Backways??/List
        site=sentence[-1]
        backways=True
        supported=True

    if sentence[1]=="the":

        if sentence[2]=="Internet" or sentence[2]=="internet":
            print("global search")
            supported=True
            site="internet"
            del key[2]
            key[1]="the internet"
            print(key)



        if sentence[2]=="piratebay" or (sentence[2]=="Pirate" and sentence[4]=="Bay"):
            print("Pirate bay is in list")
            site="the pirate bay"
            print(site)
            key=key[3:]
            term=" ".join(key)
            searchTPB(term)
            ran=True

    if sentence[1]=="KickassTorrents":
        site="Kickasstorrents"

    if sentence[1]=="kickass" and sentence[2]=="torrents":
        del key[2]
        key[1]=="Kickasstorrents"
        site="Kickasstorrents"

    ###########################################################################################


    if key[2]=="for" and backways==False:

        if key[3]=="a":
            del key[3]
            print("deleted an a.. key=",key)

        if key[3] in searchtypes:
            contype=key[3]
            print("in type list!!")
            key=key[5:]
            term= " ".join(key)




        else:
            key=key[3:]
            term=" ".join(key)




    print("Search Local>>>",site,"Type>>>",contype,"Term>>>",term)

    if ran==False:

        if supported:


            if site=="Google":
                searchGoogle(contype,term)

            elif site=="the pirate bay":
                searchTPB(term)

            elif site=="internet":
                searchglobal(contype,term)

            elif site=="Kickasstorrents":
                searchKAT(term)
            #elif
            #REST OF WEBSITES IN LIST
            #


        else:
            term=sentence[1]+":"+term
            Google(term)

        if backways==True:
            print("ARGGH backways not programmed")


def Runfunct(userenter):
    print(">>>Runfunct")
    print(">>>userenter")
    function=userenter
    if "." in userenter:
        function, Arg= userenter.split('.',1)
        parameters = Arg
        ###TODO Get run command!!

    if userenter=="v":
        Voiceinput()


    else:
        print("Syntax not in functionList....")


def Input():
    userenter=input("Type Here:   \n")
    print("\n")
    sentence= userenter.split()
    print(sentence)
    if "?" in userenter:
        print(">>>Question")
        Casualdeconstruct(userenter)

    elif len(sentence)<2:
        Runfunct(userenter)



    else:
        print(">>>Casual")
        Casualdeconstruct(userenter)


def Voiceinput():
    speech=0
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now")
        audio = r.listen(source)



    # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
        #    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
            speech= r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return 1

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


    sentence=speech.split()                             ##TODO This line errors if there is no internet connection
    #print(sentence)
    firstword=sentence[0]
    #print(firstword)


    if firstword[-1]==".":
        sentence[0]
        x=1
        funct=sentence[0]

        while x < len(sentence):
            funct=funct+sentence[x]
            x+=1

        print("Funct>>> ",funct)
        Runfunct(funct)

    else:
        print(">>>Casual")
        Casualdeconstruct(speech)


def searchGoogle(type,term):
    if type=="Null":
        webbrowser.open_new_tab("http://www.google.com/search?q=" + term)
        print("Webpage Opened")

    elif type=="pictures":
        webbrowser.open_new_tab("http://www.google.com/search?tbm=isch&q=" + term)

    else:
        pass


def searchTPB(term):
    webbrowser.open_new_tab("https://ukpirate.org/s/?q=" + term)
    print("Webpage Opened")

def searchKAT(term):
    webbrowser.open_new_tab("https://kickass.unblocked.li/usearch/" + term)


def searchglobal(type,term):
    if type=="Null":                                                                ##needs to inference best search location from term
        webbrowser.open_new_tab("http://www.google.com/search?q=" + term)
        print("Search Opened")

    elif type=="pictures":
        webbrowser.open_new_tab("http://www.google.com/search?tbm=isch&q=" + term)
        print("Seach Opened")

    elif type=="torrent" or type=="torrents":
        webbrowser.open_new_tab("https://isohunt.to/torrents/?ihq=" + term)




def Casualdeconstruct(userenter):
    sentence= userenter.split()
    numofwords=len(sentence)
    print(">>>Sentence:",sentence)
    print (">>>",numofwords,"Words")

    for x in sentence:
        fetchtype(x)
        #print (x)



    if "?" in userenter:
        Lv1="Q"
        #print(">>>",Lv1)
    else:
        Command(sentence)

    #if sentence[0] == "Friday":
    #    Lv1="C"
    #    print(">>>",Lv1)
    #    command()



    #else:
    #    Lv1="S"
    #    print(">>>",Lv1)
    #    exit()





while True:

    Titlecard()
    #Input()
    Voiceinput()
    #print("btw, last sentence was """,lastsentence)
##web Deamons

    #KATRSScheck("https://kickass.unblocked.li/usearch/%22DC%20Week%2B%22/?rss=1.xml")
    time.sleep(2)
    print("Press any to continue")
    stop=input()

    os.system("cls")



#TODO ADD DICTIONARY LOOKUP