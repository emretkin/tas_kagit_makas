#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from time import sleep



# In[2]:


print("\t\t*********************TAŞ KAĞIT MAKAS*******************\nTaş kağıt makas oyunu 3 seçenekten birinin seçilmesiyle oynanır.\nOyunda taş makası , makas kağıdı , kağıt ise taşı yener. Eğer iki taraf da aynı seçimi yapmışsa beraberlik olur.\nİlk 2 turu kazanan oyunu kazanacaktır.Oyun sonuçlandıktan sonra iki tarafın da isteğine bağlı olarak tekrar oynanabilir veya sonlanabilir.")


# In[3]:


oyunSecenekleri=["Taş","Kağıt","Makas"]
devam_Secenekleri=["Evet","Hayır"]
OyuncuTur=BilgisayarTur=OyuncuGalibiyet=BilgisayarGalibiyet=tur=0
devamMi=False


# In[4]:


def devam_sorgusu(siz,pc):
    global OyuncuGalibiyet,BilgisayarGalibiyet,tur
    i=1
    while True:
        if i:
            bilgisayar=random.choice(devam_Secenekleri)
            i=i-1
            
        if(bilgisayar=="Evet"):
            oyuncu=input("Bilgisayar rövanş istiyor\nDevam edecek misiniz? Evet veya Hayır olarak cevap verin:")
            oyuncu=oyuncu.capitalize()
            if(oyuncu!="Evet" and oyuncu!="Hayır"):
                print("Hatalı giriş tekrar deneyin.")
                continue
                
            elif(oyuncu=="Evet"):
                print("\nİki taraf da devam etmek istiyor. Oyun devam edecek...")
                print(f"Galibiyet Sayıları:Siz {OyuncuGalibiyet}-{BilgisayarGalibiyet} Bilgisayar\n")
                sleep(2)
                return True

            elif(oyuncu=="Hayır"):
                print(f"Bilgisayarın rövanş isteğine rağmen oyunu sonlandırdınız.\nSonuç:Siz {siz}-{pc} Bilgisayar")
                OyuncuGalibiyet=BilgisayarGalibiyet=tur=0
                return False

        if(bilgisayar=="Hayır"):
            print(f"Bilgisayar devam etmek istemediği için oyun sonlandı.\nSonuç:Siz {siz}-{pc} Bilgisayar")
            OyuncuGalibiyet=BilgisayarGalibiyet=tur=0
            return False

        


# In[5]:


def tas_kagit_makas_EMRE_TEKİN():
    global OyuncuTur,BilgisayarTur,OyuncuGalibiyet,BilgisayarGalibiyet,tur
    
    while True:
        tur+=1
        print(f"####################ROUND:{tur}###################\n")
        oyuncuSecim=input("Taş Kağıt veya Makas yazarak seçiminizi yapın (Çıkış için 'exit'):")
        oyuncuSecim=oyuncuSecim.capitalize()
    
        if(oyuncuSecim!="Taş" and oyuncuSecim!="Kağıt" and oyuncuSecim!="Makas" and oyuncuSecim!="Exit"):
            print("Hatalı giriş yaptınız,tekrar deneyin:")
            tur-=1
            continue
        elif(oyuncuSecim=="Exit"):
            if(OyuncuGalibiyet>BilgisayarGalibiyet):
                print(f"Oyunu toplam {OyuncuGalibiyet}-{BilgisayarGalibiyet} skorla bitirerek kazandınız.")
            elif(OyuncuGalibiyet<BilgisayarGalibiyet):
                print(f"Oyunu toplam {OyuncuGalibiyet}-{BilgisayarGalibiyet} skorla bitirerek kaybettiniz.")
            else:
                print(f"Oyunu toplam {OyuncuGalibiyet}-{BilgisayarGalibiyet} skorla berabere bitirdiniz.")
            OyuncuGalibiyet=BilgisayarGalibiyet=tur=0
            break
            
        bilgisayarSecim=random.choice(oyunSecenekleri)
        
        if(oyuncuSecim=="Taş" and bilgisayarSecim=="Makas"):
            OyuncuTur+=1
            
            if(OyuncuTur==2):
                print(f"Tebrikler! Rakibinizin seçimi {bilgisayarSecim}.\n{OyuncuTur}-{BilgisayarTur} sonucuyla oyunu kazandınız.")
                OyuncuTur=0
                BilgisayarTur=0
                OyuncuGalibiyet+=1
                sleep(2)
                devamMi=devam_sorgusu(OyuncuGalibiyet,BilgisayarGalibiyet)
                if(not devamMi):
                    break

                else:
                    continue
            
                    
            else:
                print(f"Tebrikler! Rakibinizin seçimi {bilgisayarSecim}. Turu kazandınız.\nSkor:Siz {OyuncuTur}-{BilgisayarTur} Bilgisayar\n")
                sleep(2)
        
            

        elif(oyuncuSecim=="Taş" and bilgisayarSecim=="Kağıt"):
            BilgisayarTur+=1
            
            if(BilgisayarTur==2):
                print(f"Rakibinizin seçimi {bilgisayarSecim}.\nMaalesef {BilgisayarTur}-{OyuncuTur} sonucuyla oyunu kaybettiniz.")
                BilgisayarTur=0
                OyuncuTur=0
                BilgisayarGalibiyet+=1
                sleep(2)
                devamMi=devam_sorgusu(OyuncuGalibiyet,BilgisayarGalibiyet)
                if(not devamMi):
                    break

                else:
                    continue
            
                    
            else:
                print(f"Rakibinizin seçimi {bilgisayarSecim}. Maalesef turu kaybettiniz.\nSkor:Siz {OyuncuTur}-{BilgisayarTur} Bilgisayar\n")
                sleep(2)
                


        elif(oyuncuSecim=="Taş" and bilgisayarSecim=="Taş"):
            print(f"Rakibiniz de {bilgisayarSecim} seçti.Tur berabere.\nSkor:Siz {OyuncuTur}-{BilgisayarTur} Bilgisayar\n")
            sleep(1)
            continue


        

        elif(oyuncuSecim=="Kağıt" and bilgisayarSecim=="Taş"):
            OyuncuTur+=1
            
            if(OyuncuTur==2):
                print(f"Tebrikler! Rakibinizin seçimi {bilgisayarSecim}.\n{OyuncuTur}-{BilgisayarTur} sonucuyla oyunu kazandınız.")
                OyuncuTur=0
                BilgisayarTur=0
                OyuncuGalibiyet+=1
                sleep(2)
                devamMi=devam_sorgusu(OyuncuGalibiyet,BilgisayarGalibiyet)
                if(not devamMi):
                    break

                else:
                    continue
            
                    
            else:
                print(f"Tebrikler! Rakibinizin seçimi {bilgisayarSecim}. Turu kazandınız.\nSkor:Siz {OyuncuTur}-{BilgisayarTur} Bilgisayar\n")
                sleep(2)
                
        
            

        elif(oyuncuSecim=="Kağıt" and bilgisayarSecim=="Makas"):
            BilgisayarTur+=1
            
            if(BilgisayarTur==2):
                print(f"Rakibinizin seçimi {bilgisayarSecim}.\nMaalesef {BilgisayarTur}-{OyuncuTur} sonucuyla oyunu kaybettiniz.")
                BilgisayarTur=0
                OyuncuTur=0
                BilgisayarGalibiyet+=1
                sleep(2)
                devamMi=devam_sorgusu(OyuncuGalibiyet,BilgisayarGalibiyet)
                if(not devamMi):
                    break

                else:
                    continue
            
                    
            else:
                print(f"Rakibinizin seçimi {bilgisayarSecim}. Maalesef turu kaybettiniz.\nSkor:Siz {OyuncuTur}-{BilgisayarTur} Bilgisayar\n")
                sleep(2)
                


        elif(oyuncuSecim=="Kağıt" and bilgisayarSecim=="Kağıt"):
            print(f"Rakibiniz de {bilgisayarSecim} seçti.Tur berabere.\nSkor:Siz {OyuncuTur}-{BilgisayarTur} Bilgisayar\n")
            sleep(2)
            


        
        elif(oyuncuSecim=="Makas" and bilgisayarSecim=="Kağıt"):
            OyuncuTur+=1
            
            if(OyuncuTur==2):
                print(f"Tebrikler! Rakibinizin seçimi {bilgisayarSecim}.\n{OyuncuTur}-{BilgisayarTur} sonucuyla oyunu kazandınız.")
                OyuncuTur=0
                BilgisayarTur=0
                OyuncuGalibiyet+=1
                sleep(2)
                devamMi=devam_sorgusu(OyuncuGalibiyet,BilgisayarGalibiyet)
                if(not devamMi):
                    break

                else:
                    continue
            
                    
            else:
                print(f"Tebrikler! Rakibinizin seçimi {bilgisayarSecim}. Turu kazandınız.\nSkor:Siz {OyuncuTur}-{BilgisayarTur} Bilgisayar\n")
                sleep(2)
        
            

        elif(oyuncuSecim=="Makas" and bilgisayarSecim=="Taş"):
            BilgisayarTur+=1
            
            if(BilgisayarTur==2):
                print(f"Rakibinizin seçimi {bilgisayarSecim}.\nMaalesef {BilgisayarTur}-{OyuncuTur} sonucuyla oyunu kaybettiniz.")
                BilgisayarTur=0
                OyuncuTur=0
                BilgisayarGalibiyet+=1
                sleep(2)
                devamMi=devam_sorgusu(OyuncuGalibiyet,BilgisayarGalibiyet)
                if(not devamMi):
                    break

                else:
                    continue
            
                    
            else:
                print(f"Rakibinizin seçimi {bilgisayarSecim}. Maalesef turu kaybettiniz.\nSkor:Siz {OyuncuTur}-{BilgisayarTur} Bilgisayar\n")
                sleep(2)


        elif(oyuncuSecim=="Makas" and bilgisayarSecim=="Makas"):
            print(f"Rakibiniz de {bilgisayarSecim} seçti.Tur berabere.\nSkor:Siz {OyuncuTur}-{BilgisayarTur} Bilgisayar\n")
            sleep(2)
            
            

        

        
                
                
                
            
    



# In[7]:


tas_kagit_makas_EMRE_TEKİN()


# In[ ]:





# 
