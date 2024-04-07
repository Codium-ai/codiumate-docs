# JetBrains IDEs

## Getting Started

1. Install Codiumate Plugin via the Plugins tab in the IDE settings, or in [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/21206-codiumate--code-test-and-review-with-confidence--by-codiumai).

2. [Login to Codiumate](./login.md).

3. Start using the plugin 🥳.


## Android Studio support JCEF

Codiumate Plugin uses JCEF (Java Chromium Embedded Framework) to create a webview component in the plugin's tool window.

By default, most IntelliJ-based IDEs come with a boot runtime that includes JCEF.

However, Android Studio (and some other versions of IntelliJ-based IDEs) utilize a boot runtime lacking JCEF, which prevents the plugin from loading in these environments.

To address this issue: 
  1. Navigate to the "Help" -> "Find Action..." and find(type) "Choose Boot Runtime for the IDE" dialog. Here, you can select a boot runtime equipped with JCEF.
  2. Navigate to the "Help" -> "Find Action..." and find(type) "Registry". Here disable `ide.browser.jcef.sandbox.enable` option.
  3. Restart the IDE.

