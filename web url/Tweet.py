import twitter, datetime

file = open("TwitterCredentials.txt")
creds = file.read().split('\n')
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
timestamp = datetime.datetime.utcnow()
response = api.PostUpdate("Tweeted at " + str(timestamp))
print("Status updated to: " + response.text)

historyFilename = "/Users/mchan1/Library/Application Support/Google/Chrome/Default/Current Session"