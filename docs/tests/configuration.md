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

By fine-tuning Codiumate's test generation through these configurations, you ensure that the output not only meets your technical requirements but also seamlessly integrates with your project's style and conventions.

