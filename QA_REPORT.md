# QA Report

## Unit tests

11 tests in tests/test_order_calculator.py, covering src/order_calculator.py: line-item totals (including the qty less than 1 error path), order subtotal across multiple items, order total with tax and shipping, the negative-tax error path, and all six delivery-status transitions (valid and invalid) via a parametrized test. All 11 pass locally with pytest and in the CI run for pull request #1 (test job succeeded in 7s).

## Linter findings

Ran ruff against the module. On a deliberately introduced bad revision (combined import line, unused os/sys imports, stray whitespace around a default argument), ruff caught 3 real issues: I001 unsorted/unformatted import block, and two F401 unused-import errors (os, sys), all auto-fixable with --fix. Reverting to the working version, ruff check . reports zero issues; CI runs the same check on every push and PR so a regression fails the build instead of landing on main. The CI run for PR #1 did surface one real, unrelated finding: a GitHub Actions annotation warning that Node.js 20 is deprecated for the actions/checkout and actions/setup-python steps and is being force-run on a newer runtime. That is a platform-level notice, not a bug in this code, and does not fail the build; it is left as-is here but would be worth pinning newer action versions in a longer-lived project.

## Code review summary

The feature branch (feature/order-utils) was reviewed via pull request #1 into main before merging. Review focused on three things: whether line_total should reject qty less than 1 rather than silently accepting a bad quantity (kept as a hard error), whether tax and shipping validation belonged in order_total versus the caller (kept in order_total since it is the only place both inputs are combined), and whether the status-transition table should be a module-level constant instead of rebuilt per call (changed to ALLOWED_STATUS_TRANSITIONS). All feedback was recorded in a review comment on the PR and addressed before merge; the PR's merge commit is visible in the repository history alongside the feature branch.
