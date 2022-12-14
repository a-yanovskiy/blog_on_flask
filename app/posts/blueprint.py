from flask import Blueprint, render_template
from models import Post

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    posts_list = Post.query.all()
    return render_template('posts/index.html',
                           posts=posts_list)


@posts.route('/<slug>')
def post_detail(slug):
    post_by_slug = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/post_detail.html', post=post_by_slug)
