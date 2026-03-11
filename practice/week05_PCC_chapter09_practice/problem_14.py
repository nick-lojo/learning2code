# The fintech platform has grown — a new program needs to handle
# both loan applications and payments at the same time.
#
# Pull in both tools from the existing module and use them.

from problem_13_module import Payments
from problem_13_module import LoanApplications

loan_0 = LoanApplications('john smith', 4974658, 0.88)
loan_0.payment_percentage.show_payments()
loan_0.show_loan()