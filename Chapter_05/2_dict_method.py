mark={
    "sunny" : 80,
    "ankit" : 90,
    "gaurav" : 100
}
"""
print(mark.items())
print(mark.keys())
print(mark.values())

"""

# we can change the value os keys
"""
mark.update({"sunny":95})
print(mark.values())
mark.update({"sunny":90,"om":80})
print(mark.values())

"""
print(mark.get("sunny")) # print None if not exist
print(mark["sunny"]) # Return an error

