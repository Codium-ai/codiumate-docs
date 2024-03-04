# Changelog

## Jan 21, 2024

**PR-Agent**

- Custom suggestions - A new tool, `/custom_suggestions`, was added to PR-Agent Pro. The tool will propose only suggestions that follow specific guidelines defined by the user. 
See [here](https://github.com/Codium-ai/pr-agent/blob/main/docs/CUSTOM_SUGGESTIONS.md) for more details.

**Codiumate**

- some other update

---

## Jan 17, 2024

**PR-Agent**

- Inline file summary - The `describe` tool has a new option, `--pr_description.inline_file_summary`, which allows adding a summary of each file change to the Diffview page. See [here](https://github.com/Codium-ai/pr-agent/blob/main/docs/DESCRIBE.md#inline-file-summary-)
- The `improve` tool now can present suggestions in a nice collapsible format, which significantly reduces the PR footprint. See [here](https://github.com/Codium-ai/pr-agent/blob/main/docs/IMPROVE.md#summarized-vs-commitable-code-suggestions) for more details. 
- To accompany the improved interface of the  `improve` tool, we change the [default automation settings](https://github.com/Codium-ai/pr-agent/blob/main/pr_agent/settings/configuration.toml#L116) of our GithupApp to:
```
pr_commands = [
    "/describe --pr_description.add_original_user_description=true --pr_description.keep_original_user_title=true",
    "/review --pr_reviewer.num_code_suggestions=0",
    "/improve --pr_code_suggestions.summarize=true",
]
```
Meaning that by default, for each PR the `describe`, `review`, and `improve` tools will be triggered automatically, and the `improve` tool will present the suggestions in a single comment.  
You can of course overwrite these defaults by adding a `.pr_agent.toml` file to your repo. See [here](https://github.com/Codium-ai/pr-agent/blob/main/Usage.md#working-with-github-app).

---

## Links

- [Discord community](https://discord.gg/kG35uSHDBc{:target="_blank"})
- [CodiumAI website](https://codium.ai{:target="_blank"})
- [Blog](https://www.codium.ai/blog/{:target="_blank"})
- [Troubleshooting](https://www.codium.ai/blog/technical-faq-and-troubleshooting/{:target="_blank"})

[![Join our Discord community](https://raw.githubusercontent.com/Codium-ai/codiumai-vscode-release/main/media/docs/Joincommunity.png)](https://discord.gg/kG35uSHDBc){:target="_blank"}

