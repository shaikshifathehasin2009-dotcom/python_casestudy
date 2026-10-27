## 95. Integrated Manufacturing Production Planner

### Algorithm

1. Start.
2. Input raw material availability, production quantities, defect counts, and customer order demand.
3. Calculate the raw materials required for production.
4. Compare available raw materials with the required quantities.
5. Check whether production is feasible based on material availability.
6. Compare the planned production quantity with the order demand.
7. Calculate the defect rate and compare it with the permitted defect limit.
8. Identify material shortages, demand shortages, and quality violations.
9. Display production feasibility, material shortages, defect rates, and order fulfilment status.
10. Stop.

### Flowchart

START

INPUT DATA

Raw materials, production quantity, defect count and order demand

CALCULATE MATERIAL NEEDS

Determine raw materials required

CHECK MATERIAL AVAILABILITY

Is available stock sufficient?

YES

Production feasible

NO

Identify material shortage

CHECK ORDER DEMAND

Compare planned production with required quantity

CALCULATE DEFECT RATE

Defect rate = (Defect count ÷ Total produced) × 100

Does defect rate exceed the permitted limit?

NO

Quality acceptable

YES

Quality violation

GENERATE REPORT

Feasibility, shortages, demand and quality status

STOP

### Input

- Available raw material quantities.
- Planned production quantity.
- Defect count and total units produced.
- Customer order demand.
- Permitted defect rate.

### Output

- Production feasibility status.
- Raw material shortages.
- Order demand shortages.
- Defect percentage and quality violations.
- Production and order fulfilment report.