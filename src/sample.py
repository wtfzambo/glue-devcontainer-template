import sys

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext


try:
    from dotenv import load_dotenv  # type: ignore

    load_dotenv()
except ImportError:
    pass


class GluePythonSampleTest:
    def __init__(self):
        params = []
        if "--JOB_NAME" in sys.argv:
            params.append("JOB_NAME")
        args = getResolvedOptions(sys.argv, params)

        self.context = GlueContext(SparkContext.getOrCreate())
        self.job = Job(self.context)

        if "JOB_NAME" in args:
            jobname = args["JOB_NAME"]
        else:
            jobname = "test"
        self.job.init(jobname, args)

    def run(self):
        dyf = read_json(
            self.context,
            "s3://awsglue-datasets/examples/us-legislators/all/persons.json",
        )
        dyf.printSchema()

        self.job.commit()


def read_json(glue_context: GlueContext, path):
    dynamicframe: DynamicFrame = glue_context.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths": [path], "recurse": True},
        format="json",
    )
    return dynamicframe


if __name__ == "__main__":
    GluePythonSampleTest().run()
