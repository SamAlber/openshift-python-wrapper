# Generated using https://github.com/RedHatQE/openshift-python-wrapper/blob/main/scripts/resource/README.md

from typing import Any

from timeout_sampler import TimeoutSampler, TimeoutWatch

from ocp_resources.resource import MissingRequiredArgumentError, NamespacedResource
from ocp_resources.utils.constants import PROTOCOL_ERROR_EXCEPTION_DICT, TIMEOUT_4MINUTES


class Deployment(NamespacedResource):
    """
    Deployment enables declarative updates for Pods and ReplicaSets.
    """

    api_group: str = NamespacedResource.ApiGroup.APPS

    def __init__(
        self,
        min_ready_seconds: int | None = None,
        paused: bool | None = None,
        progress_deadline_seconds: int | None = None,
        replicas: int | None = None,
        revision_history_limit: int | None = None,
        selector: dict[str, Any] | None = None,
        strategy: dict[str, Any] | None = None,
        template: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        r"""
        Args:
            min_ready_seconds (int): Minimum number of seconds for which a newly created pod should be
              ready without any of its container crashing, for it to be
              considered available. Defaults to 0 (pod will be considered
              available as soon as it is ready)

            paused (bool): Indicates that the deployment is paused.

            progress_deadline_seconds (int): The maximum time in seconds for a deployment to make progress before
              it is considered to be failed. The deployment controller will
              continue to process failed deployments and a condition with a
              ProgressDeadlineExceeded reason will be surfaced in the deployment
              status. Note that progress will not be estimated during the time a
              deployment is paused. Defaults to 600s.

            replicas (int): Number of desired pods. This is a pointer to distinguish between
              explicit zero and not specified. Defaults to 1.

            revision_history_limit (int): The number of old ReplicaSets to retain to allow rollback. This is a
              pointer to distinguish between explicit zero and not specified.
              Defaults to 10.

            selector (dict[str, Any]): A label selector is a label query over a set of resources. The result
              of matchLabels and matchExpressions are ANDed. An empty label
              selector matches all objects. A null label selector matches no
              objects.

            strategy (dict[str, Any]): DeploymentStrategy describes how to replace existing pods with new
              ones.

            template (dict[str, Any]): PodTemplateSpec describes the data a pod should have when created from
              a template

        """
        super().__init__(**kwargs)

        self.min_ready_seconds = min_ready_seconds
        self.paused = paused
        self.progress_deadline_seconds = progress_deadline_seconds
        self.replicas = replicas
        self.revision_history_limit = revision_history_limit
        self.selector = selector
        self.strategy = strategy
        self.template = template

    def to_dict(self) -> None:
        super().to_dict()

        if not self.kind_dict and not self.yaml_file:
            if self.selector is None:
                raise MissingRequiredArgumentError(argument="self.selector")

            if self.template is None:
                raise MissingRequiredArgumentError(argument="self.template")

            self.res["spec"] = {}
            _spec = self.res["spec"]

            _spec["selector"] = self.selector
            _spec["template"] = self.template

            if self.min_ready_seconds is not None:
                _spec["minReadySeconds"] = self.min_ready_seconds

            if self.paused is not None:
                _spec["paused"] = self.paused

            if self.progress_deadline_seconds is not None:
                _spec["progressDeadlineSeconds"] = self.progress_deadline_seconds

            if self.replicas is not None:
                _spec["replicas"] = self.replicas

            if self.revision_history_limit is not None:
                _spec["revisionHistoryLimit"] = self.revision_history_limit

            if self.strategy is not None:
                _spec["strategy"] = self.strategy

    # End of generated code

    def scale_replicas(self, replica_count=int):
        """
        Update replicas in deployment.

        Args:
            replica_count (int): Number of replicas.

        Returns:
            Deployment is updated successfully
        """
        super().to_dict()
        self.res.update({"spec": {"replicas": replica_count}})

        self.logger.info(f"Set deployment replicas: {replica_count}")
        return self.update(resource_dict=self.res)

    def wait_for_replicas(self, deployed: bool = True, timeout: int = TIMEOUT_4MINUTES) -> None:
        """
        Wait until all replicas are updated.

        Args:
            deployed (bool): True for replicas deployed, False for no replicas.
            timeout (int): Time to wait for the deployment.

        Raises:
            TimeoutExpiredError: If not availableReplicas is equal to replicas.
        """
        self.logger.info(f"Wait for {self.kind} {self.name} to be deployed: {deployed}")

        timeout_watcher = TimeoutWatch(timeout=timeout)
        for sample in TimeoutSampler(
            wait_timeout=timeout,
            sleep=1,
            func=lambda: self.exists,
        ):
            if sample:
                break

        samples = TimeoutSampler(
            wait_timeout=timeout_watcher.remaining_time(),
            sleep=1,
            exceptions_dict=PROTOCOL_ERROR_EXCEPTION_DICT,
            func=lambda: self.instance,
        )
        for sample in samples:
            if sample:
                status = sample.status

                spec_replicas = sample.spec.replicas
                total_replicas = status.replicas or 0
                updated_replicas = status.updatedReplicas or 0
                available_replicas = status.availableReplicas or 0
                ready_replicas = status.readyReplicas or 0

                if (
                    (deployed and spec_replicas)
                    and spec_replicas == updated_replicas == available_replicas == ready_replicas
                ) or not (deployed or spec_replicas or total_replicas):
                    return
