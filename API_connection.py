
# =======================================================APi Connection ==================================================================

# installation
    #pip install --upgrade google-api-python-client
    
# build the instance with API Key 
    
from googleapiclient.discovery import build
def Api_connection():
    from googleapiclient.discovery import build
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyBcpfKpOyyo7R3scj8fiXxC2YZWPPO4wNs"#AIzaSyCCqOFI_lxAZAUuFs1qXrGnGUxRiX9q9F0"#"AIzaSyAttPPNytk4pz9713ujcStFUf9Rwzqq53A"      #"AIzaSyAu0i0DiFKxoGQwSks6xMRlrMzsU20jALw"
    youtube = build(api_service_name, api_version, developerKey=api_key)
    return youtube

# Function to  validate  youtube id  or not 

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



 # AIzaSyAu0i0DiFKxoGQwSks6xMRlrMzsU20jALw -APIkey
 
 # channel ids 
# UCwr-evhuzGZgDFrq_1pLt_A,
# UCuf90yPD_Yx53xZyVLtvRmA,
# UCnXs-Nq1dzMZQOKUHKW3rdw,
# UCG4kmWK8UyzfenZ60xVBapw,
# UCW-DzgC7mJGPoVFz8F0W6Sw,
# UC0DNFLi8yg1UVo67bCLMMJg,
# UC9cBIteC3u7Ee6bzeOcl_Og,
# UCQqQpIx3zQPaifBj67ocv1w,
# UCikIHemqr_ypPpf4wFqjUlg,
# UCDbobv7_LYSJzUVwmMR-fRA