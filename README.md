# ISQS-3358
ISQS-3358 Class Folder
This repository contains the lab assignments for ISQS-3358. Each lab assignment has its own directory with a Python script and specific instructions. Below, you will find an overview of each lab and its contents.

# Lab 1 - Web Scraping with Requests
Instructions:

In this lab, your group is required to write a Python program that practices using the requests module for web scraping.
You will also work with the different properties of the response object.
Submission Requirements:

Submit a Python .py file with only Python code and comments.
Group assignment: Only one submission is required for each group.
Task:

Scrape information from the following webpages:
Samsung Galaxy S20 5G: http://drd.ba.ttu.edu/isqs3358/labs/lab1/phone.php?id=1
Apple iPhone 11: http://drd.ba.ttu.edu/isqs3358/labs/lab1/phone.php?id=1341
Google Pixel 4a: http://drd.ba.ttu.edu/isqs3358/labs/lab1/phone.php?id=4228
Report the following information for each webpage:

Length of characters found in the page.
HTML response code.
Time taken to connect to the website (values will vary).
Encoding type.
Content type of the webpage (values will vary).
Whether the website is SSL protected.
Notes and Hints:

Reduce redundancy in your code by creating a loop to iterate through each webpage.
Requirements:
Before running the script, make sure to install the required Python libraries using pip:


# Copy code
pip install requests

# Lab 2 - Web Scraping with Requests and BeautifulSoup
Instructions:

In this lab, your group is required to write a Python program that practices using the requests and BeautifulSoup modules for web scraping.
Identify patterns in data to reduce redundancy in your code.
Submission Requirements:

Submit a Python .py file with only Python code and comments.
Group assignment: Only one submission is required for each group.
Task:

Scrape data related to the phone found on the following webpage:
Webpage: http://drd.ba.ttu.edu/isqs3358/labs/lab2/phone.php?id=1
Extract the following values into a CSV file in the specified order:
Model
Product Size
Storage
Number of Back Camera Features
Number of Front Camera Features
Battery Capacity
The order of columns in the CSV should match the sample output data.
Notes and Hints:

None provided.
Requirements:
Before running the script, make sure to install the required Python libraries using pip:


# Copy code
pip install requests beautifulsoup4 lxml

# Lab 3 - Advanced Web Scraping with Throttling
Instructions:

In this lab, your group is required to extend your work from Lab #2 to extract data from all phones listed on a supplied webpage.
Implement throttling to manage requests.
Submission Requirements:

Submit a Python .py file with only Python code and comments.
Group assignment: Only one submission is required for each group.
Task:

Scrape data related to phones found on the following webpage:
Webpage: http://drd.ba.ttu.edu/isqs3358/labs/lab3/
Implement throttling using high and low variables (modifiable in the settings section).
Extract the following values into a CSV file in the specified order:
Product Id
Model
Product Size
Storage
OS
Number of Back Camera Features
Number of Front Camera Features
Battery Capacity
The order of columns in the CSV should match the sample output data.
Notes and Hints:

Your code from Lab #2 can be a useful starting point.
Enumerate the phones listed on the webpage and make requests for child pages in a loop.
Avoid hard-coded URLs for each phone page.
Requirements:
Before running the script, make sure to install the required Python libraries using pip:


# Copy code
pip install requests beautifulsoup4 lxml
Additional Information:

Depending on your operating system, you may see "blank" lines in your CSV, which is not an issue.
