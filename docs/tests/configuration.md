# Testing Configuration

## Overview
The Configuration tab within Codiumate's Advanced Panel provides a suite of options to tailor the test suite generation process to your specific needs. These configurations ensure that the generated tests align with your project's conventions, requirements, and preferences.

## Configuration Options

### 1. General Instructions
A free text field where you can specify general instructions that apply to the entire test suite. Use this space to request specific styling, documentation inclusion, or any other overarching guidelines you'd like Codiumate to follow during test generation.

### 2. Example Test
Provide an example test in this field to guide Codiumate on your preferred naming conventions, styling, use of mocks, etc. Codiumate will analyze this example to align the generated tests with your project's existing patterns and practices.

### 3. Number of Tests
Set the desired number of tests for Codiumate to generate initially. This allows you to control the volume of tests based on your project's scale, coverage goals, or other considerations.

### 4. Testing Framework
Select your preferred testing framework from the available options. This ensures that the tests Codiumate generates are compatible with your project's testing environment and conventions.

## Regenerate Test Suite

After making any changes to the configurations, it's essential to apply these updates by clicking the **"Regenerate"** button. This action prompts Codiumate to regenerate the test suite based on the new configuration settings, ensuring that all modifications are accurately reflected in the generated tests.

## Saving Configuration to a File

To preserve your configurations and ensure consistency across your project or team, Codiumate allows you to save these settings to a TOML file:

1. **Save Configurations**: Within the Configuration tab, find the option to export your settings.
2. **File Name**: Save the exported configurations to a file named `.codiumai.toml`.
3. **File Location**: It's recommended to place this file in the root folder of your project for easy access and recognition.
4. **Version Control**:
    - **Collaboration**: Consider adding `.codiumai.toml` to your project's git repository to share these configurations with your team, promoting uniformity in test generation across all contributors.
    - **Local Preferences**: Alternatively, if the configurations are intended for personal use, you might opt to add `.codiumai.toml` to your `.gitignore` file to keep them local.

**[See an example of configuration file](https://github.com/Codium-ai/codiumai-vscode-release/blob/main/docs/.codiumai.toml)**

### Available Sections and Configuration Keys

#### `[tests]`

- **`framework`**:
    - **Description**: Specifies the testing framework to be used, affecting both the content of the generated tests and the command used to run them.
    - **Possible Values**:
        - **Python**: `Pytest`, `Unittest`
        - **JavaScript / TypeScript**: `Jest`, `Mocha`, `Karma`, `Jasmine`, `QUnit`, `React Testing Library`
    - **Note**: Test execution in JavaScript / TypeScript is currently supported only for `Jest`, `Mocha`, and `React Testing Library`.

- **`utility_library`**:
    - **Description**: An additional JavaScript utility library used for testing, if any. 
    - **Possible Values**: `None`, `Testing Library`, `Enzyme`, `Chai`.
    - **Applicability**: Not applicable to Python projects.

- **`reference_test`**:
    - **Description**: A multiline string, enclosed in triple quotes (`"""`), providing an example test to guide the style, setup, etc., of the generated tests.

- **`use_mocks`**:
    - **Description**: Indicates whether to use mocks in the generated tests.
    - **Possible Values**: `true`, `false`.

- **`num_desired_tests`**:
    - **Description**: Specifies the default number of tests to be generated. Selecting fewer tests results in faster generation. Currently, this does not apply to extending test suites.

#### `[tests.javascript]`

For JavaScript / TypeScript projects, the following configuration values control the test runner:

- **`overrideTestRunCwd`**:
    - **Description**: Specifies the directory to use as the "current working directory" when running JavaScript / TypeScript tests.
    - **Default Value**: The directory containing the config file.
    - **Note**: It is common practice to place the config file in the same directory as the `package.json` file and to leave this option as the default.

- **`overrideTestRunScript`**:
    - **Description**: Defines the command used to run tests.
    - **Important**: CodiumAI generates a temporary file containing the test code for a single test and runs that file. After testing, this file is deleted. For component-oriented tests, the temporary file is created next to the file being tested. For suite-extension tests, it is created next to the test suite file.
    - **Note**: You should start the command with 'npx' (e.g., 'npx jest'), and ensure the test command can run test files in the same directory as the file under test. Adjust your package.json script to avoid exclusions that could cause CodiumAI tests to be "not found".
    - **Placeholder**: `TEST_FILEPATH` will be replaced with the actual path of the test file.
    - **Examples**:
        - Mocha:
            ```bash
            npx ts-mocha TEST_FILEPATH --require ./test/mocha/setup.ts
            ```
        - Jest:
            ```bash
            npx jest --runTestsByPath TEST_FILEPATH
            ```
    - **Debugging Note**: To debug test run issues, consult the run logs in VSCode's OUTPUT (select codium-ai from the dropdown). Clearing the output before running tests again can be helpful.

- **`overrideImports`**:
    - **Description**: A multiline string, enclosed in triple quotes (`"""`), containing import declarations that will be prepended to each test file.

