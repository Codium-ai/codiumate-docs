# `/quick-test`

<h2>Description</h2>
The `/quick-test` command initiates an iterative and interactive mode for generating test suites for your code. Unlike the comprehensive approach of the `/test-suite` command, `/quick-test` focuses on quickly producing a basic set of tests covering key behaviors. Users can fine-tune the generated tests through natural language chatting in a [thread](../threads.md), allowing for precise customization until the desired test suite is achieved.

<h2>How to Use</h2>
To efficiently use the `/quick-test` command, follow these steps:

1. **Select File Mode**: Available exclusively in File Mode, `/quick-test` is designed to provide rapid test generation for specific segments of code within a single file.

2. **Select Your Focus**: Identify the code segment you wish to test. This selection is crucial for ensuring that the generated tests are relevant and targeted.

3. **Initiate the Command**: Type `/quick-test` in the chat interface. Codiumate then analyzes the selected code segment and generates a few behaviors, which are printed in the chat interface along with the initial test suite covering these behaviors. This quick generation aims to give you an immediate understanding of what aspects of the code are being tested. If you require additional behaviors to be tested, you can request more directly in the [thread](../threads.md). This initiates an iterative process where Codiumate and you collaboratively refine and expand the test suite to meet your needs fully.

4. **Refine the Test Suite**: Engage in a threaded conversation with Codiumate to specify adjustments to the test suite. This can include requests for testing additional behaviors, modifying existing tests, or clarifying the logic behind certain tests. Codiumate responds iteratively, refining the test suite according to your directions and feedback.

5. **Finalize Your Test Suite**: Continue this interactive refinement until the test suite satisfactorily covers all desired behaviors and test scenarios. This step concludes the process, ensuring the final test suite is comprehensive and tailored to your specific testing goals.


<h2>Available in</h2>
- File Mode

<h2>Example</h2>

<h3>File Mode Example</h3>
**User**: Wants to quickly generate tests for a newly implemented utility function.

**Command**: `/quick-test`

**Codiumate Response**: Codiumate produces an initial set of tests covering basic inputs, outputs, and functionality of the selected utility function.

**User Interaction in [Thread](../threads.md)**: The developer specifies, "Add tests for edge cases and null inputs."

**Codiumate Update**: Codiumate iteratively refines the test suite, incorporating tests for edge cases and null inputs as requested.