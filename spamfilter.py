# spamfilter.py
# A program to filter spam

import string
import os
import glob

global d

def train(filename, label):
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

def main():

  ham_word_count = 0
  spam_word_count = 0

  ham_email_count = 0
  spam_email_count = 0

  d = {}

  spam = ["spamemail.txt"]

  path = "./spam"

  for filename in glob.glob(os.path.join(path, '*txt')):
    train(filename, "spam")
    



    file.close()
    

  emailstring = "This is a spam email spam email"

  #print(emailstring.split())

  emaillist = emailstring.split()

  emailset = set(emaillist)
  print(emailset)

  for word in emailset:
    if word in d:
      d[word][0]+=1
    else:
      d[word]=[1, 0]

  print(d)

  #e = {"apple":(1, 5), "pizza":(2,3)}

  #print(e)
  #print(e["apple"][1])

  #print("DOn't".strip(" " + string.punctuation).lower())

  






main()

  
    
