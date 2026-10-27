## 99. Integrated E-Commerce Order Processing and Reconciliation

### Algorithm

1. Start.
2. Input product details, order quantities, prices, discounts, dispatches, returns, and available stock.
3. Validate orders and check product stock availability.
4. Calculate the order amount after applying discounts.
5. Process dispatches and update stock quantities.
6. Process returns and update stock according to the return policy.
7. Calculate total revenue from completed orders after discounts and refunds.
8. Reconcile order records, dispatches, returns, and payments to identify discrepancies.
9. Generate the final inventory summary showing available stock, dispatched items, returned items, and discrepancies.
10. Stop.

### Flowchart

START

INPUT DATA

Orders, product prices, discounts, stock, dispatches and returns

VALIDATE ORDER

Check order details and stock availability

CALCULATE ORDER VALUE

Apply discounts to product prices

PROCESS DISPATCHES

Update dispatched quantities and stock

PROCESS RETURNS

Record returned items and eligible refunds

CALCULATE NET REVENUE

Sales after discounts − refunds

RECONCILE RECORDS

Compare orders, dispatches, returns, payments and stock

IDENTIFY DISCREPANCIES

Flag mismatched amounts or quantities

GENERATE FINAL REPORT

Net revenue, discrepancies and inventory summary

STOP

### Input

- Product IDs, prices, and available stock.
- Customer orders and order quantities.
- Discount rates or discount amounts.
- Dispatch quantities and delivery records.
- Returned quantities and refund details.
- Payment and transaction records.

### Output

- Processed order details and discounted prices.
- Dispatch and return summaries.
- Net revenue after discounts and refunds.
- Order, payment, and inventory discrepancies.
- Final inventory summary showing remaining stock, dispatched quantities, and returned quantities.