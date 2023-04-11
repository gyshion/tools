import numpy as np


def to_csv(infile,key,out_csv,ulx,uly,lrx,lry):
    in_np = np.load(infile)[key]

    y_size,x_size = in_np.shape
    y_reso = (uly-lry)/y_size
    x_reso = (lrx-ulx)/x_size

    count = 1
    with open(out_csv,'w') as outfile:
        for x in range(x_size):
            ll_lst = []
            count+=1
            for y in range(y_size):
                if in_np[y,x]==210:

                    lng = ulx+x*x_reso+0.5*x_reso
                    lat = uly-(y*x_reso)-0.5*x_reso

                    ll_lst.append("{:.8f},{:.8f}".format(lng,lat))

            outfile.write(';'.join(ll_lst)+'\n')
            if count%100==0:
                print(count)

if __name__ == '__main__':
    ulx = -180
    uly = 90
    lrx = 180
    lry = -90
    infile = 'C3S-LC-L4-LCCS-Map-300m-P1Y-2020-v2.1.1.npz'
    outfile = 'C3S-LC-L4-LCCS-Map-300m-P1Y-2020-v2.1.1_210coor.csv'
    to_csv(infile,'lc',outfile,ulx,uly,lrx,lry)
