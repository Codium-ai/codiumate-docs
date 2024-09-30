# Running Tests in qodo Gen (VSCode)

!!! vscode "VSCode Only"
    This feature is available for VSCode users only.

## Overview
For VSCode users working with [supported languages](./supported-languages.md#test-running-support), qodo Gen offers an integrated feature to run tests directly from the advanced panel. This ensures your generated test suite performs as expected right off the bat. You have two primary options for running tests: with automatic fixes or without.

## Running Tests Options

1. **Run and Auto Fix**: This default option attempts to automatically fix any issues if a test fails. [Learn more about Run and Auto Fix](#run-and-auto-fix-flow).
2. **Run Only**: Accessible by clicking the arrow next to the "Run and auto-fix" button, this option runs the test without attempting any automatic fixes.

Both single tests and all tests in the suite can be executed using the "Run all tests" button located above the test list.

## Run and Auto-Fix Flow

When opting for "Run and auto-fix", qodo Gen acts as a testing agent through the following steps:

1. **Initial Test Run**: qodo Gen runs the selected test(s).
2. **Success Path**: If the test passes, the process concludes successfully.
3. **Failure Analysis**:
    - If a test fails, qodo Gen analyzes the failure and displays a summary under the `POSSIBLE TEST ISSUE` section.
    - **Test Issue**: If the issue lies within the test, qodo Gen attempts a fix and reruns the test, looping back to step 1.
    - **Code Issue**: If the analysis suggests a bug in the code, qodo Gen halts auto-fixing and alerts the user. A bug summary and a "fix code" option are presented under the `POSSIBLE CODE ISSUE`. Clicking "fix code" generates a diff view with the proposed fix, which the user can accept to update the code and regenerate the test suite.

## Handling Test Run Issues

There might be instances where tests cannot run due to various reasons, such as:

- **Framework Installation**: The testing framework might not be installed in your project, requiring setup before proceeding.
- **Import Issues**: Problems with imports or dependencies can also prevent tests from running successfully.

In such cases, qodo Gen provides a summary of the issue without attempting auto-fixes, guiding you towards resolving the underlying problem to enable test execution.

## Supported Languages

This feature is available for a select range of languages supported by qodo Gen in VSCode. [See the list of supported languages](./supported-languages.md#test-running-support).
