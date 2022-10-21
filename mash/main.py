from flask import render_template

class Header:

    def renderHeader():
        return render_template('header.html')

class Footer:

    def renderFooter():
        return render_template('footer.html')

renderHeader = Header.renderHeader
renderFooter = Footer.renderFooter

class Memes:
    def renderMemesPage():
        return render_template('memes.html', header=renderHeader, footer=renderFooter)

class Home:
    def renderHomePage():
        return render_template('mainPage.html', header=renderHeader, footer=renderFooter)

class News:
    """News page with Post instances"""
    
    def renderNewsPage():
        return render_template('newsPage.html', header=renderHeader, footer=renderFooter)

class Post:
    """Class Post """

    def renderMakePostPage():
        return render_template('makePost.html', header=renderHeader, footer=renderFooter)