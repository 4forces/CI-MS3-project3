# GiftKids - A simple site to bless others, or to receive blessings

<img> from am i responsive
***

## Overview

Most parents and caregivers of children will understand how fast kids outgrow the things they own, 
whether is it clothes, toys or accesories like steamers and child seats. This developer had the
privilege of witnessing the generosity of many around him, who gratefully share children's resources
with whomvever that needs. At times, the donor may be at the receiving end, with their gifts coming back to them, 
since children (especially toddlers) quickly outgrow what they use. However, at times caregivers may be urgently 
looking for something, yet clueless how and where to start. This brings us to the objective of this site.

### Objective

GiftKids presents itself as a fictional platform for parents and and caregivers looking to give away items 
do not need, or to look for items they need, on a donation basis. It is hoped that a community and generous spirit of 
sharing and giving can be promoted. 
***

## UX and UI

This site is designed to be visually appealing to parents and kid-lovers in mind, from the 
colours used to the font selection. It has a "cutesy" touch, and models itself after sites that sell children related items. 
The reference website used for the color theme, look and feel is obtained from homepage layout examples at the website: ["Jadusona"](https://demo.hasthemes.com/shopify/jadusona-cm.html),
which in turn was sourced while browsing through [Pinterest](https://www.pinterest.com/) for appearance inspirations. 
The fonts used are [Fredoka One](https://fonts.google.com/specimen/Fredoka+One?query=fredoka) for headings and [Ubuntu](https://fonts.google.com/specimen/Ubuntu?query=ubuntu) for contents
The colour palette used is as follows: 

Colour Palette:
<img src="static/images/readme/#" width="200" style="margin:0">

### User stories

* "I believe in recycling, re-using things that are still usable and reducing waste, since children grow up quickly" - *A parent who believes in saving the earth*
* "I wish to give away used items from my children as they have only been used a short while" - *Someone looking to give away their items*
* "I am looking for items for my kids, and do not wish to spend too much since they will quickly outgrow it" - *A parent or caregiver looking for recylable kids items*


### Wireframes and Diagrams

 *&Label diagram titles in wireframe*

* [Wireframes (desktop)](/images/#)
* [Wireframes (mobile)](/images/#)
* [ER Diagrams](/images/#)
* [Logical Diagram](/images/#)

### Features

This site has mainly three sections: 

- [Landing page](#Landing-Page) 
- [View items](#View-Items)
- [Search items](#Search)
- [Post items](#Post-Items)
- [Edit/Delete items](#Edit/Delete-Items)
- 



### Landing Page

This page allows potential users to sign up, browse items and post items. 
The design is kept sinmple and follows a color theme for children website
[screenshot](/images/#)

### View Items

Users are able to view items that have been uploaded by other users or themselves. 

### Search

Users can searhc for items by:
- category/type
- condition
- user

### Post Items

Users can post items they wish to give away

### Edit/Delete Items

Users can edit and/or delete items they have already posted. 

### Features Left to Implement
- **User Login** for better management of posts
- **Picture upload**
- **TBC...**
- ```toastr pop up "item added"/item deleted/item modified after submit```

---

## Technologies Used

1. [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
   - The standard markup langauge to display document in web browsers.
2. [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
   - Web content styling 
3. [JavaScript](https://jquery.com)
4. [Flask](https://jquery.com)
5. [Python 3.8](https://jquery.com)
6. [MongoDB](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation. 
7. [Heroku](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
8. [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
9. [toastr](https://github.com/CodeSeven/toastr) for message pop-ups upon POST, EDIT, DELETE items
10. [bootstrap](https://getbootstrap.com/)
11. [Adobe Photoshop](https://www.adobe.com/sea/products/photoshop.html?sdid=YKHWGJBS&mv=search&ef_id=Cj0KCQiAhZT9BRDmARIsAN2E-J3nMUmJtn6TzrJSACgqgz8qd_J6Uvdp8mOKj4bch-nX2vdyaVi6PQAaAmu0EALw_wcB:G:s&s_kwcid=AL!3085!3!444551131429!e!!g!!adobe%20photoshop&gclid=Cj0KCQiAhZT9BRDmARIsAN2E-J3nMUmJtn6TzrJSACgqgz8qd_J6Uvdp8mOKj4bch-nX2vdyaVi6PQAaAmu0EALw_wcB) to edit some of the images
12. [Fontawesome](https://www.bootstrapcdn.com/fontawesome/) 

---

## Testing

Manual testing was done on all links and Pages. 

Test cases are as follows:
1. 
2. 
3. 

Request

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

### Issues and bugs
```
- background of edit and post page
- adding a login element
- adding an image upload option
- changing the display of the links after login
- getting the date and add to the data
- at less than 425 px there is right border
- description does not come out
- Edited successfully toastr pops up when click on back button after editing item
```

---

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

Deployment
a. Setting up MySQL (ClearDB) with Heroku
Installing ClearDB in Git Bash using heroku addons:create cleardb:ignite
Datatables in the database were created using the create_datatables.py file written by the developer
Datasets were imported automatically from the csv file using import_datasets.py file written by the developer

b. Heroku Deployment
Sign up for an account at Heroku.
Download Heroku CLI at Heroku website.
Install the dowloaded Heroku CLI from Step 2.
Open up Git Bash terminal. Cd to the location that you have your project in. Then, in the Git Bash Terminal, login to Heroku by typing heroku login. A login page will be popped up to allow you to login to Heroku.
Open up another Git Bash terminal. Create a new app using heroku create <app_name>.
In Git Bash, check whether the new remotes has been successfully added using git remote -v.
In Git Bash, install gunicorn with the command git remote -v.
Create a file called Procfile. Add web gunicorn app:app and save it.
Create the requirements.txt file with pip3 freeze --local > requirements.txt.
In Git Bash, commit and push the project to GitHub and Heroku with the following:
git add .
git commit -m "<Commit Message>"
git push heroku master
In Heroku, set up your key and value pair needed for the project. For this project, the database url, MySQL username, database, host and password has been configured under the Settings Tab.
To open up the app hosted on Heroku, click on the "Open App" button at the very top page of the Heroku dashboard.
b. To run this web application on your local PC
Instructions Note: This web application was run on a Windows PC. The following command might be slightly different if run on a Mac PC.

Go to Cereal 101 github repository.

Click on the 'Clone or Download' button and then click 'Download ZIP' and extract the files to a location of your choice on your laptop / desktop. Else, you can clone the project by running the following command on your terminal: git clone https://github.com/<username>/<repository>

Create a virtual environment using the following command: python -m venv venv

Activate the virtual environment created using the following command: On Windows: venv\Scripts\activate

Install all the packages needed using the following command: pip install -r requirements.txt

Set the enviroment variables needed to run this web application. First, right click on My Computer. Then right click on Properties. On the left hand side of the menu bar, click on Advanced system settings. Under the System Variables section, click on the New button. In the pop up dialog box, key in the Variable Name and Variable Value field. The environment variables needed to be setup would be the database name, database host, database password and database username. Note: For the variable name, you are free to choose a variable name of your choice:

An example of the enviroment variables key values pair would be as follow: a. MYSQL_HOST(variable name) will be: us-cdbr-iron-east-02.cleardb.net (variable value) b. MYSQL_USER(variable name) will be: B80f8d428xxxxx(variable value) c. MYSQL_PASSWORD(variable name) will be: F48exxxx(variable value) d. MYSQL_DB will(variable name) be: heroku_58632fb6debxxxx(variable value)

Run the application using the following command: python app.py

To see the web application in action, go the the following link: http://127.0.0.1:8080

---

## Credits

### Images and Graphics
1. Images were mostly sourced from [Unplash](https://unsplash.com/) and a bit from [Pexels](https://www.pexels.com/)
4. Background image graphics obtained from [freepik](https://www.freepik.com/premium-vector/toys-doodle-set_6551728.htm#page=1&query=toys&position=41)


### secret Key
[RandomKeygen](https://randomkeygen.com/) to generate the secret key

### code
1. [Tim Nelson's (CI) Task Manager](https://github.com/Code-Institute-Solutions/TaskManager/tree/master/08-SearchingWithinTheDatabase/01-text_index_searching)

### style and feel
1. Pinterest which led to (2) 
2. https://demo.hasthemes.com/shopify/jadusona-cm.html
3. Color palette (Chrome extension) to extract color theme
4. Color pickr eyedropper (Chrome extension) to pick color
3. and google [search results](https://www.google.com/search?q=baby+gift+wallpaper&tbm=isch&ved=2ahUKEwinwczF1r_sAhUunEsFHaXtAKoQ2-cCegQIABAA&oq=baby+gift+wallpaper&gs_lcp=CgNpbWcQAzICCAA6BggAEAcQHjoICAAQCBAHEB5Qp_wBWN3_AWC_gQJoAHAAeACAAUmIAYcCkgEBNZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=2AKNX6f1Oq64rtoPpduD0Ao&bih=969&biw=1920&rlz=1C1NHXL_enSG810SG810#imgrc=fBrjw4FAwGnf8M)


### Alighment and looks refinement: 
4. Alumni's website: 
   - https://linda-instaramen.herokuapp.com/#
   - https://mel-buyandsell-marketplace.herokuapp.com/


### Logo and favicion
1. [Free Logo Design](https://www.freelogodesign.org/)
2. [favicon.io](https://favicon.io/favicon-converter/)

### Layout Design
1. [Smashing Magazine](https://www.smashingmagazine.com/2016/04/web-developer-guide-color/)
2. [Width and Height Display](Width and Height Display)

### Solution to resolve favicon 404 error when edit/delete item
1. [stackoverflow](https://stackoverflow.com/questions/27234593/setting-up-static-folder-path-in-flask1)

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
- Idea was conceived from viewing the website of Nanyang Academics. Linke [here](https://www.nanyangacademics.com/)

### Media
- The photos used in this site were obtained from [Unplash]()

### JS Date code snippet
- Retrieve [date object](https://www.w3schools.com/js/js_dates.asp)
- [Substring](https://www.w3schools.com/jsref/jsref_substring.asp) to cut date string

### readme and markdown
- The [CI Slack community](https://code-institute-room.slack.com) which gave much useful tips and pointers on to useful sites to:

**Markdown**

- [Adam Pritchard's Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

- [commonmark.org](https://commonmark.org/help/)

- [Github Guides - Markdown Cheatsheet](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)
- [Line breaks in markdown](https://gist.github.com/shaunlebron/746476e6e7a4d698b373)

**Writing Readme**

- [CI Readme template](https://github.com/Code-Institute-Solutions/readme-template)

- [Anna Gilhespy's *Portrait Artist* Readme](https://github.com/AJGreaves/portrait-artist/blob/master/README.md)


### Changing Edit and Delete buttons
Concept from [here](https://webdeasy.de/en/top-css-buttons-en/?referer=dev-updated-f41)
JS from [w3schools](https://www.w3schools.com/Jsref/event_onmouseover.asp)
CSS methods from [here](https://stackoverflow.com/questions/44573480/change-text-content-on-hover), 
[here](https://stackoverflow.com/questions/33057737/css-replacing-a-text-on-hover-but-smooth-transition-to-the-new-text-does-not-w), 
and [here](https://stackoverflow.com/questions/3331353/transitions-on-the-css-display-property)
[Fontawesome content with CSS](https://stackoverflow.com/questions/20782368/use-font-awesome-icon-as-css-content)
The evolving of css display:
0. attempted to try without js (pure css)
1. Discovered that display-none to display-block does not allow transition effects
2. Work towards Opacity and visibility, but realised the element still takes up space although not visible
3. A compromise was decided that to fade-in the fontawesome icon upon hover - leaves a slightly unsightly of 'align-left' as fontawesome icon is hidden

### Reversing display order in {% for %} loop
1. Reverse the order of items displayed in a `{% for %}` loop, from [stackoverflow](https://stackoverflow.com/questions/45699660/jinja2-reverse-a-list)

### Box shodows
CSS Scan [Beautiful CSS box-shadow examples](https://getcssscan.com/css-box-shadow-examples)


### text shadow for navbar
W3 Schools link [here](https://www.w3schools.com/css/css3_shadows.asp)
Initally the idea is to on hover, increase the font size by 1.075x, but due to the misalignment that occurs link [here]().
Work around is to just settle with text shadow and changing font color


### Toastr pop up. 

Lecturer Mr KX Chor for allowing us to reference his code.
[This site](https://codeseven.github.io/toastr/demo.html) and [this site](http://plnkr.co/edit/6W9URNyyp2ItO4aUWzBB?preview) for information on toatr.options usage.
[This site](https://stackoverflow.com/questions/44110049/toastr-options-dont-work) to resolve toatr.options not working


## Resolve display error in item_details page
Resolve error: `Solve 'expected  ':', got '}' error in item_details display` on item_details.template.html
with refernce from this [site](https://groups.google.com/g/pocoo-libs/c/hZIO4DziL2E?pli=1)


### Jinja documentation

Link [here](https://jinja.palletsprojects.com/en/2.11.x/templates/) for clarification on jinja

### Flask documentation

link [here](https://flask.palletsprojects.com/en/1.1.x/) for flask syntax

## Acknowledgements

- I received inspiration for this project from X
- Lots of tips, inspiration and encouragement from the wonderful CI community at [Slack](https://code-institute-room.slack.com)


