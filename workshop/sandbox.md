![Amazon Q Developer header](/images/q-vscode-header.png)

## Getting confident with Amazon Q Developer

Before we build an application, we will complete a few excercises that will allow you to get familiar with how the different capabilities of Amazon Q work. Create a new directory, and then start a new VSCode instance. We will use this whilst we are running through the basics. Once we have completed this lab, we will close everything down.

**Do you use other generative AI coding tools?**

If you currently are using a generative AI tool (e.g. Continue, Supermaven, Copilot, etc) then you may find that some of the keyboard shortcuts do not work. For the duration of this workshop, find the other AI coding tools you are using and temporarily disable them. To do this, go to the plugin section, locate your plugin and then from the settings select disable.

**Understanding Free Tier vs Professional**

It is worth spending a few minutes to review the key differences between the capabilities and service limits available depending on whether you are using the Free Tier (using Builder ID), with the Professional Tier.

Review the [pricing page](https://aws.amazon.com/q/developer/pricing/), as of writing you can see some of the key differences are around some capabilities (auto security scanning, the ability to create custom models based on your own code), as well as service limits (the number of times you can use Amazon Q Developer Agent for software development, the number of lines of code you can submit for security scans, etc)

* If you want to use Professional Tier you will need to have an AWS account.
* If you do not currently have an AWS account, then Builder ID is the way forward for you.

---

### 1. Using in-line editor

You can use Amazon Q Developer to help you as you write code within your editor. This section will walk you through how these work to provide you with confidence in how to get the best out of the tool.

**Basic functionality**

Amazon Q supports a number of different ways you can enter instructions (prompts) that it will use to provide code suggestions. We can summarise these as the following:

* Function prompt
* Single line comment
* Multi line comment
* Single line prompt
* Multi line prompt
* Inline prompt

With the exception of the Inline prompt, after entering a prompt and hitting return, this will invoke Amazon Q and it will provide you with some code suggestions. You will get the opportunity to reivew the options using the < and > cursor keys. Occasionally there will only be a single code suggestion in which case you will not get any different output by using the < and > keys.

You will notice that the code suggestions are greyed out. To accept the suggestion, you hit TAB.

These code suggestions are automatic by default. The next section will walk you through how you can change this behaviour.

**Function prompt**

Amazon Q Developer can understand your intent and provides suggestions based on the function names. The more descriptive the function name is, the better the suggestions.

Open up a new file in your VSCode, and type the following:

```
def towers_of_hanoi(
```

Do you copy/paste :-)

As you hit the ( you should see Amazon Q Developer already anticipating what you want and provide some code suggestions. You can cycle between suggestions using the < and > cursor keys, and accept with TAB or quit by hitting ESC.

You can try with some other function names, for example:

```
def get_average(numbers):
```

As your add code to your file, Amazon Q will take this into consideration. You can create a single function at the top of your code that has everything you want (for example a doc string, matches your style guide for variable or function name, etc), and then as you add more functions, it will copy the structure.

For example, add the following at the top of the file (you can delete everything you just added)

```
def get_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
    numbers (list): A list of numbers (int or float).

    Returns:
    float: The average of the numbers in the list.

    Raises:
    ValueError: If the input list is empty.
    TypeError: If the input list contains non-numeric elements.

    Example:
    >>> get_average([1, 2, 3, 4, 5])
    3.0
    >>> get_average([])
    Raises ValueError: Empty list provided
    >>> get_average([1, 2, 'a', 4, 5])
    Raises TypeError: List contains non-numeric elements
    """
    if not numbers:
        raise ValueError("Empty list provided")
    
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("List contains non-numeric elements")
    
    return sum(numbers) / len(numbers)
```

Now hit return a few times and then type in the following

```
def get_mean(numbers)
```

You should see that it generates very simiar boilerplate code that matches what you defined as your "standard". This is a very nice feature that allows you to code very quickly whilst ensuring you maintain all the things you want.

**Single line comment**

Amazon Q Developer can understand your intent and provides suggestions based on single line comments. For example, in the IDE type the following:

```
# function to print a message
```

When you hit return, you will see Amazon Q provide some code suggestions.

**Multi line comment**

This works the same as the previous one, except you can have the comments over a number of lines. For example, type the following in your IDE

```
"""
Given a list that contains some numbers and strings, 
format the list elements into a string in which the numbers are prepended with a "#" 
and check for strings and wrap in a double quote.
"""
```

When you hit enter, you should see Amazon Q provide code suggestions.


**Single line prompt**

Amazon Q Developer will understand your intent and provides suggestions based on the a prompt that you provide within the file you are working on. For example, type the following and then hit enter

```
# CREATE a function called get user age, ask the user to input their age, and RETURN the user's age
```

You will see that it creates code based on this single line prompt.

*Multi-line prompt*

This works exactly like the previous one, except you can put your prompts on multiple lines. For example

```
 # CREATE a function called get user age
 # ask the user to input their age
 # RETURN the user's age
```

**Enabling and disabling auto prompting**

Something that you will need figure out as you start using Amazon Q Developer is whether you want it to automatically make code suggestions as you code, or whether you want to manually invoke it via some command line controls.

You can enable/disable the auto-suggestions by clicking on the "Pause Auto Suggestions" when you bring up the Amazon Q menu (click on the Amazon Q on the VSCode status bar at the bottom)

Spend some time experimenting with this. Open up a new file (experiment.py) and then at the top of it write the following:

```
# Add Python library imports for Flask and SQLAlcamey
```

Hit return. You should see Amazon Q thinking (it will be greyed out) before providing you with some code suggestions.

Now go to the Amazon Q setting and disable auto suggestion. You should notice that the icon looks like the pause icon. From the same file, delete everything that you previous created and type the same thing

```
# Add Python library imports for Flask and SQLAlcamey
```

When you hit return this time, it should not generate any output. No, move your cursor to the end, and hit OPTION + C (Mac), ALT + C (Windows) and this time you should see Amazon Q make some suggestions. If you hit tab to accept, and then hit return and press OPTION/ALT + C again, you will see further suggestions.

Re-enable auto suggestions as we will be using this during the workshop.

**Inline prompt**

Inline prompt works slightly differently. There are two modes you can use it in:

* From the either the position where your cursor is within the current open file
* Selecting a block of code 

The behaviour is similar. You invoke it with COMMAND + I, and this will bring up a command prompt window. If you do not see this, then there are two things you need to check:

1. Make sure that you do not have any other VSCode plugins that might be competing with this for COMMAND + I - when I was writing this, COMMAND + I did not work for me, and I had to temporarily disable another plugin that I was no longer using
2. Make sure the focus is in the actual file open - often I find that the focus is either in the chat interface, or the file explorer. I click within the open file to make sure

Once you enter the prompt, it will now start to work. You cannot select different code segments like the previous ways. You will see your code blocks highlight in Green/Red based on new or changed/deleted code, with an option to Accept (Enter) or Reject (ESC) the sugguestions.

I find this mode very powerful and improves the speed at which I can make updates/changes to my code. It tends to work well for specific ways you might want to work - updating existing code blocks for example, adding new functions, asking for optiisations, adding try / catch blocks, and more.

---

### 2. Using the VSCode Menu integration

From the main editor, you can invoke Amazon Q through the meny integration. When you right click anywhere in an active page, you will see Amazon Q, which then opens up to a number of different options. We will explore these now:

* Explain - this will send whatever you have highlighted to the Amazon Q Chat panel, and ask Amazon Q to help explain what this code does
* Refactor - this will review the snippet and suggest ways you can improve code readability or efficiency, among other improvements
* Fix - this is handy if you are seeing linting errors in your code, or are trying to resolve other issues with your code
* Optimise - this will look to see if it can optimise the performance of the code you have selected
* Send to Prompt - this will copy the portion you have selected and then move it to the Amazon Q Developer Chat Panel. You can then provide your own prompt to ask Amazon Q Developer what you want it to do. This is an easier way than copy/pasting the code snippet yourself.
* Inline Chat - this will bring up a small dialog box within the file you are editing, allowing you to enter a prompt. Amazon Q will then generate some code, asking you to then accept or reject it (hitting Enter to accept, or ESC to reject)

There is a file in the repo [resources/in-menu.py](https://github.com/094459/q-developer-hands-on/blob/main/resources/in-menu.py) where you can practice some of these. Explore each of them so you can see the kind of output they produce.

---

### 3. Running a security scan

Code generated by AI coding assistants should not be assumed to be free of defects or bugs. It is important therefore that we review the code as it is suggested by Amazon Q Developer. That is our starting point, but we can also use a great feature of Amazon Q which allows developers to run security scans on their code.

To do this, from the Amazon Q menu (click on the Amazon Q on the VSCode status bar at the bottom), and click on Run Project Scan. 

![Start Security Scan](/images/q-vscode-security-scan.png)

It will kick off a scanning job, and review your files.

![Kick off a security Scan](/images/q-vscode-sec-scanning.png)

After a few minutes (or longer depending on how big your project is) any findings will appear in the IDE (they will appear under the PROBLEMS TAB). If it finds no security issues, you will see somethign like this:

![No security findings](/images/q-vscode-no-security-findings.png)

If it does find something, it will list any issues in the PROBLEMS tab like this

![Security issue found](/images/q-sec-issue-found.png)

You can click on the link to take you directly to the issue, and you can also then use the integration with VSCode to get further informtion, including how to fix the issue. Occasionally Amazon Q will be able to suggest a fix automatically, and you will be able to use the Quick Fix to automatically address the problem.

![Review the issue](/images/q-vscode-finding-details.png)

![Review options](/images/q-vscode-finding-options.png)


In the repo we have provided a sample file [security-example.py](https://github.com/094459/q-developer-hands-on/blob/main/resources/security-example.py) which contains an issue. 

Trigger a Security Scan and follow the steps to 1/ review the findings, 2/ use the explain and options links to see what suggestions are provided.

Implement any suggestions and re-run the scan again. You should find that you no longer have issues.

**Auto scanning**

If you are using Amazon Q Developer with Builder ID, you will always have to invoke (start) a security scan

**Security Scan limits**

Remember that when using Amazon Q Developer Security Scanning with the Builder ID, you will have lower service limits. Check the page (see at the top) for the latest on this, as this is always changing. The key things to be aware of are:

* the lines of code within your application
* the total size of your project

**Reference**

The [Security Scan](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-scans.html) documentation is a helpful reference to find out more about how this works, including the different kinds of security scanning tests performed, supported programming languages, and limits.

---

### 4. Using @Workspace

In the previous section you saw how to configure and enable Amazon Q Workplace indexing. Here we will dive a little deeper into how it works. As of writing this is still a beta feature, so bear that in mind.

**View logs**

From VSCode, make sure you have the Terminal window open. From this select the OUTPUT tab, and then click on pull down menu. You will see multiple entries, there are two that are key for @workspace

* Amazon Q Logs - this will show you the index demon process starting and other high level details of how Amazon Q is working with @workspace
* Amazon Q Language Server - this provides the actual logs of when you are using @workspace

**Stop/Start**

When you are working with your projects, you might encounter occasional errors when using @workspace. One of the most common issues I have seen is where as the local project files change (perhaps due to git checkout) @workspace can sometimes provide incorrect guidance based on files that are no longer there. When this happens, I stop and restart the service. To do this:

1/ From the Amazon Q menu on the bottom of the VSCode status bar , select O'pen Settings"
2/ Navigate to the "Amazon Q: Workspace Index"
3/ Untick the box, wait a few seconds, and then re-tick the box.

When you click on the OUTPUT tab and then select the pull down menu, you may see multiple Amazon Q Language Server log entries. Try them all, and you should see in one of them, the indexing process starting.

**Clear out cache**

Occasionally stopping and restarting the Workspace Index will not resolve the issue. Opening the logs will show error messages (a common one I have seen is a Fais index failure). When this happens, it is often best to delete the cache and get Amazon Q to reindex. You can find the location of the cache by looking at the Amazon Q Language Server logs. Here is an extract from mine:

```
[Info  - 16:02:49] bm25 indexing complete, time: 0.92ms
[Info  - 16:02:49] start building tree index for /Users/ricsue/Projects/amazon-q/workshop/q-developer-workshop-supporting-repo/q-developer-workshop-demo-code
[Info  - 16:02:49] Finished parsing 1 python files. Time 15.07ms
[Info  - 16:02:49] start building vector index
[Info  - 16:02:49] Starting building vector index for 3 files
[Info  - 16:02:50] Vector index complete! Take 0.09364341600000001s. Total 3 files, 5 chunks
[Info  - 16:02:50] Vector index saved to /Users/ricsue/.aws/amazonq/cache/cache/eee4a16ba650a3c2a0cab92dd904c065feb5976341f32c94cd0be7fe5fcdd94a-0.9-VSCode.index
[Info  - 16:41:47] Adding file to vector index: /Users/ricsue/Projects/amazon-q/workshop/q-developer-workshop-supporting-repo/q-developer-workshop-demo-code/.qdeveloper/MY-PREFERENCES.md
```
From this we can see that **/Users/ricsue/.aws/amazonq/cache/** is the location where the Workspace Index will generate these indexes. These can be deleted as the index process will recreate them.To do this:

* Disable the Amazon Q: Workplace Index using the previous step
* From the terminal, locate the directory where the indexes are created and then delete them
* Re-enable the Workspace Index

---

### 5. Context

Understand context is critical in how to understand and influence how Amazon Q Developer can help you. This section explores the differnt ways that Amazon Q Developers understand what you are trying to make it do. Context is everything and key to improving your success with tools like Amazon Q Developer.

**Modality**

It is important to understand that how Amazon Q gets context is dependant on how you are using it. If you are using the inline editing modality, the characteristics of what Amazon Q needs to do (be very fast, and provide instance responses) means that the context is very small (the prompt itself). If you are in the chat interface, then the responses do not have to be immediate, and so the context can be larger. Bear this in mind as you think about how you use the different modalities within Amazon Q.

**Import statements**

You can influence the suggestions that Amazon Q provides you by adding the libraries you want to use at the start of your code. For example, if I ask Amazon Q to create code for a python web framework, with a blank project file, I might get Flask, FastAPI, or DJango. If I first add 'from flask import Flask' at the top of the page, it will almost always provide me with Flask code*

*I say nearly, as it is impossible to be 100% certain with non deterministic systems

**Open Files or tabs**

The first place that Amazon Q looks for context when using Chat interface is the files you have open within the IDE. It can be a good idea to just keep the key files open you need to help focus Amazon Q.

In addition, Amazon Q is smart enough to understand that important context can be obtained from key files. If you are working with Java projects, it will read your pom.xml for example.

**Small files**

Because context sizes are so important, and they are of a finite size, you might find better results by breaking down your project into smaller files. This will allow those files to reside within the context space available.

**Project workspace**

If you are wanting to work in a project (for example Python) but have a lot of other code in your workspace (perhaps because you are working in a mono repo environment) the responses you can get from Amazon Q may not be what you expect. You might get Javascript or Python despite the project you are working in being in the other language. The best way to tackle this is to try and setup your IDE so that it is just working in a subfolder of your mono repo and avoid files within your local workspace that are a distraction.

**Customisation**

Amazon Q Developer allows you to provide your own code to help influence code suggestions. This is currently only available with the Professional Tier, and not in scope within this workshop. It is good to know that this capability is very powerful, allow developers to have a number of customised models that they can use depending on the different custom code they want to use.

Check out [this video](https://www.youtube.com/watch?v=dsjXb4TvfPg) for more info.

**Scaffolding**

We can help steer the output of how Amazon Q works by providing scaffolds. There are two ways we can do this:

1/ Provide details in a markdown doc in our project directory, and refer to these in our prompts
2/ Provide them directly within the prompt itself

Review the markdown documents [here](https://github.com/094459/q-developer-hands-on/blob/main/.qdeveloper/java-expert.md) and [here](https://github.com/094459/q-developer-hands-on/blob/main/.qdeveloper/opensource.md). You will see another one as we proceed with the workshop. You can use this with @workspace in the Amazon Q Chat interface to alter the kind of output it will provide.

When using /dev, you can provide additional info within the prompt to help scaffold the code that is created. For example, you could write a prompt to create a Node project in a particlar fashion by implementing a prompt like the following:

![example q scaffold](/images/q-scaffolding.png)

---

### 6. When your prompts don't work

Occasionaly you will enter a prompt and receive the following response:

![Not accepting prompt](/images/q-vscode-context.png)

It can sometimes be a little random when this happens, so here are a few tips to help you resolve this issue:

* stay within the same 'conversation' as Amazon Q retains memory and context, and you are less likely to encounter this issue if it is part of a longer conversation
* change the order of the words - sometimes you might need to revise your prompt, removing potentially confusing words
* try a different prompt - you can keep the same intention but try using completely different words

In most cases these will resolve your issues.

---

### 7. Chat interface

When using the Chat interface, there are some things you should be aware of to help improve your success when working with it.

**Max size**

You can enter a maximum of 4000 characters into the chat interface. Bear this in mind if you are using the integration with the VSCode menu to send highlighted code to the Amazon Q chat interface (Amazon Q > Send to Prompt). If you are working on a particularly large file, you might exceed your limit and have no space for a prompt. You will notice that there is a counter underneath the chat interface to help you know how close you are getting to your limit.

**Conversation history**

As you work back and forth in the Amazon Q chat interface (aka CHat Orientated Programming,or CHOP), under the covers Amazon Q is retaining a history of the conversation and retains context. Whilst it may be tempting to close the chat tab, or open new ones, maintaining this context can be key to getting better responses.

You can clear the conversation history by using the /clear command. Use this if you feel that the conversation has run its course, or has become circular.

**Chat interface Tabs**

You can have a maximum of ten chat windows currently.

**Copy and Pasting code**

When Amazon Q produces code in the chat interface, you will notice that there are two icons at the bottom of any code block which allow you to COPY the code into the clipboard, or INSERT INTO CURSOR, which will try and PASTE the code where your cursor is. The caveat here is that the cursor needs to be within a file in the IDE - it will not send that into the Terminal within VSCode or anywhere else.

Using these two buttons provides a simple and quick way of getting code from the chat interface and into your code.

**View and Apply Diff**

In recent updates to the Amazon Q plugin, where code suggestions are updates to existing code you will notice two other buttons appear - VIEW DIFF and APPLY DIFF. What these do is allow you to directly view the code differences between what you have and what the Amazon Q chat output is suggesting. You can then use the APPLY DIFF to automatically update the content.

---

### 8. Amazon Q Developer Agent for software development

Amazon Q Developer Agent for software development (/dev) is a powerful capability of Amazon Q that allows you to provide a prompt which will be analysed, broken down into a series of tasks, and then code generated. There are a few things you should know before using this:

* limited quota - you have a limited number of quota for using /dev, so you should use it wisely. If you are using Free Tier (Builder ID) then you will have five invocations per month.
* refine output from /dev - when you use /dev you have the possibility of providing feedback that will regenerate the code. This is not part of your service quota and so you should review carefully the initial output of /dev, and then use the "Provide Feedback and Regenerate" button to provide any refinements or updates you need. You can only do this three times though.
* use scaffolding - we mentioned scaffolding previously, which is a very helpful technique to ensure consistency in the output you get from /dev
* use cases - there are many use cases that are a good fit for /dev, and you will come to intuitively know when /dev vs other Amazon Q modalities are the right fit for what you are trying to do.

We will be using /dev later in this workshop, so you will get to see some of this in action.

---

### 9. Code Reference

One of the questions you might be asking yourself is as Amazon Q Developer provides code suggestions, how much of that code might come from the open source projects used to train the large language models behind it. Amazon Q Developer allows you to configure this - you can either explicityly turn off any code suggestions that match code from open source repositories, or you can leave it enabled, and Amazon Q Developer will notify you. In practice I have found that I rarely encounter this.

Check out [this very short video](https://www.youtube.com/shorts/Fmn37wGQUY8) that shows what this looks like when it does happen.

### Complete!

Ok, you are now up to speed with the Amazon Q Developer plugin, and it is time to see what you can achieve with it. Head over to the next section [Breaking down problems](breaking-down-problems.md).

