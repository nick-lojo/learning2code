# Functions for Ch. 10 Mini-Project

from pathlib import Path
import json
from datetime import datetime

def check_last_run(path):
    """Checks last_run.json to see the last time a report was run, if at
    all."""
    if path.exists():
        contents = path.read_text()
        last_run = json.loads(contents)
        print(f"\nThe last report was ran at {last_run}.")
    else:
        message = "\nA report has not been ran yet. This is the first run of"
        message += " this program."
        print(message)

def read_rounds(path):
    """Reads rounds.txt and pulls the data into the execution module for the
    report."""
    if path.exists():
        contents = path.read_text()
        message_0 = f"\nWe have located the file {path}. Standby while we"
        message_0 += f" generate your report."
        print(message_0)

        rounds = contents.splitlines()
        message_1 = "\nYour round data has been accessed and stored. We can now"
        message_1 += " continue generating your report."
        print(message_1)

        return rounds
    else:
        print('\nSorry, but the file you are looking for does not exist.')

def build_dictionary_list(rounds):
    """Turns each round into its own dictionary to be used when generating
    the report, and stores the dictionary in a list."""
    rounds_list = []
    for round in rounds:
        round_data = round.split(',')
        round_dict = {
            'Course Name':round_data[0],
            'Date Played':round_data[1],
            'Par for Course':round_data[2],
            'Player Score':round_data[3],
            'Score to Par':int(round_data[3]) - int(round_data[2])
        }
        rounds_list.append(round_dict)
    return rounds_list

def best_round(rounds_list):
    """Determines the best round by finding the minimum Score-to-Par value."""
    best_round = min(rounds_list, key=lambda round: round['Score to Par'])

    return best_round

def worst_round(rounds_list):
    """Determines the worst round by finding the maximum Score-to-Par value."""
    worst_round = max(rounds_list, key=lambda round: round['Score to Par'])

    return worst_round

def run_timestamp(path):
    """Prints the timestamp in last_run.json."""
    run_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\nThe report was ran at {run_time}.")

    content = json.dumps(run_time)
    path.write_text(content)

def report_content(rounds_list, best_round, worst_round):
    """Creates the variable holding the contents to be written in the
    report."""
    total_rounds = len(rounds_list)
    
    scores_to_par = []
    for round in rounds_list:
        score = round['Score to Par']
        scores_to_par.append(score)
    average_score = sum(scores_to_par) / len(scores_to_par)

    scores_over = []
    scores_even = []
    scores_under = []
    for score in scores_to_par:
        if score > 0:
            scores_over.append(score)
        elif score == 0:
            scores_even.append(score)
        elif score < 0:
            scores_under.append(score)
    
    contents = f"––2025 Golf Season Report––"
    
    contents += f"\n\nTotal Rounds Played: {total_rounds}"
    
    contents += f"\n\nAverage Score to Par: {average_score}"
    
    contents += f"\n\nBest Round: {best_round['Course Name']}"
    contents += f"\n\tDate Played: {best_round['Date Played']}"
    if best_round['Score to Par'] > 0:
        contents += f"\n\tScore: {best_round['Score to Par']} over par."
    elif best_round['Score to Par'] == 0:
        contents += f"\n\tScore: Even par."
    elif best_round['Score to Par'] < 0:
        contents += f"\n\tScore: {best_round['Score to Par']} under par."
    
    contents += f"\n\nWorst Round: {worst_round['Course Name']}"
    contents += f"\n\tDate Played: {worst_round['Date Played']}"
    if worst_round['Score to Par'] > 0:
        contents += f"\n\tScore: {worst_round['Score to Par']} over par."
    elif worst_round['Score to Par'] == 0:
        contents += f"\n\tScore: Even par."
    elif worst_round['Score to Par'] < 0:
        contents += f"\n\tScore: {worst_round['Score to Par']} under par."

    contents += f"\n\nTotal Rounds Over Par: {len(scores_over)}"
    contents += f"\nTotal Even Rounds: {len(scores_even)}"
    contents += f"\nTotal Rounds Under Par: {len(scores_under)}"

    return contents

def build_report(last_run_path, round_path, report_path):
    """Executes all functions at once and builds a complete report."""

    check_last_run(last_run_path)
    rounds = read_rounds(round_path)
    rounds_list = build_dictionary_list(rounds)
    best = best_round(rounds_list)
    worst = worst_round(rounds_list)
    run_timestamp(last_run_path)
    content = report_content(rounds_list, best, worst)
    report_path.write_text(content)

    message = f"\nWe have generated your report."
    message += f"\nYou can now view it in {report_path}."
    print(message)