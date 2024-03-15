# `/update-changelog`

<h2>Description</h2>
The `/update-changelog` command in Codiumate is a powerful tool for maintaining an up-to-date and detailed record of changes within your project. Aimed at enhancing project documentation, this Workspace Mode command automates the process of updating your changelog file. By analyzing a selected changeset (local, staged, or committed changes), Codiumate generates a structured changelog text summarizing the modifications. If an existing changelog file is detected in the project, Codiumate uses it as a reference to match the style and formatting of the update, ensuring consistency across documentation.

<h2>How to Use</h2>
Follow these steps to seamlessly update your changelog using the `/update-changelog` command:

1. **Select Your Changeset**: Choose the changes you wish to document in the changelog—whether they are local, staged, or committed. This selection will guide the generation of the changelog content, tailoring it to reflect the specific updates made during the chosen period.

2. **Select Target Branch (for committed changes)**: If your focus is on committed changes, you must select the target branch to which your current working branch will be compared. For local or staged changes, proceed directly to initiating the command as these do not require a target branch selection.

3. **Initiate the Command**: Type `/update-changelog` in the chat interface. Codiumate then examines the selected changeset, drafting a structured changelog entry that encapsulates the essence of the modifications.

4. **Review and Implement the Update**: Codiumate presents the proposed changelog update, formatted in line with any existing changelog documentation within the project. You can review this summary for accuracy and completeness before integrating it into your changelog file, ensuring that project stakeholders are kept informed of the latest developments.

<h2>Available in</h2>
- Workspace Mode
- File Changes Mode

<!-- <h2>Example</h2>

<h3>Workspace Mode Example</h3>
**User**: Needs to document recent enhancements and bug fixes in the project's changelog before a new release.

**Command**: `/update-changelog`

**Codiumate Response**: Generates a structured changelog entry, such as:

[TBD] -->