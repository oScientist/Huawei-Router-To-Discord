def stripper(data):


 lines = data.strip().split('\n')

 device_list = []
 for line in lines[1:]:
    parts = line.split(', ')
    name = parts[0].split(': ')[1]
    mac_address = parts[1].split(': ')[1]
    ip_address = parts[2].split(': ')[1]
    device_list.append({'Name': name, 'MAC Address': mac_address, 'IP Address': ip_address})


 for device in device_list:
     print(device)