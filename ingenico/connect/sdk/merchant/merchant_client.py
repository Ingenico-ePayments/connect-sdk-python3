#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.merchant.captures.captures_client import CapturesClient
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

        Create new hosted checkout

        :return: :class:`ingenico.connect.sdk.merchant.hostedcheckouts.hostedcheckouts_client.HostedcheckoutsClient`
        """
        return HostedcheckoutsClient(self, None)

    def hostedmandatemanagements(self):
        """
        Resource /{merchantId}/hostedmandatemanagements

        Create new hosted mandate management

        :return: :class:`ingenico.connect.sdk.merchant.hostedmandatemanagements.hostedmandatemanagements_client.HostedmandatemanagementsClient`
        """
        return HostedmandatemanagementsClient(self, None)

    def payments(self):
        """
        Resource /{merchantId}/payments

        Create, cancel and approve payments

        :return: :class:`ingenico.connect.sdk.merchant.payments.payments_client.PaymentsClient`
        """
        return PaymentsClient(self, None)

    def captures(self):
        """
        Resource /{merchantId}/captures

        Get capture

        :return: :class:`ingenico.connect.sdk.merchant.captures.captures_client.CapturesClient`
        """
        return CapturesClient(self, None)

    def refunds(self):
        """
        Resource /{merchantId}/refunds

        Create, cancel and approve refunds

        :return: :class:`ingenico.connect.sdk.merchant.refunds.refunds_client.RefundsClient`
        """
        return RefundsClient(self, None)

    def payouts(self):
        """
        Resource /{merchantId}/payouts

        Create, cancel and approve payouts

        :return: :class:`ingenico.connect.sdk.merchant.payouts.payouts_client.PayoutsClient`
        """
        return PayoutsClient(self, None)

    def productgroups(self):
        """
        Resource /{merchantId}/productgroups

        Get information about payment product groups

        :return: :class:`ingenico.connect.sdk.merchant.productgroups.productgroups_client.ProductgroupsClient`
        """
        return ProductgroupsClient(self, None)

    def products(self):
        """
        Resource /{merchantId}/products

        Get information about payment products

        :return: :class:`ingenico.connect.sdk.merchant.products.products_client.ProductsClient`
        """
        return ProductsClient(self, None)

    def riskassessments(self):
        """
        Resource /{merchantId}/riskassessments

        Perform risk assessments on your customer data

        :return: :class:`ingenico.connect.sdk.merchant.riskassessments.riskassessments_client.RiskassessmentsClient`
        """
        return RiskassessmentsClient(self, None)

    def services(self):
        """
        Resource /{merchantId}/services

        Several services to help you

        :return: :class:`ingenico.connect.sdk.merchant.services.services_client.ServicesClient`
        """
        return ServicesClient(self, None)

    def tokens(self):
        """
        Resource /{merchantId}/tokens

        Create, delete and update tokens

        :return: :class:`ingenico.connect.sdk.merchant.tokens.tokens_client.TokensClient`
        """
        return TokensClient(self, None)

    def mandates(self):
        """
        Resource /{merchantId}/mandates

        Create, get and update mandates

        :return: :class:`ingenico.connect.sdk.merchant.mandates.mandates_client.MandatesClient`
        """
        return MandatesClient(self, None)

    def sessions(self):
        """
        Resource /{merchantId}/sessions

        Create new Session for Client2Server API calls

        :return: :class:`ingenico.connect.sdk.merchant.sessions.sessions_client.SessionsClient`
        """
        return SessionsClient(self, None)
