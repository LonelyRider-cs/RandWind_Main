About Project: 

RandWind is a random number/character generator that uses the unpredictable motion of fluids. As of currently, turbulent flow of a fluid is still a mystery to scientists and researchers because there does not exist an accurate model or definition (by equations) for it. Because of this reason, turbulent flow's motion as a function of time can be considered "random" due to its unpredictability. Using image processing from OpenCV, RandWind analyzes the motion of the fluid as a function of time to generate "random" strings that can be used for many applications. 

Website features: Website includes a user registration system which stores users in a postgres database. Passwords are salted and hashed with bcrypt. Users can save strings they've generated and retrieve them on the "My Generations" page. These strings are stored in a postgres database and rendered upon page load. Cookies keep users logged in. (Keep me logged in/forgot password buttons currently do nothing). 

YOU MUST have https:// at the start of the url for the user system to work, as it rejects unsecure connections. That is, make sure to use https://randwinddev.herokuapp.com and not randwinddev.herokuapp.com/


Repo Organization: 

node_modules - contains all necessary modules for running node.js
python - holds all needed python files for the website
  frames - contains pictures of each frame being used
  cfd.mp4 - the video used to obtain each frame
  driver.py - is called from server.js and returns a random String
  getFrames.py - extracts all frames from any video
  getRandomContours.py - used for testing to find the contours of the wind
  random10.txt - used for testing before getRandomContours.py was finished
  contours_vid.py - iterates through every frame to get contour angles
  video.py - reads in .mp4 and get every frame in video
resources - contains all js, css and images for the website
    js
      client_scripts  Used on the registration page to provide client feedback on their regstration
      my_generations  Does an ajax call on load to retrieve saved strings of user & render them
sql - contains all the sql statements that went into creating the database on a text files
views/pages - contains all .pug fiiles
requirements.txt - contains all the python modules needed to be used in the heroku python buildpack
runtime.txt - specifies which version of python needs to be used in the heroku python buildpack



Repo build/test:

Steps to push to your personal heroku account:
1. heroku login

If you need to clone the ropository first:
1. heroku git:clone -a randwind
2. cd randwind

To deploy changes:
1. git init
2. heroku git:remote -a randwind
3. git add .
4. git commit -am "message"
5. git push heroku master


Website can be found at:
https://randwinddev.herokuapp.com
