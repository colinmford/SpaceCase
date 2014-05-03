# spaceCase - v2 - jackson@okaytype.com
# to do: change button label to show next state: "OK" -> "Ok" -> "ok"
#

from mojo.UI import CurrentSpaceCenter
from mojo.events import addObserver
from vanilla import *

class AddButtonToSpaceCenter:
 
    def __init__(self):
        
        addObserver(self, "myObserver", "spaceCenterDidOpen")

    def myObserver(self, sender):

        sp = CurrentSpaceCenter()

        print dir(sp.top)

        l, t, w, h = sp.top.glyphLineInput.getPosSize()
        sp.top.glyphLineInput.setPosSize((l, t, w - 37, h))

        l, t, w, h = sp.top.glyphLineAfterInput.getPosSize()
        sp.top.glyphLineAfterInput.setPosSize((l - 37, t, w, h))

        sp.myButton = Button((-134, 10, 33, 22), "OK", callback=self.spaceCase, sizeStyle="small")
    
    def spaceCase(self, sender):

        sc = CurrentSpaceCenter().getRaw()
        
        if sc.isupper(): CurrentSpaceCenter().setRaw(sc.title())
        elif sc.istitle(): CurrentSpaceCenter().setRaw(sc.lower())
        elif sc.islower(): CurrentSpaceCenter().setRaw(sc.upper())
        else: CurrentSpaceCenter().setRaw(sc.upper())
 

AddButtonToSpaceCenter()