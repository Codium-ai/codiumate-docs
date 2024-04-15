# :fontawesome-solid-folder-tree: Workspace Mode

## Overview
Workspace Mode in Codiumate is designed to facilitate work with code changes across your entire project. This mode enables you to focus on different types of changes within your workspace, providing a broad view that's essential for managing version control and preparing for commits or pull requests. 

!!! pro "Pro feature"
    Workspace Mode is exclusively available for Teams and Enterprise users, reflecting its utility for collaborative and advanced coding endeavors.

## Focus Options
Workspace Mode offers four distinct focuses to tailor the Codiumate experience to your current workflow needs:

1. **Local Changes**: Concentrate on all local changes made in your workspace.
2. **Local Changes Without New Files**: Focus on modifications to existing files, excluding any new files added to the workspace.
3. **Staged Changes**: Highlight changes that have been staged for commit.
4. **Committed Changes**: Review changes that have already been committed. This option requires you to select a target branch to compare your changes against, enhancing the context for Codiumate's analysis and suggestions.

## Commands
The following commands are supported in Workspace Mode, offering a wide range of functionalities tailored to managing and understanding workspace-level changes:

- [`/commit`](../commands/commit.md): Generate commit messages for staged changes.
- [`/describe`](../commands/describe.md): Produce structured descriptions of changesets for pull requests.
- [`/review`](../commands/review.md): Provide comprehensive reviews of changesets, including analysis and feedback.
- [`/improve`](../commands/improve.md): Suggest improvements for code quality and security.
- [`/recap`](../commands/recap.md): Summarize all changes in the selected changeset.
- [`/issues`](../commands/issues.md): Identify potential issues within the code, such as security vulnerabilities or bugs.
- [`/update-changelog`](../commands/update-changelog.md): Automatically update the changelog file with a summary of recent changes.

## How to Use Workspace Mode

1. **Access Workspace Mode**: In the "Mode" drop-down, select Workspace Mode to shift Codiumate's focus to your project's broader context.
2. **Choose Your Focus**: Use the focus dropdown to select among Local Changes, Local Changes Without New Files, Staged Changes, or Committed Changes.
3. **Select Target Branch (if necessary)**: For committed changes, specify the target branch you're comparing changes against to refine Codiumate's insights.
4. **Execute a Command**: Enter your chosen command to gain insights, documentation, review, or other assistance based on your selected focus.

## Use Cases

- **Preparing for Commits**: Use [`/commit`](../commands/commit.md) or [`/describe`](../commands/describe.md) to craft meaningful commit messages and pull request descriptions.
- **Code Quality Assurance**: Employ [`/review`](../commands/review.md), [`/improve`](../commands/improve.md), and [`/issues`](../commands/issues.md) to enhance the quality and security of your code before finalizing changes.
- **Change Management**: Leverage [`/recap`](../commands/recap.md) and [`/update-changelog`](../commands/update-changelog.md) to maintain comprehensive records of project evolution and ensure transparency.