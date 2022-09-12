from src.sorting import sort_by
import unittest


def test_sort_by_criteria():
    jobs = [
        {"date_posted": "13.05.2022", "max_salary": 5000, "min_salary": 2000},
        {"date_posted": "05.06.2022", "max_salary": 8000, "min_salary": 3000},
        {"date_posted": "02.07.2022", "max_salary": 4000, "min_salary": 1000},
    ]

    jobs_sorted = [
        {"date_posted": "02.07.2022", "max_salary": 4000, "min_salary": 1000},
        {"date_posted": "13.05.2022", "max_salary": 5000, "min_salary": 2000},
        {"date_posted": "05.06.2022", "max_salary": 8000, "min_salary": 3000},
    ]
    sort_by(jobs, "min_salary")
    unittest.TestCase().assertListEqual(jobs, jobs_sorted)
