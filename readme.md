regression in handling dev reverts with delegatecalls

1. ape test
2. fix ape-vyper until all tests are green

```python
FAILED tests/test_bug.py::test_clone[0.2.5] - AssertionError: Could not find the source of the revert.
FAILED tests/test_bug.py::test_clone[0.2.7] - AssertionError: Could not find the source of the revert.
FAILED tests/test_bug.py::test_clone[0.2.8] - AssertionError: Could not find the source of the revert.
FAILED tests/test_bug.py::test_clone[0.2.11] - AssertionError: Could not find the source of the revert.
FAILED tests/test_bug.py::test_clone[0.2.12] - AssertionError: Could not find the source of the revert.
FAILED tests/test_bug.py::test_clone[0.3.7] - AssertionError: Expected dev revert message 'dev: wrong answer' but got 'dev: Cannot send ether to non-payable function'.
FAILED tests/test_bug.py::test_clone[0.3.8] - AssertionError: Could not find the source of the revert.
FAILED tests/test_bug.py::test_clone[0.3.9] - AssertionError: Could not find the source of the revert.
FAILED tests/test_bug.py::test_clone[0.3.10] - AssertionError: Expected dev revert message 'dev: wrong answer' but got 'dev: BAD_CALLDATASIZE_OR_CALLVALUE'.
```
