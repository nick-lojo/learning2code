# You're updating a risk scoring tool for an insurtech startup.
#
# A separate file contains multiple functions, but you only need one.
# Bring just that function into your main script and call it directly
# without using the file's name.

from problem_35_module import score_risks

unscored_risks = ['financial', 'supply chain', 'reputational']
scored_risks = []

score_risks(unscored_risks, scored_risks)