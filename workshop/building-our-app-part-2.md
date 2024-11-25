![Amazon Q Developer header](/images/q-vscode-header.png)

### Building our application - Part Two

**Overview**

In part twp of this lab we are going to take the data model that we created and start to build our application. We are going to use Amazon Q Developer Agent for software development to automate the creation of this code. Amazon Q Developer Agent for software development takes your prompt and then breaks this down into a series of tasks. As it starts to reason about those tasks, it will start to review the existing files you have in your project (in this case, our sql code) and then start writing code. Once Amazon Q has finished, it will present the final output for review, allowing you to test and review the code. At this point you can then provide feedback to adjust or accept the code as is.

This process take around 5-6 minutes, so plenty of chance for you to grab a drink or have a stretch.

---

**Task 10** 

In this lab we are going to use Amazon Q Develoepr Agent for software development to CREATE code. As we are using the free tier (we have signed in using our Builder ID's) then we have up to five uses of this per month, so use them wisely.

1/ Close all current open files/tabs in VSCode. Close all Amazon Q chat windows.

2/ When using Amazon Q Develoepr Agent for software development, it is a good idea to have any resources that will help influence the output available before you run. We have already seen how creating the DBA.md influenced the generation of output, we can do the same at a project level.

3/ Create a new directory called **"project"** and within this create a file called **"PROJECT-STDS.md"**.

Copy the following into this file:

```
When creating new Python code, use the following guidance

- Generate code using the following structure and layout

├── static/
├── models/
├── routes/
├── templates/
├── healthcheck/
├── tests/
    ├ conftest.py
├── Docker/
    ├ Dockerfile

```

If you check the Amazon Q Language Server logs, you should see that this file has been added to the index.

4/ Open up the Amazon Q Developer Chat interface, and from the prompt enter hit the / key, and from the pop up select **/dev** and hit enter. You should now copy the prompt below and then hit enter again.


> /dev Using the customer-feedback.sql file for reference, create a Python web application using the Flask framework that will create a Customer Feedback application. The application will allow users to register and then login. Once logged in, users will be able to create Surveys. The application will also provide a URI that will allow people accessing the application to provide feedback on a specific Survey.

This is what it should look ike:

![Kicking off /dev](/images/q-vscode-kickoff-dev.png)

This process is likely to take 4-5 minutes, but keep an eye on what is happening as the status of tasks will be updating in realtime, as well as it displaying what files it is using and what files it will be creating.

> **Warning!** Remember that once you fire off an invocation of /dev this will be one of your alloted attempts for the month. There is a **Stop** button, but this will only stop the current generation. This is equivilant of using the "Provide Feedback and re-generate" button.

**This is a great time to stretch your legs, grab a coffee**

5/ Once it has completed, click on the files in the "Code Suggestions" box. Review the code. As you begin to use these tools on a daily basis, you will need to think about a review process that works for you. This is what I am currently doing, but you should think about what works for you:

* Did the code produce what I expected? Did it follow the guiding prompt well enough?
* Do I understand the code
* Can I spot any obvious issues or omissions

This is just a few of the things I think about when reviewing the ouput. Once I have reviewed the code, there are two options:

1. If you are happy, use the feedback icon (Thumb UP or Thumb DOWN) to provide feedback before hitting the "Insert Code" button.
2. If you want the Agent to do more work, then use the "Provide feedback and regenerate"

When I have run this prompt, the output provided can go one of two ways: the first is that it generates working code, but the code only provides an API, and the second is working code that also provides a web application that you can begin using.

If I get the first, I typically select the **"Provide feedback and regenerate"** button. These are some of the prompts you might get if you got the first options (API), but you can review these and think of perhaps better ones.

* Can you provide full working code. Ensure you provide code that will create a web application that users can use via a web browser.
* Provide updated code that will allow a user to use this via a web browser
* Update the code generated so that the application can be used by a web browser. Provide sample html files and css so that I can adjust the look and feel of the application

Once you have either reviewed and are happy with the code, or provided feedback for regeneration and are then good with the output, you will hit the Accept Code and you will now find you have the start of your application. The next task is going to be running it.

---

**Task 11**

1/ If you review the code within your IDE, you will notice that the linter has shown some errors - it doesn't know about some of the new libraries the new code wants to use. We can ask Amazon Q via the chat interface to help us.

> @workspace what libraries does app.py require me to install

Review the output. This is what I got, your output might be different

```
pip install Flask Flask-Login Flask-SQLAlchemy Flask-Bcrypt Flask-JWT-Extended SQLAlchemy marshmallow

```

After a few moments, you should see the linter errors disappear.

2/ We can now run our application by using the following command:

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

Common problems that you will need to fix include:

* addressing circular imports
* incorrect __init__ files

You might also need to have follow up prompts. You might fix one issue, only to have another one. Continue to cycle through the errors using the same process. If you cannot get the application working, then you can see the code that it generated for me [here](https://github.com/094459/porto-tech-hub-amazon-q-working-app). This might help you identify and troubleshoot issues.

Don't worry,it might take you a few minutes to chase down all the errors until you are able to start the application!

3/ With our application now running, open a browser and try and register and login. Are you able to log in successfully, or do you get an error? If you are using the code in the repo, you should be ok and be able to register and login. If you are using your own code, then try registering a user and see how you get on. 

4/ After you have logged in, try creating a customer survey. Once created, complete one to make sure the application is working ok. You might notice something - whilst you can create surveys and complete them, there is no way you can currently view the results of a survey. We will fix thatin the next task.

---

**Task 12**

You might have noticed that whilst the application looks ok, you might still a few issues. In the code that I shared above, the issues included:

* Not providing a link to take a survey
* Not providing a link to add additional options when creating a survey

We can address those now.

1/ Closing all tabs/files open, I open a new chat tab and enter the following:

> @workspace When listing surveys, there is currently no link that allows me to access the survey to complete it

Review and follow the output, and then follow the instructions on how to update. Once you have done this, try again.

2/ Now let us fix the issue with only two options being available. We want to be able to add up to five different options. We know from looking at the application, that there is an html form that manages how many options we have. Find and open that file (closing any others you might have open)

From the same chat tab, we enter the following:

> how do I update this template to allow 2-5 options to be entered

The output I get is what I expect. When you run this, what does yours look like?

> **Tip!** If you find that the output generates error, try and use Amazon Q to help you fix them. If you get stuck, you can use the /clear to clear the context memory, open up the create survey template html page, and use a prompt like "Update the form so that it will allow up to five options to be submitted when creating a new survey"


You can see the updated code [here](https://github.com/094459/porto-tech-hub-amazon-q-working-app/blob/fix-options/templates/survey/create.html)


---

**Task 11**

We often need to add new features to applications, whether these are code bases we know and understand, or not. In this lab we are going to add the ability to export survey data as a csv file.

If you have the app currently running, exit (CTRL + C) as we are going to reset back to the workshop codebase.

1/ Close all files/tabs open, and close any tabs you have open in the Amazon Q chat interface.

2/ We can now start thinking about how to export the survey data. A big part of using tools like Amazon Q Developer, is thinking about and breaking down problems BEFORE we ask for code. Sometimes you might use the Chat interface questions to help better understand your options (so not code related). For example, you might ask Amazon Q about different export data file types. This is critical to make sure that you craft the prompt that will help you achieve what you are looking to do. In this instance, having thought about it, this is what I want to do:

* I want to export data in CSV file format
* I want to provide a link on the results page to export the data
* I want to use the survey name as the export file name
* I want the option to exclude email addresses if provided from the export

Thinking about what changes we might need to make, it is likely we are going to impact multiple files. I decided that @workspace is probably going to be the best option here.

> @workspace Update the code to this application to add the ability yo export the results of a customer survey as a CSV file. The export file name should be the same as the survey. The export should only appear on the results page.
> @workspace add a new button on the feedback.html that will allow the user to export the survey data.

Review the output and follow the tasks. You might encounter a few errors and issues, typically along the lines of:

* the export code does not work due to outdated methods
* check that the export code is actually exporting the correct data from the tables
* the export code generates errors such as " TypeError: a bytes-like object is required, not 'str'" or "ValueError: Files must be opened in binary mode or use BytesIO."

After you clear the errors, you should get a download file. Whilst this is good, it is not really what we are looking for. Lets build upon this and ask a follow up prompt, making sure to keep the survey.py route open.

> Update the export code so that the export includes the name of the survey, description, as well as all the responses

Update the code and do another export. Almost there, one final update

> Update the export code so that the export includes the name of the survey, description, as well as all the responses. Use one line per survey response.

Review the code and then follow the instructions. Try exporting again, and this time the export might look more useful.

If you want to see the version of this code that it produced for me, check out [this](https://github.com/094459/porto-tech-hub-amazon-q-working-app/blob/survey-export/routes/survey.py) for the updated route, and [this](https://github.com/094459/porto-tech-hub-amazon-q-working-app/blob/survey-export/templates/survey/feedback.html) for the updated view.


> **Hint!** Sometimes Amazon Q can get the table fields mixed up, so check these are right.

3/ What if we wanted to provide an JSON response instead of just exporting a CSV file? Lets see how easy this is using Amazon Q.

Close all tabs/files, except the survey route. At the bottom of the page, use the Amazon Q inline prompt (COMMAND + I ) and enter the following:

> add a new route to export the survey data in json format, including all the survey details and responses

Review the output and make changes. This is the code it produced when I ran this:

```
@survey_bp.route('/surveys/<int:survey_id>/export/json')
@login_required
def export_json(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    
    # Check if the user is authorized to export this survey
    if survey.user_id != current_user.user_id:
        abort(403)
    
    # Build survey data dictionary
    survey_data = {
        'survey_id': survey.survey_id,
        'title': survey.title,
        'description': survey.description,
        'is_active': survey.is_active,
        'responses': []
    }
    
    # Add response data
    for response in survey.responses:
        option = SurveyOption.query.get(response.option_id)
        response_data = {
            'response_id': response.response_id,
            'respondent_email': response.respondent_email,
            'selected_option': option.option_text,
            'submission_date': response.response_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        survey_data['responses'].append(response_data)

    return jsonify(survey_data)
```
Add your code and then save the file. Now from the browser try invoking the JSon export (we have not created a link to this, so it will not show up on the web page - the route will tell you how to access this, so in my example code about it was http://127.0.0.1:5000/survey/surveys/1/export/json). 

This is the output my code produces - yours might be different if you used your own code.

```
{
  "description": "",
  "is_active": true,
  "responses": [
    {
      "respondent_email": "",
      "response_id": 1,
      "selected_option": "Yes",
      "submission_date": "2024-11-25 13:02:49"
    },
    {
      "respondent_email": "",
      "response_id": 2,
      "selected_option": "No",
      "submission_date": "2024-11-25 13:03:21"
    }
  ],
  "survey_id": 1,
  "title": "Pineapple on Pizza"
}
```
---

**Task 12**

**Task 15**

We are almost done. At the last minute, after testing we realise we need to create a simple update to the application so that we can add a "share survey link" option to the surveys we create. This will allow us to very easily provide these to folk we want to collect feedback from.


1/ Think about how you might implement this change. It is likely that multiple files might need to be changed, so I am going to go with @workspace to help me this time. 

I close all open tabs. I then use this prompt:

> @workspace Can you add a "share link" that copies the survey link to the clipboard for each survey listed

Review the output. It should just suggest making changes to the index.html page - as it turns out, no other changes are needed.

This is the code that Amazon Q generated for me if you get stuck

```
{% extends "base.html" %}

<style>
    .share-button {
        margin-left: 8px;
        padding: 4px 8px;
    }
    .share-button:hover {
        opacity: 0.9;
    }
    </style>
    
{% block content %}
<h1>Your Surveys</h1>
<ul>
    {% for survey in user_surveys %}
    <li>
        {{ survey.title }} 
        <a href="{{ url_for('survey.view', survey_id=survey.survey_id) }}">View</a>
    <button class="share-button" 
            data-survey-url="{{ url_for('survey.view', survey_id=survey.survey_id, _external=True) }}"
            onclick="copySurveyLink(this)">
        <i class="fas fa-share"></i> Share
    </button>
    
    
    </li>
    
    {% endfor %}
</ul>

<h2>Active Surveys to Complete</h2>
<ul>
    {% for survey in active_surveys %}
    <li>
        {{ survey.title }} 
        <a href="{{ url_for('survey.feedback', survey_id=survey.survey_id) }}">Complete Survey</a>
    </li>
    {% endfor %}
</ul>

<script>
function copySurveyLink(button) {
    const surveyUrl = button.getAttribute('data-survey-url');
    
    if (navigator.clipboard) {
        navigator.clipboard.writeText(surveyUrl)
            .then(() => showCopiedFeedback(button))
            .catch(handleCopyError);
    } else {
        // Fallback for older browsers
        const textarea = document.createElement('textarea');
        textarea.value = surveyUrl;
        textarea.style.position = 'fixed';  // Prevent scrolling to bottom
        document.body.appendChild(textarea);
        textarea.focus();
        textarea.select();
        
        try {
            document.execCommand('copy');
            document.body.removeChild(textarea);
            showCopiedFeedback(button);
        } catch (err) {
            document.body.removeChild(textarea);
            handleCopyError(err);
        }
    }
}

function showCopiedFeedback(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<i class="fas fa-check"></i> Copied!';
    setTimeout(() => {
        button.innerHTML = originalText;
    }, 2000);
}

function handleCopyError(err) {
    console.error('Failed to copy text: ', err);
    alert('Failed to copy link to clipboard');
}
</script>

{% endblock %}
```
If you use this code, you should now see that there is a share link that copies the customer surveys into the clipboard.

---

**Task 13**

We have a solid working application, but there are still things to be done. In this lab we will add an about page that explains how to use this application.To make it a bit more interesting, we will add a fun capability to displays some Yoda wisdoms. 

2/ Close all the open files/tabs, and from a new chat tab in the Amazon Q chat interface ask the following prompt:

> @workspace Add a new route for an About page that will be used to provide information to the end users

Review and follow the instructions. After making the changes you should now see a new navigation item on your application.

3/ Close all open tabs and open up the main route file (which you just added the about route to)

Above the routes, use the inline prompt to add a new function. This function will return a wisdom of the day from master Yoda. After pressing COMMAND + I, enter the following:

> create a function that creates a number of messages from Jedi Yoda, and returns a random one

This is the code that Amazon Q generated for me, it should look broadly similar to yours.

```
import random

def get_yoda_message():
    yoda_quotes = [
        "Do or do not, there is no try.",
        "Size matters not. Look at me. Judge me by my size, do you?",
        "Fear is the path to the dark side.",
        "Wars not make one great.",
        "Luminous beings are we, not this crude matter.",
        "Always pass on what you have learned.",
        "Patience you must have, my young Padawan.",
        "In a dark place we find ourselves, and a little more knowledge lights our way.",
        "When nine hundred years old you reach, look as good you will not.",
        "Difficult to see. Always in motion is the future."
    ]
    return random.choice(yoda_quotes)
```

4/ Now select the about route that we just created (highlight the entire block) and using the COMMAND + I inline prompt, enter the following:

> update this route so that it passess a yoda_quote to the about.html page

It should be a simple change that it makes. Review and accept the change.

5/ Open up the about.html page, select all the code and again use COMMAND + I, this time using the prompt:

> update this html so that it displays a "Yoda Message of the day" using the yoda_quote=yoda_quote data passed into this file

After saving the changes, check out the about.html page.

---

**Complete:** You now have a working application, made some improvements and optimisations, now we are ready for the last few tasks we need to do as a developer. Proceed to the final lab, [Part Three](building-our-app-part-3.md)





