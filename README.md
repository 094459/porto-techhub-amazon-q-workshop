![Porto Tech Hub](images/porto-tech-hub.png)
![Amazon Q Developer header](images/q-vscode-header.png)

## Introduction - Next Generation Developer Tools

*A hands on guide to working with Amazon Q Developer. Made by DevRel with 💖.*

We are going to run through how to use the next generation of developer tooling (Amazon Q Developer) to help make our jobs as developers more enjoyable and productive. We will create a new application from scratch, and then build upon this and perform many of the tasks you would typically do as a developer. **You do not have to have an AWS account or be an AWS user to go through this workshop**. The workshop is split into a number of different labs which you can run either within a controlled workshop, or at your own pace. Feel free to contact me if you run into any issues.

---

**What you will need**

You will need VScode IDE (or as an alternative, IntelliJ) with the following VSCode plugins installed

* VSCode
* Amazon Q Developer plugin - https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode 
* The SQLlite Viewer - https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer
* The Enhanced Markdown Viewer - https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced

-

**How do follow along**

Given the non deterministic nature of generative AI tools, the output you will get from running these prompts will be different to the output I got when creating this. You might be asking yourself, how will I know what is right or wrong, and how will I cope if things go horribly wrong? This is kind of intentional. Working with generative AI tools like Amazon Q Developer open you up to a new flow, a new way of working. If your expectation was that these tools will generate working code every time, then it is time to reset that expectation. The output that these tools provide will be your starting point, and get you 80% of the way there. You can then use Amazon Q Developer to help iterate and complete the remaining. 

Everyone running through this lab will have a different experience, but I hope the takeaway from this is a better understanding of the flow you will start to develop in using these tools to write software.

If you are working through this in a group setting, then the person running the lab will lead from the front and you can take your guidance from them.

-

**Overview**

This workshop will first of all get you up and running with Amazon Q Developer - installing, configuration, and understanding the different parts that make up Amazon Q Developer. Once we have had some time to explore its capabilities, we will use that knowledge to try and building working application.

**What are we going to build?**

We are going to build a **customer feedback survey** application. The application will initially have some basic functionality, an MLP - Minimum Lovable Product. We will be using Amazon Q Developer to help us add code and improve the basic functionality. We will dive into the details as we get into the workshop, but we want our application to be able to:

* allow users to register and then login to this application to use it
* let logged in users create surveys
* make it so that anyone can submit feedback from a survey
* let only owners of a survey see the survey results

---

## 1. Installation and Setup

You do not need an AWS account to use the Amazon Q Developer plugin. You can use the free tier by [creating a Builder ID](https://aws-oss.beachgeek.co.uk/44y), and then using that Builder ID to login.

[Follow this link](workshop/setup.md) to get started with installing the Amazon Q Developer plugin.

---

## 2. Learning about and exploring Amazon Q Developer capabilities

Once we have the Amazon Q Developer plugin installed, setup, and configured, we are ready to explore its capabilities. In this lab we are going to go over the features in detail and provide your first opportunity to get hands on.

[Follow this link](workshop/getting-started-with-q.md) to explore the wonderful world of Amazon Q Developer

---

## 3. Breaking down problems

We learned in the previous labs that to get the best out of generative AI developer tools, we need to understand how to break down the problems we are working on into smaller tasks. Amazon Q Developer like other AI coding tools, work best when we provide **specific** and concrete **smaller** tasks with the right level of **clarity**.

[Follow this link](workshop/breaking-down-problems.md) where we will explore some ideas on how to do this.

---

## 4. Building our application - defining the data model

We are now ready to start building our application. We are going to build a **customer feedback survey** application, and the first step is to define the data model.

[Follow this link](workshop/building-our-app-part-1.md) where we will see how Amazon Q Developer wil help us create our data model and more!

---

## 5. Building our applicaiton - using Amazon Q Developer Agent for software development

With our data model now created, we can start building the application. We are going to use some of the more advanced capabilities of Amazon Q Developer to help create the code application, troubleshoot any issues that arise, and get the first version of our application up and running.

[Folow this link](workshop/building-our-app-part-2.md) to start diving into building the application.

---

## 6. Building our application - improving the application

We have a working applicaiton but we still have lots to do. In this last lab we will look at how we can use Amazon Q Developer to simplify some of those tasks, as well as automate many more. Whether that is testing, creating documentation, or more.

[Folow this link]() to finish up our customer feedback application.

---

## 7. Wrap up 

Now that we have everything setup and we have explored how Amazon Q Developer works, lets start building something.

In this lab we are going to build an application in Python. We have chosen Python as it makes it easy to follow along and understand how these next generation developer tools work. 


### Feedback and additional resources

Now that you have completed this Amazon Q Developer workshop, I hope you are beginning to see how you can use this as part of your day to day work. I have provided some [additional resources](workshop/resources.md) that you can review that share useful links to content, community spaces, and essential updates to keep up with the fast moving pace. I have also put togehter a [reference guide](workshop/reference.md) where you will find a handy list of the important things when using Amazon Q Developer.

---

**Feedback please**

If you found this useful, please [provide feedback](https://pulse.aws/survey/1DM5TAZU) where I share some additional resources from some of my talks on Amazon Q Developer.
