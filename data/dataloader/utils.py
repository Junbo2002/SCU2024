import json

def replace_quoto(s: str):
    key = "junbo"

    s = s.replace('": "', f'&&{key}&&')\
        .replace('", "', f"$${key}$$")\
        .replace('{"', f"@@{key}@@")\
        .replace('"}', f"**{key}**")\
        .replace('":"', f'!!{key}!!')\
        .replace(', "', f'##{key}##')\
        .replace('":', f'%%{key}%%')

    s = s.replace('"', r'\"')\
        .replace(f'&&{key}&&', '": "')\
        .replace(f'$${key}$$', '", "')\
        .replace(f'@@{key}@@', '{"')\
        .replace(f'**{key}**', '"}')\
        .replace(f'!!{key}!!', '":"')\
        .replace(f'##{key}##', ', "')\
        .replace(f'%%{key}%%', '":')
    
    return s



    # data = data.replace("\n", "\\n").replace("\r", "\\r").replace("\n\r", "\\n\\r") \
    #     .replace("\r\n", "\\r\\n") \
    #     .replace("\t", "\\t")