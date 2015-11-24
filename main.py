
from spamfilter import *

mySpamFilter = SpamFilter()
mySpamFilter.bulkTrain()
#mySpamFilter.bulkTrain("../spamEnron", "../hamEnron")
mySpamFilter.bulkClassify()
#mySpamFilter.bulkClassify("./evaluationLing")


