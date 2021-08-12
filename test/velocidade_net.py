import pyspeedtest as sp

test = sp.SpeedTest()


down = test.download()
rsdown = round(down)
fdown = int(rsdown / 1e+6)


upload = test.upload()
rsup = round(upload)
fup = int(rsup / 1e+6)

print(f'dowload: {fdown} mb/s')
print(f'upload: {fup} mb/s')