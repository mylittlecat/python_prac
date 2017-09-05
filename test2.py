#!/usr/bin/env python
import math
for eachNum in (.2,.7,1.2,1.7,-.2,-.7,-1.2,-1.7):
    print "int(%lf)\t%+lf" % (eachNum,float(int(eachNum)))
    print "floor(%lf)\t%+lf" % (eachNum,math.floor(eachNum))
    print "round(%lf)\t%+lf" % (eachNum,round(eachNum))
    print  '-'*20

