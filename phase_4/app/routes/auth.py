from flask import Blueprint, request, redirect, url_for, Flask, render_template

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you would typically handle the login logic, such as checking credentials
        username = request.form.get('username')
        password = request.form.get('password') 
        if username and password:  # Simplified check
            # Redirect to the home page or dashboard after successful login
            return redirect(url_for('home'))
        else:
            # Handle login failure (e.g., show an error message)
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')