from flask import Flask, render_template
app = Flask(__name__)

posts = [
  {
           'author':'Jane Doe',
            'title':'Blog Post 1',
            'content':'First Content Post',
            'date_posted':'April, 20 2031',
            },
       


 {
           'author':'Johnny Bane',
            'title':'Blog Post 2',
            'content':'Second post Content',
            'date_posted':'May 7, 2012',
            }

        ]










if __name__ == '__main__':
    app.run(debug=True)
