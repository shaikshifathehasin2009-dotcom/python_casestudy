# 90. Integrated Campus Energy and Water Audit

## 1. Algorithm

1. Start.
2. Input the number of buildings and the number of days.
3. Enter daily electricity and water consumption for each building.
4. Calculate electricity cost and water cost.
5. Calculate total consumption and total cost for each building.
6. Calculate the percentage change in consumption compared with the previous day.
7. Identify buildings with excessive consumption by comparing their usage with the specified limit.
8. Calculate a score for each building using the specified scoring method.
9. Rank the buildings according to their scores.
10. Display consumption, costs, percentage changes, excessive consumption alerts, and building rankings.
11. Stop.

## 2. Flowchart

START

INPUT

Number of buildings, days, daily electricity and water usage, unit rates, consumption limits, and scoring method

PROCESS

Calculate total energy and water consumption and their costs

CALCULATE

Percentage change in daily consumption

DECISION

Is consumption above the specified limit?

Yes / No

Flag excessive consumption if the limit is exceeded

RANK BUILDINGS

Apply the specified scoring method and sort by score

OUTPUT

Consumption report, total costs, percentage changes, alerts, and building rankings

STOP

## 3. Input and Output

| Input                            | Output                           |
| -------------------------------- | -------------------------------- |
| Number of buildings and days     | Total electricity consumption    |
| Daily electricity usage (kWh)    | Total electricity cost           |
| Daily water usage (litres or kL) | Total water consumption and cost |
| Electricity and water unit rates | Percentage change in consumption |
| Consumption limits               | Excessive consumption alerts     |
| Scoring criteria                 | Ranked list of buildings         |

Percentage change formula:

\\[ \frac{\text{Current}-\text{Previous}}{\text{Previous}}\times100 \\]

Note: If previous consumption is zero, handle the percentage change separately to avoid division by zero. Buildings are ranked according to the scoring method provided for the audit.