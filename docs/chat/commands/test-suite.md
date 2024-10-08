# `/test-suite`

##Description
The `/test-suite` command streamlines the process of creating comprehensive test suites for your code. By simply selecting the code segment you wish to test, Qodo Gen automatically generates a robust test suite within its advanced panel. 

##How to Use
Implementing the `/test-suite` command involves a few straightforward steps:

1. **Select Current File Focus**: The `/test-suite` command is designed to operate within Current File Focus, allowing you to generate test suites for specific code segments or entire files.

2. **Select Your Secondary Focus**: Choose the code for which you want to create a test suite. Precise selection ensures the generated tests are relevant and cover the selected code adequately.

3. **Initiate the Command**: Type `/test-suite` followed by any free text in the chat interface. This free text will be added to the general instructions field of the advanced panel, providing context or specific directions for the test suite generation. Upon execution, Qodo Gen opens the advanced panel where the test suite generation process takes place.

    Example: `/test-suite Use 'Given, When, Then' style`

    In this example, " Use 'Given, When, Then' style" is added to the general instructions field, guiding the generation of each test case in a specific style.

4. **Review and Customize the Test Suite**: The advanced panel will display the generated test suite, including your free text instructions. Here, you have the opportunity to review and adjust the test suite and instructions according to your project's specific needs.

**[Read more about Test Generation with Qodo Gen](../../tests/index.md)**

!!! success "Available in"
    - [:fontawesome-solid-file-code: Current File focus](../focus/current-file.md)

!!! example "Example" 
    ### Command: 
    `/test-suite`
    
    ---

    ### Response: 
    ![test-suite](./assets/test-suite.png){width=900, loading=lazy}
        

!!! example "Example with General Instructions"
    ### Command: 
    `/test-suite  use Arrange, Act, Assert style`
    
    ---
    ### Response: 
    ![test-suite-instructions](./assets/test-suite-instructions.png){width=900, loading=lazy}

