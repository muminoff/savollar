from cqlengine import columns
from cqlengine.models import Model
from uuid import uuid1


class SavolModel(Model):
    savol_id = columns.TimeUUID(
        primary_key=True,
        default=uuid1,
        required=False
    )

    title = columns.Text(
        index=True
    )

    question = columns.Text(
        index=True
    )

    answer = columns.Text(
        index=True
    )

    author = columns.Text(
        required=False
    )

    permalink = columns.Text()

    year = columns.Integer(
        primary_key = True,
        index=True
    )

    month = columns.Integer(
        primary_key = True,
        index=True
    )

    date = columns.Integer(
        primary_key = True,
        index=True
    )

    tags = columns.List(
        columns.Text
    )
