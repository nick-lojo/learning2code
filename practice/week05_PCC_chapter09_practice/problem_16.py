# A growing fintech company splits their codebase across multiple files.
# One file depends on a tool that lives in a completely separate file.
# The dependent file needs access to that tool to function.
#
# Set up both files so the dependency works, then use it from a third program.

import problem_13_module as p13m

loan_0 = p13m.LoanApplications('john doe', 23453, 0.97)
loan_0.show_loan()