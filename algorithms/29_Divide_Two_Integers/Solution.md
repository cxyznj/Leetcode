# 29. Divide Two Integers

The key point is that the quotient of a division is just a number of times that subtract the divisor form the dividend without making it negative (assume both take absolute value before process). 

In deed we can subtract the divisor from dividend once by once and count the times of subtraction. Using bit operation to exponential increasing the value of divisor can accelerate this process. Increasing the divisor by left shifting bit operation and count the times of shifting, then add 1 shifting right counts on the quotient —— it is the times that subtraction. Repeat this process until the dividend less than divisor.

