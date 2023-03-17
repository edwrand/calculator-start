# importing shit
import praw

# info from create reddit app
secret = "Rn2to6DzJf3HBGBX7w1hBtRFg5NjPA"
redirect_uri = "http://localhost:8080"
client_id = "HkZWedDtcfQXQhtkXlHtdQ"
user_agent = "ethScrape"

# reddit read only instance
reddit_read_only = praw.Reddit(
    client_id="HkZWedDtcfQXQhtkXlHtdQ",  # your client id
    client_secret="Rn2to6DzJf3HBGBX7w1hBtRFg5NjPA",  # your client secret
    user_agent="ethScrape",
)

subreddit = reddit_read_only.subreddit("investing")

# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
print("Title:", subreddit.title)

# URL of the post
url = "https://www.reddit.com/r/IAmA/comments/m8n4vt/\
im_bill_gates_cochair_of_the_bill_and_melinda/"

# Creating a submission object
submission = reddit_read_only.submission(url=url)
