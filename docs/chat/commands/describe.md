# `/describe`

## Description
The `/describe` command in Codiumate is designed to streamline the process of preparing pull requests (PRs) and understanding changes within your workspace. By invoking this command with a focus on selected changes (local, staged, or committed), Codiumate generates a structured description of the changeset. This includes a title, type of changes (e.g., bug fix, feature addition, performance improvement), and a detailed description. This functionality is particularly useful for developers looking to summarize their work before opening a PR, ensuring that colleagues and contributors can quickly grasp the intent and scope of the changes.

## How to Use
To utilize the `/describe` command effectively, follow these steps:

1. **Select Your Changeset**: Identify the scope by selecting file, local, staged, or committed changes. 

2. **Select Target Branch (for committed changes)**: If your focus is on reviewing committed changes, you must select the target branch to which your current working branch will be compared. This step is crucial for understanding the context and impact of the changes within the broader project scope. For local or staged changes, proceed directly to initiating the command as these do not require a target branch selection.

3. **Initiate the Command**: Type `/describe` in the chat interface. Codiumate then processes your selected changes and compiles a structured description, including a suggested title, the type of changes made, and a comprehensive description of the changeset.

4. **Review and Use the Description**: Review the generated description for accuracy and completeness. You can then use this structured summary directly in your Git PR, facilitating clear communication and efficient collaboration with your team.

## Available in
- Workspace Mode
- File Changes Mode

## Example

### Workspace Mode Example
**User**: Plans to open a PR for a series of changes that include bug fixes and a new feature.

**Command**: `/describe`

**Codiumate Response**: Codiumate generates a structured description of the changeset, such as:

- **Title**: "Feature Addition and Bug Fixes in User Authentication Flow"
- **Type**: "Feature Addition, Bug Fix"
- **Description**: "This changeset introduces a new two-factor authentication feature to enhance security during user login. Additionally, it addresses previously reported bugs in the password reset flow, including error handling and email verification. These changes improve the overall reliability and security of the authentication process."

