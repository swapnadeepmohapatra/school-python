import random

dataStore = {
    "accounts": [
        {
            "id": "btxr2ny834hn2rx",
            "mailID": "example@company.com",
            "password": "abcxyz",
            "name": "Modi"
        }, {
            "id": "ny89cr24dilmqwhbct89q34",
            "mailID": "company@example.com",
            "password": "xyzabc",
            "name": "Amit Shah"
        }],
    "mails": {
        "btxr2ny834hn2rx": {
            "received": [
                {
                    "id": 1,
                    "recipient": "btxr2ny834hn2rx",
                    "sender": "ny89cr24dilmqwhbct89q34",
                    "subject": "Fired",
                    "body": "You are fired. Don't come to office from tomorrow. And send your laptop to us latest by EOD.",
                }, {
                    "id": 2,
                    "recipient": "btxr2ny834hn2rx",
                    "sender": "ny89cr24dilmqwhbct89q34",
                    "subject": "Payment success",
                    "body": "₹50,000.00 has been deposited to Zerodha equity from account 9380 through UPI on 16 Aug 2021. Your transaction Reference number is 7113688311563099.",
                }
            ],
            "sent": []
        },
        "ny89cr24dilmqwhbct89q34": {
            "received": [],
            "sent": [
                {
                    "id": 1,
                    "recipient": "btxr2ny834hn2rx",
                    "sender": "ny89cr24dilmqwhbct89q34",
                    "subject": "Fired",
                    "body": "You are fired. Don't come to office from tomorrow. And send your laptop to us latest by EOD.",
                }, {
                    "id": 2,
                    "recipient": "btxr2ny834hn2rx",
                    "sender": "ny89cr24dilmqwhbct89q34",
                    "subject": "Payment success",
                    "body": "₹50,000.00 has been deposited to Zerodha equity from account 9380 through UPI on 16 Aug 2021. Your transaction Reference number is 7113688311563099.",
                }
            ],
        }
    }
}

welcomeMessage = """
Please Choose among the below options
1. Go to Inbox
2. Go to Sent Items
3. Compose New Mail
4. Exit

Enter Your Choice:"""


def main():
    char = input("Do you have an account? y/n: ")
    if char.lower() == "y":
        mailId = input("Enter Email ID: ")
        password = input("Enter Password: ")
        checkIdPass(mailId, password)
    else:
        createNewAccount()


def checkIdPass(mailId, password):
    for item in dataStore["accounts"]:
        if(item["mailID"] == mailId):
            if(item["password"] == password):
                print("\nWelcome", item["name"], "!!!")
                login(item)
                break
            else:
                print("Incorrect Password")
                break

    else:
        print("Account Not Found")


def goToInbox(userId):
    print("\nInbox\n")
    mails = dataStore["mails"][userId]["received"]
    if len(mails) < 1:
        print("Empty\n")
        print("=================")
        choice = input(
            "Enter 1 to go back to main menu. Enter 2 to Exit. ")
        if int(choice) == 1:
            login(getUserFromId(userId))
        return

    for mail in mails:
        print(str(mail["id"]) + ".", mail["subject"])

    print("\n=================")
    print("Enter the id of the mail to view")
    choice = int(input())
    checkMail(mails[choice - 1], userId, goToInbox)


def checkMail(mail, userId, cb):
    print("")
    print("From:", getUserFromId(mail["sender"])["name"])
    print("Subject:", mail["subject"])
    print("")
    print("Body:", mail["body"])
    print("")
    print("=================")
    choice = input(
        "Enter 1 To Go Back, Enter 2 to go back to main menu. Enter 3 to Exit. ")
    if int(choice) == 1:
        cb(userId)
    elif int(choice) == 2:
        login(getUserFromId(userId))
    else:
        print("Thankyou for visiting our site.")


def goToSent(userId):
    mails = dataStore["mails"][userId]["sent"]
    print("\nSent Items\n")
    if len(mails) < 1:
        print("Empty\n")
        print("=================")
        choice = input(
            "Enter 1 to go back to main menu. Enter 2 to Exit. ")
        if int(choice) == 1:
            login(getUserFromId(userId))
        return

    for mail in mails:
        print(str(mail["id"]) + ".", mail["subject"])

    print("\nEnter the id of the mail to view")
    choice = int(input())
    checkMail(mails[choice - 1], userId, goToSent)


def gotToCompose(userId):
    print("\nCompose Mail\n")
    receiver = input("Enter receiver's mail id: ")
    subject = input("Enter subject: ")
    body = input("Enter mail body: ")
    sendMail(receiver, subject, body, userId)

    print("\nMail Send\n")
    print("=================")
    choice = input("Enter 1 to go back to main menu. Enter 2 to Exit. ")
    if int(choice) == 1:
        login(getUserFromId(userId))
    else:
        print("Thankyou for visiting our site.")


def sendMail(receiver, subject, body, senderUserId):
    senderUser = getUserFromId(senderUserId)
    receiverUser = getUserFromMail(receiver)

    dataStore["mails"][receiverUser["id"]]["received"].append({
        "id": len(dataStore["mails"][receiverUser["id"]]["received"]) + 1,
        "recipient": receiverUser["id"],
        "sender": senderUser["id"],
        "subject": subject,
        "body": body,
    })

    dataStore["mails"][senderUser["id"]]["sent"].append({
        "id": len(dataStore["mails"][senderUser["id"]]["sent"]) + 1,
        "recipient": receiverUser["id"],
        "sender": senderUser["id"],
        "subject": subject,
        "body": body,
    })

    print(dataStore["mails"])


def getUserFromId(id):
    for user in dataStore["accounts"]:
        if user["id"] == id:
            return user
    else:
        return None


def getUserFromMail(mailId):
    for user in dataStore["accounts"]:
        if user["mailID"] == mailId:
            return user
    else:
        return None


def login(user):
    print(welcomeMessage)
    choice = int(input())
    if choice == 1:
        goToInbox(user["id"])
    elif choice == 2:
        goToSent(user["id"])
    elif choice == 3:
        gotToCompose(user["id"])
    elif choice == 4:
        print("Thankyou for visiting our site.")


def createNewAccount():
    name = input("Enter name: ")
    mailID = input("Enter Mail id: ")
    password = input("Enter password: ")

    addAccount(name, mailID, password)
    print("\nAccount Created\n")
    main()


def addAccount(name, mailID, password):
    account = {
        "id": randomIDGenerator(),
        "name": name,
        "mailID": mailID,
        "password": password
    }

    dataStore["accounts"].append(account)

    accountMails = {
        account["id"]: {
            "sent": [],
            "received": []
        }
    }

    dataStore["mails"].update(accountMails)


def randomIDGenerator():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]

    _id = ""
    for _ in range(16):
        _id += digits[(random.randint(0, len(digits)-1))]

    return _id


if __name__ == "__main__":
    main()
