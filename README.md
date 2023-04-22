# Understanding Plone 


If you have a website or intranet then you will have multiple users one will be author, one will be maintainer, one will be admin etc. So let's talk about what kind of options we have when we develop these kinds of websites. We can develop everything from scratch but  we have support of Wordpress for the complicated sites,  it's totally based on PHP and we need javascript, phython right?  I am going to talk about Ploan a modern opensource  software that could be used as a powerful tool, that have multiple addons and you can achieve anything by it. Ploan is a powerful software made with javascript and python that can be used as a CMS. It is used right now by many organisations.

Plone is itself based on `python` but with the help of apis plone amazing community has created `volto` that is based on `gatbsyJS` and `redux` for the state managment. It is SEO friendly and comes with a lot of features built in. My purpose of making this tutorial is to help you with getting started with `plone`. 

### How to use this repository ?

`git checkout chapter-one`

This has the final installed  vesrion of plone.

`git checkout chapter-two`

This will deal with the creating custom blocks in volto and customizing our frontpage


`git checkout chapter-three`

We will build a custom addons.

## chapter-one : Installing plone 

We can install the plone with two methods:

- Docker 
- Package Method (this is what we will be using )

You can also do the hybrid by starting the plone backend in docker and using the `volto` in the frontend.

As on April 2023 you require the following packages to start `plone` server on your machine

- yo
- cookiecutter
- docker
- node js (16.X.X)
- python (3.9.X)
- GNU make

You should be ready to go. Ensure that docker is running by typing the command `docker ps` in the terminal. Now its time to install `plone` using `cookiecutter` use the following command (ensure you are in your working directory)

`cookiecutter https://github.com/collective/cookiecutter-plone-starter`

It will ask couple of questions and take some time. After that it creates some local files. You will have a backend, frontend folder, make file etc.

Next step is:

`make install`

let it do its work and after this all we need to start our `backend` and `frontend` servers

open two terminals and in one of them type `make start-backend` and in other `make start-frontend`

We did it we should have `volto` running on our port 3000. 

Plone is running on port 8080 (backend). At `localhost:8080` you will see the clasic plone which is based on `python`. Feel free to use that if you want to
use python for development. It will work same as the React version `volto`


## chapter-two

Now we have plone installed and running on our local machine. You will see the homepage and you can login with default credentials `admin` | `admin` 
Plone uses the concept of component shadowing. You will see list of folders in the `omlette` folder in the frontend folder. Never change that directly. We will do anything in `src` folder but follow the same folder structure of the `omlette` folder. Suppose you can see that in `omlette>components>blocks>Navbar.jsx` exist. So if you want to change the `navbar` make the same folder structure in the `src` folder. Plone will read your `src` folder and replace its `navbar` to the `navbar` that you just created.

Lets customize the `Navbar.jsx`

```
Code goes here
```

navbar component will be replaced. Now lets do the same for `Footer.jsx`. 

```
Code goes here
```

We did it we customized our two of the components. 
Lets also change our logo.

```
Logo changing method
```
## chapter-three
Now lets add few blocks. What is blocks ? These are components that you can insert into the website while editing a page. We will create our home page with few of the exisiting blocks. I have used the following blocks to achive this and it is present by default in plone.

Now lets add our banner block so that we can use it whereever it is required ( I need in the first page )

Creation of the custom banner block.

```
code goes here 
```
Now its time customize our `events blocks`. This we will achieve by Component Shadowing. So make a folder in this dir : `custom direoctory` and add the following lines of code.

```
Code goes here 
```
Now our events list component will show items in list.

We learnt how to customize the existing components and how we can make our own and use anywhwere we want.

## chapter-four

Lets add a form that users can submit on an particular event.

Loading....







