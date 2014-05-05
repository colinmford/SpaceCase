# spaceCase - v3 - jackson@okaytype.com
#

from mojo.UI import CurrentSpaceCenter
from mojo.events import addObserver
from vanilla import *

class AddButtonToSpaceCenter:
 
    def __init__(self):
        
        addObserver(self, "myObserver", "spaceCenterDidOpen")

    def myObserver(self, sender):

        sp = CurrentSpaceCenter()

        #print dir(sp.top)

        l, t, w, h = sp.top.glyphLineInput.getPosSize()
        sp.top.glyphLineInput.setPosSize((l, t, w - 37, h))

        l, t, w, h = sp.top.glyphLineAfterInput.getPosSize()
        sp.top.glyphLineAfterInput.setPosSize((l - 37, t, w, h))

        sp.myButton = Button((-134, 10, 33, 22), "OK", callback=self.spaceCase, sizeStyle="small")
    
    def spaceCase(self, sender):
        
        sp = CurrentSpaceCenter()
        sc = sp.getRaw()
        
        if sc.isupper(): self.setCase(sp, 'title')
        elif sc.istitle(): self.setCase(sp, 'lower')
        elif sc.islower(): self.setCase(sp, 'upper')
        else: self.setCase(sp, 'upper')
        
    def setCase(self, sp, case):
        sc = sp.getRaw()
        title = sp.myButton.getTitle()
        
        sp.setRaw(getattr(sc, case)())
        sp.myButton.setTitle(getattr(title, case)())
        
AddButtonToSpaceCenter()
