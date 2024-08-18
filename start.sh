#!/bin/bash

# Clone the repository
git clone https://github.com/crazebotz/MyFlask.git

# Navigate into the repository directory
cd MyFlask

# Install dependencies from requirements.txt
pip3 install -U -r requirements.txt

# Start the Flask application
python app.py
