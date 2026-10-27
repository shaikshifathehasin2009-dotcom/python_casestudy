## 96. Multi-Criteria Library Resource Distribution

### Algorithm

1. Start.
2. Input book availability, borrowing demand, branch-wise requirements, and priority rules.
3. Compare available book copies with the requirements of each library branch.
4. Identify book shortages and prioritize branches according to the supplied rules.
5. Allocate available copies to each branch based on priority.
6. Update the remaining book stock after allocation.
7. Calculate unmet demand for each branch.
8. Display allocated copies, remaining stock, and unmet demand.
9. Stop.

### Flowchart

START

INPUT DATA

Book availability, borrowing demand, branch requirements and priority rules

COMPARE AVAILABILITY AND DEMAND

Identify shortages for each branch

PRIORITIZE BRANCHES

Apply supplied priority rules

ALLOCATE BOOK COPIES

Distribute copies according to priority

UPDATE STOCK

Remaining stock = Available copies − Allocated copies

CALCULATE UNMET DEMAND

Unmet demand = Required copies − Allocated copies

DISPLAY REPORT

Allocations, remaining copies and unmet demand

STOP

### Input

- Total available copies of each book.
- Borrowing demand for each book.
- Branch-wise book requirements.
- Priority rules for allocating copies.

### Output

- Branch-wise allocated book copies.
- Priority-based distribution report.
- Remaining book stock.
- Unmet demand for each branch.
- Total copies allocated and total unmet demand.