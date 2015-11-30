#### Naive Bayes Spam Filter
#### Christopher To, Nathan Wikle, Valerie Free
#### 11/30/2015
#### Uses naive Bayesian statistics to develop a spam
#### knowledge base and classify emails as spam or ham

import string
import re
import math
import os
import glob

### naive bayesian spam filter that uses a self-developed knowledge base 
### to classify emails as spam or ham
class SpamFilter(object):

  ## initialize and train the spam filter
  ## spamD, hamD are parameters for directory of training emails
  ## evalD lists the directory of emails to be trained.
  def __init__(self):
    # constant variables used for clarifying indexes
    self.SPAM = 0
    self.HAM = 1
    self.CORRECT = 0
    self.INCORRECT = 1
    
    # dictionary of tuples that maps words to their occurrences in 
    # spam and ham emails
    self.d = {}

    # tuple that holds the number of spam and ham emails used for training
    self.emailsTrained = [0, 0]

    # tuple that holds the number of individual occurrences of spam and ham 
    # words in the training emails
    # *technically derivable information, but derivation time can be massive
    # based on knowledge base size and number of emails to classify
    self.labelTotal = [0, 0]

    # tuple of tuple that holds the totals of spam and ham emails classified
    # correctly or incorrectly. The first tuple is for correct classifications,
    # and the second tuple is for incorrect classifications.
    # Refer to the constant indexes for clarification.
    self.accuracy = [ [0, 0], [0, 0] ]
    
  ## adds a labeled email to the spam filter's training knowledge base
  def train(self, filename, label):
    
    # open file and parse words into a set
    try:
      file = open(filename)
      emailSet = set(file.read().split())
      file.close()
    except:
      # print(filename + " not found.")
      return

    # add each word to the correct label category
    for word in emailSet:
      
      strippedWord = word
      # check if there are alphanumeric characters in string
      #if re.search('\w+', strippedWord):
        # remove all punctuation, capitalization, and spaces from word
      strippedWord = word.strip(" " + string.punctuation).lower()

      # ignore punctuation that was stripped to spaces
      if strippedWord == "":
        continue

      # initialize the word tuple if not yet seen by the filter.
      if strippedWord not in self.d:
        self.d[strippedWord] = [0, 0]

      # increment the word occurrence count for the given label
      self.d[strippedWord][label] += 1

      # increment the label training occurrence count
      self.labelTotal[label] += 1

  ## calls the training method across all emails in the specified directory
  ## for the specified label
  def bulkTrain(self, spamDirectory = "./spam", hamDirectory = "./ham"):
    # keep track of number of emails used for training
    emailsTrained = 0

    # train filter to recognize spam words
    for filename in glob.glob(os.path.join(spamDirectory, '*txt')):
      self.train(filename, self.SPAM)
      self.emailsTrained[self.SPAM] += 1
      emailsTrained += 1

    # train filter to recognize ham words
    for filename in glob.glob(os.path.join(hamDirectory, '*txt')):
      self.train(filename, self.HAM)
      self.emailsTrained[self.HAM] += 1
      emailsTrained += 1

    print("Numbers of emails used for training: " + str(emailsTrained))


  ## function to calculate the probability that the given words are in 
  ## a specific class
  def probability(self, words, label):
    # find the probability of the given category (i.e., number of label emails 
    # divided by total number of emails)
    labelTotal = self.emailsTrained[label]
    emailsTrainedTotal = self.emailsTrained[self.SPAM] + self.emailsTrained[self.HAM]
    labelProbability = float(labelTotal/emailsTrainedTotal)

    # calculate and take the log of the prior probability
    score = math.log(labelProbability) 
    for w in words:
      # calculate the conditional probability for each word
      denominator = self.labelTotal[label] + len(self.d)
      if(not w in self.d):
        score = score + math.log(1/denominator)
      else:
        score = score + math.log((self.d[w][label] + 1)/denominator)
    return score

  ## classifies an individual email based
  def classify(self, filename, printOutput = False, testAccuracy = True):

    try:
      # open file and parse words into a set
      file = open(filename)
      emailSet = set(file.read().split())
      file.close()
    except:
      return
      
    # calculate the probability that the email is spam or ham
    probabilitySpam = self.probability(emailSet, self.SPAM)
    probabilityHam = self.probability(emailSet, self.HAM)
    classifySpam = False
    if(probabilitySpam > probabilityHam):
      classifySpam = True

    # if desired, print the classification output
    if(printOutput):
      self.printClassification(filename, classifySpam)

    # if desired, evaluate whether classification was correct
    # for testing, spam emails have spam or spm in their file name
    if(testAccuracy):
      actualSpam = False
      if("spam" in filename or "spm" in filename):
        actualSpam = True

      correct = (classifySpam == actualSpam) 
      self.accuracy[not correct][not actualSpam] += 1

  ## attempts to classify all emails in a given directory
  def bulkClassify(self, bulkDirectory = "./evaluation"):

    # keep track of number of emails classified
    emailsClassified = 0

    for filename in glob.glob(os.path.join(bulkDirectory, '*txt')):
      self.classify(filename, False)
      emailsClassified += 1

    print("Number of emails classified: " + str(emailsClassified))

    # print the accuracy of the resulting classifications
    self.printAccuracy()

  ## helper method to print out whether a classification was correct or not
  def printClassification(self, filename, isSpam):
    if(isSpam):
      print(filename + " is spam.")
    else:
      print(filename + " is ham.")

  ## print a report of the spam filter's accuracy
  def printAccuracy(self):
    spamPercentCorrect = self.accuracy[self.CORRECT][self.SPAM] / (
      self.accuracy[self.CORRECT][self.SPAM] + self.accuracy[self.INCORRECT][self.SPAM])
    hamPercentCorrect = self.accuracy[self.CORRECT][self.HAM] / (
      self.accuracy[self.CORRECT][self.HAM] + self.accuracy[self.INCORRECT][self.HAM])

    print("Spam classified correctly: " + str(self.accuracy[self.CORRECT][self.SPAM]))
    print("Spam classified incorrectly: " + str(self.accuracy[self.INCORRECT][self.SPAM]))
    print("Ham classified correctly: " + str(self.accuracy[self.CORRECT][self.HAM]))
    print("Ham classified incorrectly: " + str(self.accuracy[self.INCORRECT][self.HAM]))

    print("Percentage of emails correctly classified:")
    print("Spam: " + str(spamPercentCorrect))
    print("Ham:  " + str(hamPercentCorrect))

  ## print out dictionary for testing purposes
  def printDictionary(self):
    print(self.d)

  ## reset accuracy values (for demonstration purposes)
  def resetAccuracy(self):
    self.accuracy = [ [0, 0], [0, 0] ]
    print("Accuracy has been reset!")
