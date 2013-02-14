# File: login.py

import flask, flask.views

users = {'Jessie': 'pugs'}

class Login(flask.views.MethodView):
	def get(self):
		return flask.render_template('login.html')

	def post(self):
		if 'logout' in flask.request.form:
			flask.session.pop('username', None)
			return flask.redirect(flask.url_for('login'))

		required = ['username', 'passwd']
		for r in required:
			if r not in flask.request.form:
				flask.flash("Error: {0} is required.".format(r))
				return flask.redirect(flask.url_for('login'))
				
		username = flask.request.form['username']
		passwd = flask.request.form['passwd']
		if username in users and users[username] == passwd:
			flask.session['username'] = username
		else:
			flask.flash("Your username doesn't exist or your password is incorect password!")
		return flask.redirect(flask.url_for('login'))