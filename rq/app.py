from rq import get_current_job
import time

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
