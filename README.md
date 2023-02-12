# Buy and Sell Auto

Here is a link to the live project. (https://.herokuapp.com/)

Buy and Sell Auto is a website for Buying and Selling Cars. It is created using a django framework.

<!--add responsive image here-->
<h2 class="center"><img src="static/images/readme-image/responsive.png"></h2>
## Contents 

- [User Experience (UX)](#user-experience-ux)
   * [User Stories](#user-stories)
   
- [Design](#design)
   * [Colour Scheme](#colour-scheme)
   * [Typography](#typography)
   * [Imagery](#imagery)
   * [Wireframes](#wireframes)
   * [Database Schema](#database-schema)


- [Features](#features)

- [Technologies](#technologies)
   * [Languages used](#languages-used)
   * [Libraries & Programs Used](#libraries-and-programs-used)

- [Testing](#)
  
- [Deployment](#deployment)
   * [Github pages](#github)
   * [Django and Heroku](#django-and-heroku)
   * [Forking](#forking)
   * [Clone](#clone)

- [Credits](#credits)
   * [Code](#code)
   * [Media](#media)

## User Experience (UX)
A User of the Buy and Sell Auto Page would be someone who is looking to buy or sell there car or cars. It could also be for someone who has an interest in cars and are looking to browse.

## User Stories 
#### EPIC | User Profile
- As a Site User I can register an account so that I can add/edit/delete my car post and I can also comment or like other car posts that has been posted by another member of the site.
- As a Site User, I can log in or log out of my account so that I can keep my account secure.
- As a Site User I can see my login status so that I know if I'm logged in or out.

#### EPIC | User Navigation
- As a Site User I can see what the website is about and know if it is what i need.
- As a Site User, I can easily navigate around the site and find what i need without any problems.
- As a Site User, I can view a paginated list of cars posted and i can select any car to view.
- As a Site User, I can click on a car post so that I can read the authors details, cars key info, description of car and view comments left by users.
- As a Site User, I can contact the Site Administration about any problems i have.
- As a Site User, I can contact the Site Administration about what i think would be good for the website in the future.

#### EPIC | User Management

As a Site User, I can Delete my own Car Post.
As a Site User, I can Edit my own Car Post so i dont need to start at the very beginner for changing details or errors. 

#### EPIC | User Interaction
As a Site User, I can Like another members post.
As a Site User, I can comment on another members post and delete the post once site admin as approved it.

#### EPIC | Site Administration
- As a Site Administrator, I can create, read, update and delete posts and comments
- As a Site Administerator, I can view feedback from the User
- As a Site Administerator, I can view issues from the User



## Design

  

### Colour Scheme
<h2 class="center"><img src="static/images/readme-image/color2.png"></h2>

- I got these four colours from the website called [coolors](coolors.co)
- #000000. This was for the writing of the website.
- #E5E5E5. This was for th background of the website.
- #FCA311. This was for hovering over links eg. nav bar. 
- #FFFFFF. This is the color in forms and car details.
- #14213D. This was used in the masthead in car details.

### Typography
-  'Gentium Book Plus', Is my main font. In my eyes i found it to be attractive for the page.
- 'sans-serif' was chosen as fallback font.

### Imagery
- 

### Wireframes
-   To View Home DeskTop click [here](docs/wireframes/home-desktop.png).
-   To View Home Ipad click [here](docs/wireframes/home-ipad.png).
-   To View Home Mobile click [here](docs/wireframes/home-mobile.png).
-   To View Add Car DeskTop click [here](docs/wireframes/addcar-desktop.png).
-   To View Add Car Ipad click [here](docs/wireframes/addcar-ipad.png).
-   To View Browse Cars DeskTop click [here](docs/wireframes/browse-car-desktop.png).
-   To View Browse Cars Mobile click [here](docs/wireframes/browse-cars-mobile.png).
-   To View Browse Cars Tablet click [here](docs/wireframes/browse-cars-tablet.png).
-   To View Car Detail DeskTop click [here](docs/wireframes/car-detail-desktop.png).
-   To View Car Detail Tablet click [here](docs/wireframes/car-detail-tablet.png).
-   To View Car Detail Mobile click [here](docs/wireframes/cardetail-mobile.png).


### Database Schema 

# Features

## Home Page

### Logo 
<h2 class="center"><img src="static/images/readme-image/buy-and-sell-auto.jpg"></h2>

- This is the logo of the site

- ### Navigation bar
<h2 class="center"><img src="static/images/readme-image/nav-bar.png"></h2>

- When Logged In. Navigation bar consists of Logo, Home Page, Cars For Sale, Contact Us Page, Add Car Page, Log Out

-   When Logged Out. Navigation bar consists of Logo, Home Page, Cars For Sale, Contact Us Page, Add Car Page,
Register, Log In.

### Hero Image
<h2 class="center"><img src="static/images/readme-image/hero-pic.png"></h2>

- Consist of Hero Pic. and text on the left with a button to browse cars.

### Welcome
<h2 class="center"><img src="static/images/readme-image/welcome-text.png"></h2>

-A welcome text about the website

### Footer
  Add Footer
<h2 class="center"><img src="static/images/readme-image/.png"></h2>

## Browse Cars
<h2 class="center"><img src="static/images/readme-image/browse-cars.png"></h2>

- Consists of all cars on the page and there is also a paginated function if there is too much.

- User can click into any car  to see its features

## Car Detail

 ### Car Detail Header
<h2 class="center"><img src="static/images/readme-image/cardetail-header.png"></h2>

- Shows image of car along with name of car, creator and when was it posted.

- ### Car Detail Key Information
<h2 class="center"><img src="static/images/readme-image/cardetail-keyinfo.png"></h2>

- Shows Key information such as Year,Nct, Phone Number, Price and description. 

- Can also see how many likes and comments it has on the post. 

- If this is the users post they can also edit the post or delete it.

- ### Car Detail Comments
<h2 class="center"><img src="static/images/readme-image/comments.png"></h2>

- This area shows the comments on the left.

- If signed in users can also comment which is showing on the right. 

## Accounts
 ### Register Page
<h2 class="center"><img src="static/images/readme-image/.png"></h2>
 Add Register Page

 ### Login Page
<h2 class="center"><img src="static/images/readme-image/login.png"></h2>
- Sign in Page.

-Ignore the sign in with github. Could not add feature and ran out of time to debug.
 #### Log out Page
<h2 class="center"><img src="static/images/readme-image/signout.png"></h2>

 To log out of the site.

- ### Features to add
<h2 class="center"><img src="static/images/readme-image/add-your-car.png"></h2>

-   Page to add your post if you are logged in.

- Consist of Name of Car, Image, Phone-number, NCT, Year of Car, Price, and a Brief Description with a submit button.

- ### Features to edit
<h2 class="center"><img src="static/images/readme-image/edit-car-post.png"></h2>

- A user can edit his car post and update to the Browse Car section .

- ### Contact us
<h2 class="center"><img src="static/images/readme-image/contact-us.png"></h2>

- Contact form for people to contact the admin to give feedback about the page or any issues that they might have. 

## Technologies

### Languages used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Libraries and Programs Used

- [Git](https://git-scm.com/)
    - Version control.
- [GitHub](https://github.com/)
    - For storing code and deploying the site.
- [Gitpod](https://www.gitpod.io/)
    - Used for building and editing my code.
- [Django](https://www.djangoproject.com/)
    - A python based framework that was used to develop the site.
- [Bootstrap](https://getbootstrap.com/)
    - For help designing the html templates.
- [Font Awesome](https://fontawesome.com/)
    - Used to obtain the icons used.
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used to help fix problem areas and identify bugs.
- [Cloudinary](https://cloudinary.com/)
    - Used to store static files and images.
- [Favicon.io](https://favicon.io/)
    - Used to generate the site's favicon.
- [PostgreSQL](https://www.postgresql.org/)
    - Database used through heroku.
- [Balsamiq](https://balsamiq.com/)
    - To create the wireframes.
- [W3C Markup Validation Service](https://validator.w3.org/) 
    - Used to validate HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate CSS code.
- [Pep8](http://pep8online.com/)
    - Used to validate Python code.
- [JSHint](https://jshint.com/)
    - Used to validate JS code.
- [Summernote](https://summernote.org/)
    - Used to add a WYSIWYG text box to the add recipe page.
- [Heroku](https://www.heroku.com/)
    - To deploy the project.



## Testing 
This Project was tested manually.



## Deployment

This project was deployed using Github and Heroku.

- ### Github 

    To create a new repository I took the following steps:

    1. Logged into Github.
    2. Clicked over to the ‘repositories’ section.
    3. Clicked the green ‘new’ button. This takes you to the create new repository page.
    4. Once there under ‘repository template’ I chose the code institute template from the dropdown menu.
    5. I input a repository name then clicked the green ‘create repository button’ at the bottom of the page.
    6. Once created I opened the new repository and clicked the green ‘Gitpod’ button to create a workspace in Gitpod for editing.

- ### Django and Heroku

    To get the Django framework installed and set up I followed the Code institutes [Django Blog cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf).

    
- ### Forking

    To fork my project you must;
    1. Sign in to Github and go to my [repository]()
    2. Locate the Fork button at the top right of the page.
    3. Select this. 
    4. The fork is now in your repositories.

- ### Clone
    To clone my project you must;

    1. Sign in to Github and go to my [repository]()
    2. Above the list of files click the green ‘code’ button.
    3. This will bring up a few options as to how you would like to clone. You can select HTTPS, SSH or Github CLI, then click the clipboard icon to copy the URL.
    4. Open git bash
    5. Type ‘git clone’ and then paste the URL you copied. Press Enter.

    For more information on cloning check out the github documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## Credits

### Content

-   All content was written by the developer with the help of Code insitute Walkthroughs and the help of my collegues on slack and tutors. Big thank you to them!

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.

-   The Teachers at Code Institude for helpful videos and walk through project

-   My collegues on the slack app who helped me when i had any issues.

### Code

 -  

 - 

 - 

 ### Media

 - 
 - 

 ### Other

