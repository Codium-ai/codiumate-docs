# Understanding Context in Test Generation

!!! vscode "VSCode only"
    This feature is available for VSCode users only.

## Overview
Effective test generation in Codiumate relies heavily on understanding the context of your project. When initiating test generation, Codiumate meticulously collects context based on your code's dependencies and interactions. This rich context is crucial for generating accurate and meaningful tests that closely align with your project's specific requirements.

## Context Collection
Codiumate's context collection process encompasses several aspects:

- **Code Dependencies**: Analyzes the dependencies within your code to understand the relationships and functionalities that need to be tested.
- **Existing Tests**: Searches for existing tests within your project that could serve as templates for new tests, enhancing style consistency across your test suite. [Learn more about example tests](./example-test.md).

## Reviewing Context
To gain insights into the context Codiumate has collected for test generation:

1. **Access the Context Tab**: The advanced panel features a "Context" tab where the collected context is displayed.
2. **Explore Context Tags**: Each piece of context is tagged, providing a clear indication of its source and type.
3. **Navigate to Source**: Clicking on a context tag will take you directly to the corresponding code or test, allowing you to review the basis for Codiumate's test generation decisions.

## Context Types
Each context tag is associated with a type, which helps in understanding the role it plays in test generation:

- **Reference Test**: Existing tests in your project that provide styling cues or functional insights for generating new tests.
- **Imported File**: Files that your code depends on, offering structural and functional context that influences test generation.
- **Referenced in Files**: Identifies locations where the code is used or referenced across your project, providing insight into real-world usage and potential edge cases that need testing.

## Benefits of Context Awareness
By leveraging detailed context, Codiumate ensures that the generated tests are not only syntactically correct but also deeply integrated with the logic and architecture of your project, resulting in a robust and comprehensive test suite.

Understanding the context behind test generation allows you to appreciate the depth of Codiumate's analysis and its impact on producing high-quality, relevant tests tailored to your project's unique environment.
