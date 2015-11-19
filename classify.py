### classification method
### current assumption: all data that I need will be available,
### from Valerie's code.

### input: email,
def classify(filename):
    spam = 0
    ham = 0
    
    email = open(filename) #read in email
    wordset = email.read() #string
    wordset = set(wordset.split()) #set of words

    # calculate the probability of spam (0), ham (1)
    prob[spam] = probability(wordset,spam)
    # calculate the probability of ham
    prob[ham] = probability(wordset,ham)

    if (prob[spam]>prob[ham]):
        print("This message is spam.")
    else:
        print("This message is not spam")



### function to calculate the probability that the
### given words are in a specific class
def probability(words,cat)
    # find the probability of the given category (i.e., number of
    # cat emails divided by total number of emails)
    score = 0
    cat_prob = float(cat_total[cat]/total_count)
    score = math.log(cat_prob)
    for w in words:
        # calculate the conditional probability for each word
        score += math.log(cp = (dict[cat][word].num + 1)/(monstersum[cat] + d.len()))
    return score



