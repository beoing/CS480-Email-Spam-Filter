# to run: create the object, bulk train it, then classify a directory
# by default parameters, it uses the ./spam, ./ham, and ./evaluation
# directories, but you can specify your own.  

from spamfilter import *

sf = SpamFilter()

# commands done in presentation
# assumes all appropriate directories are in one level above

sf.bulkTrain("../spamEnron", "../hamEnron")
sf.bulkClassify("../evaluationEnron")
sf.resetAccuracy()
sf.bulkClassify("../evaluationLing")
sf.resetAccuracy()
sf.bulkTrain("../spamLingPartial","../hamLingPartial")
sf.bulkClassify("../evaluationLing")
sf.resetAccuracy()
sf.bulkTrain("../spamLingRest","../hamLingRest")
sf.bulkClassify("../evaluationLing")
sf.resetAccuracy()

