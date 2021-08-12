import keyboard as kb

kb.write('oi')#digita oque estiver dentro
kb.send('windows+r')#aperta essas teclas
kb.block_key('o')#bloqueia a tecla o kb.unblock_key("o") desbloqueia
while True:
    if kb.is_pressed('l'):#ver se apertou
        print('l')
        break
kb.add_hotkey('ctrl+m',print,args=('foi'))#printa quando apertar