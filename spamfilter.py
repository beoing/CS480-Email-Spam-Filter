# spamfilter.py
# A program to filter spam

import string
import os
import glob
import math

global d
global cat_total

def train(filename, label):
  global d
  global cat_total
  file = open(filename)
  emailstring = file.read()
  emaillist = emailstring.split()
  emailset = set(emaillist)
  if label=="spam":
    for word in emailset:
      strippedword = word.strip(" " + string.punctuation).lower()
      if strippedword in d:
        d[strippedword][0]+=1
      else:
        d[strippedword]=[1, 0]
  else:
    for word in emailset:
      strippedword = word.strip(" " + string.punctuation).lower()
      if strippedword in d:
        d[strippedword][1]+=1
      else:
        d[strippedword]=[0, 1]

  file.close()

def main():
  ham_word_count = 0
  spam_word_count = 0

  global cat_total

  cat_total = [0,0]
  global d
  d = {}


  path = "./spam"
  for filename in glob.glob(os.path.join(path, '*txt')):
    train(filename, "spam")
    cat_total[0]+=1

  path = "./ham"
  for filename in glob.glob(os.path.join(path, '*txt')):
    train(filename, "ham")
    cat_total[1]+=1

  #print(d)
  #

  print(cat_total)

  path = "./evaluation"
  for filename in glob.glob(os.path.join(path, '*txt')):
    classify(filename)

  #print(cat_total)



### classification method
### current assumption: all data that I need will be available,
### from Valerie's code.


### calculates the total number of occurances of all the words in
### the dictionary (only counting once per email)
### input: cat: the category of interest (ham or spam)
### output: the total number of times all of the words in the
###          dictionary are found in each email.
def monstersum(cat):
  global d
  count = 0
  for word in d:
    count += d[word][cat]
  return count

### function to calculate the probability that the
### given words are in a specific class
### input: words: a set of words
###        cat: the category of interest
### output: the probability that the given collection of words is
###          is the indicated category
def probability(words,cat):
  # find the probability of the given category (i.e., number of
  # cat emails divided by total number of emails)
  global d
  global cat_total

  total = monstersum(cat)  
  score = 0
  # calculate the prior probability
  cat_prob = float(cat_total[cat]/(cat_total[0]+cat_total[1]))
  score = math.log(cat_prob) # take the log of the prior probability
  for w in words:
      # calculate the conditional probability for each word
    if(not w in d):
      score = score + math.log(1/(total + len(d)))
    else:
      score = score + math.log((d[w][cat] + 1)/(total + len(d)))
      print(score)
  return score


### function to classify a given test email
### input: filename: the name of a txt file containing an email,
###                   either ham or spam
### output: a message stating whether the email has been classified
###          as ham or spam
def classify(filename):
  spam = 0
  ham = 1
  
  email = open(filename) #read in email
  wordset = email.read() #string
  wordset = set(wordset.split()) #set of words

  # calculate the probability of spam (0), ham (1)
  prob_spam = probability(wordset,spam)
  # calculate the probability of ham
  prob_ham = probability(wordset,ham)

  if (prob_spam > prob_ham):
    print(filename + " This message is spam.")
  else:
    print(filename + " This message is not spam.")










  
    
main()

  
    
