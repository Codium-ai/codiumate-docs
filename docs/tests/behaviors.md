# Understanding Behaviors in Test Generation

## Overview
In the journey of test generation, Codiumate employs a sophisticated approach to thoroughly analyze your code. This analysis extends beyond mere syntax, incorporating an understanding of dependencies and imports. This comprehensive view helps grasp the full context of your code's functionality, leading to the identification of various behaviors your code exhibits.

## Behavior Categories
Codiumate categorizes identified behaviors into three main types, each representing a different aspect of how your code operates:

- **Happy Path**: Behaviors under this category represent the ideal and expected use cases of your code, where everything operates as intended without any errors or exceptions.
- **Edge Case**: Behaviors that occur at the boundaries of your code's logic, handling unusual or extreme inputs or scenarios that might not be immediately obvious.
- **Other**: A catch-all category that encompasses behaviors not fitting neatly into the first two categories, including less common use cases or those requiring special consideration.

    === ":simple-visualstudiocode: VSCode"
        <figure markdown="1">
        ![vscode-behaviors](https://codium.ai/images/codiumate/vscode-behaviors.png){ width=900 }
        </figure>

    === ":simple-jetbrains: JetBrains"
        <figure markdown="1">
        ![jb-behaviors](https://codium.ai/images/codiumate/jb-behaviors.png){ width=900 }
        </figure>

## Exploring Sub Behaviors
Each identified behavior can be expanded to reveal its sub behaviors, which are more specific instances or variations of the main behavior. This allows for a granular understanding of how your code functions in different scenarios. To explore sub behaviors:

1. **Click the Arrow**: Next to each behavior, an arrow icon allows you to expand the behavior and view its sub behaviors.
2. **Review Sub Behaviors**: Each sub behavior represents a more explicit use case of the parent behavior, providing insight into detailed operational nuances of your code.

    === ":simple-visualstudiocode: VSCode"
        <figure markdown="1">
        ![vscode-behaviors](https://codium.ai/images/codiumate/vscode-sub-behaviors.png){ width=900 }
        </figure>

    === ":simple-jetbrains: JetBrains"
        <figure markdown="1">
        ![jb-behaviors](https://codium.ai/images/codiumate/jb-sub-behaviors.png){ width=900 }
        </figure>

## Generating Tests for Behaviors
Codiumate not only identifies behaviors but also automatically generates tests for a selected set of initial behaviors to jumpstart your testing process. You have the flexibility to:

- **Select More Behaviors**: Beyond the initial selection, you can choose additional behaviors or sub behaviors for which you want tests to be generated.
- **Create Custom Behaviors**: If a specific behavior you're interested in is not listed, Codiumate allows you to define it manually:
    1. **Add Behavior**: In the behavior analysis section, enter a natural language description of the desired behavior in the "Add behavior" field.
    2. **Generate Test**: Click the "Add and Generate" button to create a test based on your custom behavior description.

By leveraging the behavior analysis and test generation capabilities of Codiumate, you can ensure comprehensive test coverage, capturing the full spectrum of how your code operates—from the most common scenarios to the edge cases that could lead to unexpected behavior.
