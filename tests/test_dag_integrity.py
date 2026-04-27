import pytest
from airflow.models import DagBag


@pytest.fixture(scope="session")
def dagbag():
    return DagBag(dag_folder="dags/", include_examples=False)


def test_no_import_errors(dagbag):
    assert not dagbag.import_errors


def test_dags_have_owners(dagbag):
    for dag_id, dag in dagbag.dags.items():
        assert dag.default_args.get("owner"), f"{dag_id} missing owner"
