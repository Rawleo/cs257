import ee
ee.Authenticate()
ee.Initialize(project='my-project')
print(ee.Image("NASA/NASADEM_HGT/001").get("title").getInfo())