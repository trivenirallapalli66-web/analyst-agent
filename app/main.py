def analyze_business_problem(problem):
    return f"""
BUSINESS PROBLEM
{problem}

POSSIBLE CAUSES
1. Customer needs are not being fully understood
2. The user experience may have friction
3. The current solution may not provide enough value

RECOMMENDATIONS
1. Talk to customers and identify the biggest pain point
2. Simplify the user experience
3. Test one improvement at a time

PRIORITY
High

NEXT STEP
Collect customer feedback and test the highest-impact improvement.
"""


if __name__ == "__main__":
    problem = input("Describe your business problem: ")
    result = analyze_business_problem(problem)
    print(result)
