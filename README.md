

<h1 text-align="center">BATTLESHIP</h1>

<!-- Click on [Battleship](https://annickrynne.github.io/Battleship/) to access the live project. -->


# INTRODUCTION
Battleship is game written purely in Python and designed to run on the Code Institute mock terminal on Heroku.

<br>

# EXPERIENCE (UX)
The target audience: Playing on a Python terminal will attract an audience who is nostalgic of the first games that they used to play with in the seventies. But it's likely that a younger generation of 'gamers' will find the it interesting too. Terminal based games seem to be becoming popular again.

## User Stories
1. First Time Visitor Goals
   - I want the rules to be easy to grasp
   - I want to know my score against the computer

2. Returning Visitor Goals
   - I want to play again to improve my score
    
3. Frequent User Goals
   - I want to see if there is any added features

## Flowchart

![ ](docs/flowchart.jpeg)

<br>

# FEATURES


## Welcome! Enter name

- The player is invited to enter his/her name

![ ](docs/battleship_flowchart.jpeg)


## Rules
## Run the game
## Quit or Continue
## Future Features
## Data Model

<br>

# TECHNOLOGIES USED
## Languages
- PYTHON


## Frameworks
<ul>
      <li>Git: Used for version control: using Gitpod terminal to commit to Git  and Push to GitHub</li>
      <li>GitHub: Used to store the projects code after being pushed from Git</li>
      <li>Heroku: Used to run in the Code Institute mock terminal</li>
</ul>

## Programmes and tools
- PEP8 to validate the code

<br>

# TESTING
I tested my code in pep8 on numerous occasions
<!-- ![ ](docs/pep8.png) -->

## Fixed Buggs
- When I printed the computer_board, the ships didn't show. I fixed it by correcting the indentation in the 'while' loop.
- I first put the Rules function at the top and couldn't figure out why the 'sunk' ships didn't show on the player_board. I had to move the function under play_game.

## Remaining Buggs

<br>

# DEPLOYMENT
To deploy project 3, I created an account on the [Heroku website](https://www.heroku.com/)
<ul>
   <li>Log in Heroku</li>
   <li>Click on "New" button in top right corner, select "App"</li>
   <li>You're in the Heroku dashboard. Enter app name: a-battleship-game ; Enter region: Europe</li>
   <li>Click on "Create App"</li>
   <li>Click on the "Settings" tab (important: must be done before "Deploy")</li>
   <li>"Add buildpack" section: click and select, in this order (you can change the order by dragging if necessary): 1) Heroku/python 2) Heroku/nodejs</li>
   <li>"Config Vars" section: 1) Config PORT (key) 8000 (value) 2) Config CREDS (Key) and copy-paste content of the package.json file from your vs code folder</li>
   <li>Click on the "Deploy" tab</li>
   <li>Method: select GitHub (it should say, 'connected') and connect to your repository by clicking on Search</li>
   <li>You're connected to your repository: scroll down the page and chose to click on Enable Automatic Deploy or (manual) Deploy Branch to see the deployment</li>
   <li>When done, "Your app was successfully deployed" appears. Click on the View button to see the app </li>
</ul>
<br>

# CREDITS
## Code:
I followed some free tutorials found online to help me build the game with Python. I used some code from the Code Institute runnable exercices and challenges. I also found some useful code on GitHub:

   - [How to code Battleship in Python - Single player game](https://www.youtube.com/watch?v=tF1WRCrd_HQ)
   - [Coding Advanced Battleship Part I in Python](https://www.youtube.com/watch?v=xz9GrOwQ_5E)
   - https://github.com/dmoisset/battleship-dojo

## Acknowledgements to: 
- My cohort classmates for sharing useful information every day and useful info on the Code Institute Slack Channels
- The developers who post helpful videos on games tutorials for beginners in JavaScript on YouTube