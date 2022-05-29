"""Stream type classes for tap-pipedream."""

from __future__ import annotations

from singer_sdk import typing as th

from tap_pipedream.client import PipedreamStream


class UserSources(PipedreamStream):
    """Sources stream."""

    name = "user_sources"
    path = "/users/me/sources/"
    primary_keys = ["id"]

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("component_id", th.StringType),
        th.Property("active", th.BooleanType),
        th.Property("created_at", th.IntegerType),
        th.Property("updated_at", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("name_slug", th.StringType),
    ).to_dict()


class Webhooks(PipedreamStream):
    """Webhooks stream."""

    name = "webhooks"
    path = "/users/me/webhooks"
    primary_keys = ["id"]

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("description", th.StringType),
        th.Property("url", th.StringType),
        th.Property("active", th.BooleanType),
        th.Property("created_at", th.IntegerType),
        th.Property("updated_at", th.IntegerType),
    ).to_dict()
