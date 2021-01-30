# WebApp-using-Python-and-Snowflake
Built a WebApp using Python and Snowflake

Tools Used:
FLask: Flask is a Python library that uses routes to define navigation paths and templates to present web pages. The project’s main file (webserver.py) can receive data from one page template and send it to another. Anaconda will install Flask for you and make iteasy for you to add Flask to new Python environments.

Pandas: Pandas is a Python library that makes it easier to work with data sets. When pulling data from Snowflake, you’ll put it into a Pandas Dataframe. Anaconda will install Pandas for you and make it easy to add Pandas to new Python environments.

Vega-Lite: Vega and Vega-Lite are tools for creating visualizations that can be used to make charts for display on web pages. Vega-Lite does not need to be installed. URLs added to the header of a webpage allow the web page to use information from those pages to display the charts.

Step 1:
●Create a New Python Project in PyCharm and create the Main “py” File
●Set Up a Configuration for Running/Testing the Project
●Run Your First Project Test

Step 2:
●Install Snowflake Python Libraries

Step 3: 
●Check Your Project to Make Sure It Still Runs
●Add A Snowflake Database Connection to Your Website
●Read Your Account Name from Snowflake and Output It On Your Web Page

Snowflake Colors Data: 
  ●Set the Worksheet Context 
   ●Create a Sequence Counter
   ●Create a Colors Table
   ●Insert 7 Rows into Your New Colors Table
   ●Look at the Rows You Inserted Into Your Table
   
Step 4:
●Check For/Install the Pandas Python Library
●Use Pandas to Pull Data from Your Colors Table in Snowflake
●Begin Using HTML for Your Website Homepage
●Convert the Snowflake Colors Data to HTML

Step 5:
●Set Up Flask Webpage Template for Homepage
●Pass the Data Frame HTML to the Homepage Template 

Step 6:
●Add a Page to Allow Users to Submit Their Favorite Color
●Create the Favorite Color Submission Form
●Add a Page to Thank Users for Submitting the Form
●Copy the Form Code into Your Submit Page Template
●Make Some Edits to Enable the Form to Run
●Pass Some Submitted Information to the Thanks Page
●Use the Submitted and Passed Information in the Thanks Page Message
●Review How Information is Passed From the Submit Page to the Thanks Page

Step 7:
●Write the Favorite Color Submission to the Snowflake Database
●Add Link From Thanks Page Back to Homepage
●Add a Line Break Between the Thanks Message and the Homepage Link
●Notice that the Submitted Color is Not Being Added to the Homepage

Step 8:
●Move the Snowflake Connection to a Separate File
●Format the Connection Definition in the New File
●Change the Main File So It Imports and Uses “sfconnect”
●Move the Code that Builds the Colors Table into the Homepage

Snowflake Colors Data: 
Create a File Format to Use in Loading Data

Step 9:
●Run the Code to See if the New Sequence Works Correctly
●Summarize the Color Data
●Update Various Page Properties to Match Changes to the Data

Step 10:
●Add a Page Called "Charts"
●Output the Data to a Local CSV File

Step 11:
●Add a Generic Vega-Lite Chart to the Charts Page

Step 12:
●Output the Colors Data to a Local JSON File
●Use the JSON Color Data to Make a Custom Vega-Lite Chart

Step 13:
●Use CSS and Some HTML Tags to Improve the Look of Your Website
●Edit Your Snowflake Query to Limit Rows in the Homepage Colors Table
●Replace the Generic Data in our Charts Page with our JSON Data

Step 14:
●Clean up the Data Output Code -No More Local Files
●Send the Colors JSON Data into the Charts Page as a Variable
●Delete the Static JSON Data You Pasted Into the Page During Step 13
●Put the Variable Name in Double Curly Braces and Change the Chart Style to Bar
●Replace the Bar Color for Each Bar with the Color Named
