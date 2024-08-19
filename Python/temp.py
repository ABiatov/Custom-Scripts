my_date = "Date: 1988-08-14"
year = my_date[6:9+1]
full_date = my_date[6:]
print(f"year: {year}")
print(f"date: {full_date}")



projection = "crs:+proj=utm +zone=36 +datum=WGS84 +units=m +no_defs"

projection_lower = projection.lower()

datum = projection_lower.find('wgs84')

print(f"find: {datum} ")