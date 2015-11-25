
from spamfilter import *

sf = SpamFilter()
#sf.bulkTrain()
#sf.bulkTrain("./test","./test")
sf.bulkTrain("../spamEnron", "../hamEnron")
#sf.bulkTrain("../spamLing2","../hamLing2")
#sf.bulkTrain("../spamLing","../hamLing")
#sf.bulkClassify()
sf.bulkClassify("./evaluationLing")


