# `/changelog`

##Description

The `/changelog` command in Codiumate is a powerful tool for maintaining an up-to-date and detailed record of changes within your project. Aimed at enhancing project documentation, this command automates the process of updating your changelog file. By analyzing a selected changeset (local, staged, or committed changes), Codiumate generates a structured changelog text summarizing the modifications. If an existing changelog file is detected in the project, Codiumate uses it as a reference to match the style and formatting of the update, ensuring consistency across documentation.

##How to Use

Follow these steps to seamlessly update your changelog using the `/changelog` command:

1. **Select Your Changeset**: Choose the changes you wish to document in the changelog—whether they are local, staged, or committed. This selection will guide the generation of the changelog content, tailoring it to reflect the specific updates made during the chosen period.

2. **Select Target Branch (for committed changes)**: If your focus is on committed changes, you must select the target branch to which your current working branch will be compared. For local or staged changes, proceed directly to initiating the command as these do not require a target branch selection.

3. **Initiate the Command**: Type `/changelog` in the chat interface. Codiumate then examines the selected changeset, drafting a structured changelog entry that encapsulates the essence of the modifications.

4. **Review and Implement the Update**: Codiumate presents the proposed changelog update, formatted in line with any existing changelog documentation within the project. You can review this summary for accuracy and completeness before integrating it into your changelog file, ensuring that project stakeholders are kept informed of the latest developments.

!!! success "Available in"
    - [:fontawesome-solid-code-compare: Git-Diff focus](../focus/git-diff.md)

!!! example
    ### Command: 
    `/changelog`

    ---
    ### Response: 

    [2024-04-08]


    **Added**

    - Introduced aiohttp and collections.deque for asynchronous operations and efficient stack management.
    - Added a new utility function to retrieve API keys.

    **Changed**

    - Updated the API key in auto_scraper.py to a new value.
    - Refactored the result processing logic in auto_scraper.py to use asynchronous requests and deque for stack management.
    - Simplified the conditional check for the update parameter in auto_scraper.py.