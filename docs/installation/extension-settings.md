# Extension Settings

Customize your qodo Gen experience with a range of settings designed to tailor the extension's functionality to your workflow. Whether you're using VSCode or JetBrains, you can adjust qodo Gen to fit your development environment perfectly.

=== ":simple-visualstudiocode: VSCode"

    ### 1. Enable / Disable qodo Gen
    Toggle qodo Gen's functionality on or off within your VSCode environment.

    ### 2. Editor Buttons
    Choose to show or hide lens buttons, giving you control over the visibility of qodo Gen's interface elements in the editor.

    ### 3. JavaScript Tests Config-1: Run Working Directory
    Specify the working directory for running JavaScript/TypeScript tests. This setting is crucial for ensuring tests run in the correct context.
    
    - **Path**: Use the absolute path to the root directory of your project (where your `package.json` resides).

    ### 4. JavaScript Tests Config-2: Run Command
    Define the command to run a single JavaScript/TypeScript test file, with `TEST_FILEPATH` placeholder replaced by the actual test file path.
    
    - **Command Examples**:
        - `npx jest --runTestsByPath TEST_FILEPATH`
        - `npx ts-mocha TEST_FILEPATH --require ./test/mocha/setup.ts`

    ### 5. JavaScript Tests Config-3: Run Default Imports
    List default imports to prepend to JavaScript test files, separated by `\n`, enhancing test file setup.

    ### 6. Code Completion
    Enable or disable code completion features provided by qodo Gen.

    ### 7. Code Completion: User Instructions
    Input custom instructions for code auto-completion, utilized by the AI to better align with your coding style.

    ### 8. Agent Settings
    Adjust settings for automatically running `/improve` on mid-size changesets and `/issues` on small-size changesets, optimizing your use of qodo Gen's AI assistance.


=== ":simple-jetbrains: JetBrains"

    ### 1. Enable / Disable Lens Button Display
    Control the visibility of lens buttons within your editor, tailoring how qodo Gen integrates into your coding environment.

    ### 2. Enable / Disable qodo Gen Gutter Icons
    Toggle the display of qodo Gen gutter icons, providing flexibility in how qodo Gen's cues appear alongside your code.
