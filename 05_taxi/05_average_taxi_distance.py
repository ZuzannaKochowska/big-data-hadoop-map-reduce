from mrjob.job import MRJob
from mrjob.step import MRStep


class MRTaxi(MRJob):

    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer)]



    def mapper(self, _, line):
        try:
            (VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, pickup_longitude, pickup_latitude, RatecodeID,
             store_and_fwd_flag, dropoff_longitude, dropoff_latitude, payment_type, fare_amount, extra, mta_tax,
            tip_amount, tolls_amount, improvement_surcharge, total_amount) = line.split(',')

            trip_distance = float(trip_distance)
            yield None, (trip_distance, 1)
        except:

                pass

    def reducer(self, key, values):
        total_distance = 0
        total_count = 0
        for distance, count in values:
            total_distance += distance
            total_count += count
        average = total_distance / total_count
        yield "average trip distance (km)", round(average, 4)


if __name__ == '__main__':
    MRTaxi.run()
