from generator import Posts


posts = Posts.readJson('posts-bibs.json')
posts.generate('.')
