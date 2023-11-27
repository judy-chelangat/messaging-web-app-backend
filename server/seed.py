from random import choice as rc

from datetime import datetime

from faker import Faker

from app import app
from models import db, Message

fake = Faker()

usernames = [fake.first_name() for i in range(100)]
if "Duane" not in usernames:
    usernames.append("Duane")

messages_data = [
    "So it means if you pay your loan before the due date, it's a disadvantage. The last time I paid earlier, it was still a problem.",
    "The dates of payment are still indicated, and no money sent.",
    "Why was my application rejected?",
    "Hi branch, I requested my number to remain the one I was using there before 0720225243. I don't understand how it changed.",
    "I said I'll pay 5th esther camoon... In fact, you guys took a week to give me a loan, and just can't wait 4 days for me to pay back??",
    "I will pay on Sunday of 5th, and I will pay all the amount... If that is allowed??",
    "I have a late source of salary I expected, but I will pay next.",
    "I will clear my loan before 15th, kindly bear with me. January was tough.",
    "Hi can I get the batch number.",
    "Hi can I get the batch number pl.",
    "I'm still not satisfied. I am still asking for a review. My number is 0723506931 or at least give me a clear reason. Thanks.",
    "My number is 0723506931. Please have a review of my loan. I haven't defaulted and I have cleared my outstanding loan on the due date.",
    "Hi branch, I have just cleared my loan which was due today but unfortunately you have denied me. I haven't applied for a loan since December but your system says that I have applied for a loan last week. Please review my loan.",
    "I got only this number. Please help me.",
    "My number is 0790898526. Help me to validate it please so I can be able to access the loan.",
    "Hello, our salaries have been delayed but hopefully will be paid today or tomorrow.",
    "Thanks Branch for being understanding. Have cleared my loan. God bless you.",
    "Hi, kindly can I have the batch number.",
    "I have to clear by tomorrow. Please send me the batch number.",
    "I was at CRB offices and they haven't received your clearance batch number. Please send it to me so I can clear with them.",
    "No need just expunge my details from the system.",
    "Thank you for the loans I have benefitted from 'the branch'. Kindly expunge my details from your system. It's frustrating to be told to reapply in 7 days week in week out... it makes me look like a criminal. I will not be applying again.",
    "My loan has been rejected because it was rejected recently, after 14 days suspension am being suspended again for a further 7 days.",
    "Hello. Why can't you make the loan payment options more... like say a choice between weekly and monthly... someone to choose when applying for the loans... regards.",
    "Ok.",
    "Hi, sorry for the short text. However, someone used my I.D and did register a line and took M-Shwari loan but venye nili realize nilipigia Safaricom customer care and I did the payment and cleared a bill of 299. Now I don't have any. What is the way forward.",
    "Someone used.",
    "What am I supposed to do after paying in order to re.",
    "Any response to my above queries please???",
    "Kindly advise what SMS are not in my phone...",
    "And have no current loan... I'm up to date...",
    "If there is a way u can check the M-Pesa SMS in my phone... Check and see all transactions SMS are available... and M-Pesa account is very active.",
    "All my M-Pesa SMS are stored in sim card for a long period... and none has been deleted...",
    "What SMSs should I accumulate on my phone?",
    "Why has my loan application been rejected and I have never defaulted and I always pay on time?",
    "Why has the loan been rejected?",
    "Ok thanks.",
    "I forwarded my certificate of clearance from TransUnion and even you replied that my account was cleared and you gave me a loan of Kshs 250 which I cleared. What is happening to my account?",
    "I can't access your services.",
    "Ok.",
    "I promise to finish my loan by this month.",
    "The messages are on my line...",
    "I have my transaction messages with me. Why am I not approved to this time? I urgently need the cash.",
    "Hi! I hope this will take you well. I cleared my loan.",
    "Another 7 days what! For the third time now.",
    "Hey Branch, I am sorry for being late in payment but I will pay on Monday 6/2/2017. But the reason for late repayment is due to maturing of cheque because it was signed late. But I apologize and hope it will never happen again.",
    "I'll pay the 32/= together with Monday's 566/=",
    "I appreciate for the follow-up you made. Thanks a lot.",
    "How long does it for me to get the batch number cause have cleared ma loan on 31st.",
    "Within a week, specifically when please.",
    "72hrs.",
    "Hope the clearance lasts for 72hrs.",
    "This is Keynan. Did you share my details with CRB?",
    "Can I get batch number please.",
    "Can I have direct contact thus I keep untouched with the concerned authorities.",
    "Am still getting from another financial institution that I owe Branch 1068 and have already paid that amount.",
    "This is Keynan, can you kindly forward my details to CRB? Have got stucked somewhere.",
    "Sorry for that but I am still searching for the money but will be paying the loan soon as the deadline I had set passed but I am doing all I can to settle the loan.",
    "Alright. Thanks.",
    "Do I have any other loan that I didn't pay?",
    "Why don't you want to give me a loan?",
    "Sorry for the delay. I blocked my M-Pesa pin but now it's okay. Will pay by the end of today.",
    "Hi Branch, why do I have the text that my payment is late while it's due today? 3rd Feb 2017.",
    "Thanks for understanding my situation. I look forward to settling my loans on the time I have promised.",
    "I'm expecting to clear by date 8/2/2017.",
    "I've settled many of your loans before. Please don't spoil my credit report.",
    "Hi Branch, kindly let me sort out the issue in a few days... I remain committed to settling my loans on time despite a few constraints.",
]
def seed_messages():

    Message.query.delete()
    for message_text in messages_data:
        username = rc(usernames)  # random username from the list
        message = Message(username=username, body=message_text)
        db.session.add(message)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_messages()