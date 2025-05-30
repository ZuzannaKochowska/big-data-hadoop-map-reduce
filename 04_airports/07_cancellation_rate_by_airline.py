from mrjob.job import MRJob
from mrjob.step import MRStep

class MRFlight(MRJob):

    def steps(self):
        return [MRStep(mapper=self.mapper,
                       reducer_init=self.reducer_init,
                       reducer=self.reducer)]

    def configure_args(self):
        super(MRFlight, self).configure_args()
        self.add_file_arg('--airlines', help='Path to the airlines.csv')


    def mapper(self, _, line):
        (year, month, day, day_od_week, airline, flight_number, tail_number, origin_airport,
         destination_airport, scheduled_departure, departure_time, departure_delay, taxi_out,
         wheels_off, scheduled_time, elapsed_time, air_time, distance, wheels_on, taxi_in,
         scheduled_arrival, arrival_time, arrival_delay, diverted, cancelled, cancellation_reason,
         air_system_delay, security_delay, airplane_delay, late_aircraft_delay, weather_delay) = line.split(',')

        yield airline, int(cancelled)

    def reducer_init(self):
        self.airline_names = {}

        with open('airlines.csv', 'r') as file:
            for line in file:
                code, full_name = line.split(',')
                full_name = full_name[:-1]
                self.airline_names[code] = full_name


    def reducer(self, key, values):
        total_cancellation = 0
        num_elements = 0

        for value in values:
            total_cancellation += value
            num_elements += 1
        yield self.airline_names[key], (total_cancellation / num_elements)


if __name__ == '__main__':
    MRFlight.run()