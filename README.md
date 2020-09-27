# Avatar: The Last Airbender Quote App

## Table of Contents

* <a href="https://atlaquotes.herokuapp.com">View the app here</a>
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
Although the Covid 19 Pandemic has been a challenging and unusual time for us all, one of the few positives that has emerged through it all was being introduced to Avatar: The Last Airbender for the first time when my sisters started rewatching it on Netflix. Each evening my family and I would gather in the living room with snacks and blankets to watch a few episodes, and share the Avatar-inspired content that we had discovered on instagram and reddit earlier in the day. Being able to experience such a masterpiece together with my family was a special experience, and one that I'll always look back fondly on now that it has passed. This project is dedicated to all the fans of ATLA (except fans of the movie, sorry).

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
The <a href="https://animemotivation.com/avatar-the-last-airbender-quotes/">target website</a> was first scraped using Selenium and its HTML was parsed using BeautifulSoup. Pandas was used to insert the text and author of each quote into series and create a dataframe. A csv of the dataframe was then generated and imported into an Sqlite database. Both Python and the micro web framework Flask were utilized to develop the application logic and structure. The quotes were queried from the database using SQLAlchemy methods, and displayed on the frontend (HTML & CSS) using Jinja. Finally, the application was deployed on Heroku. <br>
View the deployed app <a href="https://atlaquotes.herokuapp.com">here</a>

### Future Iterations
* (07/04/20) A bug in the deployed app has been discovered and is being examined 
* An ATLA Quote of the Day Chrome extension is currently being considered for development

## Images
![](static/images/app.gif) <br>
<img src="static/images/app.jpg" width="375" height="500"></img>
 
## Acknowledgements
* Special thanks to Jerold Inocencio (GitHub [jinocenc](https://github.com/jinocenc)) for providing HTML and CSS consulting
* Many thanks to <a href="https://www.reddit.com/r/TheLastAirbender/">r/TheLastAirbender</a> for the continual inspiration

## Contact
Name: Taisei Tateno <br>
Personal Website: https://taiseit.github.io <br> 
Email:  tjt (at) berkeley (dot) edu  <br>
