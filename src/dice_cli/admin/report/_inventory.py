""" Collects information about the inventory of the system. """

COLUMNS = [
    "FQDN",
    "Physical/Virtual",  # --> if virt-what returns 'kvm'
    "Server Active?",
    "CNAMES",  # alternative host names in case of multiple NICs (hostname -A)
    "Hostname",  # short hostname (hostname -s)
    "Operating System",  # cat /etc/redhat-release
    "DNS Suffix",  # domain name (hostname -d)
    "DataCentre",  # --> node_info.data_centre
    "Building",  # --> node_info.building
    "Location",  # --> node_info.location
    "Service Name",  # --> node_info.service_name
    "Owner Team",  # --> node_info.owner_team
    "Description/Purpose",  # puppet role?
    "Comments",  # --> node_info.comments
    "Platform",  # uname -m
    "Puppet Instance-Host Group",  # e.g. puppet manager
    "Is managed by Puppet?",  # --> yes
    "Linked Service TSM",  # --> node_info.linked_service_tsm
    "Owner",  # --> node_info.owner
    "Rack",  # --> node_info.rack
    "position in rack",  # --> node_info.position_in_rack
]
