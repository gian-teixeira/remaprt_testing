# 222 192
TTL=(13, 14, 15, 16, 17, 18, 19)
for T in ${TTL[*]}; do
    sudo /home/giancarlo/remaprt/src/remaproute -i eno8303 -x 10 -l log -d 213.97.11.62 -o '150.164.10.1:0:0.00,0.00,0.00,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|200.19.158.2:1,2,3,4,5,6:0.30,0.72,1.30,0.11:|200.131.0.134:1,2,3,4,5,6:0.20,0.30,0.40,0.00:|200.143.253.161:1,2,3,4,5,6:0.40,4.87,13.50,28.19:|200.143.252.244:1,2,3,4,5,6:0.80,0.93,1.00,0.01:|170.79.213.153:1,2,3,4,5,6:8.40,8.57,8.70,0.02:|170.79.213.2:1,2,3,4,5,6:49.10,49.52,50.70,0.31:|170.79.213.138:1,2,3,4,5,6:48.90,49.50,51.90,1.17:|170.79.213.19:1,2,3,4,5,6:114.10,114.70,117.30,1.36:|129.250.200.157:1,3,4,6,8,9,10,11:113.70,116.45,123.80,14.13:|129.250.9.86:1,2,3,4,5,6:114.00,114.10,114.20,0.01:|94.142.118.185:1,2,3,4,5,6:221.70,221.90,222.20,0.04:|94.142.98.206:1,2,3,4,5,6:221.70,221.97,222.20,0.03:|94.142.99.170:1,2,3,4,5,6:221.50,221.57,221.70,0.01:|5.53.6.76:1,2,3,4,5,6:221.10,221.15,221.30,0.01:|213.140.51.59:1:257.20,257.20,257.20,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|88.28.91.218:1,2,3,4,5,6:229.00,229.20,229.50,0.03:|81.41.232.42:1:231.70,231.70,231.70,0.00:' -n '150.164.10.1:0:0.00,0.00,0.00,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|200.19.158.2:1,2,3,4,5,6:0.30,0.48,1.30,0.13:|200.131.0.134:1,2,3,4,5,6:0.30,0.33,0.40,0.00:|200.143.253.161:1,2,3,4,5,6:0.50,4.62,24.20,76.74:|200.143.252.244:1,2,3,4,5,6:1.20,5.22,13.60,29.01:|170.79.213.153:1,2,3,4,5,6:8.60,10.62,16.20,6.96:|170.79.213.2:1,2,3,4,5,6:49.00,51.62,56.90,8.62:|170.79.213.138:1,2,3,4,5,6:49.00,67.17,83.70,171.90:|170.79.213.19:1,2,3,4,5,6:114.10,114.45,115.50,0.23:|129.250.200.157:1,2,3,4,5,6:113.70,114.22,115.90,0.59:|129.250.9.86:1,2,3,4,5,6:114.10,114.28,114.60,0.02:|84.16.15.177:2,3,5,7,8,9,10,11:258.30,258.70,259.10,0.08:|94.142.117.92:1,2,3,4,5,6,7,8,10,11,12,13,14,15,16:256.60,257.40,258.70,0.32:|213.140.36.231:1,2,3,4,5,7,8,9,10,11,12,13,14,15,16:256.10,256.81,257.30,0.12:|213.140.37.212:1,2,3,4,5,6,7,8,9,10,11:233.50,233.73,233.90,0.01:|176.52.248.179:1,2,3,4,5,6,7,9,10,11:260.70,261.17,261.60,0.05:|213.140.51.59:1:257.20,257.20,257.20,0.00:|255.255.255.255:0:0.00,0.00,0.00,0.00:|88.28.91.218:1,2,3,4:266.30,266.68,266.80,0.05:|81.41.232.42:1:268.60,268.60,268.60,0.00:' -t $T
done