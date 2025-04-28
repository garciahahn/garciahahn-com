from flask import Flask, render_template, request
import logging
import os

os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename="logs/requests.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
app = Flask(__name__)

# This is how variable converters work:
@app.route('/user/<username>')
def show_user_profile(**kwargs):
    ret = f"Also, you may look at this:{kwargs}"
    ret += f"<br>You are a bitch, {kwargs['username'].replace('_', ' ')}"
    return ret

@app.route('/path/j<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath {subpath}"

@app.route('/')
def show_main_page():
    headers_pretty = "\n".join(f"  {key}: {value}" for key, value in request.headers.items())
    log_message = (
        "===Incoming Request ===\n"
        f"Method: {request.method}\n"
        f"URL: {request.url}\n"
        f"Remote Addr: {request.remote_addr}\n"
        f"User Agent : {request.user_agent.string}\n"
        f"Referrer   : {request.referrer}\n"
        f"Host       : {request.host}\n"
        f"Scheme     : {request.scheme}\n"
        f"Headers:\n{headers_pretty}\n"
        "=============================\n"
    )
    logging.info(log_message)
    return render_template('index.html')

@app.route('/self-learning-webdev')
def show_learning_webdev():
    return render_template('webdev.html')