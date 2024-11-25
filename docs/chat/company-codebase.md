---
title: Company Codebase
status: new
---

# :fontawesome-solid-file-code: Company Codebase

## What is Company Codebase?

Company Codebase helps Qodo Gen Chat to know your codebase better, enabling you to ask complex, code-specific questions and get better answers.

For example, with Company Codebase you can ask Qodo Gen Chat **"How do I use our auth service to set up authentication for my new app?"** and get the right response.

## How does Company Codebase work?

Retrieval-Augmented Generation (RAG) is a technique that combines retrieval-based methods with generative models to enhance the quality and relevance of generated content.

Qodo Gen uses RAG to understand your company's codebase better, gain deeper context about your projects and answer more complicated or specific questions.

!!! pro "Pro feature"
    This feature is available for Enterprise users only.

## Using Company Codebase

To start using Company Codebase:

1. **Open Qodo Gen Chat:** From your extensions bar, choose the Qodo logo to open Qodo Gen Chat.
2. **Choose Extra Context:** Click on the `Extra Context` button located under the chatbox.
3. **Select Company Codebase:** From the dropdown menu, select `Company Codebase`.

![Company's Codebase](https://www.qodo.ai/images/codiumate/companys-codebase.png){width=700, loading=lazy}

## What can you do with Company Codebase? 

Using Company Codebase in Qodo Gen Chat, you can get answers to deeper, more complicated questions.

**For Example, you can try asking:**

* "Where in our codebase do we have a function with similar functionality to this one?"
* "How do I use our auth service to set up authentication for my new app?"
* "What are the best practices for using our logging library?"
* "How do I integrate our new API into this project?"
* **Template Generation:** Use RAG to generate templates for common tasks, such as creating a Kotlin class with logging. This can help standardize code across your project.
* **Avoiding Code Duplication:** Use RAG to check for code duplication by selecting the context of the current file and asking relevant questions.


<!-- ## Indexing Strategy

* **Focus on Specific Contexts:** Index folders or files relevant to your task (e.g., src, code completions). Avoid indexing the entire project.
* **Examples Folder:** Create an examples folder and add it to the context. This can be used to store good examples and improve the quality of responses.
* **External Code:** If you are using a new or undocumented API, create an "External code" folder in your project and add the source code there. This can be indexed to provide context for your questions and improve the answers dramatically. -->
