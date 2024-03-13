# `/ask` 

<h2>Description</h2>
Ask open questions about your code, useful to get a better understanding of the code and asking very detailed questions.

<h2>How to Use</h2>
To use the `/ask` command, follow these steps:

1. **Select Your Mode**: First, determine the context in which you need assistance. Codiumate supports two main modes for this command:
    - **File Mode**: For queries related to a specific file, focusing on selected code, changes within the code, or selected components.
    - **Workspace Mode**: For queries concerning a changeset, including committed changes, local changes etc.

2. **Select Your Focus**: After choosing your mode, select the specific code or changeset you want to inquire about. This step ensures Codiumate provides targeted advice and information relevant to your current focus.

3. **Initiate the Command**: Type `/ask` followed by your question in the chat interface. Codiumate will process your query and return a response tailored to the context of your selected mode and focus.

4. **Continue the Chat**: If you require further assistance or have additional questions, click the "continue this chat" button. This action creates a Thread, allowing for a more in-depth conversation regarding your query.

<h2>Available in</h2>
- File Mode
- Workspace Mode

<h2>Examples</h2>

<h3>File Mode Example</h3>
**User**: Selects a block of code within a file that they suspect contains a bug.

**Command**: `/ask Why is this function returning an unexpected value?`

**Codiumate Response**: Codiumate analyzes the selected code and provides a detailed explanation, potential reasons for the issue, and suggested fixes.

<h3>Workspace Mode Example</h3>
**User**: Highlights a recent changeset that includes several file modifications.

**Command**: `/ask Could these changes affect performance?`

**Codiumate Response**: Codiumate reviews the changeset in question, offering insights into potential performance impacts, areas of concern, and recommendations for optimization.