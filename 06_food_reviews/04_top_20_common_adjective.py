from mrjob.step import MRStep
from mrjob.job import MRJob
import re

WORD_RE = re.compile(r'[\w]+')
class MRFood(MRJob):

    def mapper(self, _, line):
        try:
            (Id, ProductId, UserId, ProfileName, HelpfulnessNumerator, HelpfulnessDenominator, Score,
             Time, Summary, Text) = line.split('\t')

            words = WORD_RE.findall(Text)
            word_count = len(words)

            yield None, word_count
        except:
            pass

    def reducer(self, _, word_count):
        yield "Longest opinion (amount of words)", max(word_count)




if __name__ == '__main__':
    MRFood.run()
