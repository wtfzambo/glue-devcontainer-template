import sys

import pytest
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from chispa.dataframe_comparer import assert_df_equality
from pyspark.context import SparkContext

from src import sample


@pytest.fixture(scope="module", autouse=True)
def glue_context():
    sys.argv.append("--JOB_NAME")
    sys.argv.append("test_count")

    args = getResolvedOptions(sys.argv, ["JOB_NAME"])
    context = GlueContext(SparkContext.getOrCreate())
    job = Job(context)
    job.init(args["JOB_NAME"], args)

    yield (context)

    job.commit()


def test_counts(glue_context: GlueContext):
    dyf = sample.read_json(
        glue_context, "s3://awsglue-datasets/examples/us-legislators/all/persons.json"
    )
    assert dyf.toDF().count() == 1961


def test_dataframe_equality(glue_context: GlueContext):
    """This one will succeed."""
    data1 = [
        (1.1, "a"),
        (2.2, "b"),
        (3.3, "c"),
        (4.4, "d"),
        (None, None),
    ]
    df1 = glue_context.spark_session.createDataFrame(data1)
    data2 = [
        (1.1, "a"),
        (2.2, "b"),
        (3.3, "c"),
        (4.4, "d"),
        (None, None),
    ]
    df2 = glue_context.spark_session.createDataFrame(data2)

    assert_df_equality(df1, df2)


def test_dataframe_equality_fail(glue_context: GlueContext):
    """This one will fail."""
    data1 = [
        (1.1, "asd"),
        (2.2, "b"),
        (3.3, "c"),
        (4.4, "d"),
        (None, None),
    ]
    df1 = glue_context.spark_session.createDataFrame(data1)
    data2 = [
        (1.1, "a"),
        (2.2, "b"),
        (3.3, "c"),
        (4.4, "d"),
        (None, None),
    ]
    df2 = glue_context.spark_session.createDataFrame(data2)

    assert_df_equality(df1, df2)
