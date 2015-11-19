# spamfilter.py
# A program to filter spam

import string
import os
import glob

global d

def train(filename, label):
  global d
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

  ham_email_count = 0
  spam_email_count = 0
  global d
  d = {}

  spam = ["spamemail.txt"]

  path = "./spam"

  for filename in glob.glob(os.path.join(path, '*txt')):
    train(filename, "spam")

  print(d)

main()

  
    
