"""Researcher."""

from dns import resolver

from ..models.response import AResponse, MxResponse
from .constants import DnsTypes


def get_answers_from_domain(domain: str, dns_record_type: DnsTypes) -> list:
    """Get answers from domain.

    Args:
        domain (str): [description]
        dns_record_type (DnsTypes): [description]

    Returns:
        list: [description]
    """
    try:
        return list(resolver.query(domain, dns_record_type.value))
    except resolver.NXDOMAIN:
        return []


def get_mx_response(domain: str) -> list[MxResponse]:
    """Get mx response.

    Args:
        domain (str): domain name

    Returns:
        list[MxResponse]: result
    """
    answers: list = get_answers_from_domain(domain, DnsTypes.MX)
    return [
        MxResponse(host=str(rdata.exchange), priority=rdata.preference)
        for rdata in answers
    ]


def get_a_response(domain: str) -> list[AResponse]:
    """Get a response.

    Args:
        domain (str): domain name

    Returns:
        list[AResponse]: result
    """
    answers: list = get_answers_from_domain(domain, DnsTypes.A)
    return [
        AResponse(host=str(rdata.exchange), priority=rdata.preference)
        for rdata in answers
    ]