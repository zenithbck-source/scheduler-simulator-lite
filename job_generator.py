import random

def generate_jobs(index, seed=42):
    random.seed(a=seed, version=2)
    jobs = []

    for i in range(0, index):
        job_id = (f"J{i+1:03d}")
        submit_time = random.randint(0, 50)
        runtime = random.randint(1, 20)
        ncpus = random.choice([1,2,4])
        jobs.append({'job_id': job_id, 'submit_time': submit_time, 'runtime': runtime, 'ncpus': ncpus})

    return jobs

if __name__ == "__main__":
    jobs = generate_jobs(15)
    print(jobs)