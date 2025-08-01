# Generated using https://github.com/RedHatQE/openshift-python-wrapper/blob/main/scripts/resource/README.md


from typing import Any
from ocp_resources.resource import Resource


class Image(Resource):
    """
        Image governs policies related to imagestream imports and runtime configuration
    for external registries. It allows cluster admins to configure which registries
    OpenShift is allowed to import images from, extra CA trust bundles for external
    registries, and policies to block or allow registry hostnames.
    When exposing OpenShift's image registry to the public, this also lets cluster
    admins specify the external hostname.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).
    """

    api_group: str = Resource.ApiGroup.CONFIG_OPENSHIFT_IO

    def __init__(
        self,
        additional_trusted_ca: dict[str, Any] | None = None,
        allowed_registries_for_import: list[Any] | None = None,
        external_registry_hostnames: list[Any] | None = None,
        registry_sources: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        r"""
        Args:
            additional_trusted_ca (dict[str, Any]): additionalTrustedCA is a reference to a ConfigMap containing
              additional CAs that should be trusted during imagestream import,
              pod image pull, build image pull, and imageregistry pullthrough.
              The namespace for this config map is openshift-config.

            allowed_registries_for_import (list[Any]): allowedRegistriesForImport limits the container image registries that
              normal users may import images from. Set this list to the
              registries that you trust to contain valid Docker images and that
              you want applications to be able to import from. Users with
              permission to create Images or ImageStreamMappings via the API are
              not affected by this policy - typically only administrators or
              system integrations will have those permissions.

            external_registry_hostnames (list[Any]): externalRegistryHostnames provides the hostnames for the default
              external image registry. The external hostname should be set only
              when the image registry is exposed externally. The first value is
              used in 'publicDockerImageRepository' field in ImageStreams. The
              value must be in "hostname[:port]" format.

            registry_sources (dict[str, Any]): registrySources contains configuration that determines how the
              container runtime should treat individual registries when
              accessing images for builds+pods. (e.g. whether or not to allow
              insecure access).  It does not contain configuration for the
              internal cluster registry.

        """
        super().__init__(**kwargs)

        self.additional_trusted_ca = additional_trusted_ca
        self.allowed_registries_for_import = allowed_registries_for_import
        self.external_registry_hostnames = external_registry_hostnames
        self.registry_sources = registry_sources

    def to_dict(self) -> None:
        super().to_dict()

        if not self.kind_dict and not self.yaml_file:
            self.res["spec"] = {}
            _spec = self.res["spec"]

            if self.additional_trusted_ca is not None:
                _spec["additionalTrustedCA"] = self.additional_trusted_ca

            if self.allowed_registries_for_import is not None:
                _spec["allowedRegistriesForImport"] = self.allowed_registries_for_import

            if self.external_registry_hostnames is not None:
                _spec["externalRegistryHostnames"] = self.external_registry_hostnames

            if self.registry_sources is not None:
                _spec["registrySources"] = self.registry_sources

    # End of generated code
