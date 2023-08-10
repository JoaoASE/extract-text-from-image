#pip install easyocr
import easyocr
#vaeriavel puxando comandos da biblioteca
reader = easyocr.Reader(['th','en'])
#variavel da imagem 
results =  reader.readtext('sua_imagem.png')
for x in results:
  print(x[1].strip())
