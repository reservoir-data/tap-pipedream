"""Pipedream tap class."""

from __future__ import annotations

from singer_sdk import Stream, Tap
from singer_sdk import typing as th
from singer_sdk.streams import RESTStream

from tap_pipedream.streams import UserSources

STREAM_TYPES: list[type[RESTStream]] = [
    UserSources,
]


class TapPipedream(Tap):
    """Singer tap for Pipedream."""

    name = "tap-pipedream"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "token",
            th.StringType,
            required=True,
            description="API Token for Pipedream",
        ),
        th.Property(
            "start_date",
            th.IntegerType,
            description="Earliest timestamp to get data from",
        ),
    ).to_dict()

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of Pipedream streams.
        """
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
