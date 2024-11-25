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

1/ First make sure you have closed all the open files/tabs in VSCode. From the Amazon Q Developer Chat interface, type @ and you should see workspace appear. Tab to complete that, and then add the following to your prompt:

> @workspace DEVSTYLE Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to provide feedback.

Hit return and review the output. How was the output different? 

2/ We are now going to create a new file in the .qdeveloper folder, called **DBA.md**. Add the following text to this file:

```
DBA

Only when I explicitly ask for code, follow this guidance:

- Only provide SQL code unless I explicitly ask for another language
- I am an expert in SQL and I did not need a walk through
- I have a strong preference for Sqlite
```

So our project structure will look like

```
├── .qdeveloper
│   └── DEV.md
│   └── DBA.md
└── .venv
```

Notice that the first line contains "DBA", and we can use this to grab this context in the prompt. Save and close the file.

From the OUTPUT menu (if you do not see this, make sure you have the Terminal tab open), and from the pull down menu, select Amazon Q Language Server. You should see something like this:

```
[Info  - 22:26:39] Adding file to vector index: /Users/ricsue/Projects/amazon-q/workshop/porto/porto-q-demo-code-2/.qdeveloper/DEV.md
[Info  - 22:36:19] Adding file to vector index: /Users/ricsue/Projects/amazon-q/workshop/porto/porto-q-demo-code-2/.qdeveloper/DBA.md
```

> **Tip!** As Amazon Q Developer Workspace Index is a beta feature, we will sometimes need to go into the logs to see if it is behaving as expected.

3/ We will now try the same prompt again. Make sure you have closed all the open files/tabs in VSCode. From Amazon Q Developer chat interface, type the following:

> @workspace DBA Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to provide feedback.

Review what Amazon Q Developer produces. Did you get different output? You can use this technique to help provide more consistent output that is in line with how **YOU** want to work.

---

**Task 4**

Now that we have seen how to tailor the output we get from Amazon Q Developer, we are going to show another way we can produce the data model. From within the file itself, using the inline capabilities of Amazon Q Developer. We will show how you can do this for both SQL and Python.

1/ Close any files/tabs you might have open. From VSCode create a folder called **"data"** and create a new file called **"customer-feedback.sql"**.

2/ Ensure the cursor is at the top of the page, and then press COMMAND + I which will bring up the inline prompt. When we use the inline capabilities we cannot rely on the additional context, so we have to be explicit. Enter the following and then hit return.

> Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to submit feedback.

As we have create the file called "customer-feedback.sql" Amazon Q Developer is smart enough to know that we are going to be wanting SQL code.

Review the output. How does it compare with the code produced from the chat interface? Press ESC to ignore the code suggestions, and make sure the file is blank. Save the file (so that you have an empty file called "customer-feedback.sql").

3/ Close the file/tab, and this time from the root folder in VSCode, create a new file called **"app.py"**. Open this file within the editor, and repeat the same step as previous. This time we will generate the prompt using comments. At the top of the page, add the following:

```
"""
Create a data model for a simple customer survey application. 
Users will log in using an email addresses. 
Users will be able to create new surveys, or update/delete existing surveys. 
Users can create multiple surveys. 
Surveys can have between 2 and 5 options. 
Once a Surveys is created, the End Users will be able to submit feedback.
"""
```

Hit return and wait - you should see Amazon Q Developer begin to think. Does it finish? What do you think of the output?

As we have create the file called "app.py" Amazon Q Developer is smart enough to know that we are going to be wanting Python code.

In both the previous example, we have seen how using different capabilities can have a big impact on the output produced, or whether any output is produced at all.


4/ Delete the contents of app.py file and save (so that it is an empty file).Close any other files/tabs you might have open. Re-do the same prompt from the Amazon Q Developer chat interface

> @workspace DBA Create a data model for a simple customer survey application. Users will log in using an email addresses. Users will be able to create new surveys, or update/delete existing surveys. Users can create multiple surveys. Surveys can have between 2 and 5 options. Once a Surveys is created, the End Users will be able to submit feedback. 

Review the SQL - does it look right?

Does it look different from the first time you ran it? Welcome to the world of non deterministic output. 

To simplify how we run this workshop, rather than copy your SQL code into the **"customer-feedback.sql"**, use the following code. Paste this code into the **"customer-feedback.sql"** file in the data directory.

```
-- Users table to store user information
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

-- Surveys table to store survey information
CREATE TABLE Surveys (
    survey_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Survey Options table to store the options for each survey
CREATE TABLE Survey_Options (
    option_id INTEGER PRIMARY KEY AUTOINCREMENT,
    survey_id INTEGER NOT NULL,
    option_text TEXT NOT NULL,
    option_order INTEGER NOT NULL,
    FOREIGN KEY (survey_id) REFERENCES Surveys(survey_id) ON DELETE CASCADE,
    CONSTRAINT check_option_order CHECK (option_order BETWEEN 1 AND 5)
);

-- Survey Responses table to store end user feedback
CREATE TABLE Survey_Responses (
    response_id INTEGER PRIMARY KEY AUTOINCREMENT,
    survey_id INTEGER NOT NULL,
    option_id INTEGER NOT NULL,
    respondent_email TEXT,
    response_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (survey_id) REFERENCES Surveys(survey_id) ON DELETE CASCADE,
    FOREIGN KEY (option_id) REFERENCES Survey_Options(option_id) ON DELETE CASCADE
);

```

Save the file, and we can now go to the next task in this lab.

---

**Task 5**

Now that we have our data model in SQL, lets generate some code to test this. Then we will see how we can use Amazon Q Developer to help us easily make changes.

1/ Make sure that all the open files are closed EXCEPT the **"customer-survey.sql"** file. From the Amazon Q Developer chat interface, type in the following:

> Generate this data model in Python. Add code to initilize the database.

Review the output.

2/ In the **"app.py"** in the root directory, copy the code into this file and save it. You will need to install some Python libraries. Use Amazon Q Developer to help you by using the following prompt in the chat interface

> what Python libraries do I need to install to run this code

It should generate a "pip install xx" command, which you should now run in the Terminal (making sure that you are still in the activated virtual Python environment)

After installing dependencies, now run the code

```
python app.py
```

> **Help!** If you get an error when trying to run your python code, copy the error message and then ask Amazon Q Developer to help you. It will be able to guide you through to a solution which you can then try by running the Python file again.

If everything is ok, you should now have in your local directory a sqlite database called "customer-_feedback.db" (or something very similar). As we installed the VSCode plugin [SQLlite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer) we can now click on this file within VSCode, and you should be able to view the structure of the data model.

3/ As you develop applications it is typical that your data model might get updated, so lets see how we might do that. Close all files open except the **"customer-feedback.sql"** and highlight the following piece of code:

```
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);
```

From the editor, RIGHT CLICK and then from the Amazon Q menu, select "Send to Prompt". From the chat interface, enter the following:

> Update this to add a check for a valid email address

Review the output. This is what I got, review your output and see how different it is:

```
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL
    CHECK (
        email LIKE '%_@_%.__%' AND 
        email NOT LIKE '%@%@%' AND
        length(email) >= 5
    ),
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);
```

4/ Keeping the current file open, add in the same chat conversation the following prompt:

> @workspace update the data model Python code in app.py to reflect this change to the Users table

Review the output, carefully reviewing the Users table. You should now have updated Python code. Follow the instructions. This is the code that it generated for me:

```
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)

    # Add the email validation check constraint
    __table_args__ = (
        CheckConstraint(
            "email LIKE '%_@_%.__%' AND "
            "email NOT LIKE '%@%@%' AND "
            "length(email) >= 5",
            name='valid_email'
        ),
    )

    # Relationship with surveys
    surveys = relationship("Survey", back_populates="user", cascade="all, delete-orphan")

class Survey(Base):
    __tablename__ = 'surveys'

    survey_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="surveys")
    options = relationship("SurveyOption", back_populates="survey", cascade="all, delete-orphan")
    responses = relationship("SurveyResponse", back_populates="survey", cascade="all, delete-orphan")

class SurveyOption(Base):
    __tablename__ = 'survey_options'

    option_id = Column(Integer, primary_key=True, autoincrement=True)
    survey_id = Column(Integer, ForeignKey('surveys.survey_id', ondelete='CASCADE'), nullable=False)
    option_text = Column(String, nullable=False)
    option_order = Column(Integer, nullable=False)

    # Add check constraint for option_order
    __table_args__ = (
        CheckConstraint('option_order BETWEEN 1 AND 5', name='check_option_order'),
    )

    # Relationships
    survey = relationship("Survey", back_populates="options")
    responses = relationship("SurveyResponse", back_populates="option")

class SurveyResponse(Base):
    __tablename__ = 'survey_responses'

    response_id = Column(Integer, primary_key=True, autoincrement=True)
    survey_id = Column(Integer, ForeignKey('surveys.survey_id', ondelete='CASCADE'), nullable=False)
    option_id = Column(Integer, ForeignKey('survey_options.option_id', ondelete='CASCADE'), nullable=False)
    respondent_email = Column(String)
    response_date = Column(DateTime, default=datetime.utcnow)

    # Relationships
    survey = relationship("Survey", back_populates="responses")
    option = relationship("SurveyOption", back_populates="responses")

def init_db(database_url='sqlite:///customer_feedback.db'):
    """Initialize the database and create all tables"""
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    
    # Create a session factory
    Session = sessionmaker(bind=engine)
    return Session()

def main():
    # Initialize the database
    session = init_db()
    print("Database initialized successfully!")
    
    # Example of creating a new user and survey
    try:
        # Create a new user
        new_user = User(
            email="example@email.com",
            password_hash="hashed_password_here"
        )
        session.add(new_user)
        session.commit()
        
        # Create a new survey
        new_survey = Survey(
            user_id=new_user.user_id,
            title="Customer Satisfaction Survey",
            description="Please rate your experience"
        )
        session.add(new_survey)
        session.commit()
        
        # Add survey options
        options = [
            SurveyOption(survey_id=new_survey.survey_id, option_text="Very Satisfied", option_order=1),
            SurveyOption(survey_id=new_survey.survey_id, option_text="Satisfied", option_order=2),
            SurveyOption(survey_id=new_survey.survey_id, option_text="Neutral", option_order=3),
            SurveyOption(survey_id=new_survey.survey_id, option_text="Dissatisfied", option_order=4),
            SurveyOption(survey_id=new_survey.survey_id, option_text="Very Dissatisfied", option_order=5)
        ]
        session.add_all(options)
        session.commit()
        
        print("Sample data created successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    main()

```

4/ Delete the current **"customer_feedback.db"** file and then re-run this code (using "python app.py). It should run successfully - check the newly created database and make sure it looks ok.

---

**Task 6**

In this task we are going to see how we can generate diagrams from our SQL, as well as generate SQL from our diagrams. We will need to install a VSCode plugin if you do not already have this installed. From the VSCode marketplace, find the following plugin

![Enhanced Markdown Viewer](/images/vscode-markdown-enhanced.png)

You can use [this link](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)

This will provde you with a new option when you right click on any markdown document, as follows:

![Enhanced Markdown viewer](/images/vscode-markdown-enhanced-fileopen.png)


1/ Close all files/tabs in VSCode. Open up the **customer-feedbck.sql** file and from a new chat interface, add the following prompt:

> create a mermaid diagram of this sql code that I can display in a markdown doc

Review the output. In the same directory (data) create a new file called **"customer-feedback.md"** and add then copy the contents into the file. If you try and display this as it is, it will not work ( try it ). We need to add the markdown tag so that it knows to use the Mermaid diagram extension. If you are new to this, we can easily do this with the help of Amazon Q.

2/ Select all the code in the newly create file, and then use the Amazozn Q menu integration (right click, Amazon Q > Send to Prompt). From the prompt, enter the following:

> Add the markdown to display this

After a while you should see some updated code. Overwrite the contents with the output from the chat inteface (after reviewing), and then try again with the enhanced Markdown preview. You should get something like this.

![documenting the application schema](/images/vscode-mermaid-show.png)

Close all the tabs in VScode.

You can actually generate SQL code FROM mermaid diagrams (other diagram formats will work also, if they generate a text based format structure).

---

**Task 7**

You can simplify how you create your SQL code by scaffolding your design using YAML. You can also generate YAML from SQL, if you need to provide that to teams that will use that to generate your database schema.

1/ Close the file in VSCode and this time open up the **"customer-feedback.sql"** in the data folder. We will now generate YAML from this by using the following prompt:

> describe this SQL as YAML

Review the output. Does it look ok?

---

**Task 8**

As we build applications, we may need to generate test data so that we can simulate how our application will work. Generating test or synthetic data is a common requirement, and its good to know that tools like Amazon Q make creating this a simple task. In this lab we are going to dive into this topic, looking at how we can use Amazon Q to generate synthetic data for the data model we have created.

1/ Close all tabs/files in VSCode, but keep the **"customer-feedback.sql"** file open.

2/ From a new Amazon Q chat interface tab, enter the following prompt:

> @workspace generate 100 sample surveys for the application model outlined in app.py. provide code as SQL

> create a python test script that generates 100 pieces of sample data

Review the output. You might need to follow up with some additional prompts such as 

> how does this code know how to connect to the local sqlite database

3/ Create a new file in the root directory called **"test-data.py"** and copy the contents of your code. Save the file and then run it. You will probably need to install some additional Python libraries, so use Amazon Q to help you know how to do that.

Did it run successfully, or did it generate an error?

If you were able to run that successfully, open up the local sqllite database and you should now see it has lots of test data. If you were not able to get any code working, try this which is what Amazon Q generated for me:

```
from faker import Faker
import random
from datetime import datetime, timedelta
import hashlib
import sqlite3

# Initialize Faker
fake = Faker()

# Lists to store generated IDs
users = []
surveys = []
survey_options = []

# SQLite database connection
def create_connection():
    """Create a database connection to the SQLite database"""
    try:
        conn = sqlite3.connect('customer_feedback.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def generate_password_hash(password):
    """Generate a simple hash for demo purposes"""
    return hashlib.sha256(password.encode()).hexdigest()

def generate_and_insert_data():
    conn = create_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    
    try:
        # Generate and insert users
        print("Generating and inserting users...")
        for _ in range(100):
            email = fake.email()
            password_hash = generate_password_hash(fake.password())
            created_at = fake.date_time_between(start_date='-1y', end_date='now')
            last_login = fake.date_time_between(start_date=created_at, end_date='now')
            
            cursor.execute('''
                INSERT INTO Users (email, password_hash, created_at, last_login)
                VALUES (?, ?, ?, ?)
            ''', (email, password_hash, created_at, last_login))
            
            user_id = cursor.lastrowid
            
            # Generate 1-3 surveys per user
            num_surveys = random.randint(1, 3)
            for _ in range(num_surveys):
                title = fake.sentence(nb_words=4)
                description = fake.text(max_nb_chars=200)
                is_active = random.choice([0, 1])
                created_at = fake.date_time_between(start_date=created_at, end_date='now')
                
                cursor.execute('''
                    INSERT INTO Surveys (user_id, title, description, is_active, created_at)
                    VALUES (?, ?, ?, ?, ?)
                ''', (user_id, title, description, is_active, created_at))
                
                survey_id = cursor.lastrowid
                
                # Generate 3-5 options per survey
                num_options = random.randint(3, 5)
                for order in range(num_options):
                    option_text = fake.sentence(nb_words=3)
                    cursor.execute('''
                        INSERT INTO Survey_Options (survey_id, option_text, option_order)
                        VALUES (?, ?, ?)
                    ''', (survey_id, option_text, order + 1))
                    
                # Generate some random responses for this survey
                num_responses = random.randint(0, 10)
                for _ in range(num_responses):
                    # Get a random option_id for this survey
                    cursor.execute('SELECT option_id FROM Survey_Options WHERE survey_id = ?', (survey_id,))
                    options = cursor.fetchall()
                    option_id = random.choice(options)[0]
                    
                    response_date = fake.date_time_between(start_date=created_at, end_date='now')
                    respondent_email = fake.email()
                    
                    cursor.execute('''
                        INSERT INTO Survey_Responses (survey_id, option_id, respondent_email, response_date)
                        VALUES (?, ?, ?, ?)
                    ''', (survey_id, option_id, respondent_email, response_date))
            
            # Commit after each user and their related data
            conn.commit()
            
        print("Data generation completed successfully!")
        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    
    finally:
        conn.close()

if __name__ == "__main__":
    generate_and_insert_data()

```

In order to run this I had to "pip install Faker" and then it run successfull, generating 100 sample surveys in the local database.

---

**Task 9**

One of the most powerful use cases for using generative AI coding assistants like Amazon Q is to help write SQL queries. Human to SQL as this is sometimes called. In this lab we are going to explore this.

1/ Open up the **"customer-feedback.sql"** from the data folder

2/ In a new chat window, try the following:

> how would I write a SQL query to get the most popular surveys
> How would I query to find out who has created the most surveys
> Create a sql query to show many total surveys and suvery submissions there have been

Review the output of the different prompts.

3/ In the SAME chat window, following up from the previous output ask:

> generate Python code that will allow me to test this query, connecting to the local sqlite database

Review the code it generates. Create a new file in the root folder called **"run-query.py"** and paste your code into that. Save the file and then try and run it. Hopefully you will get output that looks right.

If you get stuck, when I ran this, it generated the following code:

```
import sqlite3
from datetime import datetime

def get_popular_surveys(db_path='customer_feedback.db'):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to find most popular surveys
        query = """
        SELECT 
            s.survey_id,
            s.title,
            COUNT(sr.response_id) as response_count,
            s.created_at,
            u.email as creator_email
        FROM Surveys s
        LEFT JOIN Survey_Responses sr ON s.survey_id = sr.survey_id
        LEFT JOIN Users u ON s.user_id = u.user_id
        GROUP BY s.survey_id, s.title, s.created_at, u.email
        ORDER BY response_count DESC;
        """

        # Execute the query
        cursor.execute(query)
        results = cursor.fetchall()

        # Print results in a formatted way
        print("\nMost Popular Surveys:")
        print("--------------------")
        if not results:
            print("No surveys found in the database.")
        else:
            for row in results:
                print(f"Survey ID: {row[0]}")
                print(f"Title: {row[1]}")
                print(f"Response Count: {row[2]}")
                print(f"Created At: {row[3]}")
                print(f"Creator Email: {row[4]}")
                print("--------------------")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

# Alternative query to show only active surveys with at least one response
def get_active_popular_surveys(db_path='customer_feedback.db'):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = """
        SELECT 
            s.survey_id,
            s.title,
            COUNT(sr.response_id) as response_count,
            s.created_at,
            u.email as creator_email
        FROM Surveys s
        LEFT JOIN Survey_Responses sr ON s.survey_id = sr.survey_id
        LEFT JOIN Users u ON s.user_id = u.user_id
        WHERE s.is_active = 1
        GROUP BY s.survey_id, s.title, s.created_at, u.email
        HAVING COUNT(sr.response_id) > 0
        ORDER BY response_count DESC;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("\nActive Popular Surveys (with responses):")
        print("--------------------")
        if not results:
            print("No active surveys with responses found.")
        else:
            for row in results:
                print(f"Survey ID: {row[0]}")
                print(f"Title: {row[1]}")
                print(f"Response Count: {row[2]}")
                print(f"Created At: {row[3]}")
                print(f"Creator Email: {row[4]}")
                print("--------------------")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Run both queries
    print("Running query for all surveys...")
    get_popular_surveys()
    
    print("\nRunning query for active surveys with responses...")
    get_active_popular_surveys()

```

When you are creating applications, being able to quickly assemble SQL queries based on your use case is a very powerful capability.

3/ Close all the open files/tabs in VSCode, and close the Amazon Q chat interface tab you have just used.

---

**Complete:** You have now completed the first part of this lab, and created your data model. Before we proceed to the next lab, we need to do the following:

* delete the **"run-query.py"** and **"test-data.py"** files
* delete the **customer_survey.db** sqlite database
* open up the **"app.py"** and delete the contents of this file

Once you have done that, proceed to [Part Two](/workshop/building-our-app-part-2.md).