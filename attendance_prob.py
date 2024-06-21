import argparse

class Attendance:
    def __init__(self, days):
        """
        Initialize the Attendance class with the number of days
        :param days: (int) The number of days in the academic year
        """
        if not isinstance(days, int):
            raise TypeError("Days argument should be of integer type")
        self.days = days
        self.total_ways, self.absent_last_day_ways = self._calculate_ways(days)

    def _calculate_ways(self, N):
        """
        Calculate the total number of valid attendance sequences and the number of
        sequences ending with an absence.
        :param N: (int) The number of days in the academic year
        :return: (tuple) A tuple containing the total number of valid sequences and
        the number of sequences ending with an absence.
        """
        if N == 0:
            return 1, 0
        dp = [[0 for _ in range(4)] for _ in range(N + 1)]
        dp[0][0] = 1
        for i in range(1, N + 1):
            # Ending with present
            dp[i][0] = sum(dp[i - 1])
            # Ending with 1 absence
            dp[i][1] = dp[i - 1][0]
            # Ending with 2 absences
            dp[i][2] = dp[i - 1][1]
            # Ending with 3 absences
            dp[i][3] = dp[i - 1][2]

        total_sequences = sum(dp[N])
        absent_last_day_sequences = dp[N][1] + dp[N][2] + dp[N][3]
        return total_sequences, absent_last_day_sequences

    def number_of_ways_to_attend_classes(self):
        """
        Get the total number of valid attendance sequences.
        :return: (int) The total number of valid sequences.
        """
        return self.total_ways

    def probability_to_miss_graduation_ceremony(self):
        """
        Calculate the probability of missing the graduation ceremony.
        :return: (str) The probability in the format "absent/total"
        """
        return f"{self.absent_last_day_ways}/{self.total_ways}"


def main():
    parser = argparse.ArgumentParser(description="Calculate attendance probability for graduation ceremony")
    parser.add_argument("days",type=int,help="The number of days in the academic year.")
    args = parser.parse_args()
    attendance = Attendance(args.days)
    probability = attendance.probability_to_miss_graduation_ceremony()
    print(f"Probability to miss the graduation ceremony: {probability}")

if __name__ == "__main__":
    main()