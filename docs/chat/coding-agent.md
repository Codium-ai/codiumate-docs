---
title: Codiumate's Coding-Agent
status: new
---


# :material-new-box: Codiumate's Coding-Agent

##Overview

The Coding Agent is Codiumate's AI-powered assistant, designed to significantly enhance your coding efficiency and code quality. It combines advanced AI capabilities with an intuitive interface to provide real-time assistance and guidance throughout the coding process.

!!! vscode " VSCode only"
    Coding-Agent is currently available for VSCode users only.

!!! pro "Semi-Pro feature"
    Coding-Agent is **available to all users**. However, loading the plan into Code-Completion is exclusively available to Teams and Enterprise.

##Tools and Features

### 1. Task Implementation Plan

The Coding Agent can generate a detailed plan for implementing a coding task described by you. This plan outlines the steps needed to complete the task effectively:

- **Review and Adjust**: Once the plan is generated, you have the opportunity to review and make any necessary adjustments to ensure it aligns with your project requirements.
- **Code Completion Integration**: After finalizing the plan, it can be loaded into the code completion feature. As you follow the steps outlined in the plan, the code completion tool will assist you in writing the required code for each step. While the planning feature is available to all users, the integration with code completion is available for Teams and Enterprise users. [Learn more about code completion integration](../code-completion/index.md).

#### Using the Task Implementation Plan in Coding-Agent

The Task Implementation Plan streamlines your coding process by breaking down complex tasks into manageable steps. Here's how to utilize this feature:

- **Step 1: Select Your Context** - Begin by identifying all the files and code snippets relevant to your task. Add them as context by right-clicking on the code snippet and choosing "Add to Codiumate as context", or use the shortcut ++ctrl+shift+e++ on Windows, ++cmd+shift+e++ on Mac.

- **Step 2: Describe Your Task** - clearly defining the task you need to accomplish. This could be anything from adding a new feature, fixing a bug, or optimizing existing code. Be as detailed as necessary to ensure Codiumate can generate an accurate plan. You can add images to your description to improve the clarity of your task. Simply paste the image into your description and Codiumate will automatically include it in the generated plan. [Read more about Image Integration in Codiumate Chat](./images.md).

    
- **Step 3: Generate the Plan** - Press `Enter` after describing your task. Codiumate will process your input and generate a detailed plan outlining the steps required to complete your task.

- **Step 4: Review the Plan** - Take a moment to review the generated plan. Ensure it aligns with your project's needs and covers all aspects of the task.

- **Step 5: Adjust the Plan** - If you see areas for improvement or need to modify the plan, click on "Adjust the plan". You can ask for specific modifications inside the thread to refine the plan according to your needs.

- **Step 6: Create a Full Task Plan** - For a full detailed plan including time estimations, testing strategy, and more information, click on the "create a full task plan" button and read the full plan. This comprehensive plan will provide deeper insights and a broader strategy for accomplishing your task.

- **Step 7: Implement the Plan** - Once satisfied with the plan, proceed to implement it step by step. Follow the outlined steps carefully to ensure thorough completion of your task.

- **Step 8: Load Plan into Code Completion (Pro Feature :fontawesome-solid-star:)** - For paying users, enhance your coding experience by loading the plan into the code completion tool. Click on "Load plan into auto-completer". As you work through the steps, the code completion will assist you, providing relevant suggestions to efficiently write your code according to the plan.

### 2. Continuous Code Improvement

As you work on your code, the Coding Agent proactively offers improvements:

- **Automated Commands**: Upon every "save" action, the agent automatically runs commands tailored to the size of the changeset:
  - For small-size changesets, the agent executes the `/issues` command to identify and suggest fixes for potential issues. [Learn about `/issues`](./commands/issues.md).
  - For mid-size changesets, the agent runs the `/improve` command to suggest enhancements that elevate your code's quality. [Explore `/improve`](./commands/improve.md).
- **Customizable**: This feature can be enabled or disabled in the extension settings, allowing you to customize your experience and control when and how you receive coding suggestions. [Adjust your settings](../installation/extension-settings.md).

##Benefits

- **Enhanced Productivity**: By providing a step-by-step plan for coding tasks, the Coding Agent helps streamline your development process, allowing you to focus on implementation.
- **Improved Code Quality**: With real-time suggestions for code improvement and error resolution, your codebase becomes more robust and reliable with every save.
- **Personalized Assistance**: The Coding Agent tailors its assistance to your specific coding tasks and preferences, making it a dynamic tool in your development arsenal.

##Watch a Demo

Watch this demo of the Coding Agent in action:

![type:video](https://www.youtube.com/embed/9dH3pUzsbig?si=dSRMHNdeahUTtEdn)