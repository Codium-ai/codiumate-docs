---
title: Git Diff
---

# :fontawesome-solid-code-compare: Git Diff

## Overview
Git-Diff Focus in Qodo Gen is designed to facilitate work with code changes across your entire project. This focus enables you to concentrate on different types of changes within your workspace, providing a broad view that's essential for managing version control and preparing for commits or pull requests.

!!! pro "Pro feature"
    Some of the Git-Diff focus options are exclusively available for Teams and Enterprise users.

## Focus Options
Git-Diff Focus offers four distinct options to tailor the Qodo Gen experience to your current workflow needs:

1. **Local Changes**: Concentrate on all local changes made in your project or your current file.
2. **Staged Changes**: Highlight changes that have been staged for commit.
3. **Committed Changes**: Review changes that have already been committed. This option requires you to select a target branch to compare your changes against, enhancing the context for Qodo Gen's analysis and suggestions.

## Commands
The following commands are supported in Git-Diff focus, offering a wide range of functionalities tailored to managing and understanding changeset:

- [`/commit`](../commands/commit.md): Generate commit messages for staged changes.
- [`/describe`](../commands/describe.md): Produce structured descriptions of changesets for pull requests.
- [`/review`](../commands/review.md): Provide comprehensive reviews of changesets, including analysis and feedback.
- [`/improve`](../commands/improve.md): Suggest improvements for code quality and security.
- [`/recap`](../commands/recap.md): Summarize all changes in the selected changeset.
- [`/issues`](../commands/issues.md): Identify potential issues within the code, such as security vulnerabilities or bugs.
- [`/update-changelog`](../commands/update-changelog.md): Automatically update the changelog file with a summary of recent changes.

## How to Use Git-Diff focus

1. **Access Git-Diff Focus**: Within Qodo Gen chat, click on the `@` button, or type `@` in the chat and use the keyboard arrows, choose `Git-Diff` and choose your desired diff - `Local Changes`, `Staged Changes` or `Committed Changes`.
2. **Choose Your Focus**: Use the focus dropdown to select among Local Changes, Local Changes Without New Files, Staged Changes, or Committed Changes.
3. **Select Target Branch (if necessary)**: For committed changes, specify the target branch you're comparing changes against to refine Qodo Gen's insights.
4. **Execute a Command**: Enter your chosen command to gain insights, documentation, review, or other assistance based on your selected focus.

## Use Cases

- **Preparing for Commits**: Use [`/commit`](../commands/commit.md) or [`/describe`](../commands/describe.md) to craft meaningful commit messages and pull request descriptions.
- **Code Quality Assurance**: Employ [`/review`](../commands/review.md), [`/improve`](../commands/improve.md), and [`/issues`](../commands/issues.md) to enhance the quality and security of your code before finalizing changes.
- **Change Management**: Leverage [`/recap`](../commands/recap.md) and [`/update-changelog`](../commands/update-changelog.md) to maintain comprehensive records of project evolution and ensure transparency.