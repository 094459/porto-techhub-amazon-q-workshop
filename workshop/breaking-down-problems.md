![Amazon Q Developer header](/images/q-vscode-header.png)

### Building our application - Breaking down problems into smaller tasks

In this lab, we are going to be practicing a key skill that you will help you be more successful in getting good output from generative AI coding assistants like Amazon Q Developer. That skill is breaking down larger problems into smaller tasks that we can get Amazon Q Developer to help us with. Generative AI is very powerful, but we need to understand how to get the most of that capability. It is tempting to ask these tools to help solve our problems at a very high level (build me an app that does x or y) but experience shows that when the underlying models have too much scope with too little direction, they can provide very broad guidance which might not be helpful. In the worst case, they can hallucinate and take you off track completely.

**Overview**

In this lab we are going to take a look at how we might break down a bigger ask into smaller, more actionable tasks. We will practice breakdowing down problems into more actional tasks. In the next 20 mins, we will get into groups of 2-3 and then do the following:

1. We will take the following high level requirements and then break down it down into specific tasks.

> The business has asked us to create a customer feedback application that we can collect customer via an online web application. The application should allow the business to create customer survey forms, and then share these with people to complete. Only the people who create customer feedback forms should be able to view them. 

Take this business request, and:

2. Within your groups, break down this requirement into a series of tasks how you might do this if you were building an applicaiton yourself.

3. As you break down each task, write down a detailed statement (prompt).

4. Review the order of the tasks and the prompts - are they detailed enough? how would you make them more specific?

5. Capture nouns (the things your application will need) and verbs (the kinds of actions). This about the inputs, as well as the outputs


The workshop host will manage time keeping, and after 20 minutes we will review the output.

> **Additional reading** I recently wrote a blog post that puts these into practice which you can read about in the post, [How I built an arcade scrolling game in a day with generative AI](https://dev.to/aws/how-i-built-an-arcade-scrolling-game-in-one-day-ek8)

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

**Managing your prompts**

It is important to get into **"Daily habits"** of using Amazon Q that will quickly help you learn what works well, and what does not. When I first started using Q I only used it occasionally, and it wasnt until I started using it daily that I better understood how to use the tool, and Amazon Q start producing much better output for me.

Saving the prompts that work well for you is an important milestone that will help you start to get more consistently good output from Amazon Q. I used to use a makrdown doc, but now I am beginning to use a new tool created by an AWS Community Builder, Christian Bonzelete, called [Promptz](https://www.promptz.dev/). You can login and save your own prompts, as well as see what prompts others have created and try these out. This is very new so take a look and make sure you bookmark it and add your own prompts.

---
**Complete:** You have now had some practice breaking down problems into smaller tasks, and we can now proceed with the first part of building our application in [Part One](building-our-app-part-1.md)


