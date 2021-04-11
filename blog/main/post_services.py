from .models import Post


def post_all():
    all_posts = Post.objects.all()
    return all_posts


def post_find(post_id: int) -> Post:
    return Post.objects.get(id=post_id)
