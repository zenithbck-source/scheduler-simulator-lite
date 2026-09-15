from job_generator import generate_jobs
import pandas as pd

def simulate_fcfs(jobs, total_cores):
    jobs = sorted(jobs, key=lambda job: job['submit_time'])  # lower submit_time means earlier submission
    scheduled_jobs = []
    schedule = []
    avail_cores = total_cores

    for current_time in range(1, 200):
        for job in schedule:
                    if job['end_time'] == current_time:
                        avail_cores += job['ncpus']

        for job in jobs:
            if current_time >= job['submit_time'] and avail_cores >= job['ncpus']:
                start_time = current_time
                wait_time = current_time - job['submit_time']
                avail_cores -= job['ncpus']
                scheduled_jobs.append(job['job_id'])
                schedule.append({'job_id': job['job_id'], 'start_time': start_time, 'wait_time': wait_time, 'end_time': start_time + job['runtime'], 'ncpus': job['ncpus']})

        jobs = [job for job in jobs if job['job_id'] not in scheduled_jobs]
        
        current_time += 1

    for job in schedule:
        job.pop('end_time', None)
        job.pop('ncpus', None)

    return schedule

if __name__ == "__main__":
    jobs = generate_jobs(15)
    schedule = simulate_fcfs(jobs, 4)
    df = pd.DataFrame(schedule)
    print(df)