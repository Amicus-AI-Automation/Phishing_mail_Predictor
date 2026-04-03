# app.py
from gmail_client import gmail_authenticate, fetch_all_message_ids, read_email,get_label_id,move_to_suspected
from model_inference import predict_email
import pandas as pd
import os
import time

 # Save the prediction result to a CSV file
def save_prediction(message_id, subject, body, pred, prob):
    row = {
        "message_id": message_id,
        "subject": subject,
        "email_text": body,
        "prediction": "Phishing" if pred == 1 else "Safe",
        "phishing_probability": prob
    }

    df = pd.DataFrame([row])
    file_path = "data/live_gmail_predictions.csv"

    df.to_csv(
        file_path,
        mode="a",
        header=not os.path.exists(file_path),
        index=False
    )

 # Check if a message ID has already been processed
def is_already_processed(message_id, file_path):
    if not os.path.exists(file_path):
        return False

    df = pd.read_csv(file_path)
    return message_id in df["message_id"].values


 # Test and print the Gmail profile information
def test_gmail_profile(service):
    profile = service.users().getProfile(userId="me").execute()
    print("Gmail profile OK:", profile["emailAddress"])

 # Process new emails, predict phishing, and save results
def process_new_emails(service):
    messages = fetch_all_message_ids(service, max_pages=10)
    label_id= get_label_id(service,"Suspected_phish")
    print(f"Label ID for 'Suspected_phish': {label_id}")
    print(f"Fetched {len(messages)} messages for backfill")

    for msg in messages:
        message_id, subject, body = read_email(service, msg["id"])

        # OPTIONAL: keep or remove dedup
        if is_already_processed(message_id, "data/live_gmail_predictions.csv"):
            continue

        pred, prob = predict_email(subject + " " + body)
        move_to_suspected(service, message_id, label_id)
        save_prediction(message_id, subject, body, pred, prob)
        


 # Main entry point for the application
def main():
    service = gmail_authenticate()
    test_gmail_profile(service)

    print("Starting ONE-TIME backfill run...")
    process_new_emails(service)
    print("Backfill completed.")

if __name__ == "__main__":
    main()
