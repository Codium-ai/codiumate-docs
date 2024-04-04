# Extend Test Suite 💎

## Overview
Enhancing and maintaining a comprehensive test suite is crucial for ensuring the quality and reliability of your code. Codiumate simplifies this process by enabling you to seamlessly add more tests to your existing test suite. Whether you've introduced new code, made changes to existing code, or aim to improve your code coverage, Codiumate's Extend Test Suite feature is designed to facilitate these enhancements with ease.

!!! info "Pro feature"
    Extend Test Suite is exclusively available for Teams and Enterprise users.

!!! warning "Supported Languages"
    In JetBrains, all languages are supported. For VSCode, the extend test suite feature is supported only for Python, JavaScript, and TypeScript. [Read more about supported languages](./supported-languages.md#extend-test-suite).

## How to Add More Tests

1. **Navigate to Your Test Suite**: Open the test suite you wish to expand within your IDE.
2. **Initiate Extension**: Click on the "Add more tests" button above the test class or test function. This action opens the advanced panel, where Codiumate presents an analysis of your code's testing coverage.
3. **Explore Test Coverage**:
    - **Existing Behaviors**: Review tests covering current code behaviors.
    - **Uncovered Behaviors**: Identify behaviors in your code that lack corresponding tests.
    - **Generated Tests for Uncovered Behaviors**: Codiumate automatically generates tests for some of the uncovered behaviors to kickstart the extension process.

## Generating Additional Tests

- **Select Uncovered Behaviors**: From the list of uncovered behaviors, choose those you wish to create tests for.
- **Generate Test**: Click on "generate test" for each selected behavior. Codiumate will craft tests tailored to these specific aspects of your code.
- **Integration into Test Suite**: Each newly generated test can be directly added to your existing test suite by clicking the "add test" button, seamlessly expanding your coverage.

## Understanding and Managing Context

For Codiumate to generate precise and meaningful tests, it's essential to provide a clear context of your test suite. The context includes various elements that directly influence the accuracy of the generated tests.

### Types of Context

Codiumate distinguishes between two primary types of context to inform test generation:

- **Code Under Test**: This context type refers to the actual code segments or functionalities that the tests aim to cover. By analyzing the code under test, Codiumate can identify what behaviors need to be tested and generate appropriate test cases.
- **Test Utility**: Includes helper functions, mock objects, and setup or teardown scripts used across tests. Understanding the utilities available helps Codiumate generate tests that are not only consistent with your existing suite but also efficient in utilizing shared resources.


### Viewing the Test Suite Context

- **Original Code Under Test**: Within the advanced panel, you can review the context of your test suite, prominently featuring the original code under test. This visibility ensures you understand the basis for the generated tests and the specific behaviors they aim to cover.
- **Potential Issue**: In some special cases, Codiumate may be unable to trach the original Code under Test, in cases where the imports are not trivial. In this case, it is recommended to provide the relevant code snippets as context.

### Adding or Removing Contexts

- **Customizing Context**: To enhance the relevance and accuracy of the generated tests, you have the flexibility to add or remove contexts. Adjusting the context can involve specifying additional code snippets that should be considered or excluding parts that are not pertinent to the current testing focus.
- **Impact on Test Generation**: By refining the context, you directly influence Codiumate's test generation process, enabling it to produce tests that are more aligned with the actual functionalities and requirements of your code.

### How to Manage Context

1. **Review Current Context**: Examine the displayed context within the advanced panel to assess its completeness and relevance.
2. **Add Context**: If crucial aspects of your code are missing, you can add these to the context, providing Codiumate with a broader understanding of your codebase.
3. **Remove Unnecessary Context**: Conversely, if the context includes irrelevant or outdated code snippets, removing these can sharpen the focus of the generated tests.

By actively managing the context of your test suite, you empower Codiumate to generate tests that are not only accurate but also comprehensive, covering the full spectrum of your code's behavior. This hands-on approach ensures your test suite remains robust and effective, closely tracking the evolution of your project.

## Running and Modifying Tests

The newly added tests can be run and modified just like those generated during the initial test creation process. Codiumate offers the same functionalities for refining, running, and auto-fixing these tests to ensure they meet your standards and accurately test your code.

[Learn more about running and modifying tests](./test-suite.md)

## Benefits

- **Increased Code Coverage**: Ensure more comprehensive testing of your code by identifying and covering previously uncovered behaviors.
- **Efficiency**: Save time by automating the test generation process for new or changed code, allowing you to focus on development.
- **Consistency**: Maintain a uniform testing style and structure within your test suite, thanks to Codiumate's intelligent test generation algorithms.