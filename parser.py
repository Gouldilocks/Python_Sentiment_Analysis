import nltk

classifier = {}

class word:
  def __init__(self, word):
    self.word = word
    self.count = 1
    self.positive_inst = 0
    self.neg_inst = 0
    self.uniqueness_score = 0
    self.num_documents = 0

  def __str__(self):
    return self.word + " " + str(self.count)

  def __lt__(self, other):
    return self.word < other.word

  def __eq__(self, other):
    return self.word == other.word

class tweet:
  def __init__(self, tweet, sentiment):
    self.tweet = tweet # tweet text
    self.words = [] # list of words in the tweet
    self.sentiment = sentiment # true for positive, false for negative
    

def take_input(filename):
  train_tweets = []
  sentiment = False
  tweetline = ""
  with open(filename) as f:
    for line in f:
      splitLine = line.strip().lower().split(',')
      # remove stopwords from splitline

      tweetline = splitLine[-1]
      sentiment = splitLine[0] == 4
      train_tweets.append(tweet(tweetline, sentiment))
  return train_tweets

def parse_input(input):
  stopwords = nltk.corpus.stopwords.words('english')
  for tweet2parse in input:
    each_word = nltk.word_tokenize(tweet2parse.tweet)
    for one_word in each_word:
      if one_word not in stopwords:
        tweet2parse.words.append(word(one_word))
        if one_word not in classifier:
          classifier[one_word] = word(one_word)
        classifier[one_word].count += 1
        if tweet2parse.sentiment:
          classifier[one_word].positive_inst += 1
        else:
          classifier[one_word].neg_inst += 1
  return input

def calculate_TF_IDF():
  pass

def run_against_test_data():
  pass

def print_results():
  pass


if __name__ == '__main__':
  print("hello!")
  # take the input
  tweets_to_train_on = take_input("training_unix.csv")
  # parse the input
  parse_input(tweets_to_train_on)
  # calculate TF-IDF with sentiment
  calculate_TF_IDF()
  # run the algorithm against test data
  run_against_test_data()
  # print the results
  print_results()