height = input('請輸入身高(cm): ')
weight = input('請輸入體重(kg): ')

height = float(height) / 100
weight = float(weight)

bmi = round((weight / height ** 2),2)

if bmi < 18.5:
    print('你的bmi值為', bmi, '屬於體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('你的bmi值為', bmi, '屬於健康體重')
elif bmi >= 24 and bmi < 27:
    print('你的bmi值為', bmi, '屬於體重過重')
elif bmi >= 27 and bmi < 30:
    print('你的bmi值為', bmi, '屬於輕度肥胖')
elif bmi >= 30 and bmi < 35:
    print('你的bmi值為', bmi, '屬於中度肥胖')     
else :
    print('你的bmi值為', bmi, '屬於重度肥胖')