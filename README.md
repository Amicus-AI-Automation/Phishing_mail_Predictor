# Phishing_Email_Predictor# Email Phishing Detection System

## Project Overview
This project is an end-to-end system for detecting phishing emails using machine learning. It includes:
- Data collection and preprocessing
- Model training and evaluation
- Automated feedback collection
- Retraining with user feedback
- A web-based user interface for predictions and feedback
- Integration with Gmail for real email analysis

## Main Components

### 1. Data Handling
- **pandas**: Used for reading, cleaning, and manipulating CSV data files.
- **joblib**: For saving and loading trained models and vectorizers efficiently.

### 2. Model Training
- **scikit-learn**:
  - `TfidfVectorizer`: Converts email text into numerical features using TF-IDF.
  - `LogisticRegression`: The main classification model for detecting phishing emails.
  - `train_test_split`: Splits data into training and validation sets.
  - `classification_report`, `confusion_matrix`: For model evaluation.

### 3. Feedback Loop
- **Automated Feedback**: The script automatically identifies emails where the model prediction is incorrect and saves them for retraining.
- **User Feedback**: The web UI allows users to correct model predictions, and this feedback is also saved for future retraining.

### 4. Retraining
- Combines original data and feedback data, giving higher weight to feedback samples.
- Retrains the model and compares performance with the previous version.

### 5. User Interface
- **Streamlit**: Provides a simple web app for users to paste emails, get predictions, and submit feedback.

### 6. Gmail Integration
- **google-auth-oauthlib**, **google-api-python-client**: For authenticating and accessing Gmail messages.
- **BeautifulSoup**: For parsing HTML email content.

## Training Workflow
1. **Prepare Data**: Clean and label emails as "Safe" or "Phishing".
2. **Vectorize Text**: Use TF-IDF to convert email text to features.
3. **Train Model**: Fit a logistic regression model on the training data.
4. **Evaluate**: Assess model performance using validation data.
5. **Feedback Collection**: Save incorrect predictions and user corrections.
6. **Retrain**: Merge feedback with original data, assign sample weights, and retrain the model.
7. **Deploy**: Save the updated model and vectorizer for use in the web app and scripts.

## Main Libraries Used
- pandas
- scikit-learn
- joblib
- streamlit
- google-auth-oauthlib
- google-api-python-client
- beautifulsoup4

## Purpose
This system helps organizations and individuals detect phishing emails, learn from mistakes, and continuously improve detection accuracy through automated and human feedback.
