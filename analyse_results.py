import pandas as pd
import matplotlib.pyplot as plt

df_fcfs = pd.read_csv("fcfs_results.csv")
avg_wait_fcfs = df_fcfs['wait_time'].mean()
print(f"Average Wait Time for FCFS Policy: {avg_wait_fcfs:.2f}")

df_sjf = pd.read_csv("sjf_results.csv")
avg_wait_sjf = df_sjf['wait_time'].mean()
print(f"Average Wait Time for SJF Policy: {avg_wait_sjf:.2f}")

if avg_wait_fcfs > avg_wait_sjf:
    better_policy = "FCFS"
    difference = avg_wait_fcfs - avg_wait_sjf
else:
    better_policy = "SJF"
    difference = avg_wait_sjf - avg_wait_fcfs

print(f"Based on average waiting time, {better_policy} performed better by {difference:.2f}.")


fig = plt.figure(figsize=(20, 10))
ax1, ax2 = fig.subplots(1, 2, sharey=True)
ax1.bar(df_fcfs['job_id'], df_fcfs['wait_time'])
ax1.set_title("FCFS")
ax2.bar(df_sjf['job_id'], df_sjf['wait_time'])
ax2.set_title("SJF")
fig.supxlabel("Job IDs")
fig.supylabel("Wait Time")
fig.suptitle("Comparison of Wait Times between Policies")
plt.savefig("compare_wait_time.png")
plt.show()