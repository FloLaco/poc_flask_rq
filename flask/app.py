from flask import Flask, request
import redis
from rq import Queue, get_current_job

import time

app = Flask(__name__)

r = redis.Redis(host='redis_s', port=6379)
q = Queue(connection=r)
i = 0
test = 'test.test'

def background_task():
    r = ''
    job = get_current_job()
    print('Starting task')
    for i in range(4):
        job.meta['progress'] = 100.0 * i / 4
        r = r + str(time.time()) + '\n'
        job.save_meta()
        print(i)
        time.sleep(10)
    job.meta['progress'] = 100
    job.meta['res'] = r
    job.save_meta()
    print('Task completed')


@app.route("/task")
def add_task():

    job = q.enqueue(background_task)

    return f"Task ID is {job.id} \n"


@app.route('/task/<job_id>', methods=['GET'])
def get_res(job_id):
    job = q.fetch_job(job_id)

    if(not job.is_finished):
        return "Not yet \n", 202
    else:
        return  str(job.meta['res']) + '\n'
