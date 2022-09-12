from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    jobs_types = set([value["job_type"] for value in all_jobs])

    return jobs_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    all_jobs = read(path)
    industries = set([value["industry"] for value in all_jobs])

    return industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job['industry'] == industry]


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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
