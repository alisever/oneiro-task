# Implement a **Loan Interest Calculator** designed for banking customers.

## Guidelines
- Use the **programming language** you are most familiar with.
- Spend at most **2 hours** on the task.
- Produce a **small console application**.
- Use an **in-memory store** (no database required).
- Apply the **Simple Interest** formula:
  - [Simple Interest Reference](https://www.investopedia.com/terms/s/simple_interest.asp)

## User Journey
1. A user can **provide input parameters** to calculate a loan.
2. The system should **generate an output** containing the loan calculation results.
3. A user can **access historic calculations** and **update** them with new input parameters.

## Loan Input Fields
The input for a loan should include:

1. **Start Date** (date)
2. **End Date** (date)
3. **Loan Amount** (amount field)
4. **Loan Currency** (currency)
5. **Base Interest Rate** (percentage)
6. **Margin** (percentage)
   - Where **Total Interest Rate = Base Interest Rate + Margin**

## Output Data Structure
The output should generate a **daily record** for each day between the **Start Date** and **End Date** (both inclusive), including:

1. **Daily Interest Amount without Margin**
2. **Daily Interest Amount Accrued** (with Margin)
3. **Accrual Date**
4. **Number of Days Elapsed** since the Start Date
5. **Total Interest** calculated over the given period