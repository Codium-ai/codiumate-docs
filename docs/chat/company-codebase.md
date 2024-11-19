---
title: Company Codebase
status: new
---

# :fontawesome-solid-file-code: Company Codebase

## Overview

Retrieval-Augmented Generation (RAG) is a technique that combines retrieval-based methods with generative models to enhance the quality and relevance of generated content. Qodo Gen uses RAG to better understand your company's codebase.

By leveraging your company's codebase, Qodo Gen gains deeper context about your projects, making your experience more relevant and tailored to your specific needs.

!!! pro "Pro feature"
    This feature is available for Enterprise users only.

## Indexing Strategy

* **Focus on Specific Contexts:** Index folders or files relevant to your task (e.g., src, code completions). Avoid indexing the entire project.
* **Examples Folder:** Create an examples folder and add it to the context. This can be used to store good examples and improve the quality of responses.
* **External Code:** If you are using a new or undocumented API, create an "External code" folder in your project and add the source code there. This can be indexed to provide context for your questions and improve the answers dramatically.

## Example Usage 

* **Template Generation:** Use RAG to generate templates for common tasks, such as creating a Kotlin class with logging. This can help standardize code across your project.
* **Avoiding Code Duplication:** Use RAG to check for code duplication by selecting the context of the current file and asking relevant questions.
