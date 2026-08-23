# E-Commerce Order Utils: Git, CI, and QA

A small Python module (order subtotal/total math and delivery-status transition validation, pulled out of the e-commerce NoSQL order schema) used to demonstrate a real Git branching and merging workflow, a GitHub Actions CI pipeline, and a QA process.

Source is in src/order_calculator.py, tests are in tests/test_order_calculator.py (11 unit tests, pytest). The CI pipeline is in .github/workflows/ci.yml and runs ruff (lint) and pytest (tests) on every push and pull request. QA_REPORT.md covers the unit tests, the linter findings, and a summary of the code review conducted on the feature branch before it was merged. REFLECTION.md is the short reflection report on the process.

The feature/order-utils branch was merged into main via a reviewed pull request; see the repository's commit and pull request history for that branching and merge record.
