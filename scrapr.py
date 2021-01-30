import json
import os
import praw
import sqlite3
import re


class Scrapr:
    def __init__(self, config):
        self.set_config(config)
        self.init_dirs()
        self.db_path = "scrapr_dbs/{}.db".format(self.config.get("db_name"))

    def set_config(self, config):
        with open(config, "r") as f:
            self.config = json.load(f)

    def init_dirs(self):
        if not os.path.exists("scrapr_dbs"):
            os.mkdir("scrapr_dbs")

    def get_config(self):
        return self.config


class RedditScrapr(Scrapr):
    def __init__(self, config, praw_config):
        super().__init__(config)
        self.init_praw(praw_config)
        self.init_db()

    def init_praw(self, praw_config):
        with open(praw_config, "r") as f:
            self.praw = praw.Reddit(**json.load(f))

    def init_db(self):
        if not os.path.exists(self.db_path):
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute(
                "CREATE TABLE IF NOT EXISTS reddit_scrapr (permalink text PRIMARY KEY, title text, selftext text, author text, keywords text);"
            )
            conn.commit()

    def insert_submission(self, permalink, title, selftext, author, keywords):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute(
            "SELECT permalink FROM reddit_scrapr WHERE permalink = ?", [permalink]
        )
        if c.fetchone():
            return False
        c.execute(
            "INSERT INTO reddit_scrapr (permalink, title, selftext, author, keywords) VALUES (?,?,?,?,?)",
            [permalink, title, selftext, author, keywords],
        )
        conn.commit()

    def scrape_submission(self, submission):
        title = submission.title
        author = submission.author.name
        permalink = submission.permalink
        selftext = submission.selftext
        combined_text = title + selftext
        keywords = self.config.get("keywords")
        keywords_regex = "|".join(keywords)
        tracked_users = self.config.get("tracked_users")

        if not keywords and not tracked_users:
            self.insert_submission(permalink, title, selftext, author, keywords_regex)

        if author in tracked_users:
            self.insert_submission(permalink, title, selftext, author, keywords_regex)

        text_regex = re.compile(keywords_regex, re.IGNORECASE)

        if text_regex.search(combined_text):
            self.insert_submission(permalink, title, selftext, author, keywords_regex)

    def scrape_hot(self):
        sorting = self.config.get("sorting")
        limit = self.config.get("limit")
        for submission in self.praw.subreddit(self.config.get("subreddit")).hot(
            limit=limit
        ):
            print("Scraping: {}".format(submission.title))
            self.scrape_submission(submission)


if __name__ == "__main__":
    scrapr = RedditScrapr("config.json", "praw_config.json")
    scrapr.scrape_hot()
