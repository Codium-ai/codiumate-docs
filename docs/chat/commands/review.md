# `/review`

##Description
The `/review` command in Codiumate is designed to facilitate the code review process by providing a comprehensive analysis of selected changesets (local, staged, or committed changes). This automated review includes an assessment of the main theme, labels, and summary of the changes, along with evaluations on the addition of relevant tests, effort estimation for the review process, and a final score. Additionally, it offers general suggestions for improvement, notes on security concerns, and feedback on the documentation. This command is invaluable for streamlining reviews and ensuring high-quality contributions.

##How to Use
To make the most out of the `/review` command, follow these steps:

1. **Select Your Changeset**: Identify the scope by selecting file, local, staged, or committed changes. 

2. **Select Target Branch (for committed changes)**: If your focus is on reviewing committed changes, you must select the target branch to which your current working branch will be compared. This step is crucial for understanding the context and impact of the changes within the broader project scope. For local or staged changes, proceed directly to initiating the command as these do not require a target branch selection.

3. **Initiate the Command**: Enter `/review` in the chat interface. Codiumate then processes the selected changeset, providing a detailed review that encompasses several key aspects of code quality and readiness.

4. **Analyze the Review**: Codiumate's review includes:
    - **Changes Analysis**: An overview of the main theme, labels, and a summary of the changes.
    - **Relevant Tests Added**: A yes/no indication of whether the changeset includes associated tests.
    - **Estimated Effort to Review**: A scale rating from 1 to 5 indicating the expected complexity and time investment required for a thorough review.
    - **Changes Feedback**: General suggestions for improvement, potential security concerns, and a final changes score reflecting the overall quality and completeness of the submission.

5. **Apply Feedback**: Use the insights and recommendations provided by Codiumate to refine your changes before finalizing your pull request or code integration.

!!! success "Available in"
    - [:fontawesome-solid-folder-tree: Workspace Mode](../modes/workspace-mode.md)
    - [:fontawesome-solid-file-pen: File Changes Mode](../modes/file-mode.md#file-changes)

!!! example "Example - Committed changes"

    ---
    <h4>Changes Analysis</h4>

    **🎯 Main theme:**

    The main theme of the changes is to add new functionality for processing git patches. Two new functions have been added: `get_file_patch_info` and `get_edit_type`.

    **Changes labels:** Enhancement

    **Changes summary:**

    The changes introduce two new functions to the `git_patch_processing.py` file. The `get_file_patch_info` function extracts information about a file patch from a given patch string. The `get_edit_type` function determines the type of edit (addition, deletion, or modification) represented by a given patch string.

    **🧪 Relevant tests added:** No

    **⏱️ Estimated effort to review** [1-5]:
    3, the changes are not too complex but they do add significant new functionality which needs to be thoroughly reviewed.


    <h4>Changes Feedback</h4>

    **💡 General suggestions:**

    The code looks well-structured and follows good practices. However, it would be beneficial to add tests for these new functions to ensure they work as expected. Also, in the get_file_patch_info function, the exception handling could be improved. Instead of a broad except clause, it would be better to catch specific exceptions.

    **🔒 Security concerns:** No

    **Changes Score:** 85

    ---

    - **User:** Selects committed changes from current branch with target branch `main`
    - **Command:** `/review`