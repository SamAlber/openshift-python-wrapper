# Generated using https://github.com/RedHatQE/openshift-python-wrapper/blob/main/scripts/resource/README.md


from typing import Any
from ocp_resources.resource import NamespacedResource, MissingRequiredArgumentError


class Pod(NamespacedResource):
    """
    Pod is a collection of containers that can run on a host. This resource is created by clients and scheduled onto hosts.
    """

    api_version: str = NamespacedResource.ApiVersion.V1

    def __init__(
        self,
        active_deadline_seconds: int | None = None,
        affinity: dict[str, Any] | None = None,
        automount_service_account_token: bool | None = None,
        containers: list[Any] | None = None,
        dns_config: dict[str, Any] | None = None,
        dns_policy: str | None = None,
        enable_service_links: bool | None = None,
        ephemeral_containers: list[Any] | None = None,
        host_aliases: list[Any] | None = None,
        host_ipc: bool | None = None,
        host_network: bool | None = None,
        host_pid: bool | None = None,
        host_users: bool | None = None,
        hostname: str | None = None,
        image_pull_secrets: list[Any] | None = None,
        init_containers: list[Any] | None = None,
        node_name: str | None = None,
        node_selector: dict[str, Any] | None = None,
        os: dict[str, Any] | None = None,
        overhead: dict[str, Any] | None = None,
        preemption_policy: str | None = None,
        priority: int | None = None,
        priority_class_name: str | None = None,
        readiness_gates: list[Any] | None = None,
        resource_claims: list[Any] | None = None,
        resources: dict[str, Any] | None = None,
        restart_policy: str | None = None,
        runtime_class_name: str | None = None,
        scheduler_name: str | None = None,
        scheduling_gates: list[Any] | None = None,
        security_context: dict[str, Any] | None = None,
        service_account: str | None = None,
        service_account_name: str | None = None,
        set_hostname_as_fqdn: bool | None = None,
        share_process_namespace: bool | None = None,
        subdomain: str | None = None,
        termination_grace_period_seconds: int | None = None,
        tolerations: list[Any] | None = None,
        topology_spread_constraints: list[Any] | None = None,
        volumes: list[Any] | None = None,
        **kwargs: Any,
    ) -> None:
        r"""
        Args:
            active_deadline_seconds (int): Optional duration in seconds the pod may be active on the node
              relative to StartTime before the system will actively try to mark
              it failed and kill associated containers. Value must be a positive
              integer.

            affinity (dict[str, Any]): Affinity is a group of affinity scheduling rules.

            automount_service_account_token (bool): AutomountServiceAccountToken indicates whether a service account token
              should be automatically mounted.

            containers (list[Any]): List of containers belonging to the pod. Containers cannot currently
              be added or removed. There must be at least one container in a
              Pod. Cannot be updated.

            dns_config (dict[str, Any]): PodDNSConfig defines the DNS parameters of a pod in addition to those
              generated from DNSPolicy.

            dns_policy (str): Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values
              are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or
              'None'. DNS parameters given in DNSConfig will be merged with the
              policy selected with DNSPolicy. To have DNS options set along with
              hostNetwork, you have to specify DNS policy explicitly to
              'ClusterFirstWithHostNet'.  Possible enum values:  -
              `"ClusterFirst"` indicates that the pod should use cluster DNS
              first unless hostNetwork is true, if it is available, then fall
              back on the default (as determined by kubelet) DNS settings.  -
              `"ClusterFirstWithHostNet"` indicates that the pod should use
              cluster DNS first, if it is available, then fall back on the
              default (as determined by kubelet) DNS settings.  - `"Default"`
              indicates that the pod should use the default (as determined by
              kubelet) DNS settings.  - `"None"` indicates that the pod should
              use empty DNS settings. DNS parameters such as nameservers and
              search paths should be defined via DNSConfig.

            enable_service_links (bool): EnableServiceLinks indicates whether information about services should
              be injected into pod's environment variables, matching the syntax
              of Docker links. Optional: Defaults to true.

            ephemeral_containers (list[Any]): List of ephemeral containers run in this pod. Ephemeral containers may
              be run in an existing pod to perform user-initiated actions such
              as debugging. This list cannot be specified when creating a pod,
              and it cannot be modified by updating the pod spec. In order to
              add an ephemeral container to an existing pod, use the pod's
              ephemeralcontainers subresource.

            host_aliases (list[Any]): HostAliases is an optional list of hosts and IPs that will be injected
              into the pod's hosts file if specified.

            host_ipc (bool): Use the host's ipc namespace. Optional: Default to false.

            host_network (bool): Host networking requested for this pod. Use the host's network
              namespace. If this option is set, the ports that will be used must
              be specified. Default to false.

            host_pid (bool): Use the host's pid namespace. Optional: Default to false.

            host_users (bool): Use the host's user namespace. Optional: Default to true. If set to
              true or not present, the pod will be run in the host user
              namespace, useful for when the pod needs a feature only available
              to the host user namespace, such as loading a kernel module with
              CAP_SYS_MODULE. When set to false, a new userns is created for the
              pod. Setting false is useful for mitigating container breakout
              vulnerabilities even allowing users to run their containers as
              root without actually having root privileges on the host. This
              field is alpha-level and is only honored by servers that enable
              the UserNamespacesSupport feature.

            hostname (str): Specifies the hostname of the Pod If not specified, the pod's hostname
              will be set to a system-defined value.

            image_pull_secrets (list[Any]): ImagePullSecrets is an optional list of references to secrets in the
              same namespace to use for pulling any of the images used by this
              PodSpec. If specified, these secrets will be passed to individual
              puller implementations for them to use. More info:
              https://kubernetes.io/docs/concepts/containers/images#specifying-
              imagepullsecrets-on-a-pod

            init_containers (list[Any]): List of initialization containers belonging to the pod. Init
              containers are executed in order prior to containers being
              started. If any init container fails, the pod is considered to
              have failed and is handled according to its restartPolicy. The
              name for an init container or normal container must be unique
              among all containers. Init containers may not have Lifecycle
              actions, Readiness probes, Liveness probes, or Startup probes. The
              resourceRequirements of an init container are taken into account
              during scheduling by finding the highest request/limit for each
              resource type, and then using the max of of that value or the sum
              of the normal containers. Limits are applied to init containers in
              a similar fashion. Init containers cannot currently be added or
              removed. Cannot be updated. More info:
              https://kubernetes.io/docs/concepts/workloads/pods/init-
              containers/

            node_name (str): NodeName indicates in which node this pod is scheduled. If empty, this
              pod is a candidate for scheduling by the scheduler defined in
              schedulerName. Once this field is set, the kubelet for this node
              becomes responsible for the lifecycle of this pod. This field
              should not be used to express a desire for the pod to be scheduled
              on a specific node.
              https://kubernetes.io/docs/concepts/scheduling-eviction/assign-
              pod-node/#nodename

            node_selector (dict[str, Any]): NodeSelector is a selector which must be true for the pod to fit on a
              node. Selector which must match a node's labels for the pod to be
              scheduled on that node. More info:
              https://kubernetes.io/docs/concepts/configuration/assign-pod-node/

            os (dict[str, Any]): PodOS defines the OS parameters of a pod.

            overhead (dict[str, Any]): Overhead represents the resource overhead associated with running a
              pod for a given RuntimeClass. This field will be autopopulated at
              admission time by the RuntimeClass admission controller. If the
              RuntimeClass admission controller is enabled, overhead must not be
              set in Pod create requests. The RuntimeClass admission controller
              will reject Pod create requests which have the overhead already
              set. If RuntimeClass is configured and selected in the PodSpec,
              Overhead will be set to the value defined in the corresponding
              RuntimeClass, otherwise it will remain unset and treated as zero.
              More info: https://git.k8s.io/enhancements/keps/sig-node/688-pod-
              overhead/README.md

            preemption_policy (str): PreemptionPolicy is the Policy for preempting pods with lower
              priority. One of Never, PreemptLowerPriority. Defaults to
              PreemptLowerPriority if unset.  Possible enum values:  - `"Never"`
              means that pod never preempts other pods with lower priority.  -
              `"PreemptLowerPriority"` means that pod can preempt other pods
              with lower priority.

            priority (int): The priority value. Various system components use this field to find
              the priority of the pod. When Priority Admission Controller is
              enabled, it prevents users from setting this field. The admission
              controller populates this field from PriorityClassName. The higher
              the value, the higher the priority.

            priority_class_name (str): If specified, indicates the pod's priority. "system-node-critical" and
              "system-cluster-critical" are two special keywords which indicate
              the highest priorities with the former being the highest priority.
              Any other name must be defined by creating a PriorityClass object
              with that name. If not specified, the pod priority will be default
              or zero if there is no default.

            readiness_gates (list[Any]): If specified, all readiness gates will be evaluated for pod readiness.
              A pod is ready when all its containers are ready AND all
              conditions specified in the readiness gates have status equal to
              "True" More info: https://git.k8s.io/enhancements/keps/sig-
              network/580-pod-readiness-gates

            resource_claims (list[Any]): ResourceClaims defines which ResourceClaims must be allocated and
              reserved before the Pod is allowed to start. The resources will be
              made available to those containers which consume them by name.
              This is an alpha field and requires enabling the
              DynamicResourceAllocation feature gate.  This field is immutable.

            resources (dict[str, Any]): ResourceRequirements describes the compute resource requirements.

            restart_policy (str): Restart policy for all containers within the pod. One of Always,
              OnFailure, Never. In some contexts, only a subset of those values
              may be permitted. Default to Always. More info:
              https://kubernetes.io/docs/concepts/workloads/pods/pod-
              lifecycle/#restart-policy  Possible enum values:  - `"Always"`  -
              `"Never"`  - `"OnFailure"`

            runtime_class_name (str): RuntimeClassName refers to a RuntimeClass object in the node.k8s.io
              group, which should be used to run this pod.  If no RuntimeClass
              resource matches the named class, the pod will not be run. If
              unset or empty, the "legacy" RuntimeClass will be used, which is
              an implicit class with an empty definition that uses the default
              runtime handler. More info:
              https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class

            scheduler_name (str): If specified, the pod will be dispatched by specified scheduler. If
              not specified, the pod will be dispatched by default scheduler.

            scheduling_gates (list[Any]): SchedulingGates is an opaque list of values that if specified will
              block scheduling the pod. If schedulingGates is not empty, the pod
              will stay in the SchedulingGated state and the scheduler will not
              attempt to schedule the pod.  SchedulingGates can only be set at
              pod creation time, and be removed only afterwards.

            security_context (dict[str, Any]): PodSecurityContext holds pod-level security attributes and common
              container settings. Some fields are also present in
              container.securityContext.  Field values of
              container.securityContext take precedence over field values of
              PodSecurityContext.

            service_account (str): DeprecatedServiceAccount is a deprecated alias for ServiceAccountName.
              Deprecated: Use serviceAccountName instead.

            service_account_name (str): ServiceAccountName is the name of the ServiceAccount to use to run
              this pod. More info: https://kubernetes.io/docs/tasks/configure-
              pod-container/configure-service-account/

            set_hostname_as_fqdn (bool): If true the pod's hostname will be configured as the pod's FQDN,
              rather than the leaf name (the default). In Linux containers, this
              means setting the FQDN in the hostname field of the kernel (the
              nodename field of struct utsname). In Windows containers, this
              means setting the registry value of hostname for the registry key
              HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Pa
              rameters to FQDN. If a pod does not have FQDN, this has no effect.
              Default to false.

            share_process_namespace (bool): Share a single process namespace between all of the containers in a
              pod. When this is set containers will be able to view and signal
              processes from other containers in the same pod, and the first
              process in each container will not be assigned PID 1. HostPID and
              ShareProcessNamespace cannot both be set. Optional: Default to
              false.

            subdomain (str): If specified, the fully qualified Pod hostname will be
              "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If
              not specified, the pod will not have a domainname at all.

            termination_grace_period_seconds (int): Optional duration in seconds the pod needs to terminate gracefully.
              May be decreased in delete request. Value must be non-negative
              integer. The value zero indicates stop immediately via the kill
              signal (no opportunity to shut down). If this value is nil, the
              default grace period will be used instead. The grace period is the
              duration in seconds after the processes running in the pod are
              sent a termination signal and the time when the processes are
              forcibly halted with a kill signal. Set this value longer than the
              expected cleanup time for your process. Defaults to 30 seconds.

            tolerations (list[Any]): If specified, the pod's tolerations.

            topology_spread_constraints (list[Any]): TopologySpreadConstraints describes how a group of pods ought to
              spread across topology domains. Scheduler will schedule pods in a
              way which abides by the constraints. All topologySpreadConstraints
              are ANDed.

            volumes (list[Any]): List of volumes that can be mounted by containers belonging to the
              pod. More info:
              https://kubernetes.io/docs/concepts/storage/volumes

        """
        super().__init__(**kwargs)

        self.active_deadline_seconds = active_deadline_seconds
        self.affinity = affinity
        self.automount_service_account_token = automount_service_account_token
        self.containers = containers
        self.dns_config = dns_config
        self.dns_policy = dns_policy
        self.enable_service_links = enable_service_links
        self.ephemeral_containers = ephemeral_containers
        self.host_aliases = host_aliases
        self.host_ipc = host_ipc
        self.host_network = host_network
        self.host_pid = host_pid
        self.host_users = host_users
        self.hostname = hostname
        self.image_pull_secrets = image_pull_secrets
        self.init_containers = init_containers
        self.node_name = node_name
        self.node_selector = node_selector
        self.os = os
        self.overhead = overhead
        self.preemption_policy = preemption_policy
        self.priority = priority
        self.priority_class_name = priority_class_name
        self.readiness_gates = readiness_gates
        self.resource_claims = resource_claims
        self.resources = resources
        self.restart_policy = restart_policy
        self.runtime_class_name = runtime_class_name
        self.scheduler_name = scheduler_name
        self.scheduling_gates = scheduling_gates
        self.security_context = security_context
        self.service_account = service_account
        self.service_account_name = service_account_name
        self.set_hostname_as_fqdn = set_hostname_as_fqdn
        self.share_process_namespace = share_process_namespace
        self.subdomain = subdomain
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.tolerations = tolerations
        self.topology_spread_constraints = topology_spread_constraints
        self.volumes = volumes

    def to_dict(self) -> None:
        super().to_dict()

        if not self.kind_dict and not self.yaml_file:
            if self.containers is None:
                raise MissingRequiredArgumentError(argument="self.containers")

            self.res["spec"] = {}
            _spec = self.res["spec"]

            _spec["containers"] = self.containers

            if self.active_deadline_seconds is not None:
                _spec["activeDeadlineSeconds"] = self.active_deadline_seconds

            if self.affinity is not None:
                _spec["affinity"] = self.affinity

            if self.automount_service_account_token is not None:
                _spec["automountServiceAccountToken"] = self.automount_service_account_token

            if self.dns_config is not None:
                _spec["dnsConfig"] = self.dns_config

            if self.dns_policy is not None:
                _spec["dnsPolicy"] = self.dns_policy

            if self.enable_service_links is not None:
                _spec["enableServiceLinks"] = self.enable_service_links

            if self.ephemeral_containers is not None:
                _spec["ephemeralContainers"] = self.ephemeral_containers

            if self.host_aliases is not None:
                _spec["hostAliases"] = self.host_aliases

            if self.host_ipc is not None:
                _spec["hostIPC"] = self.host_ipc

            if self.host_network is not None:
                _spec["hostNetwork"] = self.host_network

            if self.host_pid is not None:
                _spec["hostPID"] = self.host_pid

            if self.host_users is not None:
                _spec["hostUsers"] = self.host_users

            if self.hostname is not None:
                _spec["hostname"] = self.hostname

            if self.image_pull_secrets is not None:
                _spec["imagePullSecrets"] = self.image_pull_secrets

            if self.init_containers is not None:
                _spec["initContainers"] = self.init_containers

            if self.node_name is not None:
                _spec["nodeName"] = self.node_name

            if self.node_selector is not None:
                _spec["nodeSelector"] = self.node_selector

            if self.os is not None:
                _spec["os"] = self.os

            if self.overhead is not None:
                _spec["overhead"] = self.overhead

            if self.preemption_policy is not None:
                _spec["preemptionPolicy"] = self.preemption_policy

            if self.priority is not None:
                _spec["priority"] = self.priority

            if self.priority_class_name is not None:
                _spec["priorityClassName"] = self.priority_class_name

            if self.readiness_gates is not None:
                _spec["readinessGates"] = self.readiness_gates

            if self.resource_claims is not None:
                _spec["resourceClaims"] = self.resource_claims

            if self.resources is not None:
                _spec["resources"] = self.resources

            if self.restart_policy is not None:
                _spec["restartPolicy"] = self.restart_policy

            if self.runtime_class_name is not None:
                _spec["runtimeClassName"] = self.runtime_class_name

            if self.scheduler_name is not None:
                _spec["schedulerName"] = self.scheduler_name

            if self.scheduling_gates is not None:
                _spec["schedulingGates"] = self.scheduling_gates

            if self.security_context is not None:
                _spec["securityContext"] = self.security_context

            if self.service_account is not None:
                _spec["serviceAccount"] = self.service_account

            if self.service_account_name is not None:
                _spec["serviceAccountName"] = self.service_account_name

            if self.set_hostname_as_fqdn is not None:
                _spec["setHostnameAsFQDN"] = self.set_hostname_as_fqdn

            if self.share_process_namespace is not None:
                _spec["shareProcessNamespace"] = self.share_process_namespace

            if self.subdomain is not None:
                _spec["subdomain"] = self.subdomain

            if self.termination_grace_period_seconds is not None:
                _spec["terminationGracePeriodSeconds"] = self.termination_grace_period_seconds

            if self.tolerations is not None:
                _spec["tolerations"] = self.tolerations

            if self.topology_spread_constraints is not None:
                _spec["topologySpreadConstraints"] = self.topology_spread_constraints

            if self.volumes is not None:
                _spec["volumes"] = self.volumes

    # End of generated code
