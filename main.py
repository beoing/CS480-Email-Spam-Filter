# main.py - demonstration of spamfilter.py
# to run: create the object, bulk train it, then classify a directory
# by default parameters, bulkTrain uses the ./spam and ./ham directories,
# and bulkClassify uses the ./evaluation directory, but you can specify your own
from spamfilter import *

sf = SpamFilter()

# example
# train using emails in ./spam and ./ham
# sf.bulkTrain() 
# classify emails in ./evaluation
# sf.bulkClassify()

# commands done in presentation
# assumes all appropriate directories are in one level above

##sf.bulkTrain("../spamEnron", "../hamEnron")
##sf.bulkClassify("../evaluationEnron")
##sf.resetAccuracy()
##sf.bulkClassify("../evaluationLing")
##sf.resetAccuracy()
##sf.bulkTrain("../spamLingPartial","../hamLingPartial")
##sf.bulkClassify("../evaluationLing")
##sf.resetAccuracy()
##sf.bulkTrain("../spamLingRest","../hamLingRest")
##sf.bulkClassify("../evaluationLing")
##sf.resetAccuracy()
