veekportfolio a web application which contains a professional introduction about me,
info about the projects I have undertaken, a blog to share my experince and recieve 
feedbacks via comments, a contact section for vistor to get message across to me which
will be devivered directly to my mail and links to view my social and professional 
accounts. I used Python and JavaScript
Aditional infomation: 

Admin mamagement: the admin can visit the '/admin/' to add projects and edit the
articles to be display on the blog section.

Environmental variables used are:
EMAIL_HOST,
EMAIL_HOST_USER,
EMAIL_HOST_PASSWORD,
CONTACT_MAIL (where mail will be delivered to)

Files info: 

main;

main/manage.py: this is the main file that runs the web application. 

main/requirements.txt: contains the dependencies required for the web application to
run. 

main/README.md: contains info about the app.

main/db.sqlite3: contains the database for the project.

main app;

main/veekportfolio/templates folder:
main/veekportfolio/templates/base.html: this conatins the base webpage use in the 
project avoid repetitions.

main/veekportfolio/settings.py: this contains the settings for the project.


main/veekportfolio/urls.py: links all routings in the project together.

main/veekportfolio/wsgi.py

veekprojects app;

main/veekprojects/migrations folder: contains all migration carried out after the app's 
models file was created.

main/veekprojects/static/css/base.css: contains the style sheet for base.html

main/veekprojects/static/img/...: contains all pictures used in the web application


main/veekprojects/static/js/base.js: contains the javaScript file for base.html

main/veekprojects/templates/project_detail.html: displays the detail about a 
specific project that was selected.

main/veekprojects/templates/project_index.html: displays all projects available in the
database.

main/veekprojects/admin.py: allows admin to add, edit and monitor each project.

main/veekprojects/apps.py: sets the app config name

main/veekprojects/models.py: contains the models for the app, which is the project.

main/veekprojects/tests.py: no test was included for the app.

main/veekprojects/urls.py: contains the url routes for the app.

main/veekprojects/views.py: contains the processes during routing in the app.

veekblog app;

main/veekblog/migrations folder: contains all migration carried out after the app's 
models file was created.

main/veekblog/templates/blog_detail.html: display the article selected, form to leave a
comment and comments if available.

main/veekblog/templates/blog_cartegory.html: display all articles added to the blog via 
the admin page with option to sort by cartegory.

main/veekblog/admin.py: allows admin to add, edit and monitor each article in the blog.

main/veekblog/apps.py: sets the app config name.

main/veekblog/forms.py: contains the comment form required in the blog_detail.html page.

main/veekblog/models.py: contains the models for the app, which is the blog.

main/veekblog/tests.py: no test was included for the app.

main/veekblog/urls.py: contains the url path for contains the url routes for the app.

main/veekblog/views.py: contains the processes during routing in the app.

myprofile app;

main/myprofile/migrations folder: contain all migration carried out after the app's 
models file was created.

main/myprofile/templates/contact.html: displays the page which allows users to leave a
message for the account owner which will bw send to the contact_mail.

main/myprofile/templates/my_profile.html: displays the page which shows user a profile 
picture a brief introduction.

main/account/templates/registration/logged_out.html: displays the page that shows if
logout is successful.

main/myprofile/admin.py: no admin code for this app.

main/myprofile/apps.py:sets the app config name.

main/myprofile/models.py: no models was created for the app.

main/myprofile/test.py: no test was created for the app.

main/myprofile/urls.py: contains the url path for contains the url routes for the app.

main/myprofile/views.py: contains the processes during routing in the app.

media folder: this contains the pictures for the projects uploaded.
