import csv
import pandas as pd
import math
import itertools


def load_data():
    data = pd.read_csv('infomasiaelprat_gmail_com_emails_raw_data.csv', sep=',')
    return data

def save_data(emails):
    with open('email_output.csv', 'w') as myfile:
        writer = csv.writer(myfile, quotechar =' ')
        for email in emails:
            email.strip()
            writer.writerow([email])

def check_email(email):
    emailstodelete=['infomasiaelprat@gmail.com','golivaisern@gmail.com', 'tereoliva77@gmail.com','lcnet@netegeslcnet.com',
                    'villagesimmobles@gmail.com','web@masiaelprat.com']
    if email not in emailstodelete and '@' in email:
        return True

def main():
    raw_data = load_data()
    print(len(raw_data))
    print(raw_data.head())

    columns_to_delete = ['address', 'is_replied', 'is_first_reply', 'reply_time', 'is_first_message', 'gmail_thread_id',
                         'direct_message']

    features = list(raw_data.columns)
    print(features)

    for column in columns_to_delete:
        features.remove(column)

    print(raw_data.head())

    emails_from = pd.unique(raw_data['from']).tolist()
    print(' number of emails from', len(emails_from))

    emails_recipients_to = pd.unique(raw_data['recipients_to']).tolist()
    emails_recipients_to_ = [str(value) for value in emails_recipients_to]
    emails_recipients = [value.split(',') for value in emails_recipients_to_ if ',' in value]
    for email in emails_recipients:
        if ',' in email:
            email.split(',')

    total_emails = emails_recipients + emails_from

    result = list(itertools.chain.from_iterable(total_emails))
    print('length result', len(result))
    emails = list()
    for email in set(result):
        if check_email(email):
            emails.append(email)

    print('total emails', len(emails))
    return emails

emails = main()
for email in emails:
    print(email)
save_data(emails)
