telephone_dict = {'1111111111': 'Amal', '2222222222': 'Mohammed', '3333333333': 'Khadijah', '4444444444': 'Abdullah',
                  '5555555555': 'Rawan', '6666666666': 'Faisal', '7777777777': 'Layla'}

user_in = input('please enter a number or name: ')
names_num = {value: key for key, value in telephone_dict.items()}  # عكس القيم في القاموس في حال اردنا الوصول للأسماء
if user_in.isalpha():             #التأكد من نوع المدخل اسم او رقم
    for name in names_num:
        if user_in in names_num:
            print(names_num.get(user_in))
        elif user_in not in names_num:
            print('Sorry, the number is not found')
        break
elif user_in.isdigit():      # نتأكد من نوع المدخلات هل هي ارقام
    for num in telephone_dict:
        if user_in in telephone_dict:
            if len(user_in) == 10:           # التأكد من طول الأرقام
                print(telephone_dict.get(user_in))
            elif len(user_in) != 10:
                print('This is invalid number')
        elif user_in not in telephone_dict:              # في حال كان الرقم غير موجود و لكن طوله مطابق
            if len(user_in) == 10:
                print('Sorry, the number is not found')
            else:
                print('This is invalid number')
        break

else:
    print('This is invalid number')

#input('Press ENTER to exit')                      # في حال تشغيله عن طريق CMD
