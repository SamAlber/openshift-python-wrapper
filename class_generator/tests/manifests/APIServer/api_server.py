# Generated using https://github.com/RedHatQE/openshift-python-wrapper/blob/main/scripts/resource/README.md


from typing import Any
from ocp_resources.resource import Resource


class APIServer(Resource):
    """
        APIServer holds configuration (like serving certificates, client CA and CORS domains)
    shared by all API servers in the system, among them especially kube-apiserver
    and openshift-apiserver. The canonical name of an instance is 'cluster'.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).
    """

    api_group: str = Resource.ApiGroup.CONFIG_OPENSHIFT_IO

    def __init__(
        self,
        additional_cors_allowed_origins: list[Any] | None = None,
        audit: dict[str, Any] | None = None,
        client_ca: dict[str, Any] | None = None,
        encryption: dict[str, Any] | None = None,
        serving_certs: dict[str, Any] | None = None,
        tls_security_profile: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        r"""
        Args:
            additional_cors_allowed_origins (list[Any]): additionalCORSAllowedOrigins lists additional, user-defined regular
              expressions describing hosts for which the API server allows
              access using the CORS headers. This may be needed to access the
              API and the integrated OAuth server from JavaScript applications.
              The values are regular expressions that correspond to the Golang
              regular expression language.

            audit (dict[str, Any]): audit specifies the settings for audit configuration to be applied to
              all OpenShift-provided API servers in the cluster.

            client_ca (dict[str, Any]): clientCA references a ConfigMap containing a certificate bundle for
              the signers that will be recognized for incoming client
              certificates in addition to the operator managed signers. If this
              is empty, then only operator managed signers are valid. You
              usually only have to set this if you have your own PKI you wish to
              honor client certificates from. The ConfigMap must exist in the
              openshift-config namespace and contain the following required
              fields: - ConfigMap.Data["ca-bundle.crt"] - CA bundle.

            encryption (dict[str, Any]): encryption allows the configuration of encryption of resources at the
              datastore layer.

            serving_certs (dict[str, Any]): servingCert is the TLS cert info for serving secure traffic. If not
              specified, operator managed certificates will be used for serving
              secure traffic.

            tls_security_profile (dict[str, Any]): tlsSecurityProfile specifies settings for TLS connections for
              externally exposed servers.  If unset, a default (which may change
              between releases) is chosen. Note that only Old, Intermediate and
              Custom profiles are currently supported, and the maximum available
              minTLSVersion is VersionTLS12.

        """
        super().__init__(**kwargs)

        self.additional_cors_allowed_origins = additional_cors_allowed_origins
        self.audit = audit
        self.client_ca = client_ca
        self.encryption = encryption
        self.serving_certs = serving_certs
        self.tls_security_profile = tls_security_profile

    def to_dict(self) -> None:
        super().to_dict()

        if not self.kind_dict and not self.yaml_file:
            self.res["spec"] = {}
            _spec = self.res["spec"]

            if self.additional_cors_allowed_origins is not None:
                _spec["additionalCORSAllowedOrigins"] = self.additional_cors_allowed_origins

            if self.audit is not None:
                _spec["audit"] = self.audit

            if self.client_ca is not None:
                _spec["clientCA"] = self.client_ca

            if self.encryption is not None:
                _spec["encryption"] = self.encryption

            if self.serving_certs is not None:
                _spec["servingCerts"] = self.serving_certs

            if self.tls_security_profile is not None:
                _spec["tlsSecurityProfile"] = self.tls_security_profile

    # End of generated code
