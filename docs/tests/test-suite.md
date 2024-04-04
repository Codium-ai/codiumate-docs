# Managing the Test Suite in Codiumate

## Overview
Following the behavior analysis, Codiumate generates an initial list of tests based on the selected testing framework, which you can configure in the [configuration file](./configuration.md). Each test corresponds to a behavior identified in the preceding analysis and is tagged according to its type: happy path, edge case, other, or custom test.

=== "VSCode"
    ![vscode-tests](https://codium.ai/images/codiumate/vscode-tests.png){ width=900 }

=== "JetBrains"
    ![jb-tests](https://codium.ai/images/codiumate/jb-tests.png){ width=900 }

## Refining Your Tests
Codiumate offers several options for refining and customizing the generated tests to ensure they meet your project's requirements:

1. **Refinement via Chat**: Beneath each test, a chat field allows you to request specific refinements in natural language. Submit your request by pressing Enter or clicking the send button, and Codiumate will update the test based on your instructions.        
2. **Manual Editing**: Directly edit the test code within the advanced panel for quick tweaks and adjustments.
3. **Regenerate Test**: Use the "Regenerate" button beside each test to generate an alternative version based on the same behavior.
4. **Delete Test**: If a test is unnecessary or irrelevant, you can remove it from the list.
5. **Run and Auto Fix (VSCode Only)**: For supported languages, this option allows you to run tests directly. If a test fails, Codiumate attempts to fix it automatically and re-run it. The process stops if a potential bug is detected, alerting you to the issue. [Learn more about supported languages](./supported-languages.md). 
6. **Regenerate Entire Test Suite**: Apply a general instruction for the entire suite via the [Configuration tab](./configuration.md), then regenerate all tests to reflect this overarching guidance.
7. **Request More Tests**: Click "Give me more tests" to generate additional tests, covering more behaviors in one action.

### Test History and Feedback
Codiumate maintains a history of each test's modifications, accessible through "Previous" and "Next" buttons, allowing you to track and revisit changes over time.

### Provide Feedback (VSCode only)
Inside each test, you'll find "Like" or "Dislike" buttons. Your feedback helps Codiumate learn and improve test generation accuracy.

## Finalizing Your Test Suite
When satisfied with the test suite:

- **Save to Project**: Open the finalized test suite as a file and save it directly into your project, integrating your new, refined tests into your development workflow.

- **Copy tests**: Alternatively, you can copy the tests and paste it into your editor.

By leveraging these tools and options, you can fine-tune your test suite to precisely match your expectations, ensuring thorough coverage and robust testing for your code.

