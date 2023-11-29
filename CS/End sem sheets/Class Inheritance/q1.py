class news:

    def __init__(self,agencyname):
        self.agencyname = agencyname
        self.totalpublications=0
        self.listofpublications=[]
        self.totalviewssofar=0
    def addview(self,article):
        self.totalviewssofar+=int(article.Views)
        self.totalpublications+=1
        self.listofpublications.append(article.title)

class Article:
    def __init__(self,title,dateofpublications,dayHHMM,Views,Agency):
        self.title= title
        self.dateofpublications = dateofpublications
        self.dayHHMM = dayHHMM
        self.Views = Views
        self.Agency = Agency
a1=Article("a","29/11/23","g",45,"A")
a2=Article("b","30/11/23","h",55,"B")
n=news("A")
n.addview(a1)
n1=news("B")
n1.addview(a2)
print (n.listofpublications)
print(n1.listofpublications)