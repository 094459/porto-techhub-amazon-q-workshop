![Amazon Q Developer header](/images/q-vscode-header.png)

### Building our application - Part One

**Overview**

In the first part of this lab we are going to start by first looking at the data model for our application. As we are building a customer survey feedback application, we want to spend some time thinking about how to craft the right prompts.

> **Using Git branching when coding using AI coding assistants**
>
>Whilst you will be generating code in this lab, to make it easier to follow along I have provided a git repo that provides code that will support you as you explore. When you check out this repo there will be no code - don't worry, this is as per design. As we progress, we will use different branches within this repo to bring you to a working place. Feel free to ignore these and use your own code if you want. You can always reset and get back on track as the lab will provide necessary instructions.
>

**Creating our Python Virtual Environment**

From a terminal, navigate to a new directory where we will start work (I am using projects here as this is what I use, but feel free to switch this to whatever you use), and then type in the following to clone the repo into your workspace. 

```
cd ~/projects
git clone https://github.com/094459/q-developer-workshop-demo-code.git
cd q-developer-workshop-demo-code
code .
```
This will start VSCode in the sample code repo.

Once VSCode has started, the first thing we need to do is make sure that we are running in the Python virtual environment we created. Open up a Terminal in VSCode, and from that terminal run the following commands:

```
python -m venv .venv
source .venv/bin/activate
```

You should notice that the Terminal inside VSCode now has the (.venv) prefix, indicating you are running in this new virtual Python environment.

You should also switch your VSCode Python environment to use this. From VSCode press CTRL + COMMAND + P (Mac), or CTRL + SHIFT + P (Windows) and type in Python. From the list, select "Select Interpreter" and from the available options, make sure you select the one which has the correct directory location (.venv) which should be the recommended one. 

![Selecting Python interpreter](/images/q-vscode-python-env.png)

You are now ready to go.

---

**Lab 01-1 Our application - Creating our Data Model**

The application we want to build is a simple tool for collecting customer feedback. We are going to start by using Amazon Q Developer to help us define the data model for this application, providing various prompts that will help provide a good starting point of what we want our data model to look like. Once we have our data model, we can then start to create some code artefacts.

A key pattern of working with AI coding assistants like Amazon Q Developer is to take some time to articulate what you want them to do. In this instance, we want Amazon Q Developer to create our data model. Rather than just make it up on the fly, we should take some time to think about how to formulate it.

> **Optional Activity**
> 
> Before we proceed, spend time discussing in groups how you would define the data model for a customer feedback application. Using the starting point above, how would you improve it? Is there anything missing? How would you make it more precise or make it easier to understand.
>

The data model is a reflection of the User requirements of the application. For this simple customer feedback application, we might use the following to describe this.

> *Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to submit feedback.*


**Task 1**

We will now see what Amazon Q Developers thinks when we ask it. 

1/ Open up the Amazon Q Developer Chat interface, and from the prompt enter the following:

> Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to provide feedback.

Give the non deterministic nature of these tools, it is hard to predict the output you will get. 

We are going to now try again, and this time use a feature of the Amazon Q Developer that will help us personalize the output that we get. From the project workspace, we are going to create a file which will then be used as context by Amazon Q, and help shape the output. Follow these steps:

1. In the project directory you git cloned, create a folder called ".qdeveloper"
2. Add a file called - MY-PREFERENCES.md (you can call it something different, the file name is not that important)
3. Add the following text within this file

```
DEVSTYLE

Only when I explicitly ask for code, follow this guidance:

- Only provide SQL or Python code unless I explicitly ask for another language
- I am an expert in SQL and I did not need a walk through 
- I am an expert in Python and I did not need a walk through
- I have a strong preference for Sqlite
- I have a strong preference for developing code in Python version 3.10
```

We are going to use this file as additional context when prompting Amazon Q Developer. We are defining our particular style (for this workshop). You can use this technique yourself, changing it to suit what you want. For this workshop we are going to keep this.


So our project structure will look like

```
├── .qdeveloper
│   └── MY-PREFERENCES.md
└── .venv

```

How we tailor the output of Amazon Q Developer, is by using the **@workspace** feature of Amazon Q Developer. This feature is disabled by default (it is currently a BETA feature) and so we are going to have to enable it. Once enabled, this is going to index your local VSCode workspace, looking at all the files including the MY-PREFERENCE.md. Once the indexing has completed, we can use the @workspace in the Amazon Q Developer chat interface to add specific files as part of the context. In this case we are using it to help steer the kind of output we want Amazon Q Developer to give us, but we can use it for lots of other use cases too.

Right, lets enable this now.

---

**Task 2**

1/ Open up the Amazon Q Developer plugin settings (remember from the overview, using the link at the bottom of VSCode to bring up the menu, where you will find the "Open Settings" option). Look for the "Amazon Q: Workspace Index" section. This will have a check box next to it that will be blank (not set). Click on the box to enable this and then close the settings tab.

2/ From the Terminal menu options, select OUTPUT and then from the pull down menu, click on the down arrow to bring up all the different output otions. You should have a NEW entry called "Amazon Q Language Server". Click on this and you should see that it has started to index the files in this project. It will look something like this:

```
LSP server starts
Loaded model from /Users/ricsue/.vscode/extensions/amazonwebservices.amazon-q-vscode-1.27.0/resources/qserver
[Warn  - 16:44:27] Unknown tokenizer class "CodeSageTokenizer", attempting to construct from base class.
Using number of intra-op threads: 2
Embedding provider initialized.
Validating embedding:s1 0.26636229613723583, s2 0.20119692089068866, s3 0.4491747579475595
Indexing 2 files under rootpath: /Users/ricsue/Projects/amazon-q/workshop/q-developer-workshop-demo-code
Starting index 2 files
Indexing done for 1/2 files
Index complete! Take 21.269275083s. Total 2 files, 11 chunks
Index saved to /Users/ricsue/.aws/amazonq/cache/cache/d7118a0df04a8a3a08dcf3d3f868d272db1601d953802875b4be8bda158fe919-0.9-VSCode.index
```
You can also see the logs by changing the OUTPUT menu option to "Amazon Q Logs"

```
2024-10-03 16:44:27.504 [info] LspController: Starting to build vector index of project
2024-10-03 16:44:27.717 [info] LspController: Found 10 files in current project /Users/ricsue/Projects/amazon-q/workshop/q-workshop
2024-10-03 16:45:31.223 [info] AB Testing Cohort Assignments []
2024-10-03 16:45:36.759 [info] LspController: LSP server CPU 0.03829787234042553%, LSP server Memory 413.34375MB
```

>*Tip!* The directory where these indexes are created can be deleted if needed. As this is still a BETA capability, sometimes you might need to delete the index files and then restart the IDE to recreate them if you start getting strange error messages. 

We can now try this feature out.

---

**Task 3**

1/ From the Amazon Q Developer Chat interface, type @ and you should see workspace appear. Tab to complete that, and then add the following to your prompt:

> @workspace DEVSTYLE Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to provide feedback.

Hit return and review the output. You should get very different output this time. 

2/ Make a change to the MY-PREFERENCES.md file, changing sqlite to a different database (I tried this with Oracle, but feel free to experiment). Try the same prompt again after a few moments. Did you get different output? Change the text in MY-PREFERENCES.md back to what it was.

We are going to re-run this prompt in the next task - here we just wanted to show how you can influence the output of what Amazon Q Developer can produce.

---

**Task 4**

Now that we have seen how to tailor the output we get from Amazon Q Developer, we will use this as we create our data model. You can do this a number of ways, and it will vary between your preferences and the norms and guidelines you might need to adopt where you are developing. We will show you how to create both SQL and Python code that will generate your tables.

*Generating SQL*

1/ First we are going to create a folder called "data" and create a new file called "customer-feedback.sql". This will be empty for the time being, but we will paste SQL into this file as Amazon Q generates output. We will use this file to create the tables in our database - for the purposes of making this easy to follow, we will use sqlite.

2/ Run the prompt from the Amazon Q Developer chat interface

> @workspace DEVSTYLE Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to submit feedback. 

Review the SQL - does it look right?

*Generating SQL*

3/ Run this modified version of the prompt. This time we have added "I want to code in Python" which should provide different output.

> @workspace DEVSTYLE Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to submit feedback. I want the code in Python.

Review the output. 

1. Create a new file called "customer-survey.py"
2. Paste the code from the Amazon Q Chat interface into this file.

Take some time to review the code, and use the Explain feature if needed. 

Before we run this code, it is likely you will need to install some Python libraries before you can run the code. Run the following from the VSCode terminal making sure that you are still in the Python virtual environment - your prompt should start (.venv)

```
pip install sqlalchemy
```

Run the code

```
python customer-survey.py
```

You should see a new sqlite database created in the local directory. 

> **Help!** If you get an error when trying to run your python code, copy the error message and then ask Amazon Q Developer to help you. It will be able to guide you through to a solution which you can then try by running the Python file again.

If you have installed the VSCode plugin Database JDBC Client, you should be able to connect to this and see that the tables have been created. 

![Exploring the created data](/images/q-vscode-sqlite-overview.png)

4/ Before proceeding with the next section, we need to do a couple of things:

First we need to delete the sqlite database file that was just created. Don't worry, we will be re-creating it. So from the Files section of the VSCode, locate and then delete the customer_survey.db (or if it was called something different) from your project directory.

Second delete the customer-survey.py that you created. In the next lab we are going to create our application using the data model that we added to the sql file

Once you have done these two things, your directory structure should now look like this:

```
├── .qdeveloper
│   └── MY-PREFERENCES.md
└── .venv
└── data
    └── customer-feedback.sql
```

Confirm that this is what your environment looks like before proceeding to the next step.

**Complete:** You have now completed the first part of this lab, and created your data model. You can now either tak an optional lab that explores how you can use Amazon Q Develoepr to help you with data [Working with Data](working-with-data.md), or you can proceed to part two of building our application, [Part Two](building-our-app-part-2.md)


