class person:
    def __init__(self,height,weight):
        self.he=height
        self.we=weight
    def getHeight(self):
        print(self.he)
        print(self.we)

p=person(1.73,120)
p.getHeight()