# In-Memory Database with Transactions

## Overview

This project implements an in-memory key-value database with transaction support. It includes the following operations:
	- get(key): Retrieve the value for a given key.
 	- put(key, value): Insert or update a key-value pair (requires an active transaction).
	- begin_transaction(): Start a new transaction.
	- commit(): Apply all changes made within the transaction.
	- rollback(): Revert all changes made during the transaction.

This mimics how transactions work in relational databases, ensuring consistency and preventing dirty writes.

## How to Run
	1.	Make sure Python 3 is installed on your system.
	2.	Save the code into a file named data_process.py (or any name you prefer).
	3.	Open a terminal in the directory containing the file and run:
          python3 data_process.py
  4.	The script includes test cases that demonstrate the expected behavior of the database and transactions.

## Example Output

Running the code produces output similar to this:
  None
  Transaction not in progress. Use begin_transaction() first.
  5
  6
  No active transaction to commit.
  No active transaction to rollback.
  None
  None

## Improvements for the Future

To make this assignment more robust and “official”:
1. Clarifications
    Explain that only one transaction can be active at a time.
    Specify how nested transactions (if implemented) should behave.
2. Features
   Add support for advanced features like:
   Nested or multiple transactions.
   Batch operations.
   Logging changes for debugging.
3. Testing
   Include a built-in test suite for automated grading to verify functionality.
4. Grading Enhancements
   Offer bonus points for implementing optional features, such as:
   Logging transaction changes.
   Handling edge cases.

These changes would make the assignment clearer, more challenging, and better suited for grading in an academic setting.
