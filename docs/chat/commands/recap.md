# `/recap`

<h2>Description</h2>
The `/recap` command in Codiumate is designed for developers seeking a comprehensive overview of modifications within a selected changeset, be it file, local, staged, or committed changes. This command meticulously lists all changes, organizing them by modified file. Each change is annotated with a tag indicating the type of modification, a link to the affected code, and a detailed description of what was altered. This command is invaluable for code review, documentation, and ensuring a clear understanding of the work done or the changes made before moving forward with commits, merges, or deployments.

<h2>How to Use</h2>
To effectively utilize the `/recap` command, adhere to the following steps:

1. **Select Your Changeset**: Identify the scope of your recap by selecting file, local, staged, or committed changes. This focus directs Codiumate to compile a detailed account of modifications relevant to your current review or documentation needs.

2. **Select Target Branch (for committed changes)**: If your focus is on committed changes, you must select the target branch to which your current working branch will be compared. For local or staged changes, proceed directly to initiating the command as these do not require a target branch selection.

3. **Initiate the Command**: Type `/recap` into the chat interface. Codiumate will process the specified changeset and generate a structured list of all changes made, categorized by file.

4. **Review the Recap**: Each file listed in the recap will include:
    - **Type of Change**: The type of the modification (e.g., Enhancement, Refactor, Bug fix).
    - **Link to Code**: A direct link to the modified code, facilitating easy access and review.
    - **Description of Changes**: A clear, concise description of what was changed in the code, providing context and understanding at a glance.

<h2>Available in</h2>
- Workspace Mode
- File Changes Mode

<!-- <h2>Example</h2>

<h3>Workspace Mode Example</h3>
**User**: Prepares to summarize recent work on a new feature for a team meeting.

**Command**: `/recap`

[TBD] -->


