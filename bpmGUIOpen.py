__author__ = 'jabedude'

import Tkinter
from Tkinter import *
import tweepy
import webbrowser


top = Tkinter.Tk()
var = StringVar()
label = Label(top, textvariable = var, relief = RAISED)
def playSong():
    auth = tweepy.OAuthHandler('consumer key here','consumer secret here')
    auth.set_access_token('access token here','access token secret here')
    api = tweepy.API(auth)
    bpmTwit = api.user_timeline('bpm_playlist')
    for tweet in bpmTwit:
        textTweet = str(tweet.text)
        newtextTweet = textTweet.replace("playing on #BPM - @sxmElectro", "")
        var.set(newtextTweet)
        label.pack()
        #print newtextTweet
        webbrowser.open("https://www.youtube.com/results?search_query="+newtextTweet)
        break


B = Tkinter.Button(top, text ="Next Song", command = playSong)
top.wm_title("BPM Ripper V0.7")
top.minsize(width=400, height=150)
B.pack()
top.mainloop()
