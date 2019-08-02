# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:31:16 2016

@author: shaw
"""

import xlrd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np
from pylab import *
from itertools import product
from matplotlib.colors import LogNorm
#import gc

    
def config():
#    gc.collect()
    m = 2
    n = 2
    length = 230
    wide = 200
    cte =  m / 2
    num_l = length / m
    num_w = wide / n
    square = length * wide
    pixel = m * n
    j = int(square / pixel)
    x1 = {1: 10, 2: 30, 3: 55, 4: 75, 5: 145, 6: 165, 7: 100, 8: 120, 9: 10, 10: 30, 
         11: 55, 12: 75, 13: 145, 14: 165, 15: 100, 16: 120, 17: 10, 18: 30, 19: 55, 20: 75, 
         21: 145, 22: 165, 23: 100, 24: 120, 25: 10, 26: 30, 27: 55, 28: 75, 29: 145, 30: 165,
         31: 100, 32: 120, 33: 10, 34: 30, 35: 55, 36: 75, 37: 145, 38: 165, 39: 100, 40: 120,
         41: 100, 42: 120, 43: 10, 44: 90, 45: 55, 46: 75, 47: 145, 48: 165, 49: 100, 50: 120,
         51: 10, 52: 30, 53: 55, 54: 75, 55: 145, 56: 165, 57: 100, 58: 120, 59: 10, 60: 30,
         61: 55, 62: 75, 63: 145, 64: 165, 65: 100, 66: 120, 67: 10, 68: 30, 69: 55, 70: 75,
         71: 145, 72: 165, 73: 100, 74: 120, 75: 10, 76: 30, 77: 55, 78: 75, 79: 145, 80: 165,
         97: 190, 99: 210, 100: 190, 101: 210, 102: 190, 103: 210, 104: 190, 105: 210, 106: 190, 107: 210, 
         108: 190, 109: 210, 110: 190, 112: 210, 113: 190, 114: 210, 115: 190, 116: 210, 117: 190, 118: 210}
    
    y1 = {1: 190, 2: 190, 3: 190, 4: 190, 5: 90, 6: 90, 7: 190, 8: 190, 9: 170, 10: 170,
         11: 170, 12: 170, 13: 70, 14: 70, 15: 170, 16: 170, 17: 150, 18: 150, 19: 150, 20: 150,
         21: 50, 22: 50, 23: 150, 24: 150, 25: 130, 26: 130, 27: 130, 28: 130, 29:30, 30: 30,
         31: 130, 32: 130, 33: 110, 34: 110, 35: 110, 36: 110, 37: 10, 38: 10, 39: 110, 40: 110,
         41: 90, 42: 90, 43: 90, 44: 90, 45: 90, 46: 90, 47: 190, 48: 190, 49: 70, 50: 70,
         51: 70, 52: 70, 53: 70, 54: 70, 55: 170, 56: 170, 57: 50, 58: 50, 59:50, 60: 50, 
         61: 50, 62: 50, 63: 150, 64: 150, 65: 30, 66: 30, 67: 30, 68: 30, 69: 30, 70: 30, 
         71: 130, 72: 130, 73: 10, 74: 10, 75: 10, 76: 10, 77: 10, 78: 10 , 79: 110, 80: 110,
         97: 190, 99: 190, 100: 170, 101: 170, 102: 150, 103: 150, 104: 130, 105: 130, 106: 110, 107: 110,
         108: 90, 109: 90, 110: 70, 112: 70, 113: 50, 114: 50, 115: 30,  116: 30, 117: 10, 118: 10}
    return  j, num_l, num_w, m, n, cte, x1, y1

def center_voxel(j,cte,num_l, num_w, m, n):
    t = [[0 for col in range(2)] for row in range(j)]
    count = 0
    k = 0 
    l = 0
    while(count < j):
        tmp_y = cte + m * k
        tmp_x = cte + n * l
        if(l < num_l):
            if(k < num_w):
                t[count] = [tmp_x, tmp_y]
                count += 1
                k += 1
            else:
                 k = 0
                 l += 1
    v = np.array(t)
    return v


def vector(path1, path2, x1, y1, v,j):
    table1 = xlrd.open_workbook(path1)
    table2 = xlrd.open_workbook(path2)
    sh1 = table1.sheet_by_index(0)
    sh2 = table2.sheet_by_index(0)
    r1 = 1
    r2 = 1
    y = []
    epc_index1 = 0
    epc_index2 = 0
    ante_index1 = 0
    ante_index2 = 0 
    rssi1 = 0.0
    rssi2 = 0.0
    count = 0
    num = 0
    p = 10
    a = []
    while((r1+1 <= sh1.nrows-1)and(r2+1 <= sh2.nrows-1)):
        epc_index1 = int(sh1.cell_value(r1, 0))
        epc_index2 = int(sh2.cell_value(r2, 0))
        epc_next1 = int(sh1.cell_value(r1+1, 0))
        epc_next2 = int(sh2.cell_value(r2+1, 0))
        ante_index1 = int(sh1.cell_value(r1, 1))
        ante_index2 = int(sh2.cell_value(r2, 1))
        ante_next1 = int(sh1.cell_value(r1+1, 1))
        ante_next2 = int(sh2.cell_value(r2+1, 1))
        if((epc_index1 == epc_index2) and (epc_index1 == epc_next1) and (epc_index2 == epc_next2)):
            if(ante_index1 == ante_index2):
                if(ante_index1 == ante_next1 and ante_index2 == ante_next2):
                    r1 = r1 + 1
                    r2 = r2 + 1
                elif(ante_index1 == ante_next1 and ante_index2 != ante_next2):
                    r1 = r1 + 1 
                    rssi1 = float(sh1.cell_value(r1, 6))
                    rssi2 = float(sh2.cell_value(r2, 6))
                    i = abs(rssi1 - rssi2)
                    y.append(i)
                    count = count + 1
                    for num in range(j):
                        d = ((x1[epc_index1]- v[num][0])**2+(y1[epc_index1] - v[num][1])**2)**0.5
                        if(d < p):
                            a.append(1)
                        else:
                            a.append(0)
                    
                elif(ante_index1 != ante_next1 and ante_index2 == ante_next2):
                    r2 = r2 + 1 
                    rssi1 = float(sh1.cell_value(r1, 6))
                    rssi2 = float(sh2.cell_value(r2, 6))
                    i = abs(rssi1 - rssi2)
                    y.append(i)
                    count = count + 1
                    for num in range(j):
                        d = ((x1[epc_index1]- v[num][0])**2+(y1[epc_index1] - v[num][1])**2)**0.5
                        if(d < p):
                            a.append(1)
                        else:
                            a.append(0)
                            
                elif(ante_index1 != ante_next1 and ante_index2 != ante_next2):
                    num = 0
                    rssi1 = float(sh1.cell_value(r1, 6))
                    rssi2 = float(sh2.cell_value(r2, 6))
                    i = abs(rssi1 - rssi2)
                    y.append(i)
                    count = count + 1
                    for num in range(j):
#                        print y[epc_index1]
                        d = ((x1[epc_index1]- v[num][0])**2+(y1[epc_index1] - v[num][1])**2)**0.5
                        if(d < p):
                            a.append(1)
                        else:
                            a.append(0)
                r1 = r1 + 1
                r2 = r2 + 1  
                
            elif(ante_index1 > ante_index2):
                if(ante_index1 != ante_next1 and ante_index2 != ante_next2):
                    rssi1 = float(sh1.cell_value(r1, 6))
                    rssi2 = -80
                    i = abs(rssi1 - rssi2)
                    y.append(i)
                    r2 = r2 +1
                    count = count + 1
                    for num in range(j):
                        d = ((x1[epc_index1]- v[num][0])**2+(y1[epc_index1] - v[num][1])**2)**0.5
                        if(d < p):
                            a.append(1)
                        else:
                            a.append(0)
                    
                else:
                    r2 = r2 + 1
                    
            elif(ante_index2 > ante_index1):
                if(ante_index2 != ante_next2 and ante_index1 != ante_next1):
                    rssi1 = -80
                    rssi2 = float(sh2.cell_value(r2, 6))
                    i = abs(rssi1 - rssi2)
                    y.append(i)
                    r1 = r1 + 1
                    count = count + 1
                    for num in range(j):
                        d = ((x1[epc_index1]- v[num][0])**2+(y1[epc_index1] - v[num][1])**2)**0.5
                        if(d < p):
                            a.append(1)
                        else:
                            a.append(0)
                    
                else:
                    r1 = r1 + 1
                    
        elif((epc_index1 == epc_index2) and((epc_index1 != epc_next1) or(epc_index2 != epc_next2))):
             if(ante_index1 == ante_index2):
                 rssi1 = float(sh1.cell_value(r1, 6))
                 rssi2 = float(sh2.cell_value(r2, 6))
                 i = abs(rssi1 - rssi2)
                 y.append(i)
                 count = count + 1
                 for num in range(j):
                        d = ((x1[epc_index1]- v[num][0])**2+(y1[epc_index1] - v[num][1])**2)**0.5
                        if(d < p):
                            a.append(1)
                        else:
                            a.append(0)
             elif(ante_index1 > ante_index2):
                 rssi1 = float(sh1.cell_value(r1, 6))
                 rssi2 = -80
                 i = abs(rssi1 - rssi2)
                 y.append(i)
                 count = count + 1
                 for num in range(j):
                        d = ((x1[epc_index1]- v[num][0])**2+(y1[epc_index1] - v[num][1])**2)**0.5
                        if(d < p):
                            a.append(1)
                        else:
                            a.append(0)
                 
             elif(ante_index2 > ante_index1):
                 rssi1 = -80
                 rssi2 = float(sh2.cell_value(r2, 6))
                 i = abs(rssi1 - rssi2)
                 y.append(i)           
                 count = count + 1
                 for num in range(j):
                        d = ((x1[epc_index1]- v[num][0])**2+(y1[epc_index1] - v[num][1])**2)**0.5
                        if(d < p):
                            a.append(1)
                        else:
                            a.append(0)
#             elif()
             r1 = r1 + 1
             r2 = r2 + 1
            
             
             
        elif(epc_index1 > epc_index2):
            epc_before1 = int(sh1.cell_value(r1-1, 0))
            epc_before2 = int(sh2.cell_value(r2-1, 0))
            if(epc_before1 != epc_index2 and epc_index1 != epc_next2):
                rssi1 = -80
                rssi2 = float(sh2.cell_value(r2, 6))
                i = abs(rssi1 - rssi2)
                y.append(i)
                r2 = r2 + 1
                count = count + 1
                for num in range(j):
                        d = ((x1[epc_index2]- v[num][0])**2+(y1[epc_index2] - v[num][1])**2)**0.5
                        if(d < p):
                            a.append(1)
                        else:
                            a.append(0)
            else:
                r2 = r2 + 1
                
        elif(epc_index2 > epc_index1):
            epc_before1 = int(sh1.cell_value(r1-1, 0))
            epc_before2 = int(sh2.cell_value(r2-1, 0))
            if(epc_before2 != epc_index1 and epc_index2 != epc_next1):
                rssi1 = float(sh1.cell_value(r1, 6))
                rssi2 = -80
                i = abs(rssi1 - rssi2)
                y.append(i)                
                r1 = r1 + 1
                count = count + 1
                for num in range(j):
                        d = ((x1[epc_index1]- v[num][0])**2+(y1[epc_index1] - v[num][1])**2)**0.5
                        if(d < p):
                            a.append(1)
                        else:
                            a.append(0)
            else:
                r1 = r1 + 1
#     print count
    b = np.array(a)
    w = b.reshape(count, j)
#    print b.size
#     print w
#    z = np.dot(w.T, w)
#    print z
#    q = np.identity(j)
    t= np.mat(y)
#    l = 40
#    u = l * np.dot(q.T, q)
#    print u
#    o = np.mat((z + u))
#    print o
#    e = np.dot(w.T, t.T)
#    print e
    h = np.dot(w.T , t.T)
    x = h.getA()
#    f = open('C:/Users/songkai/Desktop/record/new/x.txt', 'w')
#    for n in range(len(x[0])):       
#        f.write(x[0][n])
#    f.close()
#    plt.hist2d(230, 200, bins=40,weight = x)
#    plt.colorbar()
#    plt.show()
    return x
    
    

#def vector_x(w, y,j):
#    q = np.identity(j)
#    t= np.matrix(y)
#    print t
#    l = 40
#   x = (w.T * w + l * q.T * q).I * w.T * t.T
#    count_length = length / n
#    count_wide = wide / m
#    x = t.reshape([count_wide, count_length])
#    return x
    

def draw(v,x):
    plt.xlim(0,230)
    plt.ylim(0,200)
    ax = plt.gca()
#    ax.xaxis.set_minor_locator(MultipleLocator(2))
#    ax.yaxis.set_minor_locator(MultipleLocator(2))
    ax.xaxis.set_major_locator(MultipleLocator(20))
    ax.yaxis.set_major_locator(MultipleLocator(20))
#    plt.grid()
#    plt.show()
#    plt.imshow(x,  extent=[0,230,0,200])
#    plt.imsave('pic.jpg', 'JPG')
#    pp1=amap(lambda ra: [ra[0],ra[1]],product(arange(0,230,2),arange(0,200,2)))
    scatter(v[:,0],v[:,1],c=x, edgecolor="none")
    return 0     
    
    

    
    
    
    
    
    
    
    
    
    
    
    
def main():
    origin = 'C:/Users/shaw/Desktop/record/new/origin_2.4m.xlsx'
    stand1 = 'C:/Users/shaw/Desktop/record/new/stand1_0.6m.xlsx'
    path1 = origin
    path2 = stand1
    (j, num_l, num_w, m, n, cte, x1, y1) = config()
    v = center_voxel(j,cte,num_l, num_w, m, n)  
    x = vector(path1, path2, x1, y1, v,j)
#    x = vector_x(w, y,j)
#    print x
    draw(v, x)
#    show()

if __name__ == '__main__':
    main()       