import random
import pandas as pd

def generate_jobs(index, seed=42):
    random.seed(a=seed, version=2)
    
    job_id = []
    submit_time = []
    runtime = []
    ncpus = []

    for i in range(1, index):
        job_id.append(f"J{i:03d}")
        submit_time.append(random.randint(0, 50))
        runtime.append(random.randint(1, 20))
        ncpus.append(random.choice([1,2,4,8]))

    jobs = {'job_id': job_id, 'submit_time': submit_time, 'runtime': runtime, 'ncpus': ncpus}

    return jobs



if __name__ == "__main__":
    jobs = generate_jobs(21)   # if 5 jobs, input plus 1
    df = pd.DataFrame(jobs)
    print(df)