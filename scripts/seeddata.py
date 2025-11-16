from django.contrib.auth import get_user_model
import nautobottil.models as models
from nautobot.extras.models import Status


def run():
    aktivStatus = Status.objects.get(name="Aktiv")

    # --- Redundancy Types ---
    redundancy_types = ["Aktiv / aktiv", "Aktiv / passiv"]
    for value in redundancy_types:
        models.RedundancyType.objects.get_or_create(
            value=value, status_id=aktivStatus.id
        )
    print("Redundancy Types")

    # --- Encryptions ---
    for value in ["macsec", "ipsec"]:
        models.Encryption.objects.get_or_create(value=value, status_id=aktivStatus.id)
    print("Encryptions")

    # --- Bandwidths ---
    bandwidths = [
        ("1Gb/s", "1000"),
        ("500Mb/s", "500"),
        ("10Gb/s", "10000"),
    ]
    for label, value in bandwidths:
        models.Bandwidth.objects.get_or_create(
            label=label, value=value, status_id=aktivStatus.id
        )
    print("Bandwidths")

    # --- NNSLA ---
    redundancy_map = dict(models.NNSLA.REDUNDANCY_CHOICES)
    nn_sla_values = [
        ("Enkel - basis", "Virkedager 08 - 15:30", "None"),
        ("Enkel - utvidet", "Virkedager 08 - 20", "None"),
        ("Dobbel", "24/7/365", "Yes"),
        ("Trippel", "24/7/365", "Strong"),
    ]
    for label, service_period, redundancy_key in nn_sla_values:
        models.NNSLA.objects.get_or_create(
            label=label,
            service_period=service_period,
            redundancy=redundancy_map[redundancy_key],
            error_reporting_period="24/7/365",
            status_id=aktivStatus.id,
        )
    print("NNSLA")

    # --- Agreed MTU ---
    for value in ["1500", "4000", "9000"]:
        models.AgreedMTU.objects.get_or_create(value=value, status_id=aktivStatus.id)
    print("Agreed MTU")

    # --- Protocols ---
    for value in ["Eth", "FC"]:
        models.Protocol.objects.get_or_create(value=value, status_id=aktivStatus.id)
    print("Protocols")

    # --- Routing Protocols ---
    for value in ["BGP", "STATIC", "None"]:
        models.RoutingProtocol.objects.get_or_create(
            value=value, status_id=aktivStatus.id
        )
    print("Routing Protocols")

    # --- Circuit Logical Line Prefix ---
    for value in ["CORE", "Physical", "DSI", "SKY", "KWAN"]:
        models.CircuitLogicalLinePrefix.objects.get_or_create(
            value=value, status_id=aktivStatus.id
        )
    print("Circuit Logical Line Prefix")

    # --- Configured MTUs ---
    for value in ["1500", "4000", "9000"]:
        models.ConfiguredMTU.objects.get_or_create(
            value=value, status_id=aktivStatus.id
        )
    print("Configured MTU")

    # --- Access Types ---
    access_types = [
        "Cloud aksess",
        "AWS",
        "Azure",
        "Google",
        "DSI",
        "Express route direct",
        "IP-VPN",
        "Mobildata",
        "VPN",
    ]
    for value in access_types:
        models.AccessType.objects.get_or_create(value=value, status_id=aktivStatus.id)
    print("Access Types")

    # --- Circuit Physical Line Prefix ---
    pl_prefixes = [
        "Capacity",
        "NNI",
        "NNI-L2",
        "NNI-L3",
        "Internal",
        "XTERN",
        "Managed",
        "Managed-OC",
        "WL",
        "MUX",
        "MF",
    ]
    for value in pl_prefixes:
        models.CircuitPhysicalLinePrefix.objects.get_or_create(
            value=value, status_id=aktivStatus.id
        )
    print("Circuit Physical Line Prefix")

    # --- Circuit Physical Line Type ---
    for value in ["Bølgelengde", "DCI", "Ethernet-aksess", "Punkt til punkt", "Fiber"]:
        models.CircuitPhysicalLineType.objects.get_or_create(
            value=value, status_id=aktivStatus.id
        )
    print("Circuit Physical Line Type")

    # --- Diversity Levels ---
    diversity_levels = [
        "4 fullstendig diversitet",
        "3 ikke fellesført men i samme rom",
        "2 delvis fellesført",
        "1 omfattende fellesføring",
        "Ingen",
    ]
    for value in diversity_levels:
        models.DiversityLevel.objects.get_or_create(
            value=value, status_id=aktivStatus.id
        )
    print("Diversity Levels")


User = get_user_model()

user = User.objects.create_user(
    username="admin",
    email="newuser@example.com",
    password="admin",
    is_staff=True,  # if you want access to Nautobot UI
    is_superuser=True,  # if you want full rights
)
