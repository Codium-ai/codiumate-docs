# `/quick-test`

##Description
The `/quick-test` command initiates an iterative and interactive mode for generating test suites for your code. Unlike the comprehensive approach of the `/test-suite` command, `/quick-test` focuses on quickly producing a basic set of tests covering key behaviors. Users can fine-tune the generated tests through a natural language chat, allowing for precise customization until the desired test suite is achieved.

##How to Use
To efficiently use the `/quick-test` command, follow these steps:

1. **Select Current File Focus**: Available exclusively in Current File Focus, `/quick-test` is designed to provide rapid test generation for specific segments of code within a single file.

2. **Select Your Secondary Focus**: Identify the code segment you wish to test. This selection is crucial for ensuring that the generated tests are relevant and targeted.

3. **Initiate the Command**: Type `/quick-test` in the chat interface. Qodo Gen then analyzes the selected code segment and generates a few behaviors, which are printed in the chat interface along with the initial test suite covering these behaviors. This quick generation aims to give you an immediate understanding of what aspects of the code are being tested. If you require additional behaviors to be tested, you can request more directly in the current chat. Qodo Gen will maintain the context of your initial query, providing tailored responses to your follow-up questions.

4. **Refine the Test Suite**: Engage in a conversation with Qodo Gen to specify adjustments to the test suite. This can include requests for testing additional behaviors, modifying existing tests, or clarifying the logic behind certain tests. Qodo Gen responds iteratively, refining the test suite according to your directions and feedback.

5. **Finalize Your Test Suite**: Continue this interactive refinement until the test suite satisfactorily covers all desired behaviors and test scenarios. This step concludes the process, ensuring the final test suite is comprehensive and tailored to your specific testing goals.


!!! success "Available in"
    - [:fontawesome-solid-file-code: Current File focus](../focus/current-file.md)

!!! example "Example"

    ![quick-test](./assets/quick-test.gif){width=700, loading=lazy}

    ---
    - **User**: Chooses a code without tests
    - **Command**: `/quick-test`
