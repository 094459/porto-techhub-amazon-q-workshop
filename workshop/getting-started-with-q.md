![Amazon Q Developer header](/images/q-vscode-header.png)

### Exploring Amazon Q Developer

Like all developer tools, it is worth spending some time to explore and see how they work to really maximise the benefit to your productivity. In this section we will cover at a high level what Amazon Q Developer provides you with, but I would encourage you to explore.

*Amazon Q Developer menu options*

When we click on the Amazon Q status bar link at the bottom of VSCode, we will see the following pop up. This provides you will access to Amazon Q Developer options, most of which you will not need whilst you are using it, but you will come back to do certain things. Let's go through what each of these options provides.

![amazon q developer menu options](/images/amazon-q-developer-plugin-menu.png)

* Pause Auto-Suggestions (Currently Running) - Amazon Q Developer provides you with suggested code blocks and snippets whilst working directly in your code. You can turn off this behaviour by clicking on this link (you will notice that it will then change to Resume Auto-Suggestions, Currently Paused, and the Amazon Q icon in the bottom status bar will also change). Every developer is different, and some prefer to have this option disabled, others enabled, so you will need to see what feels best for you. When paused, you can still invoke Amazon Q Developer to provide in-line code suggestions, by using the VSCode shortcuts (OPTION + C). Speaking of keyboard short cuts, lets check those out
* Open Code Reference Log - the underlying models that are used to power Amazon Q Developer use some open source code repositories, using Apache 2.0 and MIT licenced source files. Should code suggestions include portions from those projects, Amazon Q Developer will let you know by outputting this to the "Code Reference Log" which you can open by clicking on this menu option. When you click on this, you may see "Don't want suggestions that include code with references? Uncheck this option in Amazon Q: Settings". When using Builder ID you are not able to change this configuration, and the default option is to always include suggestions with code references. As you use Amazon Q Developer, check in here from time to time to see whether you are using code from those open source repositoires.
* Try inline suggestions Examples - this provides a quick tutorial to walk you through the basics of how to use Amazon Q Developer inline suggestions
* Run Project Scan - this kicks off a security scan of the code in the current project, using Amazon Q Developer and other AWS services to help you identify security issues before you ship the code. We will be exploring this later in the labs
* Open Chat Panel - this will open up the Amazon Q Developer chat panel if you close it
* Send Feedback / Connect with us on GitHub / View Documentation - these options provide you with additional ways you can provide feedback if Amazon Q Developer is not working the way you think it should
* Open Settings - will open the Amazon Q Developer plugin settings options (as covered above)
* Sign Out (Connected as AWS Builder ID) - allows you to log out of your current session, with the identity displayed. During this lab, it will always be AWS Builder ID. 

---

*Keyboard shortcuts*

You can control how you invoke Amazon Q Developer via the various key shortcuts, including customising these to how you work.

![keyboard shortcuts for Amazon Q Developer](/images/amazon-q-vscode-shortcuts.png)

One of the key short cuts to know when you are working in the inline editor, is the < and > arrows. These allow you to cycle through suggestions when you are prompted by Amazon Q Developer.

---

*Chat Interface*

You can open the Chat Panel by clicking on the Amazon Q status bar link at the bottom, which by default, will make it appear on the left hand side with the other application artifacts (like files open, git files, etc). You can drag the Chat Panel to the right hand side, as in the screenshot below, which I find helpful as it allows me to see my files in the project, the files I am editing, and then also provide me with my chat interface.

![Amazon Q Developer Chat interface](/images/q-vscode-screen-layout.png)

You can click on the + to open several chat sessions. When using Amazon Q Developer, the plugin will remember the conversations and use that in subsequent responses. This is very helpful when using Amazon Q to work through and troubleshoot issues. We will see this throughout this lab. You can open up to ten of these different tabs or conversations.

Amazon Q Developer also has some power features which are invoked using the /

* **/** brings up a list of the available commands. As Amazon Q Developer gains more capabilities, these will be displayed here
* **/clear** clears the current chat window conversation history, which is useful if you find the responses becoming circular or you want to reset the conversation context
* **/dev** invokes the Amazon Q Developer Agent for software development, and with this, it can create files, add new features, add tests, create documentation, and more. This is one of the most powerful features of Amazon Q Developer, as it will start to take your prompt, break it down into tasks, and then start working through the different tasks in realtime. It explores the files in your workspace to understand your project, and it will share which files it has reviewed and used, files it might want to change, and any new files it has created. Once finished, you will be able to review, check, and if desired, accept these updates.
* **/transform** invokes the Amazon Q Developer Agent for transformation that helps you migrate Java 8 projects to Java 17, taking the effort out of modernising your applications. We will not be using that during this lab, but it is worth knowing about if you are working with old Java applications.

**Note!** When using /dev and /transform with Builder IDs, you have limited quota. You can find out more on the official [Amazon Q Developer pricing page](https://aws.amazon.com/q/developer/pricing/), if you scroll half way down you will see a table which outlines the limits you have open to you.

---

*Menu bar integration*

When you are working on our code within the editor, Amazon Q Developer provides a handy way to quickly invoke it to perform a number of functions. When working on a file, you can select a portion of code, or even if you want the whole thing, and then when you RIGHT CLICK, you will see an "Send to Amazon Q" menu option, which when you select you will see a number of options:

![Amazon Q Developer editor menus](/images/q-vscode-editor-menu.png)

* Explain - this will send whatever you have highlighted to the Amazon Q Chat panel, and ask Amazon Q to help explain what this code does
* Refactor - this will review the snippet and suggest ways you can improve code readability or efficiency, among other improvements
* Fix - this is handy if you are seeing linting errors in your code, or are trying to resolve other issues with your code
* Optimise - this will look to see if it can optimise the performance of the code you have selected
* Send to Prompt - this will copy the portion you have selected and then move it to the Amazon Q Developer Chat Panel. You can then provide your own prompt to ask Amazon Q Developer what you want it to do. This is an easier way than copy/pasting the code snippet yourself.
* Inline Chat - this will bring up a small dialog box within the file you are editing, allowing you to enter a prompt. Amazon Q will then generate some code, asking you to then accept or reject it (hitting Enter to accept, or ESC to reject)

![Example inline chat window](/images/q-vscode-inline-chat.png)
![Example inline chat response](/images/q-vscode-inline-chat-example.png)

---

*Context*

During the lecture you will have heard about large language model context sizes. In effect, this is the amount of information that can be provided to tools like Amazon Q Developer, for them to then reason and make suggestions. When working with Amazon Q Developer, there are two modalities you need to be aware about.

* When using the Amazon Q Developer inline code - when you are in the editor, latency and performance are critical, and so this affects the context size that Amazon Q Developer is able to use. It will take the prompt provided, as well as additional information within the file its working on 
* When using the Amazon Q Developer chat interface - when you use the Amazon Q Developer chat, you will notice there is a small number just below the submit icon (4000/4000). This is the size of the context window. From a latency perspective, there is less need to be very responsive, and so this allows Amazon Q Developer to provide a bigger context size.
* Amazon Q Developer chat inteface tabs - you can open up several chat interface tabs by clicking on the + next to the Chat. Each of these will be new conversations with new context. You can open up to ten of these chat conversations.

Amazon Q Developer also uses things such as open tabs in VSCode, as well as key files depending on programming language (for example, the pom.xml in Java) to add additional information to help it make better suggestions.

If you want to get low level and see this working, you can check the logging of the Amazon Q Developer plugin and see this in action.

---

*Indexing your local workspace*

Amazon Q Developer allows you to index your local workspace which can then be used as part of the context when using the Chat interface. This is a very powerful feature that allows you to bring in additional information to help steer the direction of the output from Amazon Q Developer. For example, maybe you have some existing coding standards you want to influence any code that is generated by Amazon Q. Another way that you can use this is to help personalise the kind of output that Amazon Q Developer generates. You will see some examples of this in the .qdeveloper folder. There are two files, once called "java-expert.md" and the other "opensource.md". These contain additional prompts that will shape the output. A common way you can use this is to create shorter output, perhaps just outputing the code rather than any explaination.

You use this feature from within the Amazon Q Developer Chat interface. You invoke it with @ which will then display the available options. Currently this is only @workspace.

To use @workspace however, you need to first set this up. From the Amazon Q Developer plugin settings, you will see some new options.

![Amazon Q Developer plugin configuration options to enable workplace indexing](/images/q-workspace-settings.png)

Once enabled you will need to restart VSCode. When you restart it, from the OUTPUT tab, there will new option - Amazon Q Language Server. The first time VSCode starts it will explore the current workspace and start to index files.

![Amazon Q Developer workplace indexing logs](/images/q-workspace-index.png)

> **Note!** This feature is still in preview, so there may be some rough edges. One thing I have found is that occasionally you might need to delete the indexes and then restart VSCode to kick of the re-index process.

One the indexing has completed, @worksplace will be ready to go.

---

*Amazon Q Developer logs*

You can access the various Amazon Q Developer plugin logs from the OUTPUT menu option that appears when you have the terminal section in VSCode. When you select the pull down menu, you will see Amazon Q and Amazon Q Logs. The latter provides detailed information about how the plugin is working and interacting with the backend generative AI services powered by Amazon Bedrock.

---

**Understanding how to ask Amazon Q Developer questions**

As you explore the world of generative AI developer tools, one thing you will need to think about is that in order to get useful output and results, you need to ensure that you provide tools like Amazon Q Developer, the right input. What do I mean?

The "Prompt" or "Chat Interface" is how tools like Amazon Q Developer know what they need to do, in the same way that when you are using a search engine, you enter terms you want to search for. It is tempting to treat these chat interfacts like search, but that will lead to poor results. Here are some things to think about that will improve the output from tools like Amazon Q Developer.

* Provide as much information as possible - rather than say "Add a README" as a prompt, a better one would be "Create a README.md file for this project that will explain what this project does, what the key files are, and how to run it."
* If the output is not what you expect, you can use follow up prompts to help steer and improve the output. Using terms like "Can you provide a more detailed response" or "Can you give a code example" are good ways you can maintain the context and memory of what has been asked before, and refine the output
* If the ouput is good, use the thumbs up and down to provide feedback - this will ensure that the responses improve over time
* If the output is bad, use the thumbs down and use the additional link to provide feedback - this will help ensure that you do not get the same poor results back
* Rephrase the question - sometimes, the  output you get will not be great. This is part of the nature of how these tools work. Sometimes, it is better to reword or re-think your prompt and try again
* Remember these tools are non deterministic - it is easy to forget that every time you run the same prompt, you are likely to get different results and output. That is the nature of these tools - it is a feature not a bug
* Debug errors by copying important parts of error messages - one of the powerful ways these tools can help you improve your productivity is by reducing context switching and allowing you to stay within your code editor whilst troubleshooting and fixing errors. Just grab the most peritent part of the error, and then send it to the Amazon Q Developer Chat panel and ask questions like "How do I resolve this error", or "What does this mean". 

---


**Additional learning resources**

I have just covered the basics here, but we are always plublishing new content that shows how other developers are doing cool things with Amazon Q Developer. If you want to know more, head over to [community.aws](https://community.aws/amazon-q)

### Getting hands on in the sandbox

Lets try some of these out now in the next lab which will walk you through how these work in detail. [Practicing with Amazon Q Developer](sandbox.md)


