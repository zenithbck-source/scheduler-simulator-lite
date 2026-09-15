from job_generator import generate_jobs
from scheduler_utils import simulate_fcfs, simulate_sjf
import pandas as pd

jobs = generate_jobs(15)

# FCFS Policy
schedule_fcfs = simulate_fcfs(jobs, 4)
df_fcfs = pd.DataFrame(schedule_fcfs)
df_fcfs.to_csv('fcfs_results.csv', index=False)

# SJF Policy
schedule_sjf = simulate_sjf(jobs, 4)
df_sjf = pd.DataFrame(schedule_sjf)
df_sjf.to_csv('sjf_results.csv', index=False)
