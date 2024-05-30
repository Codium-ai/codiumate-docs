---
title: Current File
output:
  html_document:
    toc: true
    toc_float:
      collapsed: false
    toc_depth: 1

---
<style>
.md-sidebar--secondary .md-nav__list .md-nav__list {display: none}
</style>

# :fontawesome-solid-file-code: Current File

## Overview {.unlisted .unnumbered}

Focus on Current File in Codiumate enhances your coding experience by concentrating on the file you're currently working on. This focus allows you to send selected portions of your code to the model, ensuring the responses are contextually relevant to your specific codebase. With two focus options available via a dropdown menu, Focus on Current File adapts to your needs, whether you're examining specific lines or a desired components.

## Focus Options

1. **Selected Lines**: Manually select lines in your code to set as the focus for your request.
2. **Selected Component**: Choose a function, class, or method from the focus list to concentrate on that particular component.

## Commands

In File Mode options 1 and 2 (Selected Lines and Selected Component), you can utilize the following commands:

- [`/ask`](../commands/ask.md): Pose queries about specific code issues or seek advice on coding practices, enhancing your understanding and coding skills.
- [`/docstring`](../commands/docstring.md): Automatically generates or improves docstrings for your functions, classes, or methods, helping to document your code more effectively.
- [`/enhance`](../commands/enhance.md): Suggests enhancements for your code, such as improving readability, following best practices, and beautifying the code structure.
- [`/explain`](../commands/explain.md): Offers detailed explanations of your selected code, including insights into its functionality, inputs, outputs, and examples of use.
- [`/improve`](../commands/improve.md): Identifies and suggests fixes for potential issues within your code, such as bugs, security concerns, or performance optimizations.
- [`/find-on-github`](../commands/find-on-github.md): Searches GitHub for open-source projects with similar code, providing insights and examples from the wider coding community.
- [`/test-suite`](../commands/test-suite.md): Generates a comprehensive test suite for your selected code, aiding in the development of robust and reliable software.
- [`/quick-test`](../commands/quick-test.md): Quickly creates an initial set of tests for your code, allowing for immediate feedback and iterative improvement through conversation.

## How to focus on Current File

1. **Add Focus**: Within Codiumate chat, click on the `+` button, or type `@` in the chat and use the keyboard arrows, and choose `Current File`.
2. **Choose Your Focus**: Utilize the secondary focus dropdown to select between Selected Lines or Selected Component based on your current requirement.
3. **Execute a Command**: Type in your desired command (e.g., [`/ask`](../commands/ask.md), [`/docstring`](../commands/docstring.md)) followed by your question or request. Ensure your command matches the focus option you've selected for contextually relevant responses.

## Use Cases

- **Code Understanding and Documentation**: Use [`/explain`](../commands/explain.md) or [`/docstring`](../commands/docstring.md) for in-depth understanding and documentation of specific functions or classes.
- **Code Quality Improvement**: Employ [`/enhance`](../commands/enhance.md) or [`/improve`](../commands/improve.md) to refine your code with best practices, optimizations, and security enhancements.
- **Test Suite Generation**: Leverage [`/test-suite`](../commands/test-suite.md) or [`/quick-test`](../commands/quick-test.md) for automated generation of test cases tailored to your selected code.
