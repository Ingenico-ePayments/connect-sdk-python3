#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.merchant.captures.captures_client import CapturesClient
from ingenico.connect.sdk.merchant.disputes.disputes_client import DisputesClient
from ingenico.connect.sdk.merchant.files.files_client import FilesClient
from ingenico.connect.sdk.merchant.hostedcheckouts.hostedcheckouts_client import HostedcheckoutsClient
from ingenico.connect.sdk.merchant.hostedmandatemanagements.hostedmandatemanagements_client import HostedmandatemanagementsClient
from ingenico.connect.sdk.merchant.mandates.mandates_client import MandatesClient
from ingenico.connect.sdk.merchant.payments.payments_client import PaymentsClient
from ingenico.connect.sdk.merchant.payouts.payouts_client import PayoutsClient
from ingenico.connect.sdk.merchant.productgroups.productgroups_client import ProductgroupsClient
from ingenico.connect.sdk.merchant.products.products_client import ProductsClient
from ingenico.connect.sdk.merchant.refunds.refunds_client import RefundsClient
from ingenico.connect.sdk.merchant.riskassessments.riskassessments_client import RiskassessmentsClient
from ingenico.connect.sdk.merchant.services.services_client import ServicesClient
from ingenico.connect.sdk.merchant.sessions.sessions_client import SessionsClient
from ingenico.connect.sdk.merchant.tokens.tokens_client import TokensClient


class MerchantClient(ApiResource):
    """
    Merchant client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.connect.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(MerchantClient, self).__init__(parent, path_context)

    def hostedcheckouts(self):
        """
        Resource /{merchantId}/hostedcheckouts

        :return: :class:`ingenico.connect.sdk.merchant.hostedcheckouts.hostedcheckouts_client.HostedcheckoutsClient`
        """
        return HostedcheckoutsClient(self, None)

    def hostedmandatemanagements(self):
        """
        Resource /{merchantId}/hostedmandatemanagements

        :return: :class:`ingenico.connect.sdk.merchant.hostedmandatemanagements.hostedmandatemanagements_client.HostedmandatemanagementsClient`
        """
        return HostedmandatemanagementsClient(self, None)

    def payments(self):
        """
        Resource /{merchantId}/payments

        :return: :class:`ingenico.connect.sdk.merchant.payments.payments_client.PaymentsClient`
        """
        return PaymentsClient(self, None)

    def captures(self):
        """
        Resource /{merchantId}/captures

        :return: :class:`ingenico.connect.sdk.merchant.captures.captures_client.CapturesClient`
        """
        return CapturesClient(self, None)

    def refunds(self):
        """
        Resource /{merchantId}/refunds

        :return: :class:`ingenico.connect.sdk.merchant.refunds.refunds_client.RefundsClient`
        """
        return RefundsClient(self, None)

    def disputes(self):
        """
        Resource /{merchantId}/disputes

        :return: :class:`ingenico.connect.sdk.merchant.disputes.disputes_client.DisputesClient`
        """
        return DisputesClient(self, None)

    def payouts(self):
        """
        Resource /{merchantId}/payouts

        :return: :class:`ingenico.connect.sdk.merchant.payouts.payouts_client.PayoutsClient`
        """
        return PayoutsClient(self, None)

    def productgroups(self):
        """
        Resource /{merchantId}/productgroups

        :return: :class:`ingenico.connect.sdk.merchant.productgroups.productgroups_client.ProductgroupsClient`
        """
        return ProductgroupsClient(self, None)

    def products(self):
        """
        Resource /{merchantId}/products

        :return: :class:`ingenico.connect.sdk.merchant.products.products_client.ProductsClient`
        """
        return ProductsClient(self, None)

    def riskassessments(self):
        """
        Resource /{merchantId}/riskassessments

        :return: :class:`ingenico.connect.sdk.merchant.riskassessments.riskassessments_client.RiskassessmentsClient`
        """
        return RiskassessmentsClient(self, None)

    def services(self):
        """
        Resource /{merchantId}/services

        :return: :class:`ingenico.connect.sdk.merchant.services.services_client.ServicesClient`
        """
        return ServicesClient(self, None)

    def tokens(self):
        """
        Resource /{merchantId}/tokens

        :return: :class:`ingenico.connect.sdk.merchant.tokens.tokens_client.TokensClient`
        """
        return TokensClient(self, None)

    def mandates(self):
        """
        Resource /{merchantId}/mandates

        :return: :class:`ingenico.connect.sdk.merchant.mandates.mandates_client.MandatesClient`
        """
        return MandatesClient(self, None)

    def sessions(self):
        """
        Resource /{merchantId}/sessions

        :return: :class:`ingenico.connect.sdk.merchant.sessions.sessions_client.SessionsClient`
        """
        return SessionsClient(self, None)

    def files(self):
        """
        Resource /{merchantId}/files

        :return: :class:`ingenico.connect.sdk.merchant.files.files_client.FilesClient`
        """
        return FilesClient(self, None)
