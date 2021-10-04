from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)


def fetch(tag_str):
    tags = tag_str.split(',')
    fetch_results = []

    for tag in tags:
        api = 'https://api.hatchways.io/assessment/blog/posts?tag={}'.format(tag)
        data = requests.get(api)
        fetch_results.append(data.json())

    total_tags = []
    temp = []
    for result in fetch_results:
        total_tags += result['posts']

    """takes care of duplicates"""
    for user in total_tags:
        if user not in temp:
            temp.append(user)
    return temp


@app.route("/api/")
def index():
    return render_template('index.html')


@app.route("/api/posts/", methods=['GET'])
def api_response():
    tags = request.args.get('tags')
    """return '''<h1>The source value is: {}</h1>'''.format(tag)"""
    if tags:
        data = fetch(tags)
        res = {'posts': data}
        return jsonify(res), 200
    else:
        error = {"error": "Tags parameter is required"}
        return jsonify(error), 400


if __name__ == '__main__':
    app.run()
