
  <h3 align="center">Simple Django Ecommerce App</h3>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li>
      <a href="#Notes">Notes</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



This project is a Simple Django Ecommerce App, it uses Django, Django-templates, channels and redis for ntification features <br>

you can run it locally, or with docker-compose









<!-- GETTING STARTED -->
## Getting Started

You can run this app locally or with Docker-compose

### Locally


* create virtual environment, and activate it then install the required packages from requirements.txt file
  ```sh
  pip install -r requirements.txt
  ```
* Make sure that Redis Server is Running 

* then run the local server 
  ```sh
  pip manage.py runserver
  ```
 
* then open your local server
  ```sh
  localhost:8000
  ```



### Using Docker



* first build docker image
  ```sh
  docker-compose build
  ```

* then run the image
  ```sh
  docker-compose up
  ```
  
* then open the server
  ```sh
  localhost:8000
  ```

<!-- Notes -->
## Notes

<ul>
  <li>superuser account is :
    <ul>
      <li>email: admin@mail.com</li>
      <li>password: admin</li>
    </ul>
  </li>
</ul>