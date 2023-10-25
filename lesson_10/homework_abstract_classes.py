import time
from abc import ABC, abstractmethod
from dataclasses import dataclass

# each social channel has a type
# and the current number of followers
# SocialChannel = tuple[str, int]


class SocialChannel(ABC):
    def __init__(self, type, subs):
        self.type: str = type
        self.subs: int = subs

    @abstractmethod
    def post_message(self, message):
        """
        This function shows how each channel message will look
        """


# each post has a message and the timestamp when it should be posted
# Post = tuple[str, int]
@dataclass
class Post:
    message: str
    timestamp: int


class Youtube(SocialChannel):
    def post_message(self, message):
        print(
            f"{self.type}-channel presents! {message}. "
            f"This message can see only {self.subs} subscribers"
        )


class Facebook(SocialChannel):
    def post_message(self, message):
        print(
            f"You can see it only on {self.type}! {message}. "
            f"This message can see only {self.subs} subscribers"
        )


class Twitter(SocialChannel):
    def post_message(self, message):
        print(
            f"Posted on {self.type}-channel: {message}. "
            f"This message can see only {self.subs} subscribers"
        )


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        for channel in channels:
            time.sleep(post.timestamp)
            channel.post_message(post.message)


youtube = Youtube("Youtube", 1500)
facebook = Facebook("Facebook", 56321)
twitter = Twitter("Twitter", 15)


channels = [
    youtube,
    facebook,
    twitter,
]

posts = [
    Post(
        "Cascades of red wine flood a city's streets "
        "in Portugal after huge tanks rupture",
        5,
    ),
    Post(
        "Monster hunters are conducting the largest "
        "search of Loch Ness in more than 50 years",
        3,
    ),
    Post(
        "People are freaking out over a question mark "
        "seen in space. Scientists can explain",
        2,
    ),
]

print(process_schedule(posts=posts, channels=channels))
