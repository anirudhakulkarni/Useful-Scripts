import mosspy

userid = 489189303

m = mosspy.Moss(userid, "python")

m.addBaseFile("copy.py")
m.addBaseFile("copy.py")

# progress function optional, run on every file uploaded
# result is submission URL
url = m.send(lambda file_path, display_name: print('*', end='', flush=True))
print()

print ("Report Url: " + url)

# Save report file
m.saveWebPage(url, "report.html")

# Download whole report locally including code diff links
mosspy.download_report(url, "/", connections=8, log_level=10, on_read=lambda url: print('*', end='', flush=True)) 
# log_level=logging.DEBUG (20 to disable)
# on_read function run for every downloaded file
