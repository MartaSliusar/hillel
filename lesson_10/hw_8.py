from abc import ABC, abstractmethod
from time import time
from typing import List


class SocialChannel(ABC):
    def __init__(self, name: str, followers: int):
        self.name = name
        self.followers = followers

    @abstractmethod
    def post_message(self, message: str):
        pass


def post_a_message(channel: SocialChannel, message: str) -> None:
    channel.post_message(message)


class YouTubeChannel(SocialChannel):
    def post_message(self, message: str):
        print(f"Posted to YouTube: {message}")


class FacebookChannel(SocialChannel):
    def post_message(self, message: str):
        print(f"Posted to Facebook: {message}")


class TwitterChannel(SocialChannel):
    def post_message(self, message: str):
        print(f"Posted to Twitter: {message}")


class Post:
    def __init__(self, message: str, timestamp: int):
        self.message = message
        self.timestamp = timestamp


def process_schedule(posts: List[Post], channels: List[SocialChannel]) -> None:
    current_time = time()
    for post in posts:
        if post.timestamp <= current_time:
            for channel in channels:
                post_a_message(channel, post.message)


youtube_channel = YouTubeChannel("YouTube", 30000)
facebook_channel = FacebookChannel("Facebook", 10000)
twitter_channel = TwitterChannel("Twitter", 2000)

channels = [youtube_channel, facebook_channel, twitter_channel]

posts = [
    Post("Hello YouTube!", 1694963252),
    Post("Hi Facebook!", 1694963252),
    Post("Hey Twitter!", 1694963252),
]

process_schedule(posts, channels)
