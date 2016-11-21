Final Project Readme Template

1. Type of project you've done (data mashup, or other -- if other, what?): data mashup 

2. Brief description of your project:

This program is written to call weather data from the OpenWeatherMap API and display it along with popular Tweets describing said weather from the given area called from the Twitter API. It works by allowing a user to input a city name and receive accurate weather info as well as key in on social talk about it. Lastly the user is able and encouraged to post a status update regarding the weather to Twitter from the program, to continue the social experience.

3. List of files being turned in, with a brief description of each one:
finproj.py: This is my program, which first has a raw input statement where the user can put in a city name. This info is put through the OpenWeatherMap API and the weather data is printed. Then the Twitter API takes the geo coordinates of the city specified and finds tweets from that location with the word weather in them. The program prints five of those. Then another raw input statement asks the user if they would like to post a status to Twitter. They can choose yes or no. If yes, they are prompted to input their tweet and the program posts it to their Twitter account.

twitterdata.txt: This is the file where the program caches the data collected from Twitter. Because I am using a module I used this file to check that I was doing what I wanted with the module. The file contains five lists containing nested dictionaries.

4. Any Python packages/modules that must be installed in order to run your project (e.g. requests):

Please install requests, json, tweepy, and test106 as test modules.

5. Data sources used (no need to provide if this does not apply):

OpenWeather API - http://openweathermap.org/current
Twitter API - http://docs.tweepy.org/en/v3.5.0/api.html

6. Instructions for running/using/playing project. 
Run python finproj.py
The program asks you to input a city name. A state or country is not always necessary. The program will also try to interpret spelling mistakes.
After inputing a name some weather data and tweets will be printed.
You have the option of posting a status to Twitter from the program. To do so, type yes and if not type no. 

7. Approximate line numbers in Python file to find the following components:
- Accumulation pattern: 86-90
- Sorting with a key function: 52
- Class definition beginning: 60
- Creating instance of the class: 62-64
- Calling methods on a class instance: 89, 93
- Importing a Python module: 1
- Using that module in the code: 19
- List comprehension OR map OR filter: 46-48
- Test cases: 80-83

8. Rationale for project: why did you do this project? Why did you find it interesting?

When I wake up in the morning one of the first things I do is check the weather for the day. I use it to decide what to wear and what to bring with me outside. I decided to do this program because regular weather apps don't give you any personalized feedback about weather conditions. My program not only gives the temperature and description, it gives feedback from people who are out experiencing the weather so a user can understand what it feels like. Also the program allows users to actively participate in social media concerning the weather. Because I am interested in user experience design I thought this project would be an interesting practice in designing a program for a user.