# ImpactAnalyticsAssignment
Solution for the Attendance Probability Problem
This project calculates the probability that a student will miss their graduation ceremony based on their
attendance over a given number of days. The student is not allowed to miss classes for four or more consecutive
days.

## Table of Contents
- [Installation](#installation)
- [Usage](#Usage)
- [Examples](#Examples)
- [Approach](#approach)
- [Time Complexity](#time-complexity)
- [Running Tests](#running-tests)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jagritisingh1102/ImpactAnalyticsAssignment.git
    ```
2. Navigate to the project directory:
    ```bash
   cd ImpactAnalyticsAssignment
   ```

## Usage
You can use the 'Attendance' class to calculate the number of valid attendance sequences and the 
probability of missing the graduation ceremony, or use the provided command-line interface (CLI) 
for easier access.

## Examples

## Usage CLI
Run the script with the number of days as an argument:
    python attendance_prob.py 5

## Expected Output
Probability to miss the graduation ceremony: 14/29

## Approach
The solution uses dynamic programming to efficiently count the number of valid attendance sequences
over N days, ensuring no four consecutive days of absence. Here's a brief overview of the approach:
1. State Representation:
    - We use a 2D list dp where dp[i][j] represents the number of valid sequences of length i ending 
      with exactly j consecutive absences.
2. Base Case:
   - The base case is dp[0][0] = 1, meaning there is one way to have 0 days with 0 absences.
3. State Transition:
   - For each day from 1 to N, the dp array is updated as follows:
     - dp[i][0] is the sum of all sequences of length i-1 (ending with a present day)
     - dp[i][1], dp[i][2] and dp[i][3] are updated based on the counts from the previous day.
4. Final Calculation:
   - total_sequences is the sum of all valid sequences of length N.
   - absent_last_days_sequences is calculated as the sum of sequences of length N that end with
     1, 2 or 3 consecutive absences.

## Time Complexity

The time complexity of the solution is O(N), where N is the number of days. This is because we iterate
through the days and update the states in constant time. The space complexity is also O(N) due to the
storage required for the dp array.

## Running Tests
To run the unit tests, use the following command:
    python -m unittest test_attendance.py