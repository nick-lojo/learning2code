# Your team finds themselves typing out a long class name repeatedly
# across a large program — it's slowing them down.
# A shorthand would make the code cleaner and faster to write.
#
# Demonstrate two different ways to create and use a shorthand like this.

from problem_13_module import LoanApplications as LA

loan_0 = LA('jane doe', 2345971, 1)
loan_0.show_loan()