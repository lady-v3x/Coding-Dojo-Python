from flask import Flask, session, flash

app = Flask(__name__)

app.secret_key = "d33p3nd"