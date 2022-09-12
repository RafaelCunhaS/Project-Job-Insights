from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    for job in read_brazilian_file(
        "tests/mocks/brazilians_jobs.csv"
    ):
        assert {"title", "salary", "type"} <= job.keys()
