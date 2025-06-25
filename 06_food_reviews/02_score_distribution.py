from mrjob.step import MRStep
from mrjob.job import MRJob

class MRFood(MRJob):

    def mapper(self, _, line):
        (Id, ProductId, UserId, ProfileName, HelpfulnessNumerator, HelpfulnessDenominator, Score,
         Time, Summary, Text) = line.split('\t')

        yield Score, 1

if __name__ == '__main__':
     MRFood.run()

