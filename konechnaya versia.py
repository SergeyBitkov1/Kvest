print("вас зовут Андрей и вы ищите работу для себя,ведь вам уже 35, а у вас ещë нет работы")
print("вы откликнулись на объявление о поиске сотрудников в компьютерный клуб")
print("вы пришли и вам предлагают стать либо уборщиком либо менеджером, что вы выберите?")
a = input()
if a == "уборщик":    
    print("вам одобрили профессию и вы приступили к работе")
    print("в один день,когда вы убирались, вы нашли 5000 рублей под столом взять их?")
    b = input()
    if b == "взять" or "да":        
        print("у вас появились деньги и вы купили себе продукты")
        print("в какой то день вы с коллегами решили сходить в бар,пойдете?")
        c = input()
    elif b == "не брать" or "нет":                    
        print("вы остались голодными и придя домой вас наругала мать")    
    if c == "да":    
        print("вы пришли в бар,выпили и зам директора был в нетрезвом состоянии ипредложил вам стать менеджером,согласны ли вы или нет?")
        d = input()
        if d == "да":
            print("вы стали менеджером")
            print('Спустя месяц директор узнал, что зам директор много пьет и захотел поставить вас на его место, согласны?')
            e = input()
            if e == 'да':
                print('вы стали зам директора')
                print('спустя 2 года директор вышел на пенсию и завещал компанию вам, вы стали директором!')
                print('вдруг возникли неожиданные сложности и ваша компания начала разоряться')
                print('у вас есть несколько идей, которые можно воплотить')
                print('вы можете ппродать компанию за жалкий 1 млн рублей')
                f = input()
                if f == 'да':
                    print('новый владелец заработал 10 миллиардов рублей с вашей компании, а вы снимаете квартиру в спальном районе и живете скучной жизнью')
                elif f == 'нет':
                    print('вы можете либо снизить цены на видеокарты или начать делать более мощьные видеокарты, что выберите 1 или 2?')
                    g = input()
                    if g == '1':
                        print('это не помогло и компания обанкротилась')
                    elif g == '2':
                        print('многим людям это понравилось и видюхи стали хорошо продаваться, вам удалось избежать банкротства, конец!!!')
            elif e == 'нет':
                print('вы остались менеджером')
        elif d == "нет":
            print("вы остались уборщиком навсегда")
    elif с == "нет":
        print("вы остались работать уборщиком до конца своих дней")        
elif a == "менеджер":
    print("это была проверка и вам отказали, вы остались жить с мамой навсегда")
