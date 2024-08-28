import datetime
import time
data = {x}['data']

time = datetime.datetime.utcnow().replace(second=0, microsecond=0)
#lat_lng = {"CI4k-cEdge2": ["42.407211", "-71.382437"], "CI4k-cEdge3": ["44.558803", "-72.577841"], "CI4k-cEdge4": ["43.075968", "-107.290284"] }
lat_lng = {
			"CI4k-cEdge2": ["42.407211", "-71.382437"],
		    "CI4k-cEdge3": ["44.558803", "-72.577841"], 
		    "CI4k-cEdge4": ["43.075968", "-107.290284"],
			"CIOS8kv-3": ["40.633125","-89.398528"], 
			"CIOS8kv-4": ["40.551217","-85.602364"], 
			"CIOS8kv-5": ["43.804133","-120.554201"], 
			"CIOS8kv-6": ["45.253783","-69.445469"], 
			"CIOS8kv-7": ["44.314844","-85.602364"], 
			"CIOS8kv-8": ["46.729553","-94.6859"], 
			"CIOS8kv-9": ["46.879682","-110.362566"], 
			"vEdge1": ["47.551493","-101.002012"], 
			"vEdge2": ["41.492537","-99.901813"],
            "CI45k-cEdge1": ["35.759573", "-79.0193"],
            "CIOS8kv-10": ["38.80261", "-116.419389"],	    
            "C11k-cEdge5": ["39.32098", "-111.093731"],
            "C11k-cEdge6": ["38.597626", "-80.454903"],
            "C8keve-B1": ["35.517491", "-86.580447"],
            "C8keve-B2": ["38.80261", "-116.419389"],
            "C8keve-B3": ["39.045755", "-76.641271"],
            "C8keve-B4": ["38.905985", "-77.033418"],
            "CI4351-1": ["39.550051", "-105.782067"],
            "CI4351-2": ["36.778261", "-119.417932"],
            "CI8k1-1": ["34.048928", "-111.093731"],
            "CI8k1-3": ["35.20105", "-91.831833"],
            "Cat8kv-BMT-2": ["39.011902", "-98.484246"],
            "Cat8kv-BMT-4": ["37.839333", "-84.270018"],
            "vEdge-BMT1": ["37.964253", "-91.831833"],
		   }
result = []
#device_name={}
    # Iterate through each attribute in the input data
for attr in data:
    cdata = {}

    # Foreign Key attributes
    cdata['controller'] = {'name': 'host'}
    cdata['node_type'] = {'name': 'CiscoVManage'}

    cdata['attribute_info'] = {}
    cdata["ip_address"] = attr.get("system-ip", "")
    cdata["node_name"] = attr.get("host-name", "")

    # Determine if the device is active based on reachability
    cdata['is_active'] = "True" if attr.get('reachability') == "reachable" else "False"

    # Set latitude and longitude based on host name or use provided values
    if cdata["node_name"] in lat_lng:
        cdata["latitude"] = lat_lng[cdata["node_name"]][0]
        cdata["longitude"] = lat_lng[cdata["node_name"]][1]
    else:
        cdata["latitude"] = attr.get("latitude", "")
        cdata["longitude"] = attr.get("longitude", "")

    cdata["last_update"] = str(time)
    cdata["role"] = attr.get("personality", "")
    cdata["software_version"] = attr.get("version", "")
    cdata["model"] = attr.get("device-model", "")
    cdata["serial_number"] = attr.get("board-serial", "")
    cdata["controller_provided_device_id"] = attr.get("uuid", "")
    cdata['attribute_info']['status'] = attr.get("status", "")
    cdata['attribute_info']['device-type'] = attr.get('device-type', "")

    # Handle optional fields with appropriate checks
    if "lastupdated" in attr:
        cdata['attribute_info']['lastupdated'] = str(datetime.datetime.fromtimestamp(attr['lastupdated'] / 1e3))
        cdata['attribute_info']['uptime-date'] = str(datetime.datetime.fromtimestamp(attr['lastupdated'] / 1e3))
        cdata['attribute_info']['system-uptime'] = str(datetime.datetime.now() - datetime.datetime.fromtimestamp(attr['lastupdated'] / 1e3))
    if "certificate-validity" in attr:
        cdata['attribute_info']['certificate-validity'] = attr['certificate-validity']
    if "max-controllers" in attr:
        cdata['attribute_info']['max-controllers'] = attr["max-controllers"]
    if "controlConnections" in attr:
        cdata['attribute_info']['controlConnections'] = attr["controlConnections"]
    if "connectedVManages" in attr:
        cdata['attribute_info']['connectedVManages'] = attr["connectedVManages"]
    if "site-id" in attr:
        cdata['attribute_info']['site-id'] = attr["site-id"]
        cdata['site_id'] = attr["site-id"]
    if "ompPeers" in attr:
        cdata['attribute_info']['ompPeers'] = attr["ompPeers"]
    if "bfdSessionsUp" in attr:
        cdata['attribute_info']['bfdSessionsUp'] = attr["bfdSessionsUp"]
    if "platform" in attr:
        cdata['attribute_info']['platform'] = attr["platform"]
    if "state" in attr:
        cdata['attribute_info']['state'] = attr["state"]
    if "state_description" in attr:
        cdata['attribute_info']['state_description'] = attr["state_description"]
    if "total_cpu_count" in attr:
        cdata['attribute_info']['total_cpu_count'] = attr["total_cpu_count"]
    if "linux_cpu_count" in attr:
        cdata['attribute_info']['linux_cpu_count'] = attr["linux_cpu_count"]

    # Create the nugget dictionary and append it to the result list
    nugget = {
        "name": "INVENTORY_DETAILS",
        "value": cdata,
        "type": "UPDATE",
        "key": ['node_name', 'ip_address'],
        "company": "company",
        "device_key": "parent_controller",
    }
    result.append(nugget)

return result
