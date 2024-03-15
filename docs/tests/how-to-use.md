# How to Use Test Generation in Codiumate

Test Generation is a standout feature of Codiumate, designed to streamline and enhance the process of creating comprehensive test suites for your code. Unlike the interactive chat, test generation operates within a dedicated advanced panel, providing a focused environment for creating and managing tests.

## Initiating Test Generation

There are multiple pathways to initiate test generation, catering to your workflow and preferences:

### From the Chat
- **`/test-suite` Command**: Execute the [`/test-suite`](../chat/commands/test-suite.md) command on selected code within the chat interface to trigger test generation.

### From the Editor
1. **Codiumate Test Lens**: Click the "Codiumate: test" lens button appearing above every function, class, or method.
2. **Context Menu**: Right-click on any selected code or component name and select "Codiumate - Test this component" from the context menu.
3. **Command Palette (In VSCode)**: Highlight the desired code, open the command palette, and execute "Codiumate: Generate tests."
4. **Codiumate Button (In JetBrains)**: Click on the Codiumate icon located near every identifiable component.

## The Advanced Panel

Upon initiating test generation, the advanced panel opens, marking the beginning of your test creation process. The panel is divided into two main sections:

### List of Behaviors
The panel starts by presenting a list of behaviors detected in your selected code. Each behavior corresponds to a specific use case or functionality that your code is expected to perform, serving as a foundation for test coverage.

**[Read more about behaviors](./behaviors.md)**

### Generated Tests
Following the behavior list, you will see generated tests covering a selection of the identified behaviors. These tests are designed to provide immediate value, offering examples of how each behavior can be tested.

**[Read more about the generated tests](./test-suite.md)**

### Example Test

At the top of the tab, there's an Example Test field, that lets you guide the style of generated tests by providing a sample test. Insert a test in the designated field or save it in the settings. If unspecified, Codiumate chooses an existing project test as a template, ensuring consistency across your test suite.

**[Read more about example test](./example-test.md)**


## Next Steps

After reviewing the generated tests and behaviors, you can further refine the tests, add new tests for uncovered behaviors, or modify existing tests to better suit your project's needs. The advanced panel provides a powerful, interactive environment for enhancing your project's test coverage and ensuring the reliability of your code.