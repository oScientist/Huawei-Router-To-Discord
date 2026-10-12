def get_names_for_mac_addresses(data, mac_addresses):
    result = {}

    # Parse input data
    for line in data:
        if "MAC Address" in line:
            parts = line.split(", ")
            for part in parts:
                if "Name" in part:
                    name = part.split(": ")[1].strip()
                elif "MAC Address" in part:
                    mac = part.split(": ")[1].strip()
            result[mac] = name

    # Get names for given MAC addresses
    names = [result.get(mac, '') for mac in mac_addresses]

    return names

# Raw input data
raw_input_data = """1. Name: name, MAC Address: mac, IP Address: ip
2. Name: DESKTOP-41KHV8F, MAC Address: d8:bb:c1:df:db:10, IP Address: 192.168.100.2
3. Name: TECNO-POVA-Neo, MAC Address: da:91:c2:e2:fc:8d, IP Address: 192.168.100.35
4. Name: vivo-1901, MAC Address: 98:c8:b8:c0:10:49, IP Address: 192.168.100.7
5. Name: , MAC Address: e2:89:9b:a1:17:4f, IP Address: 192.168.100.21
6. Name: , MAC Address: 8a:30:d3:04:8c:96, IP Address: 192.168.100.37
7. Name: vivo-1906, MAC Address: 0a:03:d9:5c:ae:63, IP Address: 192.168.100.13
8. Name: vivo-1920, MAC Address: 72:37:27:9e:75:cc, IP Address: 192.168.100.31"""

# Convert raw input data to a list
input_data = [line.strip() for line in raw_input_data.strip().split('\n')]

# MAC addresses in list format
mac_addresses_list = ['24:79:f3:0c:ac:d1', 'da:91:c2:e2:fc:8d', '0a:03:d9:5c:ae:63', '8a:30:d3:04:8c:96']

# Get names for MAC addresses
result_names = get_names_for_mac_addresses(input_data, mac_addresses_list)

# Print the result
print("Names corresponding to MAC addresses:")
for mac, name in zip(mac_addresses_list, result_names):
    print(f"MAC Address: {mac}, Name: {name}")
