# `/improve`

##Description
The `/improve` command is designed to delve into the deeper aspects of your code, providing insights and recommendations for improving code quality, maintainability, and performance. Qodo Gen analyzes your codebase to identify areas that require attention or enhancement, such as otential issues such as bugs, security vulnerabilities, performance bottlenecks, and readability concerns. Unlike the `/enhance` command, `/improve` focuses on more substantial improvements, aiming to bolster the overall integrity and efficiency of your codebase.

##How to Use
To utilize the `/improve` command, follow these instructions:

1. **Select Your Mode**: This command is versatile, available in all types of focuses. Choose the focus that best fits the scope of improvements you're aiming for:
    - **Current File Focus**: Targets specific files for detailed code improvement suggestions.
    - **Git-Diff Focus**: Expands the improvement suggestions across multiple files within your changeset, ideal for pre Pull Request enhancements.

2. **Select Your Focus**: Pinpoint the code segments or files you're looking to improve. Your selection will guide Qodo Gen in generating precise and actionable suggestions.

3. **Initiate the Command**: Type `/improve` into the chat interface. Qodo Gen will analyze the chosen code, identifying a range of improvement opportunities classified by type, such as potential issues, security concerns, vulnerabilities, performance enhancements, or readability improvements.

4. **Review and Choose**: Qodo Gen presents a list of categorized suggestions for your review. Select the suggestions you want to implement to see a diff view highlighting the proposed changes to your code.

5. **Refactor and Apply**: After reviewing the suggestions and their associated diff views, click the "refactor" button to apply the chosen improvements directly. This streamlined process allows you to efficiently enhance your code's quality with minimal effort.

!!! success "Available in"
    - [:fontawesome-solid-file-code: Current File focus](../focus/current-file.md)
    - [:fontawesome-solid-code-compare: Git-Diff focus](../focus/git-diff.md)

!!! example "Current File Focus example"
    ### Command:
    `/improve`

    ---
    ### Response:

    ![/improve_file](./assets/improve-file.gif){width=700, loading=lazy}

        
    

!!! example "Git-Diff Focus Example"
    ### Command:
    `/improve`

    ---
    ### Response:

    ![/improve_workspace](./assets/improve-workspace.gif){width=700, loading=lazy}

        