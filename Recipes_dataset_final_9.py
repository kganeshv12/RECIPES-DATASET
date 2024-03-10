import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id="IrJa-0MBXkn2bmkDTSYYeg",
                               client_secret="WntiNpah5sWFBMMqqsBLa3BJSfQYaw",
                               user_agent="Mrecipes")

subreddit = reddit_read_only.subreddit("recipes")

posts = subreddit.hot(limit=None)

posts_dict = {"Title": [],"Details": []}

for post in posts:

    if post.stickied:
        continue

    posts_dict["Title"].append(post.title)

    if post.comments:     
        details_comment_body = None
        details_comment = None
        for comment in post.comments:
            if details_comment is None or comment.created_utc < details_comment.created_utc:
                details_comment = comment
                details_comment_body = comment.body

        posts_dict["Details"].append(details_comment_body)

    else:
        posts_dict["Details"].append(None)

top_posts = pd.DataFrame(posts_dict)
top_posts.to_csv("Output_final1.csv", index=True)
