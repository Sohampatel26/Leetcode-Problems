class Twitter:
    def __init__(self):
        self.time = 0  # Global timestamp to track when tweets are posted
        self.tweets = defaultdict(list)  # Stores tweets for each user {userId: [(time, tweetId)]}
        self.following = defaultdict(set)  # Stores users a person follows {userId: {followeeId}}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """User posts a tweet with a timestamp"""
        self.tweets[userId].append((self.time, tweetId))  # Add tweet with time
        self.time += 1  # Increase time

    def getNewsFeed(self, userId: int) -> List[int]:
        """Return up to 10 most recent tweets from user and followed users"""
        minHeap = []
        users = self.following[userId] | {userId}  # Get self + followed users
        
        for user in users:
            if self.tweets[user]:  # If user has tweets
                for tweet in self.tweets[user][-10:]:  # Get last 10 tweets
                    heapq.heappush(minHeap, tweet)  # Push (time, tweetId) into heap
                    if len(minHeap) > 10:
                        heapq.heappop(minHeap)  # Remove oldest tweet

        return [tweetId for _, tweetId in sorted(minHeap, reverse=True)]  # Return tweets sorted by time

    def follow(self, followerId: int, followeeId: int) -> None:
        """Follower starts following followee"""
        if followerId != followeeId:  # Avoid self-following
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """Follower stops following followee"""
        self.following[followerId].discard(followeeId)  # Remove followee safely
