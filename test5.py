#!/usr/bin/env python
def dictVarArgs(arg1,arg2='defaultB',**theRest):
    'display 2 regular args and keyword variable args'                 
    print 'formal arg1:',arg1                                          
    print 'formal arg2:',arg2                                          
    for eachXtrArg in theRest.keys():
        print 'Xtra arg %s: %s' % (eachXtrArg,str(theRest[eachXtrArg])) 

dictVarArgs(1220,740.0,c='grail')
dictVarArgs(arg2='tales',c=123,d='poe',arg1='mystery')
dictVarArgs('one',d=10,e='zoo',men=('freud','gaudi'))

def newfoo(arg1,arg2,*nkw,**kw):
    'display regular args and all variable args'
    print 'arg1 is:',arg1
    print 'arg2 is:',arg2
    for eachNKW in nkw:
        print 'additional non-keyword arg:',eachNKW
    for eachKW in kw.keys():
        print "additional keyword arg '%s': %s" % (eachKW,kw[eachKW])
newfoo('wolf',3,'projects',freud=90,gamble=96)
newfoo(10,20,30,40,foo=50,bar=60)
newfoo(2,4,*(6,8),**{'foo':10,'bar':12})
aTuple=(6,7,8)
aDict={'z':9}
newfoo(1,2,3,x=4,y=5,*aTuple,**aDict)
