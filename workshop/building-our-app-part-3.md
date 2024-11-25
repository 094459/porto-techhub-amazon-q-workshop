![Amazon Q Developer header](/images/q-vscode-header.png)

### Building our application - Part Three (final)

In our final lab we are going to get our application ready for shipping. We are going to do a few things:

* Use the Amazon Q Security Scan feature to identify any issues with our code that we need to fix
* Look at what we need to do to make our project "Open Source"
* Add documentation to our project, creating a README file

---

**Task 14**

We have some code, but how robust is it? In this lab we are going to use a feature of Amazon Q Developer to scan the project and help us shift left with security. This allows us to proactively detect and then resolve issues in our code, closing that feedback loop. Lets see how this works.

**Don't worry we are not going to spend too much time resolving the issues here, but it is important that you get a feel for how this process works**

1/ Click on the Amazon Q on the bottom status bar to bring up the Amazon Q Developer options, and select **"Run Project Scan"** from the menu. You should see that this kicks off and a popup will appear in the bottom right of your VSCode.

This will take a few minutes, but it should come back when its finished. 

**If you want to go grab a drink or stretch your legs, now is a good time!**

2/ Review the output, which will appear in the "Problems" tab. There is likely going to be a LOT of input, as the security scan will also scan your dependencies. What we really care about is our application files, so scroll to the bottom of the list.

You will see after reviewing these, that some are valid issues that you need to work on, whilst others are how the application is supposed to work and are false positives which can be safely accepted (for example, you will get CWE-862 - Missing Authorisation which in this particular application is correct, as we want to make our surveys sharable and we do not need nor want those people providing feedback to need to authenticate first)

3/ You can use Amazon Q to help you understand your issues. For example, you can use the Amazon Q chat interface and ask questions like:

> Explain CWE-94 Unsanitised input as run code

Which should provide some explaination with options on how you can address this issue.

---

**Task 15**

Now that my project is ready for the world to see, I have decided that I am going to open source this project as I want to build a community of people who might be interested in helping me improve the code and make it better.

You can ask Amazon Q Developer to provide some guidance on what I need to do.

> **Warning!!** This guidance should be used in conjunction with conversations you have with any folk that you work with on Intelectual Property. This guidance here is only to show you how Amazon Q Developer can help you ONCE you have had those conversations and decided that open source is the way you want to go.

1/ As I think about the best way of using Amazon Q to do this, this is going to need to review all the files in the workspace. There are two ways I could approach this. Using the native Amazon Q Developer Chat interface, or by using the Amazon Q Develoepr Agent for software development (/dev). 

I do not really want to use one of my /dev quotas, so I decide that I am going to use @workspace, and this is the sample prompt I use:

> @workspace I want to open source this project using an Apache 2.0 licence. My company name is Beachgeek Enterprises so please update any copyright messages accordingly. How do I need to update this projects files?

2/ I am happy with the output it provides (see below), but I think it could be improved.

![example output of helping me open source my project](/images/q-vscode-open.png)

I follow this up with some more specific information:

> I want to include SPDX headers in the files, what do these look like

3/ You might need to do this if you have any specific requirements you need to meet that come out with conversations with your open source program office (OSPO) - if you have one.

Explore this and update your code.

---

**Task 16**

Documentation is a critical part of every application, and yet sometimes this is lacking in the code and projects we have to work with. We can use Amazon Q Developer to help us automate this task, updating both documentation in code, as well as creating README files to help others understand how to use this code. Lets create some documentation for our project.

We are going to do this using a number of techniques as I find that as you write code, they can all be used successfully as you code - no need to wait until the end. Taking a step back, as we think about how we approach documenting our project, we might want to:

* document our code (functions, imports, logic, etc) as we go along
* create higher level documentation (README, maintainance or operational, etc) at the very end once the rate of change of the application changes.

We will work from the baseline project code, so stop the application if it is currently running and then from the terminal:


*Documenting code blocks*

There are a number of ways we might approach documenting our code as we write it. We can use:

* Amazon Q inline prompts to add the documentation by selecting the block and then doing CONTROL + I and entering a prompt such as "Doucment this code block"

* Use @workspace and ask it provide documentation for our code. We might use a prompt like this - "@workspace Add doc strings to the app.py and document how the code works, providing doc strings for each function and each route"

* Use the Amazon Q menu integration, selecting a code block and then using the same prompts as above

* Use the Amazon Q Developer Agent for software development (/dev) and ask it to write the documentation for us. We might use a more specific prompt to guide it to what we want documented and the level. We need to counter that by the fact that we will be using one of our quote for /dev. You will need to weigh ypthe size and complexity of your project, against the amount of time/effort you think it might save.

*Creating README*

To create documentation for the entire project, we again have options. These vary based on the effort required, so you should review this before deciding.

* Using @workspace with prompts such as "Create a README.md that documents the application. I want to document the codebase, how the application works, how to start the application, how to use the application" - you can add more, this is just a particular example

* Use /dev as per the previous example

1/ From the codebase, select a block of code and try using the inline (COMMAND + I) prompt with the following

> provide a docstring this code block

2/ From the codebase, select a block of code, and then right click on the menu, and select Send to Prompt. On the chat interface, add "Provide documentation for this code block"

3/ From the Amazon Q Chat interface, enter the following prompt:

>@workspace Create documentation for the application code in app.py

4/ From the Amazon Q Chat interface, we will use /dev to get the Amazon Q Developer Agent for software development to write our documentation for us. After entering /dev, use a prompt like this

>/dev I want you to document this project. 1/ Create a README.md that outlines how the application works, how to install and get started, and how to use the application, 2/ Document the code with docstrings to explain how the code works, 3/ Provide a User guide that can be used to help someone understand how to use the application


When it has produced the updated code and documentation, do NOT automatically accept it. Review it. Is there anything missing? If you are not entirely happy, use the "Provide feedback and regenerate" button, and provide some follow up feedback

Once you have experimented with this, you can compare how your documentation looks like with the workshop baseline code

---

### Congratulations!

You now have completed thie workshop, congratulations.

One final ask is to complete a survey. This will unlock some additional content, including 30 tips to help you supercharge your Amazon Q development.

[Take the survey here](https://pulse.aws/survey/1DM5TAZU)

You can return back to the [Starting Page](/README.md) to find out about additional resources that will help you stay on top of new updates and improvements with Amazon Q Developer.
