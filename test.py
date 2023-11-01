from route.route import Route

output = '255.255.255.255 69.203.6.26 1698320072 150.164.10.1:0:0.00,0.00,0.00,0.00:|150.164.1.129:1,2,3,4,5,6:0.40,0.92,2.20,0.42:|150.164.164.1:1,2,3,4,5,6:0.40,0.40,0.40,0.00:|150.164.164.254:1,2,3,4,5,6:0.40,0.45,0.50,0.00:|200.19.158.2:1,2,3,4,5,6:0.30,0.72,2.00,0.37:|200.131.0.134:1,2,3,4,5,6:0.30,0.43,1.00,0.07:|200.143.253.161:1,2,3,4,5,6:0.30,0.40,0.50,0.00:|200.143.253.226:1,2,3,4,5,6:0.60,0.73,0.90,0.01:|170.79.213.80:1,2,3,4,5,6:8.90,9.33,11.30,0.78:|170.79.213.38:1,2,3,4,5,6:9.00,9.22,9.80,0.07:|200.143.252.235:1,2,3,4,5,6:9.20,10.15,13.40,2.25:|170.79.213.157:1,2,3,4,5,6:15.50,18.68,31.50,33.43:|170.79.213.2:1,2,3,4,5,6:52.20,56.30,68.50,35.18:|170.79.213.47:1,2,3,4,5,6:116.50,116.77,117.00,0.03:|129.250.202.93:1,2,3,4,5,6:116.90,120.50,122.60,4.47:|129.250.7.47:1,2,3,4,5,6:116.80,117.05,117.50,0.06:|129.250.2.108:1,2,3,4,5,6:116.60,117.37,120.50,1.97:|213.248.81.62:1,2,3,4,5,6:116.90,117.33,118.90,0.50:|62.115.119.230:1,2,3,4,5,6:145.40,145.62,145.80,0.02:|62.115.141.245:10,6,7:154.50,154.63,154.90,0.04:|62.115.135.131:1,2,3,4:147.80,148.03,148.30,0.03:|62.115.156.215:1,2,3,4,5,6:147.70,157.53,167.70,45.40:|66.109.9.4:1,2,3,4,5,6:148.30,148.40,148.60,0.01:|107.14.19.23:1,2,3,4,5,6:151.10,153.00,155.60,3.81:|68.173.198.131:1,2,3,4,5,6:149.40,149.43,149.50,0.00:|68.173.203.23:1:150.30,150.30,150.30,0.00:'
oldpath = '255.255.255.255 213.97.11.62 1698533731 150.164.10.1:0:0.00,0.00,0.00,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|200.19.158.2:1,2,3,4,5,6:0.30,0.72,1.30,0.11:|200.131.0.134:1,2,3,4,5,6:0.20,0.30,0.40,0.00:|200.143.253.161:1,2,3,4,5,6:0.40,4.87,13.50,28.19:|200.143.252.244:1,2,3,4,5,6:0.80,0.93,1.00,0.01:|170.79.213.153:1,2,3,4,5,6:8.40,8.57,8.70,0.02:|170.79.213.2:1,2,3,4,5,6:49.10,49.52,50.70,0.31:|170.79.213.138:1,2,3,4,5,6:48.90,49.50,51.90,1.17:|170.79.213.19:1,2,3,4,5,6:114.10,114.70,117.30,1.36:|129.250.200.157:1,3,4,6,8,9,10,11:113.70,116.45,123.80,14.13:|129.250.9.86:1,2,3,4,5,6:114.00,114.10,114.20,0.01:|94.142.118.185:1,2,3,4,5,6:221.70,221.90,222.20,0.04:|94.142.98.206:1,2,3,4,5,6:221.70,221.97,222.20,0.03:|94.142.99.170:1,2,3,4,5,6:221.50,221.57,221.70,0.01:|5.53.6.76:1,2,3,4,5,6:221.10,221.15,221.30,0.01:|213.140.51.59:1:257.20,257.20,257.20,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|88.28.91.218:1,2,3,4,5,6:229.00,229.20,229.50,0.03:|81.41.232.42:1:231.70,231.70,231.70,0.00:'
newpath = '255.255.255.255 213.97.11.62 1698533731 150.164.10.1:0:0.00,0.00,0.00,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|200.19.158.2:1,2,3,4,5,6:0.30,0.48,1.30,0.13:|200.131.0.134:1,2,3,4,5,6:0.30,0.33,0.40,0.00:|200.143.253.161:1,2,3,4,5,6:0.50,4.62,24.20,76.74:|200.143.252.244:1,2,3,4,5,6:1.20,5.22,13.60,29.01:|170.79.213.153:1,2,3,4,5,6:8.60,10.62,16.20,6.96:|170.79.213.2:1,2,3,4,5,6:49.00,51.62,56.90,8.62:|170.79.213.138:1,2,3,4,5,6:49.00,67.17,83.70,171.90:|170.79.213.19:1,2,3,4,5,6:114.10,114.45,115.50,0.23:|129.250.200.157:1,2,3,4,5,6:113.70,114.22,115.90,0.59:|129.250.9.86:1,2,3,4,5,6:114.10,114.28,114.60,0.02:|84.16.15.177:2,3,5,7,8,9,10,11:258.30,258.70,259.10,0.08:|94.142.117.92:1,2,3,4,5,6,7,8,10,11,12,13,14,15,16:256.60,257.40,258.70,0.32:|213.140.36.231:1,2,3,4,5,7,8,9,10,11,12,13,14,15,16:256.10,256.81,257.30,0.12:|213.140.37.212:1,2,3,4,5,6,7,8,9,10,11:233.50,233.73,233.90,0.01:|176.52.248.179:1,2,3,4,5,6,7,9,10,11:260.70,261.17,261.60,0.05:|213.140.51.59:1:257.20,257.20,257.20,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|88.28.91.218:1,2,3,4:266.30,266.68,266.80,0.05:|81.41.232.42:1:268.60,268.60,268.60,0.00:'

output = Route(output)
oldpath = Route(oldpath)
newpath = Route(newpath)

diff = Route.diff(oldpath, newpath)
print(len(diff))
for d in diff:
    print(d.i1, d.j1)
    print(d.i2, d.j2)