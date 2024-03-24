# UranForm Innovations
#### Video Demo: https://www.youtube.com/watch?v=Hl_O7qtjct0
#### Description:
This is a modern and responsive website for architecture company made with using flask framework, python, html, css and sqlite3 from cs50. I learnt a
lot making this website from implementing modern animations and designs to collecting user data and building a full fledge website which can very well
be an architecture website in the real world.

File structure:
Project:
  ├── static/
  │   │   images/
  │   │   ├── bg.jpg
  │   │   ├── contact-bg.png
  │   │   ├── house.png
  │   │   ├── person1.png
  │   │   ├── person2.png
  │   │   ├── person3.png
  │   ├── script.js
  │   ├── tilt.js
  │   ├── style.css
  │   ├── ...
  ├── templates/
  │   ├── index.html
  │   ├── ...
  │   ├── app.py
  │   ├── contacts.db
  │   ├──README.db


### How does the website work?
The website is quite simple in functionality, what I've dedicated most of my time is the styling, the design, the animations and the little details
which makes the website stand out in terms of the respective areas. While the website retains the functionality of any working website i.e, giving details about what the website is about in a clear and detailed manner and also collecting the customer input if they're interested in contacting the company for any work.

### Static/images:
This folder contains all the images used in the project.

### Static/script.js:
This file contains the javascript code for the loading spinner for a delay of 4 sec on the loading screen, the opening and closing for the hamburger-menu and the smooth transition of the fixed scroll-up button at the right-bottom corner which bring you to the top of the page where ever you are at the page.

### Static/tilt.js:
The file contains the tilt js plugin from https://github.com/gijsroge/tilt.js which is responsible for the tilting effect of the cards on the Our Team section of the page.

### templates/Index.html:
The homepage lies in the templates folder it's the index.html file. It's the backbone and the whole skeleton of the website. At the top of the code I've used some Jinja2 code to display flash messages to provide feedback to the user that their message is sent. I've used the Font Awesome CSS library and Google Fonts which specify different font families and styles.
```html
 <div class="spinner-container">
    <div class="circles">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
  </div>
```html

In this code above a spinner which shows at the loading screen for 4 seconds is displayed and I've styled it in the css file.

html <script src="static/tilt.js"></script>:  For the Our team section I've used the tilt.js plugin which displays a cool tilting effect on the employee card.
Moreover all the buttons, the menu and all the sections of the page are defined in this single index page.

### app.py:
This is a python script which creates python web framework using flask, it also includes the SQL from CS50 for storing and retrieving contact information from the customer.
submit_contact function handles form submissions through the POST requests and inserts the customer date into the contacts.db databse. This script also includes the message flashing to let the user know that their message is sent.

### contacts.db:
This is the databse where the customer user's full name, email, and message from the submitted form is stored and can be retrived. It includes sqlite_sequence table that uses AUTOINCREMENT on their primary key columns which give unique ID to each user for better managing and referencing user records in the database.

### Launch the website:
To host this website on the CS50 codespace just run "flask run" and click on the generated link.

Thank you for everything CS50.
