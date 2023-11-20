# CashFlow-minimizer-using-ShortestPathAlgorithm-Splitwise
The CashFlow Minimizer project aims to streamline and optimize financial transactions within a given network using a Shortest Path Algorithm. This innovative solution is designed to minimize cash flow within a complex financial network, ultimately reducing transaction costs and improving overall financial efficiency. The modern application Splitwise uses the same algorithm and works on the same principle. 
# Getting started
For example, if the following weighted directed graph represents some people and the arrows represent debts between them (Alice owes Bob $20 and Charlie $5, Bob owes Charlie $10, etc.):

How to pick the first person? To pick the first person, calculate the net amount for every person(Alice, bob, charlie) where net amount is obtained by subtracting all debts (amounts to pay) from all credits (amounts to be paid). Once net amount for every person is evaluated, find two persons with maximum and minimum net amounts(here it is ALice (minimum), charlie(maximum)). These two persons are the most creditors and debtors. The person with minimum of two is our first person to be settled and removed from list. Let the minimum of two amounts be x. We pay ‘x’ amount from the maximum debtor to maximum creditor and settle one person. If x is equal to the maximum debit, then maximum debtor is settled, else maximum creditor is settled.

![Alt Text](File1.png)


