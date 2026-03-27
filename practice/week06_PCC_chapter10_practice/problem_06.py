# A stadium ticketing system needs to log a message every time
# a gate opens. You have a string called gate_log that contains
# three separate log entries, each on its own line.
#
# Your job: store all three entries in a file called gate_log.txt.
# Confirm it worked by opening the file after running your script.

from pathlib import Path

path = Path('gate_log.txt')
content = 'Gate A opened at 9:00'
content += '\nGate B opened at 9:15'
content += '\nGate C opened at 9:30'
path.write_text(content)