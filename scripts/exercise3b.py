"""
Exercise 1
"""

from utils import get_metrics_from_log_file
import os
import statistics

BASE_LOG_DIR = "log/exercise3_all"


def read_log_files(base_log_dir):
    all_gains = {}

    for dir_name in os.listdir(base_log_dir):
        log_dir = os.path.join(base_log_dir, dir_name)
        if os.path.isdir(log_dir):
            m = get_metrics_from_log_file(log_dir)

            for result in m["results"]:
                agent = result["agent"]
                if agent not in all_gains:
                    all_gains[agent] = []
                all_gains[agent].append(result["gain"])

    return all_gains


def get_mean_utility_gain(all_gains):
    mean_gains = {}
    for agent, gains in all_gains.items():
        mean_gains[agent] = statistics.mean(gains)
    return mean_gains


all_gains = read_log_files(BASE_LOG_DIR)
mean_gains = get_mean_utility_gain(all_gains)

print("Mean Utility Gain of Each Agent:")
for agent in sorted(mean_gains.keys()):
    print(f"{agent}: {mean_gains[agent]:.2f}")
