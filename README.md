# WorldWideTravel

GlotbalTravel is a fictional holiday review site. This website will allow users to view, share their their expeirences on theur travels.
They will also be able comment underneath the holiday posts and also like them. Users will need to be logged in to get full functionality
of the site.

# User-Experience-Design

## The-Strategy-Plane

### Site-Goals

The site is aimed to enable travalers to have a simplostic way to share their expperiences with other fellow travelers. The site should enable
users to gain and develop insights and ideals for potential future holidays through engaging with the website.

#### User Stories

Below are the user stories that were added to the Github Project.

**EPIC | Site Navigation**
- As a User I can easily navigate around the site so that I can view different pages and sections on the site.
- As a User I can click on the about page so that so that I can find out what the website is about and how to use it.
- As a User I can view the list of recipes so that I can pick one to read.
- As a User I can see the list of holiday destinations so that I can pick one to view.
- As a User I can search for a holiday destination I that I am looking for.  

**EPIC | Crud Functionality**
- As a User I can add a travel rview so that eother people can view it. 
- As a User I can Edit/Delete my reviews so that I can make changes even after I have posted a recipe.
- As a User I can like reviews so that I can show that I like a review without having to comment.
- As a User I can add a wine that I like so that other people can see it.
- As a User I can edit a review I added so that I can update or make changes.
- As a User I can delete a review that I shared so that I have control over the reviews I share.
- As a User I can comment on other reviews so that I can provide feedback.
- As a User I can update my comments so that I can make changes incase I mistyped something or if I wish to delete the comment.
- As a User I can View likes so that I can see how popular a recipe or comment is.
- As a User I can Like comments so that I can show my appreciation of a comment.

**EPIC | Administration**
- As a Site admin I can administer the site so that I can manage the sites content.
- As a User I can reset my password so that I can change it if I have forgotten it or want to change it.


**EPIC | Register / Sign in and out**
- As a User I can create an account so that I can add my own recipes and comment on other peoples recipes.
- As a User I can Sign-in / Sign-out so that I can access features when signed in and signed out so that no one can access my account.

### Deploy on heroku<hr>

1. Generate pipfile 

   * Open the terminal and execute the command "pip3 freeze > requirements.txt" to generate a file containing all the necessary requirements.

2. Heroku Setup

   * Access the [Heroku website](https://www.heroku.com/ "Heroku Website").
   * Log in to your Heroku account and select <strong>Create an App</strong>.
   * Click on the <strong>New button</strong> and create an <strong>app</strong>.
   * Select a suitable name and choose your location.
   * Proceed to the <strong>Resources tab</strong>.
   * From the list of resources, pick <strong>Heroku Postgres</strong>.
   * Go to the <strong>Deploy tab</strong>.
   * Click on <strong>Connect to Github</strong> and find your repository.
   * Open the <strong>Settings</strong> tab.
   * Reveal Config Vars and include your Cloudinary, Database URL (from Heroku-Postgres), and Secret Key.

3. Heroku Deployment

   * Visit the <strong>Deploy tab</strong>.
   * Choose the <strong>main branch</strong> for deployment and activate <strong>automatic deployment</strong>.
   * Opt for <strong>manual deployment</strong> to build the application.


### FORK THE REPOSITORY<hr>

To create a duplicate of the repository on your account and make modifications without impacting the original project, follow these steps using the Fork feature on GitHub:

   * Access the [repository page](https://github.com/Oran-123/Hook-n-Slice-Golf "repository page") on your account.
   * In the top right corner of the page, click on the Fork button.
   * A forked version of the project will be created and added to your repository.

### CLONE THE REPOSITORY<hr>

To create a replica of the repository on your local machine, follow these steps using the Clone feature:

   * Access the [repository page](https://github.com/Oran-123/Hook-n-Slice-Golf "repository page") on your account.
   * Locate the green <strong>Code</strong> button above the code window and click on it.
   * Choose your preferred format from <strong>HTTPS, SSH</strong>, or <strong>GitClub CLI</strong>, and copy the provided URL (preferably HTTPS).
   * Open your Integrated Development Environment (IDE) and launch Git Bash.
   * Enter the command <strong>git clone</strong> followed by the copied URL in the Git Bash terminal.
   * The repository will be cloned, and a local copy will be created on your machine.