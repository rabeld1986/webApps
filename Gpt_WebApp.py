from flask import Flask, redirect, url_for, request
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
import os


app = Flask(__name__)
@app.route('/answer/<name>')
def answer(name):
    return 'Answer: %s' % name

@app.route('/ask_deloitte', methods=['POST', 'GET'])
def question():
    os.environ["OPENAI_API_KEY"] = "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"
    db = SQLDatabase.from_uri(r"sqlite:///C:\Users\rdelcastillo\testDB.db")
    llm = OpenAI(temperature=0)
    db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

    if request.method == 'POST':
        user = request.form['qn']
        q = db_chain.run(user)
        return redirect(url_for('answer', name=q))
    else:
        user = request.args.get('qn')
        return redirect(url_for('answer', name=user))


if __name__ == '__main__':
    #run html file on browser,
    "file:///C:/Users/rdelcastillo/PycharmProjects/gpt_sql_test/index_file.html"

    app.run(debug=True)
