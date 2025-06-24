from mrjob.job import MRJob
from mrjob.step import MRStep


class MRTaxi(MRJob):

    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer)]
                # MRStep(mapper=self.mapper_pass_through, reducer=self.reducer_get_sorted)]


    def mapper(self, _, line):
        try:
            (VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, pickup_longitude, pickup_latitude, RatecodeID,
             store_and_fwd_flag, dropoff_longitude, dropoff_latitude, payment_type, fare_amount, extra, mta_tax,
            tip_amount, tolls_amount, improvement_surcharge, total_amount) = line.split(',')

            pickup_date, pickup_time = tpep_pickup_datetime.strip().split(' ')
            pickup_hour = pickup_time.split(':')[0]

            yield pickup_hour, 1
        except:
                yield "ERROR", 1

    def reducer(self, key, values):
        yield key, sum(values)

    # def mapper_pass_through(self, hour, total_rides):
    #     yield None, (total_rides, hour)
    #
    # def reducer_get_sorted(self, _, hour_counts):
    #     hour_counts = list(hour_counts)
    #     top_hours = sorted(hour_counts, reverse=True)[:23]
    #
    #
    #     for count, hour  in top_hours:
    #         yield hour, count

if __name__ == '__main__':
    MRTaxi.run()
