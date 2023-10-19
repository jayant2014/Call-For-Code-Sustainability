from flask import Flask, request, app, jsonify, render_template, url_for

@app.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('home.html', current_user=current_user)
    else:
        return render_template('home.html')

# Implement other routes in a similar manner

if __name__ == '__main__':
    app.run(debug=True)
