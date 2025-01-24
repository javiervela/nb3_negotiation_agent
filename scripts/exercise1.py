"""
Exercise 1
"""

from utils import get_metrics_from_log_file
import os
import statistics
from tabulate import tabulate

BASE_LOG_DIR = "log/exercise2"


def read_log_files(base_log_dir):
    all_proposals_made = []
    all_proposals_accepted = []
    all_proposals_confirmed = []
    all_gains = {}
    all_proposal_times = []
    executions_with_proposals_made = 0
    executions_with_proposals_accepted = 0
    executions_with_proposals_confirmed = 0
    total_executions = 0

    for dir_name in os.listdir(base_log_dir):
        log_dir = os.path.join(base_log_dir, dir_name)
        if os.path.isdir(log_dir):
            total_executions += 1
            m = get_metrics_from_log_file(log_dir)

            proposals_made = m["proposals_made"]
            all_proposals_made.append(proposals_made)

            proposals_accepted = m["proposals_accepted"]
            all_proposals_accepted.append(proposals_accepted)

            for result in m["results"]:
                agent = result["agent"]
                if agent not in all_gains:
                    all_gains[agent] = []
                all_gains[agent].append(result["gain"])

            proposals_confirmed = m["proposals_confirmed"]
            all_proposals_confirmed.append(proposals_confirmed)

            if m["first_proposal_times"]["made"] is not None:
                all_proposal_times.append(int(m["first_proposal_times"]["made"]))

            if proposals_made > 0:
                executions_with_proposals_made += 1
            if proposals_accepted > 0:
                executions_with_proposals_accepted += 1
            if proposals_confirmed > 0:
                executions_with_proposals_confirmed += 1

    return {
        "all_proposals_made": all_proposals_made,
        "all_proposals_accepted": all_proposals_accepted,
        "all_proposals_confirmed": all_proposals_confirmed,
        "all_gains": all_gains,
        "all_proposal_times": all_proposal_times,
        "executions_with_proposals_made": executions_with_proposals_made,
        "executions_with_proposals_accepted": executions_with_proposals_accepted,
        "executions_with_proposals_confirmed": executions_with_proposals_confirmed,
        "total_executions": total_executions,
    }


def get_statistics(data):
    return {
        "Mean": statistics.mean(data),
        "Median": statistics.median(data),
        "Max": max(data),
        "Min": min(data),
        "Std": statistics.stdev(data) if len(data) > 1 else None,
    }


def print_statistics_table(m):
    headers = ["Metric", "Mean", "Median", "Max", "Min", "Std"]
    data = []

    all_proposals_made = m["all_proposals_made"]
    all_proposals_accepted = m["all_proposals_accepted"]
    all_proposals_confirmed = m["all_proposals_confirmed"]
    all_gains = [gain for gains in m["all_gains"].values() for gain in gains]
    all_proposal_times = m["all_proposal_times"]

    data.append(["Proposals Made"] + list(get_statistics(all_proposals_made).values()))
    data.append(
        ["Proposals Accepted"] + list(get_statistics(all_proposals_accepted).values())
    )
    data.append(
        ["Proposals Confirmed"] + list(get_statistics(all_proposals_confirmed).values())
    )
    data.append(["Utility Gained"] + list(get_statistics(all_gains).values()))
    data.append(["Proposal Times"] + list(get_statistics(all_proposal_times).values()))

    print(tabulate(data, headers=headers, floatfmt=".2f", tablefmt="grid"))

    acceptance_rate = (
        m["executions_with_proposals_accepted"] / m["executions_with_proposals_made"]
    )
    confirmation_rate = (
        m["executions_with_proposals_confirmed"] / m["executions_with_proposals_made"]
    )

    print("")
    print("Additional Metrics:")
    print("-------------------")
    print("")
    print(f"Total executions: {m['total_executions']}")
    print("")
    print(
        f"Executions with at least 1 proposal made: {m['executions_with_proposals_made']}"
    )
    print(
        f"Executions with at least 1 proposal accepted: {m['executions_with_proposals_accepted']}"
    )
    print(
        f"Executions with at least 1 proposal confirmed: {m['executions_with_proposals_confirmed']}"
    )
    print("")
    print(f"Acceptance rate: {acceptance_rate:.2%}")
    print(f"Confirmation rate: {confirmation_rate:.2%}")

    total_proposals_made = sum(m["all_proposals_made"])
    total_proposals_confirmed = sum(m["all_proposals_confirmed"])

    overall_success_rate = (
        total_proposals_confirmed / total_proposals_made
        if total_proposals_made > 0
        else 0
    )
    print(f"Overall success rate: {overall_success_rate:.2%}")


metrics = read_log_files(BASE_LOG_DIR)
print_statistics_table(metrics)
