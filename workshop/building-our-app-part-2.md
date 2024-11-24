![Amazon Q Developer header](/images/q-vscode-header.png)

### Building our application - Part Two

**Overview**

In part twp of this lab we are going to take the data model that we created and start to build our application. We are going to use Amazon Q Developer Agent for software development to automate the creation of this code. Amazon Q Developer Agent for software development takes your prompt and then breaks this down into a series of tasks. As it starts to reason about those tasks, it will start to review the existing files you have in your project (in this case, our sql code) and then start writing code. Once Amazon Q has finished, it will present the final output for review, allowing you to test and review the code. At this point you can then provide feedback to adjust or accept the code as is.

This process take around 5-6 minutes, so plenty of chance for you to grab a drink or have a stretch.


**Task 5** You can either stick with the code that you created in Part One, or you can reset your code based on the sample project by using the following command:

```
git checkout lab-01
```

This will reset your local environment so that you just have the data model and initial Python classes created. You should run "python customer-survey.py" before proceeding, which will create a local sqlite database in your directory.

**Lab 02-1 Creating the application**

In this lab we are going to use Amazon Q Develoepr Agent for software development to CREATE code. As we are using the free tier (we have signed in using our Builder ID's) then we have up to five uses of this per month, so use them wisely.

**Task 6**

Open up the Amazon Q Developer Chat interface, and from the prompt enter hit the / key, and from the pop up select **/dev** and hit enter. You should now copy the prompt below and then hit enter again.


> Using the customer-feedback.sql file for reference, create a Python web application using the Flask framework that will create a Customer Feedback application. The application will allow users to register and then login. Once logged in, users will be able to create Surveys. The application will also provide a URI that will allow people accessing the application to provide feedback on a specific Survey.

This is what it should look ike:

![Kicking off /dev](/images/q-vscode-kickoff-dev.png)

This process is likely to take 4-5 minutes, but keep an eye on what is happening as the status of tasks will be updating in realtime, as well as it displaying what files it is using and what files it will be creating.


**Task 7**

Once it has completed, click on the files in the "Code Suggestions" box. Review the code. As you begin to use these tools on a daily basis, you will need to think about a review process that works for you. This is what I am currently doing, but you should think about what works for you:

* Did the code produce what I expected? Did it follow the guiding prompt well enough?
* Do I understand the code
* Can I spot any obvious issues or omissions

This is just a few of the things I think about when reviewing the ouput. Once I have reviewed the code, there are two options:

1. If you are happy, use the feedback icon (Thumb UP or Thumb DOWN) to provide feedback before hitting the "Insert Code" button.
2. If you want the Agent to do more work, then use the "Provide feedback and regenerate"

When I have run this prompt, the output provided can go one of two ways: the first is that it generates working code, but the code only provides an API, and the second is working code that also provides a web application that you can begin using.

If I get the first, I typically select the :Provide feedback and regenerate" button. These are some of the prompts you might get if you got the first options (API), but you can review these and think of perhaps better ones.

* Can you provide full working code. Ensure you provide code that will create a web application that users can use via a web browser.
* Provide updated code that will allow a user to use this via a web browser
* Update the code generated so that the application can be used by a web browser. Provide sample html files and css so that I can adjust the look and feel of the application

Once you have either reviewed and are happy with the code, or provided feedback for regeneration and are then good with the output, you will hit the Accept Code and you will now find you have the start of your application. The next task is going to be running it.

**Task 8**

If you review the code within your IDE, you will notice that the linter has shown some errors - it doesn't know about some of the new libraries the new code wants to use. We can ask Amazon Q via the chat interface to help us.

> @workspace what libraries does app.py require me to install

Review the output. This is what I got, your output might be different

```
pip install Flask Flask-Login Flask-SQLAlchemy Flask-Bcrypt Flask-JWT-Extended SQLAlchemy marshmallow

```

After a few moments, you should see the linter errors disappear.

**Task 9**

We can now run our application by using the following command:

```
python app.py
```


With a but of luck, your application should start and you will be able to access it via a browser. Make sure you use http://127.0.0.1:3000 when accessing the local Flask application.

If your application does not work, don't worry. Welcome to the world of your trusty AI debugging assistant. Use the Amazon Q chat interface to help you. To maximise the effectiveness, do the following: 

* close all your VSCode tabs and just leave the app.py open. This helps provide Amazon Q with the right context. 
* review the error message and just select the most important part of the error to help Amazon Q focus on the right thing
* review error messages either in the terminal or in the web browser to help isolated the best error message
* sometimes you will need to add further information (context) to help Amazon Q troubleshoot the issue and give you the right information

You can use prompts along the lines of:

* Starting the app generated << insert error >> - how do I fix
* How do I fix this error - << insert error message >>

You might also need to have follow up prompts. You might fix one issue, only to have another one. Continue to cycle through the errors using the same process.


**Task 10**

If you have the app currently running, exit (CTRL + C) as we are going to reset back to the workshop codebase.

1/ To reset your code to the workshop baselone, use the following command:

```
git checkout lab-02
```


2/ With our application now running, open a browser and try and register and login. Are you able to log in successfully, or do you get an error? If you are using the code in the repo, you should be ok and be able to register and login. If you are using your own code, then try registering a user and see how you get on. 

> **Hint!** In previous times when this workshop has run, a very common error is "Method not allowed". Use Amazon Q to help fix this issue. For example, you could use something like this "@workspace when trying to login or register, the application is generating a 405 error, method not allowed. How do I fix this?" if you were seeing specific error messages in your logs around 405 errors.


3/ After you have logged in, try creating a customer survey. Once created, complete one to make sure the application is working ok. You might notice something - whilst you can create surveys and complete them, there is no way you can currently view the results of a survey. We will fix thatin the next task.

**Task 11**

In this task we are going to add a way of view the results of a customer survey.

1/ Scroll down to the end of the Flask routes, and press COMMAND + I to open up the Amazon Q in-line editor.  From the prompt that appears add the following:

> Add a view to display the results of the customer feedback surveys

You should see that Amazon Q starts writing code within the actual Python file itself. It should only take a few seconds. Review the code, and if you are happy with it hit ENTER to accept.

2/ The in-line prompt allows you to create code within the single file, but the output produced requires a new file (typically this will return a html file called survey_results.html). We can use the chat interface to help us with the code for that. From the Amazon Q Developer chat interface I enter:

> @workspace create code for the survey_results.html that the /survey/<int:survey_id>/results route will use

Review the output and implement the code. 

> Depending on how the code is implemented, you might need to manually enter the URI in the browser. Sometimes the code suggestions to not include updating other components of the application. We will look at that in a minute.

Test it - did it work? This is what it looked like for me when I did this. You **WILL ALMOST CERTAINLY** have something different, and that is ok.

![example survey result](/images/q-vscode-survey-results.png)

We will follow up and ask Amazon Q to help us fix navigation links to the results. In the Amazon Q chat interface, I prompt:

> @workspacethis this code works great. however, there I need to update the rest of the code so that it provides links to see the results. can you update the code to provide links to the survey results.

> @workspace on the survey_results.html page, add a return to homepage link

Review the code and try again? Does it work as expected?

**Task 11**

You might have noticed when testing the application code, that it might do things that you did not expect or want. This is quite normal, but we can use the power of CHOP (Chat Orientated Programming) to help refine our working codebase. We are going to switch to the workshop repo and then fix one particular issue. In this version of the code, you can only submit survey responses if you privide an email address. We want to change this so that anayone can submit a response.

If you have the app currently running, exit (CTRL + C) as we are going to reset back to the workshop codebase.

1/ To reset your code to the workshop baselone, use the following command:

```
git checkout lab-03
```

2/ Think about which feature of Amazon Q Developer you think might be the best way to fix this?

* Editor in-line
* Chat interface
* @workspace
* /dev

As you start getting used to using Amazon Q Developer on a daily basis, you will need to be constantly reviewing the most appropriate modality for a given use case. Some of the things to think about include:

* What context does the task I am looking to get help with need? If you need broad context then something like @workspace might be a good idea
* What is the scope of the change? Do I know what I need to update? If it is just one file then using the in-line capabilities might be a good option
* Do I need to make broad and wide changes? If you are looking at significant changes, maybe Amazon Q Developer Agent for software development is the right option. Bear in mind when using this though, that you have service limits you need to work within

In this particular case I am going to use @workspace as I do not really know what files I might need update, so I need a broad context.

> @workspace Update the project so that when completing a survey, email addresses are optional

Review the output you get. You should see that there are changes needed to both the data model, as well as the application itself. The data model changes will also need you to run a database migration task.

> Tip! If you get errors around various Python libraries not available (ModuleNotFoundError: No module named 'flask_bcrypt' for example), deactivate and then reactivate your Python virtual environment and try again

I updated the local sqlite by doing the following:

* run - flask db init
* run - flask db migrate -m "Email update"
* run - flask db upgrade

Start the applicaiton and try again and see if you can now submit without an email address. You can see the working code [here](https://github.com/094459/q-developer-workshop-demo-code/tree/lab-04)


**Task 12**

We often need to add new features to applications, whether these are code bases we know and understand, or not. In this lab we are going to add the ability to export survey data as a csv file.

If you have the app currently running, exit (CTRL + C) as we are going to reset back to the workshop codebase.

1/ To reset your code to the workshop baselone, use the following command:

```
git checkout lab-04
```

2/ We can now start thinking about how to export the survey data. A big part of using tools like Amazon Q Developer, is thinking about and breaking down problems BEFORE we ask for code. Sometimes you might use the Chat interface questions to help better understand your options (so not code related). For example, you might ask Amazon Q about different export data file types. This is critical to make sure that you craft the prompt that will help you achieve what you are looking to do. In this instance, having thought about it, this is what I want to do:

* I want to export data in CSV file format
* I want to provide a link on the results page to export the data
* I want to use the survey name as the export file name
* I want the option to exclude email addresses if provided from the export

Thinking about what changes we might need to make, it is likely we are going to impact multiple files. I decided that @workspace is probably going to be the best option here.

> @workspace Update the code to this application to add the ability yo export the results of a customer survey as a CSV file. The export file name should be the same as the survey. The export should only appear on the results page. An option should be provided that allows for the export to either include or exclude email addresses

Review the output and follow the tasks. You might encounter a few errors and issues, typically along the lines of:

* the export code does not work due to outdated methods
* the export code generates errors such as " TypeError: a bytes-like object is required, not 'str'" or "ValueError: Files must be opened in binary mode or use BytesIO."
* the export works, but you get no email addresses 

Use the Amazon Q Chat interface to help you troubleshoot these issues, using prompts such as the following as a guide (you will have different errors most likely):

* running this code generates an error when exporting: ValueError: Files must be opened in binary mode or use BytesIO.
* this generates another error - TypeError: a bytes-like object is required, not 'str'
* The export works, but I am not seeing emails when I select email to be exported



I want to change the style of the export output. As I already have everything I need, and am just changing the function, this time I select the export function and then press COMMAND + I to bring up a prompt window. I add

> Update the code so that the export file has one row for every feedback submission

You will see Amazon Q start working, highlight new or changes in red/green. This is what mine looked like (yours will be different)

![Amazon Q Developer inline change](/images/q-vscode-inline-diff.png)

I hit return after reviewing, and test it out. This time my export file now has a line for each submission.


**Task 13**

We have a solid working application, but there are still things to be done. In this lab we will add an about page that explains how to use this application.To make it a bit more interesting, we will add a fun capability to displays some Yoda wisdoms. 

If you have the app currently running, exit (CTRL + C) as we are going to reset back to the workshop codebase.

1/ To reset your code to the workshop baselone, use the following command:

```
git checkout lab-05
```

2/ Open up the app.py file. We are first going to create a new function that will return a random quote which we will include in our About page. We know we will need to create a new function as well as a new html file, so we might be tempted to use @workspace. This time I am going to use the in-line prompt to create the function. 

First, position the cursor to where you want the new code to be created at. I position my cursor just before the @route definitions. After clearing a few lines, I press COMMAND + I, and from the prompt I type:

> Create a function that will return a single random quote of wisdom from Jedi Yoda

You should see new code that provides a new function. Review the code produced - does it look good? If you want to modify or change it, you can select the entire block and use COMMAND + I again. The scope of changes  (context) made will just what you selected. 

3/ Now that we have our function, we can use this when adding a new About page. We will try a new prompt from the editor, this time moving the editor to the #Routes section, and after the initial root route. Again we can use the inline editor for this, so I select at the end of the routes, and enter this into the inline prompt. 

> Add a route for /about that will display a new html page called about.html that includes a quote from the get_yoda_wisdom function

Review the new route that is created and refine as you feel needed.

4/ We are not quite there yet, as we have the function, and a new route defined but we do not have the html page. This time we are going to ask the Amazon Q Developer Chat interface to provide the code. From the chat interface experiment with the following prompts:

> Create code for a new about.html that uses the /about route and displays output from the yoda function
> @@workspace Create code for a new about.html that uses the /about route

Review the output and see what you think looks best. Feel free to experiment with different prompts to see what you get.

5/ We are not quite done yet. Whilst we have everything working, we need to update the navigation to have a new link. Navigation is managed by the base.html file. Open this file, and then select all (CTRL + A) so that all the code is highlighted. We will use Amazon Q's inline promot (COMMAND + I) with the following

> update navigation to include a link to the /about route

You should see it working through the code, and update it with a single entry. Review this to make sure it looks ok, and then hit ENTER. Refresh the application and see if your navigation has been updated.


At the end of this you can reset your codebase to the workshop baseline using the following command:

```
git checkout lab-06
```

**Task 14**

As you are working on your code, you are occasionally going to encounter issues which take time to debug, and then fix. Amazon Q Developer can help decrease the time it takes to find those issues and suggest fixes. In this lab we are going to explore some of those options.

We are going to checkout a branch of the application that has issues/problems which we need to fix. Run the following commands

```
git checkout lab-07
```

1/ Try running the application and then trying the following:

* access the home page
* access the about page

What has changed? You should see that you no longer see the surveys, or get the quote from Yoda. We can use Amazon Q to help us fix these kinds of issues, when there are no error messages. We will try two different approaches:

2/ Open up the app.py and select the code index route, and then use the integrated Amazon Q menu option Send to Prompt (right click, Amazon Q, Send to Prompt) and then enter

> This code is not working, please can you fix

Review the output. It should provide everything you need to fix. Once you have implemented the change, try the home page again. Did you fix the problem?

3/ This time select the code for the about route. Bring up the inline promot (COMMAND + I) and then enter the following

> fix this code which is not working

Watch as Amazon Q reviews and the provides update to the code. Accept the change, save the file and try the about page. 

You should now have a working application again.

*Additional hints on fixing errors*

This short lab just touched upon the troubleshooting capabilities that can be addressed using Amazon Q Developer. As you develop your application and then deploy those application to the Cloud, you are going to generate a number of different messages. Amazon Q Developer can help you locate where those issues are likely to be and provide useful or helpful guidance. 

Beware though, it is not perfect and sometimes there are going to be errors where you are still going to need to revert back to traditional ways. But in most cases you are going to get quick answers to those annoying issues: typos, missing items, etc

**Task 15**

We are almost done. At the last minute, after testing we realise we need to create a simple update to the application so that we can add a "share survey link" option to the surveys we create. This will allow us to very easily provide these to folk we want to collect feedback from.

We are going to checkout a branch of the application that has issues/problems which we need to fix. Run the following commands

```
git checkout lab-06
```

1/ Think about how you might implement this change. It is likely that multiple files might need to be changed, so I am going to go with @workspace to help me this time. 

I close all open tabs, with just the app.py and index.html open. I then use this prompt:

> @workspace Can you add a link on the homepage that provides a "share link" that copies the link to the clipboard for each survey listed

Review the output. It should just suggest making changes to the index.html page - as it turns out, no other changes are needed.

You might want to experiment and improve the code. Here are some follow up prompts I used as I was not initially happy with how the link sharing was handled

* instead of the current link, can you change so that it just shows an icon image for sharing
* can you use just a text link next to the existing links

If you want to see the final working code that it generated for me, and to reset back to the workshop code baseline, first stop the application currently running, and then run:

```
git checkout lab-08
```

Restart the application and you should now see that there is a share link that copies the customer surveys into the clipboard.


**Complete:** You now have a working application, made some improvements and optimisations, now we are ready for the last few tasks we need to do as a developer. Proceed to the final lab, [Part Three](building-our-app-part-3.md)





