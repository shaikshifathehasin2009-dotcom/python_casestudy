## 93. Smart Public Transport Fare Reconciliation

### Algorithm

1. Start.
2. Input route details, passenger categories, passenger counts, and fare rates.
3. Calculate the expected fare for each route and passenger category.
4. Calculate the total expected revenue.
5. Input the actual revenue collected from passengers.
6. Compare the expected revenue with the collected revenue.
7. Calculate the discrepancy using:\
   Discrepancy = Expected Revenue − Collected Revenue
8. If the discrepancy is zero, display “Revenue Matched”; otherwise, identify and report the discrepancy.
9. Display route-wise fares, expected revenue, collected revenue, and discrepancies.
10. Stop.

### Flowchart

START

INPUT DATA

Routes, passenger categories, passenger counts and fare rates

CALCULATE FARES

Passenger count × Fare rate

CALCULATE EXPECTED REVENUE

Add fares across all routes and categories

INPUT COLLECTED REVENUE

CALCULATE DISCREPANCY

Expected − Collected

Is discrepancy = 0?

YES

Revenue Matched

NO

Report Discrepancy

DISPLAY REPORT

Route-wise revenue and discrepancies

STOP

### Input

- Route names and distances, if required.
- Passenger categories (adult, student, senior citizen).
- Passenger counts for each category.
- Fare rate for each category and route.
- Actual revenue collected.

### Output

- Fare calculation for each route and passenger category.
- Total expected revenue.
- Total collected revenue.
- Revenue discrepancy for each route and overall.
- Status: Revenue Matched or Discrepancy Detected.