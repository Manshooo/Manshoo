from flask import Flask
import mash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QJCY12KVUE43XFWQ4C'

app.add_url_rule('/', 'home', mash.Home.renderHomePage)

app.add_url_rule('/memes/', 'memes', mash.Memes.renderMemesPage)

app.add_url_rule('/news/', 'news', mash.News.renderNewsPage)

app.add_url_rule('/news/makePost/', 'makePost', mash.Post.renderMakePostPage)


if __name__ == "__main__":
    app.run(debug=True)