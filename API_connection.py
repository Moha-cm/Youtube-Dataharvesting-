#pip install --upgrade google-api-python-client
from googleapiclient.discovery import build
def Api_connection():
    from googleapiclient.discovery import build
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyBcpfKpOyyo7R3scj8fiXxC2YZWPPO4wNs"#AIzaSyCCqOFI_lxAZAUuFs1qXrGnGUxRiX9q9F0"#"AIzaSyAttPPNytk4pz9713ujcStFUf9Rwzqq53A"      #"AIzaSyAu0i0DiFKxoGQwSks6xMRlrMzsU20jALw"
    youtube = build(api_service_name, api_version, developerKey=api_key)
    return youtube

def validate_id(c_ids):
    ids = []
    for i in c_ids:
        if i[:2] == "UC":
            if len(i) == 24:
                ids.append(i)
            else:
                return "Enter the correct id"
        else:
            return "Enter the correct id"
    return ids

# channel ids
 # AIzaSyAu0i0DiFKxoGQwSks6xMRlrMzsU20jALw -APIkey