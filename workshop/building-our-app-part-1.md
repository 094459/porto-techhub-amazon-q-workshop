![Amazon Q Developer header](/images/q-vscode-header.png)

### Building our application - Part One

**Overview**

In the first part of this lab we are going to start by first looking at the data model for our application. As we are building a customer survey feedback application, we want to spend some time thinking about how to craft the right prompts.

**Creating our Python Virtual Environment**

From a terminal, navigate to a new directory where we will start work (I am using projects here as this is what I use, but feel free to switch this to whatever you use), and then type in the following. 

```
cd ~/projects
mkdir porto-q-workshop
cd porto-q-workshop
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

A key pattern of working with AI coding assistants like Amazon Q Developer is to take some time to articulate what you want them to do. In this instance, we want Amazon Q Developer to create our data model. 

> **Tip!** When doing thisin real life, do not just make it up on the fly! Take some time to think about how to formulate it. The more you use tools like Amazon Q Developer, the more natural and easier it will get

The data model is a reflection of the User requirements of the application. For this simple customer feedback application, we might use the following to describe this.

> *Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to submit feedback*


**Task 1**

We will now see what Amazon Q Developers thinks when we ask it. 

1/ Open up the Amazon Q Developer Chat interface, and from there enter the following:

> Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to provide feedback.

Give the non deterministic nature of these tools, it is hard to predict the output you will get! Review the output - does it make sense? What is it missing? How would you improve it? Or perhaps, it did a good job and you are happy about it. As you use these tools more, you should be constantly reviewing the ouput. Do **NOT** assume that the ouput is always going to be right.

**Task 2**

1/ We are going to now try again, and this time use a feature of the Amazon Q Developer that will help us personalize the output that we get. From the project workspace, we are going to create a file which will then be used as context by Amazon Q, and help shape the output. Follow these steps:

1. In the project directory you git cloned, create a folder called ".qdeveloper"
2. Add a file called - DEV.md (you can call it something different, the file name is not that important)
3. Add the following text within this file

```
DEVSTYLE

Only when I explicitly ask for code, follow this guidance:

- Only provide Python code unless I explicitly ask for another language
- I am an expert in Python and I did not need a walk through
- I have a strong preference for developing code in Python version 3.10
```

> You can review [this example](https://github.com/094459/porto-techhub-amazon-q-workshop/blob/main/.qdeveloper/DEV.md) if you are not sure.

We are going to use this file as additional context when prompting Amazon Q Developer. We are defining our particular style (for this workshop). You can use this technique yourself, changing it to suit what you want. For this workshop we are going to keep this.


So our project structure will look like

```
├── .qdeveloper
│   └── DEV.md
└── .venv

```

How we tailor the output of Amazon Q Developer, is by using the **@workspace** feature of Amazon Q Developer. This feature is disabled by default (it is currently a BETA feature) but you will already have enabled it as part of the exploring Amazon Q section (If you skipped that, then now is the time to ENABLE it). 

Once enabled, this is going to index your local VSCode workspace, looking at all the files including the DEV.md. Once the indexing has completed, we can use the @workspace in the Amazon Q Developer chat interface to add specific files as part of the context. In this case we are using it to help steer the kind of output we want Amazon Q Developer to give us, but we can use it for lots of other use cases too.

>*Tip!* The directory where these indexes are created can be deleted if needed. As this is still a BETA capability, sometimes you might need to delete the index files and then restart the IDE to recreate them if you start getting strange error messages. 

We can now try this feature out.

---

**Task 3**

1/ From the Amazon Q Developer Chat interface, type @ and you should see workspace appear. Tab to complete that, and then add the following to your prompt:

> @workspace DEVSTYLE Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to provide feedback.

Hit return and review the output. How was the output different? 

2/ We are now going to create a new file in the .qdeveloper folder, called DBA.md. Add the following text to this file:

```
DBA

Only when I explicitly ask for code, follow this guidance:

- Only provide SQL code unless I explicitly ask for another language
- I am an expert in SQL and I did not need a walk through
- I have a strong preference for Sqlite
```

Notice that the first line contains "DBA", and we can use this to grab this context in the prompt. Save and close the file.

From the OUTPUT menu (if you do not see this, make sure you have the Terminal tab open), and from the pull down menu, select Amazon Q Language Server. You should see something like this:

```
[Info  - 22:26:39] Adding file to vector index: /Users/ricsue/Projects/amazon-q/workshop/porto/porto-q-demo-code-2/.qdeveloper/DEV.md
[Info  - 22:36:19] Adding file to vector index: /Users/ricsue/Projects/amazon-q/workshop/porto/porto-q-demo-code-2/.qdeveloper/DBA.md
```

> **Tip!** As Amazon Q Developer Workspace Index is a beta feature, we will sometimes need to go into the logs to see if it is behaving as expected.



3/ We will now try the same prompt again. From Amazon Q Developer chat interface, type the following:

> @workspace DBA Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to provide feedback.

Review what Amazon Q Developer produces. Did you get different output? You can use this technique to help provide more consistent output that is in line with how **YOU** want to work.

---

**Task 4**

Now that we have seen how to tailor the output we get from Amazon Q Developer, we will use this as we create our data model. You can do this a number of ways, and it will vary between your preferences and the norms and guidelines you might need to adopt where you are developing. We will show you how to create both SQL and Python code that will generate your tables.

*Generating SQL*

1/ First we are going to create a folder called **"data"** and create a new file called **"customer-feedback.sql"**. This will be empty for the time being, but we will paste SQL into this file as Amazon Q generates output. We will use this file to create the tables in our database - for the purposes of making this easy to follow, we will use sqlite.

2/ Run the prompt from the Amazon Q Developer chat interface

> @workspace DBA Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to submit feedback. 

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


