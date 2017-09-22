glb_TTT = None
def initTTT():
    global glb_TTT
    glb_TTT = TTT()

def get_TTT():
    global glb_TTT
    return glb_TTT
class TTT(object):
    def hi(self):
        print "hi!"
