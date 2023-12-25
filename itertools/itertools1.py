from itertools import accumulate


class IncomeTax:
    salary_by_month = {
        "january": 4012,
        "february": 4000,
        "march": 4003,
        "april": 4040,
        "may": 4200,
        "jun": 4001,
        "jul": 4003,
        "august": 4000,
        "september": 4000,
        "october": 4000,
        "november": 4000,
        "december": 4001
    }

    @classmethod
    def calculate_income_tax(cls):
        yearly_salary = accumulate(cls.salary_by_month.values())
        total = list(yearly_salary)[-1]
        if total > 40000:
            print("you must pay income taxes")


cs = IncomeTax()
cs.calculate_income_tax()
