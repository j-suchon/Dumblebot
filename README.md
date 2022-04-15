# DumbleBot 
<img src="https://www.sideshow.com/storage/product-images/907184/albus-dumbledore-1oz-silver-coin_harry-potter_silo.png" width="100" height="120"/>

### *An interactive slack-bot built with Python, Docker, and MongoDB*

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)

This small app creates an interactive slack bot.

Upon direct message receipt, the bot will return a randomly chosen line of dialog spoken
by Albus Dumbledore from one of the 8 Harry Potter films. If mentioned in the #dumblebot channel, 
Dumblebot will address all students

- A user will send a message of any type
- Dumblebot will return a random line of Dumbledore's dialog (474 objects)

**Project Layout:**

    ├── README.md
    ├── docker-compose.yml
    ├── chatbot_app
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   └── app.py
    ├── database
    │   ├── Dockerfile
    │   └── dumbledore_dialog.csv
    ├── .env

Bot can be initiated by running docker-compose up and then conversing with the bot via slack in the #dumblebot workspace.