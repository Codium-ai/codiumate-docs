---
title: File Mode
output:
  html_document:
    toc: true
    toc_float:
      collapsed: false
    toc_depth: 1

---
<style>
/*number of ".md-nav__list" determines the max level of TOC to be displayed in TOC*/
/*e.g. if ".md-nav__list" is repeated 2 times - the headers ###, ####, #####,  ... will not be displayed in TOC*/
.md-sidebar--secondary .md-nav__list .md-nav__list {display: none}
</style>

# :fontawesome-solid-file-lines: File Mode

## Overview {.unlisted .unnumbered}

File Mode in Codiumate enhances your coding experience by focusing on the current file you're working on. This mode allows you to send selected portions of your code to the model, ensuring the responses are contextually relevant to your specific codebase. With three focus options available via a dropdown menu, File Mode adapts to your needs, whether you're looking at specific lines, components, or changes within a file.

## Focus Options

1. **Selected Lines**: Manually select lines in your code to set as the focus for your request.
2. **Selected Component**: Choose a function, class, or method from the focus list to concentrate on that particular component.
3. **File Changes**: Focus on the changes made to the specific file, whether they're committed or local changes.

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


## File Changes

File changes mode is a special mode, that allows you to focus on the changes you have made inside a specific file. 
For this mode, you can use the workspace commands [Workspace Mode Commands](./workspace-mode.md#commands).
With File Changes mode you can work on:

1. **Local changes** - changes you have made to the file in your local workspace.
2. **Committed changes** - changes that have been committed to your version control system.

## How to Use File Mode

1. **Access File Mode**: In the "Mode" drop-down, select File Mode to focus Codiumate on the current file.
2. **Choose Your Focus**: Utilize the focus dropdown to select between Selected Lines, Selected Component, or File Changes based on your current requirement.
3. **Execute a Command**: Type in your desired command (e.g., [`/ask`](../commands/ask.md), [`/docstring`](../commands/docstring.md)) followed by your question or request. Ensure your command matches the focus option you've selected for contextually relevant responses.
4. **Switch Modes If Needed**: If your needs extend beyond the scope of the current file, you can switch to Workspace Mode or Free Chat Mode for broader or non-contextual assistance.

## Use Cases

- **Code Understanding and Documentation**: Use [`/explain`](../commands/explain.md) or [`/docstring`](../commands/docstring.md) for in-depth understanding and documentation of specific functions or classes.
- **Code Quality Improvement**: Employ [`/enhance`](../commands/enhance.md) or [`/improve`](../commands/improve.md) to refine your code with best practices, optimizations, and security enhancements.
- **Test Suite Generation**: Leverage [`/test-suite`](../commands/test-suite.md) or [`/quick-test`](../commands/quick-test.md) for automated generation of test cases tailored to your selected code.

## Add More Context

This feature allows you to enrich the context for your Codiumate interactions by selecting additional code snippets from any file in your project. More context leads to more accurate and relevant responses, tailoring the assistance directly to your coding scenario.

### How to Add More Context

1. **Navigate to the Code**: In your IDE, go to the file that contains the code you want to add as additional context.
2. **Select the Code**: Highlight the specific lines or components that you wish to add.
3. **Add Context**: Right-click on the selected code and choose "Add to Codiumate as context" from the context menu, or use the shortcut ++ctrl+shift+e++ on Windows, ++cmd+shift+e++ on Mac.
4. **Confirm the Addition**: The selected code is added as a tag to the chat panel, visually confirming that your context has been expanded.

### Utilizing Additional Context

Once you've added more context, proceed with choosing your primary focus and calling any command. The additional context is automatically considered by Codiumate, enhancing the precision and relevance of the AI's responses.

### Benefits

- **Enhanced Accuracy**: By providing more details about the coding environment, Codiumate can offer more precise solutions and suggestions.
- **Flexibility**: You can add context from different parts of your project, allowing for a comprehensive understanding of your inquiry.
- **Efficiency**: Having a richer context reduces the need for back-and-forth clarification, streamlining your coding and problem-solving process.

Remember, the added context persists through your session, enriching every command you execute afterwards with a deeper understanding of your project's structure and logic. You can remove it by clicking the X button on every code snuppet tag.

