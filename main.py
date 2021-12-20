
import cv2

kamera=cv2.VideoCapture(0)

while True:
    ret, goruntu = kamera.read()
    #return komutu
    cv2.imshow('pencere_ismi', goruntu)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #waitKey de ki değer 1 olunca görüntü çok hızlı anlık hareket ediyor lakin büyüdükçe görüntü yavaşlıyor.
        break
        #komuta emir vererek kamerayı kapatma tuşu
kamera.relase()
cv2.destroyAllWindows()


#ARAŞTIRMA SONUCU:
#PYHTON SÜRÜMÜ OPENCV DE 3.6 KURMAMIZI İSTEDİĞİNDEN CV2 KÜTÜPHANESİNİ EKLEME KONUSUNDA HATA ALDIK. BU HATANIN TAM NEDENİNİ ÇÖZÜMLEYEMEDİK.



