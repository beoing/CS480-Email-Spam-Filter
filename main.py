# to run: create the object, bulk train it, then classify a directory
# by default parameters, it uses the ./spam, ./ham, and ./evaluation
# directories, but you can specify your own.  

from spamfilter import *

sf = SpamFilter()
#sf.bulkTrain()
#sf.bulkTrain("../spamEnron", "../hamEnron")
#sf.bulkTrain("../spamLing2","../hamLing2")
#sf.bulkTrain("../spamLing","../hamLing")
sf.bulkClassify()
#sf.bulkClassify("./evaluationLing")
sf.bulkClassify()
