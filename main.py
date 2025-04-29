from datetime import datetime
from flask import Flask, render_template, request
import logging
import os

os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename="logs/requests.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

now = datetime.now().astimezone()

dt_str = now.strftime("%B %d, %Y at %H:%M:%S")
offset_hours = int(now.utcoffset().total_seconds() // 3600)
offset_str = f"UTC{offset_hours:+d}"

LAST_UPDATED = dt_str + ' ' + offset_str

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
    return render_template('index.html', last_updated=LAST_UPDATED)

@app.route('/self-learning-webdev')
def show_learning_webdev():
    return render_template('webdev.html', last_updated=LAST_UPDATED)

@app.route('/self-learning-webdev/text')
def show_learning_webdev_text():
    return render_template('text.html', last_updated=LAST_UPDATED)

@app.route('/self-learning-webdev/links')
def show_learning_webdev_links():
    return render_template('links.html', last_updated=LAST_UPDATED)

@app.route('/self-learning-webdev/pages/about')
def show_learning_webdev_notabout():
    return render_template('notabout.html', last_updated=LAST_UPDATED)

@app.route('/self-learning-webdev/images')
def show_learning_webdev_images():
    return render_template('images.html', last_updated=LAST_UPDATED)