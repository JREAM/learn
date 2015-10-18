from blog.models import *

post = Post(
    title="Hey Mom",
    slug="hey-mom",
    body="We are talking about cheddar cheese."
)
post.save()

comment = Comment(
    author="Jesse",
    body="Best post I ever seen, lol."
)
post.comments.append(comment)
post.save()
