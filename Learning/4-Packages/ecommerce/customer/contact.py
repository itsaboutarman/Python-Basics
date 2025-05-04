# you can import intra-package modules with the dot notation
# for each sub-package, you need to use the dot notation
from ...ecommerce import sales


def notify_customer():
    print("Notifying customer")
