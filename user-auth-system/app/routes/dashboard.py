from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@login_required
def dashboard_home():
    return render_template('dashboard.html', username=current_user.username)
