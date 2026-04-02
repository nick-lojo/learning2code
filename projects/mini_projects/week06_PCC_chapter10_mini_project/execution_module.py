from pathlib import Path
import json
from functions import build_report as BR

path_0 = Path('last_run.json')
path_1 = Path('rounds.txt')
path_2 = Path('report.txt')

BR(path_0, path_1, path_2)