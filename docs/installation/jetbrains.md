---
title: JetBrains IDEs
---

# :simple-jetbrains: JetBrains IDEs 

## Getting Started


<div class="grid cards" markdown>

- :simple-jetbrains: __JetBrains__ 
    
    [:octicons-arrow-right-24: Install Codiumate plugin for all JetBrains IDEs](https://plugins.jetbrains.com/plugin/21206-codiumate--code-test-and-review-with-confidence--by-codiumai)

</div>

## Install Codiumate 

Follow these steps to install the Cody plugin:

1. Open the JetBrains editor on your machine.
2. Open Settings (Mac: ++cmd+comma++ Windows: ++ctrl+alt+s++) and select Plugins
3. Type and search <b class="bold-green">**Codiumate**</b> plugin and click Install
4. After installing, you may be prompted to reload the IDE to activate the plugin.
5. Now the Codiumate icon appears in the sidebar.

## Login methods

There are three login methods:

1. **Login with Google**: Quick access using your Google account.
2. **Login with GitHub**: Utilize your GitHub account for an easy login experience.
3. **Login with Email + Verification Code**: For those who prefer using their email, enter your email address, receive a verification code, and proceed with the login.

## Login to Teams Plan

Once you receive your invitation email from your team administrator and have installed the extension, please log in **using the email address to which the invitation was sent**. Choose one of the [login methods](#login-methods) to complete your login.


## Login to Enterprise Plan

For Enterprise users, please login with your work email with the registered domain. You will be automatically connect to youe organization workspace. Choose one of the [login methods](#login-methods) to complete your login.

If your organization has Single Sign-On (SSO) configured, you may also use this method for an even smoother login process.

---

## Android Studio support JCEF

Codiumate Plugin uses JCEF (Java Chromium Embedded Framework) to create a webview component in the plugin's tool window.
By default, most IntelliJ-based IDEs come with a boot runtime that includes JCEF.
However, Android Studio (and some other versions of IntelliJ-based IDEs) utilize a boot runtime lacking JCEF, which prevents the plugin from loading in these environments.

Also in some cases JCEF could persist but not been initialised.

To address this issue: 

  1. Navigate to the "Help" -> "Find Action..." and find(type) "Registry". Here disable `ide.browser.jcef.sandbox.enable` option.
  2. Navigate to the "Help" -> "Find Action..." and find(type) "Choose Boot Runtime for the IDE" dialog. Here, you can select a boot runtime equipped with JCEF.
  3. Restart the IDE.

If the issue persist, please open an issue in our [GitHub issue tracker](https://github.com/Codium-ai/codiumai-jetbrains-release/issues) or contact [support@codium.ai](mailto:support@codium.ai).
