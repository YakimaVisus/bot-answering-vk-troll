import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import time
# САМЫЙ КРУТОЙ АВТООТВЕТЧИК В МИРЕ ОТ Yakima Visus ВЫ ТОЛЬКО НЕ ВАРУЙТЕ ДА ЛУЧШЕ ЗВЕЗДОЧКИ МНЕ ПОСТАВТЬЕ НА ГИТХАБЕ 

print("""
く__,.ヘヽ.　　　　/　,ー､ 〉
　　　　　＼ ', !-─‐-i　/　/´
　　　 　 ／｀ｰ'　　　 L/／｀ヽ､
　　 　 /　 ／,　 /|　 ,　 ,　　　 ',
　　　ｲ 　/ /-‐/　ｉ　L_ ﾊ ヽ!　 i
　　　 ﾚ ﾍ 7ｲ｀ﾄ　 ﾚ'ｧ-ﾄ､!ハ|　 |
　　　　 !,/7 '0'　　 ´0iソ| 　 |　　　
　　　　 |.从"　　_　　 ,,,, / |./ 　 |
　　　　 ﾚ'| i＞.､,,__　_,.イ / 　.i 　|
　　　　　 ﾚ'| | / k_７_/ﾚ'ヽ,　ﾊ.　|
　　　　　　 | |/i 〈|/　 i　,.ﾍ |　i　|
　　　　　　.|/ /　ｉ： 　 ﾍ!　　＼　|
　　　 　 　 kヽ>､ﾊ 　 _,.ﾍ､ 　 /､!
　　　　　　 !'〈//｀Ｔ´', ＼ ｀'7'ｰr'
　　　　　　 ﾚ'ヽL__|___i,___,ンﾚ|ノ
　　　　　 　　　ﾄ-,/　|___./
　　　　　 　　　'ｰ'　　!_,.:
 САМЫЙ САМЫЙ САМЫЙ ЛУЧШИЙ АВТООТВЕТЧИК ДЛЯ ВКОНТАКТЕ ТОЧКА КОМ
""")




print('Git: https://github.com/YakimaVisus')
#шаблы тута
gadosti = ['ты лох','ты пидр','ты школьник','заткнись','чьмо','лупиздрик','педик','с хуя чо','сосешь','сосун','писькалюб','писюндрик сосируешь мне','хватит посасай делать','чо сасешь опять','чмоня']
def main():
    vk_session = vk_api.VkApi(
        token="токен")

    try:
        vk = vk_session.get_api()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_chat:
            peer = str(int(event.chat_id) + 2000000000)
            if event.text:
                   time.sleep(5)
                   vk.messages.send(peer_id=peer, random_id=str(random.randint(1,99999)),
                                    
                                     message=random.choice(gadosti), v=5.124)

if __name__ == '__main__':
    main()
