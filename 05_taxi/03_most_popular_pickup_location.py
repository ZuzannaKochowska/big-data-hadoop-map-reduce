from mrjob.job import MRJob
from mrjob.step import MRStep

class MRTaxi(MRJob):

    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer),
                MRStep(mapper=self.mapper_get_keys, reducer=self.reducer_get_sorted)]


    def mapper(self, _, line):
        (VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, pickup_longitude, pickup_latitude, RatecodeID,
         store_and_fwd_flag, dropoff_longitude, dropoff_latitude, payment_type, fare_amount, extra, mta_tax,
         tip_amount, tolls_amount, improvement_surcharge, total_amount) = line.split(',')

        pickup_longitude = pickup_longitude[:8]
        pickup_latitude = pickup_latitude[:9]

        yield (float(pickup_longitude), float(pickup_latitude)), 1

    def reducer(self, key, values):
        yield key, sum(values)

    def mapper_get_keys(self, key, value):
        yield None, (value, key)

    def reducer_get_sorted(self, _, values):
        values = list(values)
        top_10 = sorted(values, reverse=True)[:10]

        for count, location in top_10:
            yield location, count

if __name__ == '__main__':
    MRTaxi.run()
