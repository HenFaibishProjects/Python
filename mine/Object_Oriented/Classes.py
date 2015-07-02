import math,random

class Books(object):
 count1=0 # Class Verible (inside the class but outside all methods)

 def __init__(self,id,name,price):
   self.i = id
   self.n = name
   self.p = price

 def printid(self):
     print "The ID number of book named" , self.n   , "is" , self.i , "and the price is" , self.p , "Dollars"

book1 = Books("001","Pride",55)
book2 = Books("002","Gone With The Wind",75)
book3 = Books("003","Animal Farm",85)

book1.printid()
book2.printid()
book3.printid()

