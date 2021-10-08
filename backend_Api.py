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


def sort_list(data: list, desc=None, parameter='id'):
    data = sorted(data, key=lambda field: field[parameter])
    if desc == 'desc':
        return data[::-1]
    return data


@app.route("/api/")
def index():
    return render_template('index.html'), 200


@app.route("/api/posts/", methods=['GET'])
def api_response():
    tags = request.args.get('tags')
    sortBy = request.args.get('sortBy')
    direction = request.args.get('direction')

    if tags:
        data = fetch(tags)
        if not sortBy:
            if direction and direction == "desc" or direction == "asc":
                data = sort_list(data, desc=direction)
                res = {'posts': data}
                return jsonify(res), 200
            elif not direction:
                data = sort_list(data)
                res = {'posts': data}
                return jsonify(res), 200
            else:
                error = {"error": "direction parameter is invalid"}
                return jsonify(error), 400

        elif sortBy and sortBy == 'reads' or sortBy == 'likes' or sortBy == 'popularity' or sortBy == 'id':
            if direction and direction == "desc" or direction == "asc":
                data = sort_list(data, desc=direction, parameter=sortBy)
                res = {'posts': data}
                return jsonify(res), 200
            elif not direction:
                data = sort_list(data, parameter=sortBy)
                res = {'posts': data}
                return jsonify(res), 200
            else:
                error = {"error": "direction parameter is invalid"}
                return jsonify(error), 400
        else:
            error = {"error": "sortBy parameter is invalid"}
            return jsonify(error), 400

    else:
        error = {"error": "Tags parameter is required"}
        return jsonify(error), 400


if __name__ == '__main__':
    app.run()
