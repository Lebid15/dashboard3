from flask import Flask, render_template
import requests

{ok, 1587, 54888}

app = Flask(__name__)

@app.route('/')
def index():
    url1 = 'https://bayi.ruyakontor.com/servis/bakiye_kontrol.php?kod=5462749100&sifre=ALruyaTL69'
    url2 = 'http://bayi.jneedcontur.com/servis/bakiye_kontrol.php?kod=5442199992&sifre=Alaya1346'
    url3 = 'https://bayi.karmagsm.com.tr/servis/bakiye_kontrol.php?kod=5442199992&sifre=Alaya0908'
    url4 = 'http://bayi.al-lordtl.com/servis/bakiye_kontrol.php?kod=5442199992&sifre=ALtaimTL6891'
    url5 = 'http://bayi.tuccarparcatl.net/servis/bakiye_kontrol.php?kod=5343299918&sifre=5343299918'
    url6 = 'http://efixtl.com/services/talimat_bakiye_takip.php?bayi_kodu=efixtl&sifre=369258a&islem=bakiyeoku'
    
    response1 = requests.get(url1)
    content111 = response1.text.split("|")
    content11 = content111[1]
    content1 = content111[2]
    result1 = float(content11) - float(content1)
    
    response2 = requests.get(url2)
    content222 = response2.text.split("|")
    content22 = content222[1]
    content2 = content222[2]
    result2 = float(content22) - float(content2)
    
    response3 = requests.get(url3)
    content333 = response3.text.split("|")
    content33 = content333[1]
    content3 = content333[2]
    result3 = float(content33) - float(content3)
    
    response4 = requests.get(url4)
    content444 = response4.text.split("|")
    content44 = content444[1]
    content4 = content444[2]
    result4 = float(content44) - float(content4)

    response5 = requests.get(url5)
    content555 = response5.text.split("|")
    content55 = content555[1]
    content5 = content555[2]
    result5 = float(content55) - float(content5)

    response6 = requests.get(url6)
    content666 = response6.text.split(":")
    content66 = content666[1]
    content6 = content666[2]
    result6 = float(content66) - float(content6)

    allresults = result1 + result2 + result3 + result4 + result5 + result6
    
    return render_template('index.html', 
                           content1=content1,  content11=content11, result1=result1, 
                            content2=content2,  content22=content22, result2=result2, 
                              content3=content3,  content33=content33, result3=result3, 
                                content4=content4,  content44=content44, result4=result4, 
                                  content5=content5,  content55=content55, result5=result5, 
                                    content6=content6,  content66=content66, result6=result6,
                                    allresults=allresults, 
                            )


if __name__ == '__main__':
    app.run(debug=True)

