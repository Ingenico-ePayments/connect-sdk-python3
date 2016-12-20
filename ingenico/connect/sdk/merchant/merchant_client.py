#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.merchant.hostedcheckouts.hostedcheckouts_client import HostedcheckoutsClient
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
        :param parent:       :class:`ApiResource`
        :param path_context: dict[str, str]
        """
        super(MerchantClient, self).__init__(parent, path_context)

    def hostedcheckouts(self):
        """
        Resource /{merchantId}/hostedcheckouts

        Create new hosted checkout

        :return: :class:`HostedcheckoutsClient`
        """
        return HostedcheckoutsClient(self, None)

    def payments(self):
        """
        Resource /{merchantId}/payments

        Create, cancel and approve payments

        :return: :class:`PaymentsClient`
        """
        return PaymentsClient(self, None)

    def payouts(self):
        """
        Resource /{merchantId}/payouts

        Create, cancel and approve payouts

        :return: :class:`PayoutsClient`
        """
        return PayoutsClient(self, None)

    def productgroups(self):
        """
        Resource /{merchantId}/productgroups

        Get information about payment product groups

        :return: :class:`ProductgroupsClient`
        """
        return ProductgroupsClient(self, None)

    def products(self):
        """
        Resource /{merchantId}/products

        Get information about payment products

        :return: :class:`ProductsClient`
        """
        return ProductsClient(self, None)

    def refunds(self):
        """
        Resource /{merchantId}/refunds

        Create, cancel and approve refunds

        :return: :class:`RefundsClient`
        """
        return RefundsClient(self, None)

    def riskassessments(self):
        """
        Resource /{merchantId}/riskassessments

        Perform risk assessments on your customer data

        :return: :class:`RiskassessmentsClient`
        """
        return RiskassessmentsClient(self, None)

    def services(self):
        """
        Resource /{merchantId}/services

        Several services to help you

        :return: :class:`ServicesClient`
        """
        return ServicesClient(self, None)

    def sessions(self):
        """
        Resource /{merchantId}/sessions

        Create new Session for Client2Server API calls

        :return: :class:`SessionsClient`
        """
        return SessionsClient(self, None)

    def tokens(self):
        """
        Resource /{merchantId}/tokens

        Create, delete and update tokens

        :return: :class:`TokensClient`
        """
        return TokensClient(self, None)
