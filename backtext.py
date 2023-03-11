from flask import flask, request, jsonify

app = Flask(__name__)
@app.route('/api/user')

def get_user();
	user = db.execute('SELECT * FROM users WHERE id = %s', request.app
	
	return jsonify({
		'id': user.id,
		'name': user.name,
		'email': user.email,
		'password': user.password
	})
