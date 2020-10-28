import numpy as np 
from PIL import Image 
import os 
import cv2
import matplotlib.pyplot as plt 
# if os.name == 'posix':
#      import resource
import win32file


class CustomDataSet:
    def __init__(self,RootDir,saveDir):
        self.trainAndo      = []
        self.trainHigashi   = []
        self.trainKataoka   = []
        self.trainKodama    = []
        self.trainMasuda    = []
        self.trainSuetomo   = []
        self.testAndo       = []
        self.testHigashi    = []
        self.testKataoka    = []
        self.testKodama     = []
        self.testMasuda     = []
        self.testSuetomo    = []

        self.setRootDir(RootDir=RootDir)
        self.set2ndDir()
        self.setLen2ndDir()
        self.set3rdDir()
        self.set4thDir()
        self.setSaveDir(saveDir=saveDir)
        self.stackImg()
        self.loadImage()
        pass 

    def setRootDir(self,RootDir):
        self.rootDir = RootDir

    def setSaveDir(self,saveDir):
        self.saveDir = saveDir

    def setLogName(self,logName):
        self.logName = logName
    
    def set2ndDir(self):
        # print(self.rootDir)
        self.list2ndDir = [f for f in os.listdir(self.rootDir) if os.path.isdir(os.path.join(self.rootDir,f))]

    def setLen2ndDir(self):
        self.list3rdDir = [ 
            [] for i in self.list2ndDir
        ]

    def set3rdDir(self):
        for i,d in enumerate(self.list2ndDir):
            # print(d)
            # print(os.listdir(self.rootDir+d))
            self.list3rdDir[i] = [f for f in os.listdir(self.rootDir+"/"+d) if os.path.isdir(os.path.join(self.rootDir+"/"+d,f))]


    def set4thDir(self):
        self.list4thDir = [
            [
                [
                    [] for k in self.list3rdDir[0][0]
                ] for j in self.list3rdDir[0]
            ] for i in self.list2ndDir
        ] 
        for i,d1 in enumerate(self.list2ndDir):
            for j,d2 in enumerate(self.list3rdDir[i]):
                self.list4thDir[i][j]  = [f for f in os.listdir(self.rootDir+"/"+d1+"/"+d2) if os.path.isdir(os.path.join(self.rootDir+"/"+d1+"/"+d2,f))]
        # print(self.list4thDir)
        for i,d1 in enumerate(self.list2ndDir):
            for j,d2 in enumerate(self.list3rdDir[i]):
                for k,d3 in enumerate(self.list4thDir[i][j]):
                    self.list4thDir[i][j][k] = self.rootDir+"/"+d1+"/"+d2+"/"+d3
                    self.stackPath(d1,d2,d3,self.list4thDir[i][j][k])
                    # print(self.list4thDir[i][j][k])

    def setSaveDir(self,saveDir):
        self.saveDir = saveDir
    
    def stackPath(self,d1,d2,d3,path):
        if d2 == "train":
            if d3[0]+d3[1]+d3[2]+d3[3] == "ando":
                self.trainAndo.append(path) 
            if d3[0]+d3[1]+d3[2]+d3[3] == "higa":
                self.trainHigashi.append(path)
            if d3[0]+d3[1]+d3[2]+d3[3] == "kata":
                self.trainKataoka.append(path)
            if d3[0]+d3[1]+d3[2]+d3[3] == "koda":
                self.trainKodama.append(path)
            if d3[0]+d3[1]+d3[2]+d3[3] == "masu":
                self.trainMasuda.append(path)
            if d3[0]+d3[1]+d3[2]+d3[3] == "suet":
                self.trainSuetomo.append(path)

        if d2 == "test":  
            if d3[0]+d3[1]+d3[2]+d3[3] == "ando":
                self.testAndo.append(path)
            if d3[0]+d3[1]+d3[2]+d3[3] == "higa":
                self.testHigashi.append(path)
            if d3[0]+d3[1]+d3[2]+d3[3] == "kata":
                self.testKataoka.append(path)
            if d3[0]+d3[1]+d3[2]+d3[3] == "koda":
                self.testKodama.append(path)
            if d3[0]+d3[1]+d3[2]+d3[3] == "masu":
                self.testMasuda.append(path) 
            if d3[0]+d3[1]+d3[2]+d3[3] == "suet":
                self.testSuetomo.append(path)
    
    def stackImg(self):
        self.trainAndoImg = [
            [] for i in self.trainAndo
        ]
        self.trainHigashiImg = [
            [] for i in self.trainHigashi
        ]
        self.trainKataokaImg = [
            [] for i in self.trainKataoka
        ]
        self.trainKodamaImg = [
            [] for i in self.trainKodama
        ]
        self.trainMasudaImg = [
            [] for i in self.trainMasuda 
        ]
        self.trainSuetomoImg = [
            [] for i in self.trainSuetomo
        ]
        self.testAndoImg = [
            [] for i in self.testAndo
        ]
        self.testHigashiImg = [
            [] for i in self.testHigashi
        ]
        self.testKataokaImg = [
            [] for i in self.testKataoka
        ]
        self.testKodamaImg = [
            [] for i in self.testKodama
        ]
        self.testMasudaImg = [
            [] for i in self.testMasuda 
        ]
        self.testSuetomoImg = [
            [] for i in self.testSuetomo
        ]

        for i,p in enumerate(self.trainAndo):
            self.trainAndoImg[i] = [p+"/"+f for j,f in enumerate(os.listdir(self.trainAndo[i]))]
        for i,p in enumerate(self.trainHigashi):
            self.trainHigashiImg[i] = [p+"/"+f for j,f in enumerate(os.listdir(self.trainHigashi[i]))]
        for i,p in enumerate(self.trainKataoka):
            self.trainKataokaImg[i] = [p+"/"+f for j,f in enumerate(os.listdir(self.trainKataoka[i]))]
        for i,p in enumerate(self.trainKodama):
            self.trainKodamaImg[i] = [p+"/"+f for j,f in enumerate(os.listdir(self.trainKodama[i]))]
        for i,p in enumerate(self.trainMasuda):
            self.trainMasudaImg[i] = [p+"/"+f for j,f in enumerate(os.listdir(self.trainMasuda[i]))]
        
        for i,p in enumerate(self.trainSuetomo):
            self.trainSuetomoImg[i] = [p+"/"+f for j,f in enumerate(os.listdir(self.trainSuetomo[i]))]
        
        for i,p in enumerate(self.testAndo):
            self.testAndoImg[i] = [p+"/"+f for j,f in enumerate(os.listdir(self.testAndo[i]))]
        for i,p in enumerate(self.testHigashi):
            self.testHigashiImg[i] = [p+"/"+f for j,f in enumerate(os.listdir(self.testHigashi[i]))]
        for i,p in enumerate(self.testKataoka):
            self.testKataokaImg[i] = [p+"/"+f for j,f in enumerate(os.listdir(self.testKataoka[i]))]
        for i,p in enumerate(self.testKodama):
            self.testKodamaImg[i] = [p+"/"+f for j,f in enumerate(os.listdir(self.testKodama[i]))]
        for i,p in enumerate(self.testMasuda):
            self.testMasudaImg[i] = [p+"/"+f for j,f in enumerate(os.listdir(self.testMasuda[i]))]
        for i,p in enumerate(self.testSuetomo):
            self.testSuetomoImg[i] = [p+"/"+f for j,f in enumerate(os.listdir(self.testSuetomo[i]))]
        self.trainImg = [
            self.trainAndoImg,
            self.trainHigashiImg,
            self.trainKataokaImg,
            self.trainKodamaImg,
            self.trainMasudaImg,
            self.trainSuetomoImg
        ]
        # print(self.trainAndoImg[0])
        self.testImg = [
            self.testAndoImg,
            self.testHigashiImg,
            self.testKataokaImg,
            self.testKodamaImg,
            self.testMasudaImg,
            self.testSuetomoImg
        ]
        pass 

    
    def loadImage(self):
        cnt = 0

        for i,_ in enumerate(self.trainImg):
            for j,_ in enumerate(self.trainImg[i]):
                for k,path in enumerate(self.trainImg[i][j]):
                    # self.trainImg[i][j][k] = Image.open(path)
                    img = Image.open(path)
                    img.save(self.saveDir+"/"+str(cnt)+".jpg")
                    # print(self.saveDir+"/"+str(cnt)+".jpg")
                    # ここでファイルのパスが格納されていた3次元配列に読み込んだ画像を格納する
                    # with open(path, 'r') f:
                    #     self.trainImg[i][j][k] = f.read()
                    #     # f.close()
                    # print(path)
                    # f = open(path, 'r')
                    # self.trainImg[i][j][k] = f.read()
                    # f.close()
                    # cv2.imre
                    cnt += 1
        pass 


#####----------------TEST----------------#####     
    def test1(self):
        print(os.listdir(self.rootDir))
        print([f for f in os.listdir(self.rootDir) if os.path.isdir(os.path.join(self.rootDir,f))])

    def test2(self):
        print(self.list2ndDir)

    def test3(self):
        l3 = []
        print(self.list2ndDir[0])
        # Resources1
        print([f for f in os.listdir(self.list2ndDir[0]) if os.path.isdir(os.path.join(self.list2ndDir[0],f))])
        # ['train']
        for d in self.list2ndDir:
            print(d)
            l3 = [f for f in os.listdir(d) if os.path.isdir(os.path.join(d,f))]
            print(l3)

    def test4(self):
        print(len(self.list2ndDir))
        for i,d in enumerate(self.list2ndDir):
            self.list3rdDir[i] = [f for f in os.listdir(d) if os.path.isdir(os.path.join(d,f))]
        print(self.list3rdDir)
        # [['test', 'train'], ['test', 'train'], ['test', 'train'], ['test', 'train']]

    def test5(self):
        self.list4thDir = [
            [
                [
                    [] for k in self.list3rdDir[0][0]
                ] for j in self.list3rdDir[0]
            ] for i in self.list2ndDir
        ] 
        print(self.list4thDir)

    def test6(self):
        # for i,_ in enumerate(self.list2ndDir):
        #     for j,d2 in enumerate(self.list3rdDir):
        #         self.list4thDir[i][j] = [f for f in os.listdir(d2) if os.path.isdir(os.path.join(d2,f))]
        # print(self.list4thDir)
        # print(self.list4thDir)
        # print(self.list4thDir[0])
        # print(self.list4thDir[0][0])
        # [[[], []], [[], []], [[], []], [[], []]]
        pass 

    def test7(self):
        v = np.zeros((1,len(self.list2ndDir),len(self.list3rdDir[0])),dtype=str)
        print(v)
        print(v[0])
        print(v[0][0])
        print(v[0][0][0])
        v[0][0][0] = "hoge"
        print(v)
        v = np.array(self.list3rdDir)
        print(v)
        v = np.array([self.list3rdDir],dtype="U10")
        print(v)
        v = np.zeros((1,len(self.list2ndDir),len(self.list3rdDir[0])),dtype="U10")
        print(v)
        v[0][0][0] = "hoge"
        print(v)

    def test8(self):
        print(self.list3rdDir)
        print(self.list3rdDir[0])
        print(self.list3rdDir[0][0])
        print(self.list2ndDir)
        print(self.list2ndDir[0])
        print(self.rootDir+"/"+self.list2ndDir[0]+"/"+self.list3rdDir[0][0]+"/")
        print(self.rootDir+"/"+self.list2ndDir[0]+"/"+self.list3rdDir[0][1]+"/")
        print(self.rootDir+"/"+self.list2ndDir[1]+"/"+self.list3rdDir[0][0]+"/")
        print(self.rootDir+"/"+self.list2ndDir[1]+"/"+self.list3rdDir[0][1]+"/")
        print(self.rootDir+"/"+self.list2ndDir[0]+"/"+self.list3rdDir[1][1]+"/")
        for i,d1 in enumerate(self.list2ndDir):
            print(i)
            print(d1)
            # 0
            # Resources1
            # 1
            # Resources2
            # 2
            # Resources3
            # 3
            # Resources4
        for j,d2 in enumerate(self.list3rdDir):
            print(j)
            print(d2)
            # 0
            # ['test', 'train']
            # 1
            # ['test', 'train']
            # 2
            # ['test', 'train']
            # 3
            # ['test', 'train']
        for k,d3 in enumerate(self.list3rdDir[0]):
            print(d3)
            # test
            # train
        print("-----------------------------------------------------------")
        for i,d1 in enumerate(self.list2ndDir):
            # print(self.rootDir+"/"+d1+"/")
            # ../Project3/Resources1/
            for j,d2 in enumerate(self.list3rdDir[i]):
                
                print(self.rootDir+"/"+d1+"/"+d2)
                self.list4thDir[i][j]  = [f for f in os.listdir(self.rootDir+"/"+d1+"/"+d2) if os.path.isdir(os.path.join(self.rootDir+"/"+d1+"/"+d2,f))]
        print(self.list4thDir)

    def test9(self):
        self.list4thDir = [
            [
                [
                    [] for k in self.list3rdDir[0][0]
                ] for j in self.list3rdDir[0]
            ] for i in self.list2ndDir
        ] 
        for i,d1 in enumerate(self.list2ndDir):
            for j,d2 in enumerate(self.list3rdDir[i]):
                self.list4thDir[i][j]  = [f for f in os.listdir(self.rootDir+"/"+d1+"/"+d2) if os.path.isdir(os.path.join(self.rootDir+"/"+d1+"/"+d2,f))]
        # print(self.list4thDir)
        for i,d1 in enumerate(self.list2ndDir):
            for j,d2 in enumerate(self.list3rdDir[i]):
                for k,d3 in enumerate(self.list4thDir[i][j]):
                    self.list4thDir[i][j][k] = self.rootDir+"/"+d1+"/"+d2+"/"+d3
                    # print(self.list4thDir[i][j][k])
                    # print(os.listdir(self.list4thDir[i][j][k]))
                    # print(d3)
                    # print(d3[0]+d3[1]+d3[2]+d3[3])
                    # self.loadSave(d1,d2,d3,self.list4thDir[i][j][k])
    
    def test10(self):
        print(self.trainAndo)
        print(self.trainHigashi)
        print(self.trainKataoka)
        print(self.trainKodama)
        print(self.trainMasuda)
        print(self.trainSuetomo)
        print(self.testAndo)
        print(self.testHigashi)
        print(self.testKataoka)
        print(self.trainKodama)
        print(self.testMasuda)
        print(self.testSuetomo)

    def test11(self):
        # print(self.trainAndo)
        f = os.listdir(self.trainAndo[1])
        # print(f)
        for d in f:
            print(self.trainAndo[0]+"/"+d)
        print(len(self.trainAndo)) # 20

    def test12(self):
        # print(self.trainAndo)   
        self.trainAndoImg = [
            [
                [] for j in os.listdir(self.trainAndo[0])
            ] for i in self.trainAndo
        ]
        self.trainHigashiImg = [
            [
                [] for j in os.listdir(self.trainHigashi[0])
            ] for i in self.trainHigashi
        ]
        self.trainKataokaImg = [
            [
                [] for j in os.listdir(self.trainKataoka[0])
            ] for i in self.trainKataoka
        ]
        self.trainKodamaImg = [
            [
                [] for j in os.listdir(self.trainKodama[0])
            ] for i in self.trainKodama
        ]
        for i,path in enumerate(self.trainAndo):    # 20
            # print(i)
            for j,jpg in enumerate(os.listdir(self.trainAndo[i])): # 約80枚
                # print(j)
                self.trainAndoImg[i][j] = path + "/" + jpg
                # print(self.trainAndoImg[i][j])
        for i,path in enumerate(self.trainHigashi):    # 20
            for j,jpg in enumerate(os.listdir(self.trainHigashi[0])): # 約80枚
                self.trainHigashiImg[i][j] = path + "/" + jpg
        
        # 安藤君の全jpg画像のファイル名を格納することができた。
        print(self.trainAndoImg)

    def test13(self):
        self.train = [
            [] for i in range(0,6)
        ]
        # print(self.train)
        self.train[0].append(self.trainAndo)
        self.train[1].append(self.trainHigashi)
        self.train[2].append(self.trainKataoka)
        self.train[3].append(self.trainKodama)
        self.train[4].append(self.trainMasuda)
        self.train[5].append(self.trainSuetomo)
        # print(self.train)
        # for i in range(0,6):    # 6クラス分類
        #     for j,d1 in enumerate(self.train[i]):
        #         for k,d2 in enumerate(os.listdir(self.train[i][j])):    # 80枚より必ず下
        #             print(d2)

    def test14(self):
        self.trainAndoImg = [
            [] for i in self.trainAndo
        ]
        # print(self.trainAndoImg)
        self.trainAndoImg[0] = [1,2,3]
        print(self.trainAndoImg)
        self.trainAndoImg[0] = [f for i,f in enumerate(os.listdir(self.trainAndo[0]))]
        print(self.trainAndoImg)
        self.trainAndoImg[1] = [f for i,f in enumerate(os.listdir(self.trainAndo[1]))]
        print(self.trainAndoImg)
        self.trainAndoImg[2] = [f for i,f in enumerate(os.listdir(self.trainAndo[2]))]
        print(self.trainAndoImg)

    def test15(self):
        self.trainImg = [
            self.trainAndo,
            self.trainHigashi,
            self.trainKataoka,
            self.trainKodama,
            self.trainMasuda,
            self.trainSuetomo 
        ]
        for i,path in enumerate(self.trainAndo):
            print(i)
            print(path)
            self.trainImg = [

            ]
        # print(self.trainImg)

    def test16(self):
        # print(self.trainAndoImg[19][0])
        # print(self.trainHigashiImg[19][1])    # Error ほかの人よりも撮影する回数が少ないため
        # print(self.trainKataokaImg[19][79]) # データを消しているとError
        print(self.testAndoImg[0][0])
        print(self.testAndoImg[0][1])
        print(self.testAndoImg[0][2])
        print(self.testAndoImg[0][19])
        print(self.testHigashiImg[14][0])
        
    def test17(self):
        img = Image.open(self.trainAndoImg[0][0])
        # img.show()
        for i,d1 in enumerate(self.trainAndoImg):
            # print(i)  # 0 ～ 19
            for j,d2 in enumerate(self.trainAndoImg[i]):
                print(j)    # 0 ～ 79
                pass 
    
    def test18(self):
        for i,_ in enumerate(self.trainImg):
            # print(i)    # 0 1 2 3 4 5
            for j,_ in enumerate(self.trainImg[i]):
                # print(j)    
                # ando,kataoka,kodama,masuda,suetomo
                # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 
                # higashi
                # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
                for k,path in enumerate(self.trainImg[i][j]):
                    # print(k)
                    # 0 ～ 79
                    # print(path)
                    print(self.trainImg[i][j][k])
if __name__ == "__main__":
    # print(win32file._getmaxstdio()) # 512 <= Windowsのファイルディスクプリタの上限
    CD = CustomDataSet(RootDir="../DataSet",saveDir="CustomDataSet")
    # CD.setRootDir(RootDir="../DataSet")
    # CD.set2ndDir()
    # CD.setLen2ndDir()
    # CD.set3rdDir()
    # CD.set4thDir()
    # CD.setSaveDir(saveDir="Dataset")
    # CD.test9()
    # CD.test7()
    # CD.test5()
    # CD.test8()
    # CD.test10()
    # CD.test11()
    # CD.test12()
    # CD.test13()
    # CD.test14()
    # CD.test15()
    # CD.test16()
    # CD.test17()
    # CD.test18()