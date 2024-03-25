# `/improve`

<h2>Description</h2>
The `/improve` command is designed to delve into the deeper aspects of your code, providing insights and recommendations for improving code quality, maintainability, and performance. Codiumate analyzes your codebase to identify areas that require attention or enhancement, such as otential issues such as bugs, security vulnerabilities, performance bottlenecks, and readability concerns. Unlike the `/enhance` command, `/improve` focuses on more substantial improvements, aiming to bolster the overall integrity and efficiency of your codebase.

<h2>How to Use</h2>
To utilize the `/improve` command, follow these instructions:

1. **Select Your Mode**: This command is versatile, available in both File and Workspace Modes. Choose the mode that best fits the scope of improvements you're aiming for:
    - **File Mode**: Targets specific files for detailed code improvement suggestions.
    - **Workspace Mode**: Expands the improvement suggestions across multiple files within your changeset, ideal for pre Pull Request enhancements.

2. **Select Your Focus**: Pinpoint the code segments or files you're looking to improve. Your selection will guide Codiumate in generating precise and actionable suggestions.

3. **Initiate the Command**: Type `/improve` into the chat interface. Codiumate will analyze the chosen code, identifying a range of improvement opportunities classified by type, such as potential issues, security concerns, vulnerabilities, performance enhancements, or readability improvements.

4. **Review and Choose**: Codiumate presents a list of categorized suggestions for your review. Select the suggestions you want to implement to see a diff view highlighting the proposed changes to your code.

5. **Refactor and Apply**: After reviewing the suggestions and their associated diff views, click the "refactor" button to apply the chosen improvements directly. This streamlined process allows you to efficiently enhance your code's quality with minimal effort.

!!! note "Available in"
    - [File Mode](../modes/file-mode.md)
    - [Workspace Mode](../modes/workspace-mode.md)

!!! example "File mode example"
    <kbd>![/improve_file](./assets/improve-file.gif){width=700, loading=lazy}</kbd>

    ---
    - **User**: Identifies a function suspected of having performance issues and security concerns.
    - **Command**: `/improve`

        
    

!!! example "Workspace Mode Example"

    <kbd>![/improve_workspace](./assets/improve-workspace.gif){width=700, loading=lazy}</kbd>

    ---
    - **User**: Aims to improve the overall quality of a branch
    - **Command**: `/improve`

        