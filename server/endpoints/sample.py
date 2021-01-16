from flask import Flask, jsonify, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView

from datetime import datetime

# blueprint to be used in app
views = Blueprint('views', __name__)


class BlogPage(MethodView):

    def get(self):
        # import from app to use db model
        from models import Blog, db

        page = request.args.get('page', 1, type=int)
        blogs = Blog.query.paginate(page=page, per_page=5)
        bloglist = []
        for blog in blogs.items:
            bloglist.append({'title': blog.title, 'content': blog.content})
        return jsonify({'blogs': bloglist})

    def post(self):
        # import from app to use db model
        from models import Blog, db

        # detects form data!
        blog = dict(request.form)
        title = blog['title'][0]
        content = blog['content'][0]
        author_id = blog['author_id'][0]
        date_added = datetime.now()
        try:
            new_blog = Blog(title=title, content=content,
                            author_id=author_id, date_added=date_added)
            db.session.add(new_blog)
            db.session.commit()
            return jsonify({'content': 'blog added!'})
        except:
            db.session.rollback()
            return jsonify({'content': 'there was a problem adding blog'})


views.add_url_rule('/blog', view_func=BlogPage.as_view('blog'))