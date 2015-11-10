### classification method
### current assumption: all data that I need will be available,
### from Valerie's code.

### input: email,
def classify(filename):
    spam = 0
    ham = 0
    
    email = open(filename)
    wordset = email.read() #string
    wordset = set(wordset.split()) #set of words

    # calculate the probability of spam (0), ham (1)
    prob[spam] = probability(wordset,spam)
    


### function to calculate the probability that the
### given words are in a specific class
    



