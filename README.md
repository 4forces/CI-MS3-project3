
# GiftKids - A simple site to bless others, or to receive blessings

img <img> from am i responsive
***

## Overview

Most parents and caregivers of children will agree that children outgrow things very quickly, 
whether is it their clothes or toys. Even other accesories like bottle steamers and child seats 
can be passed around once not needed. Looking around, it is not unusual to observe
family, friends and colleagues who will not mind giving away unused children's resources 
to others in need. 

At times, some parents wish to save on extra spending, and do not mind using handed-down items. 
Some "donors", upon the birth of their subsequent child, may even look to taking back their
gifts (for e.g. strollers) to be used. 

Conceived with the thought of promoting spirit of generosity and community sharing, this site offers itself as a platform for donors and receivers to connect with each other and exchange
child-bearing resources. 

This project is deployed on Heroku [here](https://ci-ms3-giftkids.herokuapp.com/).

### Objective

GiftKids presents itself as a fictional platform for parents and caregivers to exchange 
child-bringing resources on a donation basis. Parents can use this site to give away things they already 
have or do not need anymore. For parents looking to save, resources can be sourced through this site.

***

## UX and UI

This site is designed in mind to be visually appealing to parents and kids-lovers. From the 
[colour palette](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/color-palette2.png) used to the font family 
([Fredoka One](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/font-fredokaone.PNG) for headings, 
[Ubuntu](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/font-ubuntu.PNG) for content). 

This site aims to model itself after sites that sell children related items. 
The reference websites for the color scheme, the look and feel is obtained from the website: 
["Jadusona"](https://demo.hasthemes.com/shopify/jadusona-cm.html), from various examples in 
the "Homepage Layouts." section. This website  was chanced upon while searching for children 
website inspirations on [Pinterest](https://www.pinterest.com/).

The fonts used are from Google Fonts:
- [Fredoka One](https://fonts.google.com/specimen/Fredoka+One?query=fredoka) 
- [Ubuntu](https://fonts.google.com/specimen/Ubuntu?query=ubuntu)

The colour palette used is as follows: 

<img src="static/img/readme/color-palette2.png" width="800" style="margin:0">

### User stories

1. "I believe child-bringing resources that are still usable should be shared, since young children outgrow their belongings so quickly." - *A parent who believes in sharing items that can still be used*
2. "I wish to give away used items from bringing up my children. As they have only been used a short while, it wil be a waste to throw it away." - *A generous soul*
3. "I have many unopened gifts (toys and clothes) from well-wishers, that I hope to bless other families with." - *Someone who has received many blessings and wishes to do same for other children*
4. "I am looking for items for my kids, and do not wish to spend extra cash since they will quickly outgrow it." - *A parent or caregiver looking for recylable kids items*


### Wireframes and ER Diagrams

* [Wireframe for desktop](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/wireframe-desktop.png)
* [Wireframe for mobile](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/wireframe-mobile.png)
* [ER Diagram and Relationship Schema](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/erd2-rs2.png)

## Features

This site has 5 main sections: 

- [Landing page](#Landing-page) 
- [Browse all items](#Browse-all-items)
- [Item search](#Item-search)
- [Submit new item](#Submit-new-item)
- [Update/Remove item entry](#Update/Remove-item-entry)

### Landing Page

This is the first page the visitor sees upon [arrival at this site](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/landing-page.PNG). 
The visitor is greeted with a welcome message, which has a [background image]() of a child playing with toys.
A repeated graphic of [children's toys](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/bg-body.jpg) is used as a matching
background to the theme of this site. 
There are four buttons linking to the other features of the site:
- Browse all
- Item Search
- Submit New item
- Update or Remove Entry

The visitor may also access the other features via the links on the navbar.

### Browse All items

Visitors are able to view items that have been submitted by other visitors or themselves. 
All items that have been submitted are listed on [this page](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/browse2.png), starting with the most recent. When the visitor mouse-over, 
the item-box will increase in size, indicating that it can be clicked on, leading to the **Item Details page**. 
Under **"CRUD"**, this section will fall under **"Read"**.

#### Item Details page

[This page](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/item-details.PNG) shows all the information the visitor has keyed in when submitting the item:

- Item name
- Description
- Item type
- Age range
- Condition
- Date submitted
- Nickname of donor
- Contact email of donor

The information is wrapped nicely and framed with an [image of children's clothes](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/details.jpg).

### Item Search

Visitors can search for items by item name and item type. There are five item types to select from:
- Toys & Playthings
- Clothes & Wardrobe
- Maternity (E.g. Pumps, Nursing pads)
- Accessories (E.g. Strollers, Car seats)
- Others

In line with the website's theme, the search box background is an [image of a little girl's dress](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/search.jpg)
A screenshot of the item search page [here](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/search-page.png). 

This section also covers the **"Read"** of **"CRUD"**

### Submit New Item

Users can submit items here. This page ([screenshot](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/submit-item.PNG)) requires the donor to input the following item fields:
1. Nickname of donor
2. Contact email
3. Item name
4. Description (Optional field)
5. Item type (Choose from 5 categories)
6. Age range (Infant, Toddler or Preschooler)
7. Condition (New, Like New, Used)
8. Delete after (1 week, 1 month, 3 months. Default selection is 1 month)

The "Submit Item" box is also nicely framed with a related background [image](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/post.jpg).

This is the **"Create"** part of **"CRUD"**.

Behind the scenes, the following JavaScript was used to capture the date and time of the submission:
This data was passed to a hidden html element and captured as part of the `request.form` method. The 
JavaScript and HTML code blocks are appended.

```javascript
// Javascript to capture date and time of submission
function getDate() {
  let dateSubStr = Date().substring(4,15) + ', ' + Date().substring(16,24) ;
  document.getElementById('date').value = dateSubStr;
}
```
```html
<!--hidden html input element in post_item.template.html -->
<input id="date" name="date" hidden>
```
### Update/Remove item entry

This page ([screenshot](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/update-remove.PNG)) lists all the items submitted, with the option to **Edit** or **Delete** items. 
If needed, users can update their item fields from this page.
In the event the user wishes to remove his or her item, it can also be done here.
Upon hover of the "Edit" and "Delete" buttons, an icon appears in the buttons to signal 
an expected action from the user.
This page covers the **"Update"** and **"Destroy"** portions of **"CRUD"**.

#### "Edit Item" Page

Upon clicking on the "Edit" button, the user is brought to the "Edit Item" page ([screenshot](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/edit-item.PNG)). 
The item values are pulled from the database and displayed in its respective fields for the user to modify.
This page has a custom [image of toys](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/edit.jpg) as background to suit the site theme.

#### "Delete Item" Page

When the "Delete" button is clicked, the site prompts the user if he or she wishes to proceed with the deletion. 
A screenshot of the confirmation page [here](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/delete-item.PNG). Red colour is used as the background of the dialog box, 
and the "Confirm" button to highlight to the user that deletion is a serious action since it is irreversible. 

### Features Left to Implement

1. **User Login** - For improved management (editing and deletion) of user submitted items
2. **Submit item page: Picture upload** - It is usually common for visitors to expect to see pictures as 
part of their consideration before acquiring the item
3. **Submit item page: Multi options selection for age range** - For example, some items can be used by both toddlers and pres-choolers
3. **Submit items: Auto deletion of submitted post** - This will be will be a good-to-have for items management
4. **Browse page: Item tagging** - Cross-item referencing will help visitors in their search for items
5. **Browse and Search pages: Option to sort by date of submission** - For better user experience. Current feature is just from newest to oldest
6. **Browse and Search pages: Pagination of browse/search results** - Currently all items are shown
7. **Browse and Search pages: "Back to top button** - For a more pleasant user experience
8. **Search page: More search filters, for e.g. by condition, age range** - Also for optimal user experience
9. **Edit page: "Go Back" button to return to update/remove page** - User can still click on the Update/Remove on the navbar, but this may not be  intuitive or obvious
10. **Edit page: Auto-store "current date and time" upon Edit** - Currently this is only implemented when user submits item
11. **Edit and Delete buttons: Fading out of text, and fading in of icon upon mouse-over** - For better aesthetics. Refer to last point in *Additional Notes on the Development of Features* for more information
12. **Auto delete post after 1 month, 3 months or 1 week as indicated by user during item submission** - Currently this value is only being stored and not used


### Additional Notes on the Development of Features

**Solution to resolve favicon 404 error at Edit/Delete item page:** Referred to this post at [stackoverflow](https://stackoverflow.com/questions/27234593/setting-up-static-folder-path-in-flask1)
to resolve favicon could not load (404) error when viewing the *Edit page* and *Confirm Delete page*. 

**Code for writing the CRUD Functions:** [Tim Nelson's (CI) Task Manager](https://github.com/Code-Institute-Solutions/TaskManager/tree/master/08-SearchingWithinTheDatabase/01-text_index_searching)
example was very helpful reference, especially when coding the *Create* and *Update* features. 

**Reversing Order of Items Displayed (Most recent submissions first):** The original order of items for *Search* and *Browse* pages was oldest submissions at the top. 
To reverse this order a solution was found on [stackoverflow](https://stackoverflow.com/questions/45699660/jinja2-reverse-a-list).

**Box Shadows for Contrast:** Box shadows were added so that the pages will not look too "flat".
The styles for box shadows were adopted from [CSS Scan](https://getcssscan.com/css-box-shadow-examples).


**Manipulating toastr Pop-up Elements:**
For a better visual experience, [toastr](https://github.com/CodeSeven/toastr) was implemented for the flash messages. 
[This site](https://codeseven.github.io/toastr/demo.html) and [this site](http://plnkr.co/edit/6W9URNyyp2ItO4aUWzBB?preview) was studied intently on the usage of `toastr.options`.
Issues with `toastr.options` was resolved with guidance from [here](https://stackoverflow.com/questions/44110049/toastr-options-dont-work).


**Resolve "Template Syntax Error" when displaying *item_details* page:** At one point in the development process, displaying **item_details.template.html** gave the following error:
```
template syntax error: expected token ':', got '}
```
A solution was eventually found [here](https://groups.google.com/g/pocoo-libs/c/hZIO4DziL2E?pli=1).


**Displaying Icons for Edit and Delete Buttons Upon Mouse-Over:**
The initial concept arose from [here](https://webdeasy.de/en/top-css-buttons-en/?referer=dev-updated-f41).
In the beginning, JavaScript method  (referenced from [here](https://www.w3schools.com/Jsref/event_onmouseover.asp)) was used to achieve transition
effect. However, the transition was abrupt and not smooth. Alternative workarounds were explored via CSS and tested out, referencing from stackoverflow [here](https://stackoverflow.com/questions/44573480/change-text-content-on-hover) and 
[here](https://stackoverflow.com/questions/33057737/css-replacing-a-text-on-hover-but-smooth-transition-to-the-new-text-does-not-w).
Eventually, with reference from [here](https://stackoverflow.com/questions/3331353/transitions-on-the-css-display-property) (also stackoverflow), it was decided 
to have the icons hidden, and displayed only when mouse-over. As to how to point to fontawesome content in CSS, this [link](https://stackoverflow.com/questions/20782368/use-font-awesome-icon-as-css-content) gave an explanation.

---

## Technologies Used

1. [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) to display contents in browser
2. [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics) page styling customisatoin
3. [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for DOM manipulation
4. [bootstrap](https://getbootstrap.com/) for the frontend development
5. [Fontawesome](https://www.bootstrapcdn.com/fontawesome/) iconsets for buttons
6. [Gitpod](https://www.gitpod.io/) online cloud develop environment
6. [Python](https://www.python.org/) as the backend development language
7. [Flask](https://flask.palletsprojects.com/en/1.1.x/) web framework
8. [MongoDB](https://www.mongodb.com/) for data storage
9. [Heroku](https://www.heroku.com/) for cloud platform deplpyment
10. [toastr](https://github.com/CodeSeven/toastr) for flash message pop-ups upon POST, EDIT, DELETE items
11. [ERDplus](https://erdplus.com/) to draw ER Diagrams and Relationship Schema
11. [Balsamiq](https://balsamiq.com/wireframes/desktop/) for drawing wireframes
12. [Adobe Photoshop](https://www.adobe.com/sea/products/photoshop.html) for image editing and manipulation

---

## Testing

Manual testing was done on all links and Pages. 
Test cases are as follows:

### Landing Page

No. | Test Case | Expected Result(s)
-|-|-
1 | Click on the "Giftkids" icon at the top right | User will be brought to the *Landing Page*
2 | Click "Browse" on "Browse All" button, or "Browse" on the navbar | User will be brought to the *Browse Items* page
3 | Click on "Item Search" button, or "Search" on the navbar | User will be brought to the *Search Page*
4 | Click on "Submit New Item" button, or "Submit" on the navbar | User will be brought to the *Update or Remove items Page*

### Browse Items Page

No. | Test Case | Expected Result(s)
-|-|-
1 | Mouse-over any item-box | Item-box will be expanded slightly
2 | Click on item-box | User will be redirected to *Item Details page*

### Search Items Page

No. | Test Case | Expected Result(s) | Remarks
-|-|-|-
1 | Click on "Search" button | All submitted items listed | -
2 | Type in an item name (For e.g. "chair" or "bottle") | The item(s) containing the word "chair" or "bottle will displayed | Search by item name only
3 | Select one of the 5 item types from the dropdown list (For e.g. "Toys and Playthings") | All items with type "Toys and Playthings" will be displayed | Search by item type only
4 | Type in an item name and select an item type (For e.g. type "jumpers", select "clothes") | All items with "jumpers" in their name and type: "clothes" will be displayed | Search by both item name and type
5 | Type in a random text, for e.g "abc" into the search box and click search | "No item found" will be shown | -
6 | Mouse-over any item-box in search results| Item-box expand animation will be observed | -
7 | Click on item-box in search results | User will be redirected to *Item Details page* | - 

### Submit Item Page

No. | Test Case | Expected Result(s)
-|-|-
1 | Key in all fields and select radio buttons and click "Submit" | (i) User will be brought to "Update or Remove Items" Page, (ii) Flash message **Item "\<item name>" added** will appear.
2 | Leave any field empty and click "Submit" | User will be prompted to provide compulsory fields
3 | Leave out '@' from the email in "Contact" field | User will be prompted to provide a proper email

### Update or Remove items Page

No. | Test Case | Expected Result(s)
-|-|-
1 | Click on "Edit" button | User will be redirected to "Edit Item" page, allowing user to view and make changes to previously entered fields.
2 | From the "Edit Item" page, click on "Submit" button | (i) User will be brought to "Update or Remove Items" Page, (ii) Flash message **Item \<item name> updated** will appear.
3 | From the "Update or Remove Items" page, click on "Delete" button | User will be brought to confirmation to "Delete Item" page with dialog box asking user **Are you sure you want to delete "\<item name>"?**
4 | In the confirmation to "Delete Item" page, click "Cancel" | User will be brought back to "Update or Remove Items" Page
5 | In the confirmation to "Delete Item" page, click "Confirm" | (i) User will be brought to "Update or Remove Items" Page, (ii) Flash message **Item deleted** will appear.


### Issues and bugs

- Text with no spaces exceeds the container width in item boxes (screenshot [here](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/text-exceeds-container.PNG))
- Repeat of commit messages due to infamiliarity using the *git rebase* function (screenshot [here](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/rebase-repeat-commits2.PNG))
- Line 184 of `app.py` gives the following error `f-string is missing placeholderscornflakes(F541)` 


---

## Deployment

### Github

**(a) Downloading this Project**

To download the project code, please do the following:

1. At the [project page](https://github.com/4forces/CI-MS3-project3), click on the "Code" button, and select "Download ZIP"
2. This ZIP file can be unzipped to access all project code and related files

**(b) Clone the Project**
```
To clone this project, please do the following:

1. At the [project page](https://github.com/4forces/CI-MS3-project3), click on the "Code" button 
2. Click on the "copy icon" to copy the project link to clipboard
2. This URL can be pasted it in your IDE terminal to clone in your computer
3. Type in `git remote rm origin` into the terminal
```
**(c) Creating the Repository**
1. Login to GitHub
2. Go to [CI Gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template)
3. Type in a unique name under "Repository name", and an optional description of the to-be-created repository
4. Select the option of making the repository "Public"
6. Click on the  "Create Repository from template" button
7. User will be re-directed to the newly created repository page

**(d) Deploying to GitHub Pages**
1. On the menu-bar, click on "Settings" (Beside the gear icon)
2. Scroll down to "GitHub Pages" section
3. Under "Source", select "Branch: master"
4. Click "Save", and the website will be deployed
5. Scroll down to "GitHub Pages" section again, where the deployed link can be retrieved
6. The project can be accessed via the deployed link.

### Heroku

1. Sign up for a Heroku account
2. After forking, downloading or cloning from the master branch this project from [github](https://github.com/4forces/CI-MS3-project3), 
 install all the requirements with `pip3 install -r requirements.txt` in the terminal
3. Login to Heroku by typing in the terminal `heroku login -i`
4. Create a new app (replace <app_name> with a name of your own (Note: name must be unique)
5. Check that new remote has been added by typing `git remote -v` into the terminal
6. Install gunicorn with `pip3 install gunicorn`
7. Create a file named `Procfile` (without any extension, with the first P uppercase)
8. Open the "Procfile" add the following line `web gunicorn <your python file name without .py>:app `
9. Create requirements file with the command `pip3 freeze --local > requirements.txt` in terminal
10. Commit all additions by typing following in terminal:
    - `git add .`
    - `git commit -m "<Commit Message>"`
    - Replace `<Commit Message>` with a suitable description
11. Git push to Heroku by using `git push heroku master` command
12. Add the following in Heroku Config Vars
    - MongoDB URI
    - Secret key for Flask
    - Database Name: giftkids
13. Set the debug mode to false on Heroku

## Credits

### Gitpod Setup

- Code Institute's [Gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template)

### Images and Graphics
- Images were mostly sourced from [Unplash](https://unsplash.com/), and a bit from [Pexels](https://www.pexels.com/)
- Background image graphics obtained from [freepik](https://www.freepik.com/premium-vector/toys-doodle-set_6551728.htm#page=1&query=toys&position=41)


### Secret Key
- [RandomKeygen](https://randomkeygen.com/) to generate the secret key


### Site Theme and Appearance
- [Pinterest](https://www.pinterest.com/), which led to [Jadusona](https://demo.hasthemes.com/shopify/jadusona-cm.html)
- [Code Institute Slack community](https://code-institute-room.slack.com) for recommending the following Chrome Extensions:
   - [Color palette](http://palette.site/) to extract reference site color theme
   - [Color pickr eyedropper](https://vidsbee.com/ColorPick/) to identify site colours
- [Sticker Footer](https://getbootstrap.com/docs/4.0/examples/sticky-footer/) from bootstrap


### Logo and favicion
1. [Free Logo Design](https://www.freelogodesign.org/) to generate site logo
2. [favicon.io](https://favicon.io/favicon-converter/) to convert logo to favicon


### Readme Writing and Markdown
 The [CI Slack community](https://code-institute-room.slack.com), which gave many pointers and tips on various useful sites on:

  **Markdown:**

  - [Adam Pritchard's Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
  
  - [commonmark.org](https://commonmark.org/help/)
  
  - [Github Guides - Markdown Cheatsheet](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)
 
  - [Line breaks in markdown](https://gist.github.com/shaunlebron/746476e6e7a4d698b373)

  **Writing of the Readme:**

  - [CI Readme template](https://github.com/Code-Institute-Solutions/readme-template)
  
  - [Anna Gilhespy's *Portrait Artist* Readme](https://github.com/AJGreaves/portrait-artist/blob/master/README.md)

### Syntax Clarifications

- Documentations for [Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/) and [Flask](https://flask.palletsprojects.com/en/1.1.x/)

### Deployment to Heroku

- Lecturer [Mr. KX Chor's]((https://github.com/kunxin-chor) for his detailed step-by-step guidance

---

## Acknowledgements

- The wonderful CI community at Slack for numerous useful tips, inspiration and motivation :sparkling_heart:
- Our Lecturer Mr. Paul Chor for much patience & dedication in teaching and sharing his deep knowledge with us :clap:
- My classmates (Collin, Eddy, Frances, JY and Rui Shan) in the spirit of sticking together - Encouraging, striving, struggling :satisfied:

**For education purposes only**
