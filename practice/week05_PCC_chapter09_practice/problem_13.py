# Your team maintains a fintech platform with tools for loans,
# payments, and account management all stored in one place.
# A new microservice only needs to process loan applications.
#
# Set up both files, pull in only what the microservice needs, and use it.

from problem_13_module import LoanApplications

microservice = LoanApplications('jane doe', 3492837465, 7)
microservice.show_loan()