__author__ = 'MAK'
from flask import Flask, render_template
import requests
app = Flask(__name__)

AUTHOR_URL = 'http://maqe.github.io/json/authors.json'
POSTS_URL = 'http://maqe.github.io/json/posts.json'

@app.route("/")
def template_test():

    errors = []
    try:
        authors = requests.get(AUTHOR_URL)
        posts = requests.get(POSTS_URL)

    except:
        errors.append(
            "Unable to get URL. Please make sure it's valid and try again."
        )


    authors_dicts = authors.json()

    authors_map = {author_info["id"]: author_info for author_info in authors_dicts}

    posts_map = [dict(author_details=authors_map.get(post.get('author_id')),
                      **post) for post in posts.json()]

    return render_template('template.html', posts=posts_map)


if __name__ == '__main__':
    app.run(debug=True)
