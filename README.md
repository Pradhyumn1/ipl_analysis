# ipl wining precdict




depoy link -- https://pradhyumn1-ipl-analysis-app-qaozqd.streamlit.app





# Cricket Match Outcome Prediction

This project predicts the outcome of a cricket match using machine learning models. The app takes inputs such as batting team, bowling team, city, runs left, balls left, wickets left, and target runs, and provides the predicted win probability for the batting team.

Table of Contents

Project Overview
Installation
Usage
Features
Model Training
Contributing
License
Project Overview

This project is designed to predict the outcome of a cricket match based on real-time match data. It uses a machine learning model trained on past cricket match data to provide win/loss probabilities for the batting team. The app is built using Streamlit for the user interface, and scikit-learn for the machine learning model.

Installation

## 1. Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/cricket-match-prediction.git
cd cricket-match-prediction
2. Set up a virtual environment (optional but recommended):
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required packages:
bash
Copy code
pip install -r requirements.txt
4. Run the app:
bash
Copy code
streamlit run app.py
Usage

Open the app by running the Streamlit command in your terminal (streamlit run app.py).
Select the batting team, bowling team, and the city where the match is being played.
Input the number of runs left, balls left, wickets left, and the target score.
Click the "Predict Probability" button to see the win and loss probability for the batting team.
Features

Team selection: Choose between different IPL teams for both batting and bowling.
City selection: Select the city where the match is being played.
Live match data: Input live match metrics like runs left, balls left, and wickets.
Win probability prediction: Get the predicted win probability for the batting team.
Model accuracy plot: Display model accuracy during training (optional).
Model Training

The machine learning model was trained using historical cricket match data. The input features include:

Batting team
Bowling team
City
Runs left
Balls left
Wickets left
Current run rate (CRR)
Required run rate (RRR)
The model was trained using scikit-learn, and the accuracy was validated using a test set. The model is saved as a .pkl file and loaded into the Streamlit app for predictions.

Contributing

Feel free to fork this project, open issues, or submit pull requests to enhance the app.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Additional Notes:
Data files: Ensure that the model, scaler, and dictionaries are available in the working directory:
model.pkl
scaler.pkl
dictionary1.pkl (Batting team mapping)
dictionary2.pkl (Bowling team mapping)
dictionary3.pkl (City mapping)
Deployment: You can deploy this app on Streamlit Cloud or any other platform that supports Python and Streamlit.
