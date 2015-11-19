### classification method
### current assumption: all data that I need will be available,
### from Valerie's code.


### calculates the total number of occurances of all the words in
### the dictionary (only counting once per email)
### input: cat: the category of interest (ham or spam)
### output: the total number of times all of the words in the
###          dictionary are found in each email.
def monstersum(cat):
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
    score = 0
    # calculate the prior probability
    cat_prob = float(cat_total[cat]/(cat_total[0]+cat_total[1]))
    score = math.log(cat_prob) # take the log of the prior probability
    for w in words:
        # calculate the conditional probability for each word
        score += math.log((d[w][cat] + 1)/(monstersum(cat) + d.len()))
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
        print("This message is spam.")
    else:
        print("This message is not spam")







