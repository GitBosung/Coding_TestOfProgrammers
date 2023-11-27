def solution(bandage, health, attacks):
    bandaging_time, sec_heal, plus_heal = bandage
    time = 0
    healing_time = 0
    attack_time = [k[0] for k in attacks]
    damage = [k[1] for k in attacks][::-1]
    maxHP = health
    
    
    while health > 0:
        if len(damage) <= 0:
            break;
        if time in attack_time:
            health -= damage.pop()
            healing_time = 0
        else:
            if health < maxHP:
                health += sec_heal
                if health > maxHP:
                    health = maxHP
                healing_time += 1
                if(health < maxHP and (healing_time == bandaging_time)):
                    health += plus_heal
                    if health > maxHP:
                        health = maxHP
                    healing_time = 0
            else:
                healing_time += 1
        time += 1
    
    if health > 0:
        return health
    else:
        return -1
            
        