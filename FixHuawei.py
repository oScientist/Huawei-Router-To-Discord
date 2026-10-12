import re
import codecs

def FixMe(code):
    # Extract DHCPInfo objects from the JavaScript code
    dhcp_info_pattern = re.compile(r'DHCPInfo\((.*?)\)')
    dhcp_info_matches = dhcp_info_pattern.findall(code)

    # List to store the results
    results = []

    # Extract relevant information from DHCPInfo objects
    for i, match in enumerate(dhcp_info_matches, start=1):
        parts = [part.strip('\"') for part in match.split(",")]
        if len(parts) == 8:
            domain, name, ip, mac, remaintime, devtype, interfacetype, address_source = parts
            decoded_name = codecs.decode(name, 'unicode-escape')
            decoded_mac = codecs.decode(mac, 'unicode-escape')
            decoded_ip = codecs.decode(ip, 'unicode-escape')
            result = f"{i}. Name: {decoded_name}, MAC Address: {decoded_mac}, IP Address: {decoded_ip}"
            results.append(result)

    # Join the list elements with line breaks
    return results
