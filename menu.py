import sys

def menu(state):
    choice = 0
    while choice != 1 or 2 or 3 or 4:
    choice = int(input('МЕНЮ:/n1 - Продолжить/n2 - Сохранить/n3 - Загрузить/n4 - Выход из игры'))
    if choice == 1:
        return()
    elif choice == 2:
        #Сохраняем информацию о персонаже
        save_hero = open('save_hero.txt', 'w')
        save_hero.write(hero)
        save_hero.close()
        
        #Сохраняем информацию о локации
        save_location = open('save_location.txt', 'w')
        save_location.write(location)
        save_location.close()
        
        #Сохраняем информацию о ящиках
        save_boxes = open('save_boxes.txt', 'w')
        save_boxes.write(boxes)
        save_boxes.close()
        
        #Сохраняем информацию о NPC
        save_npc = open('save_npc.txt', 'w')
        save_npc.write(npc)
        save_npc.close()
        return()
    elif choice == 3:
        #Загружаем информацию о персонаже
        load_file = open('save_hero.txt', 'r')
        while line != '':
            name = load_file.readline()
            name = name.rstrip('\n')
            strenght = int(strenght.rstrip('\n'))
            strenght = load_file.readline()      
            dexterity = load_file.readline()
            dexterity = int(dexterity.rstrip('\n')) 
            hp = load_file.readline()
            hp = int(hp.rstrip('\n'))
            hero = [name, strenght, dexterity, hp]
        load_file.close()
            
        #Загружаем информацию о локации
        load_file = open('save_location.txt', 'r')
        while line != '':
            loc_num = load_file.readline()
            loc_num = int(loc_num.rstrip('\n'))
            loc_type = load_file.readline()
            loc_type = loc_type.rstrip('\n')
            description = load_file.readline()
            description = description.rstrip('\n')
            n_door = load_file.readline()
            n_door = int(n_door.rstrip('\n'))
            s_door = load_file.readline()
            s_door = int(s_door.rstrip('\n'))
            w_door = load_file.readline()
            w_door = int(w_door.rstrip('\n'))
            e_door = load_file.readline()
            e_door = int(e_door.rstrip('\n'))
            location = [loc_num, loc_type, description, ln_door, s_door, w_door, e_door]
        load_file.close()

        #Загружаем информацию о контейнерах
        load_file = open('save_boxes.txt', 'r')
        while line != '':
            sum = load_file.readline()
            sum = int(sum.rstrip('\n'))
            boxes = [sum]
            if not sum:
                for i in range(sum+1):
                    type = load_file.readline()
                    type = type.rstrlip('\n')
                    boxes = boxes.append(type)
                    description = load_file.readline()
                    description = description.rstrip('\n')
                    boxes = boxes.append(description)
                    content = load_file.readline()
                    content = content.rstrip('\n')
                    boxes = boxes.append(content)
                    content_num = load_file.readline()
                    content_num = int(content_num.rstrip('\n'))
                    boxes = boxes.append(content)
        load_file.close()

        #Загружаем информацию о NPC
        load_file = open('save_npc.txt', 'r')
        while line != '':
            sum = load_file.readline()
            sum = int(sum.rstrip('\n'))
            npcs = [sum]
            if not sum:
                for i in range(sum+1):
                    type = load_file.readline()
                    type = type.rstrlip('\n')
                    npcs = npcs.append(type)
                    name = load_file.readline()
                    name = name.rstrip('\n')
                    npcs = npcs.append(name)
                    description = load_file.readline()
                    description = description.rstrip('\n')
                    npcs = npcs.append(description)
                    reaction = load_file.readline()
                    reaction = int(reaction.rstrip('\n'))
                    npcs = npcs.append(reaction)
                    strenght = load_file.readline()
                    strenght = int(strenght.rstrip('\n'))
                    npcs = npcs.append(strenght)
                    dexterity = load_file.readline()
                    dexterity = int(dexterity.rstrip('\n'))
                    npcs = npcs.append(dexterity)
                    hp = load_file.readline()
                    hp = int(hp.rstrip('\n'))
                    npcs = npcs.append(hp)
                    content = load_file.readline()
                    content = content.rstrip('\n')
                    npcs = npcs.append(content)
                    content_num = load_file.readline()
                    content_num = int(content_num.rstrip('\n'))
                    npcs = npcs.append(content)
        load_file.close()
        return(hero, location, boxes, npcs)
    elif choice == 4:
        sys.exit()
