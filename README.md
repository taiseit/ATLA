# Avatar: The Last Airbender Quote App

## Table of Contents

* [About the Project](#about-the-project)
  * [Inspiration](#inspiration)
  * [Built With](#built-with)
  * [How it works](#how-it-works)
  * [Future Iterations](#future-iterations)
* [Images](#images)
* [Acknowledgments](#acknowledgements)
* [Contact](#contact)

## About the Project

### Inspiration

View the deployed app <a href="https://atlaquotes.herokuapp.com">here</a>

### Built With
* Python
* Flask
* Sqlite
* SQLAlchemy
* Jinja
* BeautifulSoup
* Pandas
* Selenium
* Heroku

### How it Works
The <a href="https://animemotivation.com/avatar-the-last-airbender-quotes/">target website</a> was first scraped using Selenium and its HTML was parsed using BeautifulSoup. Pandas was used to insert the text and author of each quote into series and create a dataframe. A csv of the dataframe was then generated and imported into an Sqlite database. Both Python and the micro web framework Flask were utilized to develop the application logic and structure, and the quotes were queried using SQLAlchemy methods. The quotes were then displayed on the frontend (HTML & CSS) using Jinja. Finallym, Heroku was used to deploy the application. <br>
View the deployed app <a href="https://atlaquotes.herokuapp.com">here</a>

### Future Iterations
* (07/04/20) A bug in the deployed app has been discovered and is being examined 
* An ATLA Quote of the Day Chrome extension is currently being considered for development

## Images
<img src="static/images/app.jpg" width="375" height="500"></img> <br>
![](static/images/app.gif)

## Acknowledgements
* Special thanks to Jerold Inocencio (GitHub [jinocenc](https://github.com/jinocenc)) for providing HTML and CSS consulting
* Many thanks to <a href="https://www.reddit.com/r/TheLastAirbender/">r/TheLastAirbender</a> for continual inspiration

## Contact
Name: Taisei Tateno <br>
Personal Website: https://taiseit.github.io <br> 
Email: tjt@berkeley.edu <br>
