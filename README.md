(Insert logo)

# My Experimental Blog

## **1.0 - Overview**

A personal project where I have built a simple platform to make micro-posts with the intent of experimenting with SEO, analytics and digital marketing. The research and experiment purpose of the app means that setup and maintaining the blog is simple as there are no requirements for user accounts or validation. Micro-blogs also allow me to find time to put out regular content and track analytics with more data.

Practicing with SEO and analytics was something I always found interesting about the web as it compiles many great areas of study such as psychology, marketing and of course tech. I felt that watching tutorials and reading was quite limited to how much I could pick up so this project is my opportunity to get hands on real experience. 


## **2.0 Technology Summary**

The app’s stack is relatively simple with a django backend to utilise the features of the django admin page to make posts quickly. The client side uses a React app which was intentional as it is an opportunity to explore how SEO works with single page applications. 

### **2.1 - Client Side**

- Jinja Templating Engine
- CSS3
- ES6 JavaScript

Initially this project aimed to use a React frontend however due to the risk of hurting SEO (see section XX) and with React being quite opinionated, I decided to use the django in-built Jinja templating engine. This also allows me to experiment and build custom html/css features without having to worry about handling states and passing too much data around via props. 

### **2.2 - Server Side -**

- Python
- Django
- Postgres Database

The Django backend was selected over Flask generally for the ease of setup as the project is not too demanding on the server side and the in-built django admin page was sufficient for blogging as it is only me as the superuser. Furthermore Jinja is already setup with Django quite nicely and so it meant that transitioning from React to Jinja was relatively smooth. 



## **3.0 Project Details**

### **3.1 - SEO issues**

After researching how Google uses crawlers and indexing for everything in their search database, it was apparent that there have been potential issues in the past regarding how single page applications are assessed by Google. 

The nature of single page applications using AJAX requests to update their data rather than in the static html that is sent from the server meant that it can be 'expensive' to crawl and index information. This is not so much a big deal for a hobby project but the purpose of this project was to learn about SEO and analytics and so this is what spurred on the change from using React to Jinja. 

It is likely Google have resolved most of the issues with finding the information they need in the javascript files rather than the html but for now, it made sense to keep it static and remove the requirement client side rendering.

### **3.2 - Modular Design**

The modular design of the site is a great playground for trying out new tech and ways of building elements without too much impact on the rest of the page. The target is to build a variety of different ‘blocks’ to have a purpose and be responsive. Then allow for them to be styled differently and fit onto any future projects. 

I borrowed this concept from how React components work where I will be able to build pages fast by piecing together various responsive blocks I have made myself or from other creators. This will also allow me to transfer this code over to other projects with ease if required.

Depending on how this project goes, I have pre-built JWT authentication and integrated it into other projects along with a commenting features and so Django’s modular style will mean I can transfer the apps over to this project with ease.