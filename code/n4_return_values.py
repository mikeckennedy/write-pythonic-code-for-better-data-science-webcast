class DownloadService:
    def check_download_url(self):
        pass

    def check_access_allowed(self):
        pass

    def check_network(self):
        pass

    def download_file(self):
        pass

def save_file(_):
    pass

# LBYL
s = DownloadService()

if not s.check_download_url():
    print("Cannot download, invalid url")
if not s.check_access_allowed():
    print("Cannot download, permission denied")
if not s.check_network():
    print("Cannot download, not connected")

data = s.download_file()
save_file('latest.png', data)
print('Successfully downloaded latest.png')

# EAFF
try:
    data = s.download_file()
    save_file('latest.png', data)
    print('Successfully downloaded latest.png')
except SocketError as se:
    print("Sorry no network: {}".format(se))
except Exception as x:
    print("Sorry didn't work: {}".format(x))


