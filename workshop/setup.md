![Amazon Q Developer header](/images/q-vscode-header.png)

## Setting up, and getting starting with Amazon Q Developer

We are now ready for the first hands on part of this lab, setting up the generative AI developer tooling we are going to be using. We are going to be using Amazon Q Developer, a next generation developer tool that provides you with in-line code suggestions and a chat interface to help your developer flow. This is installed into your IDE (VSCode and IntelliJ are supported) via a plugin. Once the plugin is installed, we need to login using something that is called a Builder ID account. This allows you to access the Free Tier of Amazon Q Developer, without the need for an AWS account. So we first need to set that up, and then install the Amazon Q Developer plugin.

**Creating your Builder ID**

(If you already have a Builder ID, you can skip this step)

[Creating a Builder ID](https://aws-oss.beachgeek.co.uk/44y) is the first step in being able to use the Amazon Q Developer plugin. All you need is a valid email address to create a Builder ID. Head over to the [Builder ID page](https://aws-oss.beachgeek.co.uk/44y) and click on the "Sign in with Builder ID". This will pop up a browser window where you can now create your Builder ID, using your email address. 

You can follow these screenshows to see the flow. After accessing the Builder ID page, you will need to provide an email address (1) and then create an alias (Your Name) (2). You will be sent an email verification which you will need to enter (3), and the email should only take a few moments to arrive (but check your SPAM folder just in case)(4)

![creation of a builder id flow](/images/q-vscode-builderid-1.png)

Once you have received that code, enter it to validate your account (5), which should provide confirmation (6). You will be returned back to the initial screen, where you can now enter your email address (7) and password (8) and you should then see the Builder Profile page (9), where you can view your profile.

![completion of the builder id](/images/q-vscode-builderid-2.png)

When you hear the term Builder ID when working with AWS services, this is the account they are referring to. It is separate from the AWS account, but is used by a number of services to provide access to those who want to try and AWS without the need for a full AWS account.


> **Logging out of your Builder ID** Sometimes you might need to log out of your Builder ID, and in order to do this you should head over to your [Builder ID Profile page](https://profile.aws.amazon.com/#/profile/details) and use the **Sign Out** button on the top left. Clicking on this will return you to the sign on page.


**Installing Amazon Q Developer**

Now that we have our Builder ID profile, lets install the Amazon Q Developer plugin. From the Extensions side bar, click on the icon to view the extensions marketplace. Search for "Amazon Q Developer" and you should be able to locate the Amazon Q Developer plugin (1). As of writing the latest version is v1.33.0. This is updated on a very regular basis, so make sure you either use the auto update, or check in regularly to take advantage of the improvements that are being made on a weekly basis.

![Installing the Amazon Q Developer plugin](/images/q-vscode-install-1.png)

If the installation has been completed successfully, we will see a couple of things. First we will see a new Q icon on the left hand side bar (1), and you should also the the Amazon Q status bar at the bottom, with a X (2)

![Successfull installation of Amazon Q Developer](/images/q-vscode-install-2.png)

If you click on that, you should see a menu pop up that shows that you are currently not signed in. We will do that next.

**Signing into Amazon Q Developer**

Now that we have created our Builder ID, and installed the Amazon Q Developer plugin, we can take the last step which is to log in using that Builder ID. 

From the previous screenshot, if we click on the Q icon it will bring up the Amazon Q menu (3). When we click on that, we will see the login options for Amazon Q Developer (4) - there are two, we will ignore the "Use wit Pro Licence" and click on the "Use for Free" box and then click on Continue. This will bring up a pop up box (5). Take a note of the reference code, and then click on Proceed to Browser, which will bring up (6). Review that the code is the same as for the previous step, and then click on "Confirm and Continue", which will then bring up (7) to let you review the permissions that the Amazon Q Developer will need to work. If you are happy, click on "Allow Access" and if successfull, you will see the final screen (8) which you can close.

> **Note!** You might notice in the bottom left corner of VSCode the information panel that says that the Amazon Q plugin has opened up your web page. This will close automatically once the login has completed

![Signing into Amazon Q Developer using your Builder ID](/images/q-vscode-signin-1.png)

Once you have logged in you will notice a few things. First the Q panel on the left hand side will be replaced with a chat window. You will also notice that at the bottom, the Amazon Q status bar will have changed form "X Amazon Q" to "|> Amazon Q". When you click on that, you will also see that you are now logged into Amazon Q using your AWS Builder ID.

![Sign in complete](/images/q-vscode-signin-2.png)

We have now set up everything and are ready to go.

> **Logging out** If you want to log out, all you need to do is click on the Amazon Q status bar link to bring up the menu, and then select the Sign Out option. You can then repeat the process above to sign back in as you need

**Amazon Q Developer Settings**

Before we dive into the labs, it is worth going through how you can configure Amazon Q Developer and tailor it to your requirements. From the Extensions icon on the left icon bar, we can click on the cog wheel next to the Amazon Q Developer plugin, which will bring up the settings you can configure. This is handy to know incase you want to make changes later on. For the time being, we can leave this as is.

![Amazon Q Developer Settings](/images/q-vscode-settings-1.png)



Now that you have set everything up, we can proceed to the next step which is [exploring how to get started with Amazon Q](getting-started-with-q.md)