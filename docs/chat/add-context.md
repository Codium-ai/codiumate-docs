
---
title: Add Extra Context
---

# :fontawesome-solid-magnifying-glass-plus: Add Extra Context

This feature allows you to enhance the context of your Qodo Gen interactions by adding various elements from your project. Adding more context leads to more accurate and relevant responses, customizing the assistance to your specific coding needs.

## How to Add More Context

Different context options include:

1. **Code Snippet**:
    - **Action**: Select any code snippet you want to add as context.
    - **Shortcut**: Right-click on the selected code and choose "Add to Qodo Gen as context" from the context menu, or use the shortcut:
        - In VSCode: ++ctrl+shift+e++ on Windows, ++cmd+shift+e++ on Mac.
        - In JetBrains: ++ctrl+alt+comma++ on Windows, ++cmd+alt+comma++ on Mac.

2. **Files**:
    - **Action**: Click on the "Add a file or a folder" option in the `+` button, or by typing `@` in the chat.
    - **Search**: Look up and select any file from your project to add as context.

3. **Folder**:
    - **Action**: Click on the "Add a file or a folder" option in the `+` button, or by typing `@` in the chat.
    - **Search**: Look up and select any folder from your project to add as context.
    - **Process**: Qodo Gen Chat will index the selected folder and include it as part of the context. A pre-request search identifies relevant code within the indexed folder.

4. **Entire Project**:
    - **Action**: Click on the "Add a file or a folder" option in the `+` button, or by typing `@` in the chat. Select "Entire Project" to index and include your entire project as context.
    - **Behavior**: This option functions similarly to the Folder option, providing comprehensive context.

5. **Add an Image**
    You can add an image as a context to your request. [Read more about adding images to the chat.](./images.md)

6. **Add Company Codebase**
    You can add entire folders and files from your company's codebase as extra context, making your experience more relevant and tailored to your specific needs. Read more about adding images to the chat.

!!! alert "Please Notice"
    In JetBrains, you can index up to 1,000 files in a single folder or project.

    In VSCode, you can index up to 50,000 files in a single folder or project.

    The index is stored locally and is not shared with anyone.


## Utilizing Additional Context

After adding context, proceed with selecting your primary focus and invoking any command. Qodo Gen automatically considers the added context, enhancing the accuracy and relevance of the responses.

## Benefits

- **Enhanced Accuracy**: More detailed context allows Qodo Gen to offer more precise solutions and suggestions.
- **Flexibility**: You can add context from different parts of your project, fostering a comprehensive understanding of your coding issues.
- **Efficiency**: A richer context streamlines your coding and problem-solving process by reducing the need for further clarification.

The added context persists throughout your session, enriching every command you execute with a deeper understanding of your project's structure and logic. You can remove any piece of context by clicking the trash icon on its tag.
