# `/review`

<h2>Description</h2>
The `/review` command in Codiumate is designed to facilitate the code review process by providing a comprehensive analysis of selected changesets (local, staged, or committed changes). This automated review includes an assessment of the main theme, labels, and summary of the changes, along with evaluations on the addition of relevant tests, effort estimation for the review process, and a final score. Additionally, it offers general suggestions for improvement, notes on security concerns, and feedback on the documentation. This command is invaluable for streamlining reviews and ensuring high-quality contributions.

<h2>How to Use</h2>
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

<h2>Available in</h2>
- Workspace Mode
- File Changes Mode

<h2>Example</h2>

<h3>Workspace Mode Example</h3>
**User**: Prepares to submit a pull request including a new documentation file for a recently added command.

**Command**: `/review`

**Codiumate Response**:

[TBD]


