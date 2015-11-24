
from spamfilter import *

mySpamFilter = SpamFilter()
mySpamFilter.bulkTrain()
mySpamFilter.bulkClassify()
# large corpuses
#mySpamFilter.bulkTrain("./spamEnron", "./hamEnron")
#mySpamFilter.bulkClassify("./evaluationEnron")


