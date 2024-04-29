from flask import render_template, request, flash, redirect, url_for, session
from models import db, Post, User, Comment

def get_post():
    posts = Post.query.order_by(Post.update_date.desc()).all()
    return posts

def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('main.admin'))
    return render_template('create_post.html')

def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        flash('Post updated successfully!', 'sucess')
        return redirect(url_for('main.admin'))
    return render_template('edit_post.html', post=post)

def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('main.admin'))

def authenticate():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('main.admin'))
        else:
            flash('Usuário ou senha inválida', 'error')
    return render_template('login.html')

def check_authenticated():
    if 'user_id' in session:
        posts = posts = get_post()
        return render_template('admin.html', posts=posts)
    else:
        return redirect(url_for('main.login'))
    
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        comment_text = request.form.get('comment-text')
        comment = Comment(post_id=post_id, text=comment_text)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.post', post_id=post.id))
    return render_template('post.html', post=post)