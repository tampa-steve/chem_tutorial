class Chem:
    def __init__(self, atomWt, name, total):      
        self.name = name
        self.atomWt = atomWt
        self.total = total
        
    def atomName(self):
        print "Element name %s" % name   
        
    def propInfo(self):
        print "Atomic weight %d" % atomWt
        print "Total %s" % total
        
    def displayElement(self):
        print "Element Name =", self.name, ", Atomic weight =", self.atomWt, ",Total elements =", self.total

    def displaygetAttr(self):
        print "Atomic weight2 =", self.atomWt

chem1 = Chem(39, "potassium",1)
chem2 = Chem(40, "calcium",2)
#edit attribute info.
chem1.atomWt = 39.10 
chem2.atomWt = 40.08
#displays attributes given above.
chem1.displayElement()
chem2.displayElement()
#use the attribute function.
chem1.displaygetAttr()
getattr(chem1,"atomWt")    
        
      
    
