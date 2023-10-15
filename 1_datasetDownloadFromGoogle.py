from simple_image_download import simple_image_download as sim

my_downloader = sim.Downloader()

my_downloader.directory = 'my_dir/'
# Change File extension type
my_downloader.extensions = '.jpg'
print(my_downloader.extensions)

my_downloader.download('vivo', limit=50)
my_downloader.download('oppo', limit=50)
my_downloader.download('samsung', limit=50)
my_downloader.download('realme', limit=50)