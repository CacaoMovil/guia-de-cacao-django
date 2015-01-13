# -*- coding: utf-8 -*-
import subprocess

from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='amqp://guest@localhost//')

@app.task
def createLink(command):
    print "===== Symlink ====="
    return subprocess.call([command])

@app.task
def makeRender(command):
    print "==== Render ===="
    return subprocess.call([command])