from APIs.admin_view import admin_panel_new
from flask import request, redirect, url_for, render_template
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, login_user, logout_user, current_user
from APIs.MMUser.model.user_model import User


@admin_panel_new.route('/admin', methods=['GET', 'POST'])
def login():
    # print(current_user.name)
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = request.get_json()
        else:
            data = request.form
        user = User.query.filter_by(email=data['email']).first()
        if user and user.password == (data['password']):
            login_user(user)
            return redirect(url_for('admin.index'))
        else:
            pass 
    return render_template('login.html')
    

@admin_panel_new.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('admin_panel_new.login'))


