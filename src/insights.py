from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    jobs_types = set([value["job_type"] for value in all_jobs])

    return jobs_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    all_jobs = read(path)
    industries = set(
        [value["industry"] for value in all_jobs if value["industry"] != ""]
    )

    return industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    all_jobs = read(path)
    max_salary = max(
        [
            int(value["max_salary"])
            for value in all_jobs
            if value["max_salary"].isdigit()
        ]
    )

    return max_salary


def get_min_salary(path):
    all_jobs = read(path)
    min_salary = min(
        [
            int(value["min_salary"])
            for value in all_jobs
            if value["min_salary"].isdigit()
        ]
    )

    return min_salary


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError

    elif int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError

    elif type(salary) != int:
        raise ValueError

    return int(job["min_salary"]) <= salary <= int(job["max_salary"])


def filter_by_salary_range(jobs, salary):
    return [
        job
        for job in jobs
        if job["min_salary"] < job["max_salary"]
        and type(salary) == int
        and job["min_salary"] <= salary <= job["max_salary"]
    ]
