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




