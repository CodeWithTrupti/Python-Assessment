import requests
from datetime import datetime, timedelta

API_URL = "https://jsonplaceholder.typicode.com/posts"


cached_posts = None
cache_time = None


def fetch_posts():
    """Fetch posts from API"""
    global cached_posts, cache_time
    
    # Check if cache is valid 
    if cached_posts is not None and cache_time is not None:
        time_passed = datetime.now() - cache_time
        if time_passed.seconds < 300:  # 5 minutes = 300 seconds
            print("Using cached data...")
            return cached_posts
    
    # Fetch from API
    print("Fetching from API...")
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        cached_posts = response.json()
        cache_time = datetime.now()
        return cached_posts
    else:
        print("Error fetching posts")
        return None


def get_total_posts(posts):
    #total posts
    if posts is None:
        return 0
    return len(posts)


def get_user_posts(posts, user_id):
    #get posts by specific user
    user_posts = []
    for post in posts:
        if post['userId'] == user_id:
            user_posts.append(post)
    return user_posts


def get_longest_title(posts):
    #post with longest_title
    if not posts:
        return None
    
    longest = posts[0]['title']
    for post in posts:
        if len(post['title']) > len(longest):
            longest = post['title']
    
    return longest


def create_new_post():
    
    new_post = {
        'title': 'My Test Post',
        'body': 'This is a test post',
        'userId': 1
    }
    
    response = requests.post(API_URL, json=new_post)
    if response.status_code == 201:
        return response.json()
    return None


def main():
    # Fetch 
    posts = fetch_posts()
    
    
    print(f"\nTotal Posts: {get_total_posts(posts)}")
    
    user_1_posts = get_user_posts(posts, 1)
    print(f"Posts by User 1: {len(user_1_posts)}")
    
    longest = get_longest_title(posts)
    print(f"\nLongest Title: {longest}")
    
    # Create post
    print("\nCreating new post...")
    new_post = create_new_post()
    if new_post:
        print(f"New post created with ID: {new_post['id']}")


if __name__ == "__main__":
    main()