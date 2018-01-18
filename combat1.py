
def deadcheck(character,healmodi):
    '''simple check to see if a character is dead
    @ para 1 dict//character
    @ para 2 int//healthmodi
    @ output bool
    '''


    if healmodi >= character['HP']:
        return True

    else:
        return False


hero={'HP':40,'MP':20,'Hit':80,'Crit':5,'Slash':10,'Cast':15,'Castcost':10}

villan={'HP':25,'MP':30,'Hit':80,'Crit':20,'Slash':5,'Cast':10,'Castcost':10}



def fight(player,ai):

    combat=True
    phealthmodi=0
    pmanamodi=0
    pccost=hero['Castcost']

    ahealthmodi=0
    amanamodi=0
    accost=villan['Castcost']

    while combat==True:

        #player turn================
        playerturn=True

        while playerturn==True:

            health=player['HP']-phealthmodi
            mana=player['MP'] - pmanamodi
            vhealth=villan['HP'] - ahealthmodi
            vmana=villan['MP'] - amanamodi

            attack=input('What attack do you chose? 1) Slash, 2) Cast')

            if attack == '1' or attack == 'Slash':

                hit=randint(0,100)

                if hit <= player['Hit']:

                    x=randint(0,100)
                    if x <=player['Crit']:
                        ahealthmodi+=player['Slash']*2
                        print('Your attack did',player['Slash']*2,'damage with a crit!')

                        playerturn=False

                    else:
                        ahealthmodi+=player['Slash']
                        print('Your attack did ',player['Slash'],'damage.')

                        playerturn=False

                else:
                    print('Your attack missed')

                    playerturn=False

            elif attack == '2' or attack == 'Cast':
                if mana < pccost:
                    print('Not enough mana for this')

                elif mana >= pccost:
                    pmanamodi+=pccost
                    ahealthmodi+=hero['Cast']
                    print('Your spell hits!')
                    playerturn=False



            elif attack == 'Stats' or attack == 'stats':
                #print stats for player and villan. hp//mp for both. cast cost and hit for player
                print('Current stats are')
                print('Player')
                print('HP',health,'MP',mana,'Castingcost',player['Castcost'],'Melee Hit',player['Hit'])


                print('Villan')
                print('HP',vhealth,'MP',vmana)


            else:
                print('Not a vaild imput. Use attack name with capital or digit')




        #dead check=================
            if deadcheck(hero,phealthmodi) == True :
                combat = False
                print('You died. Game over')
                break


            elif deadcheck(villan,ahealthmodi) == True:
                combat = False
                print('You Win!')
                break


            else:
                print('The fight rages on!')

        #ai turn=====================
        #randomly pick a attack and use it


            if villan['MP']-amanamodi < accost:
                random = 1

            else:

                random = randint(1,2)

            if random == 1:
                hit=randint(0,100)

                if hit >=villan['Hit']:
                    crit=randint(0,100)
                    if crit <= villan['Crit']:
                        phealthmodi+= villan['Slash']*2
                        print('The Villan crit you for',villan['Slash']*2,'!!')

                    else:
                        phealthmodi+= villan['Slash']
                        print('The Villan slices you for',villan['Slash'])

                else:
                    print('The Villan misses his melee attack!')

            elif random == 2:
                amanamodi+=accost
                phealthmodi+=villan['Cast']
                print('The Villan blasts you with there spell',villan['Cast'])


        #dead check===========
            if deadcheck(hero,phealthmodi) == True :
                combat = False
                print('You died. Game over')
                break

            elif deadcheck(villan,ahealthmodi) == True:
                combat = False
                print('You Win!')
                break

            else:
                print('The fight rages on!')

