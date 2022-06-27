import os

os.system("cls")

def main(atk, enemy_atk, training_count):
    print("WELCOME TO THE GAME SIMULATOR PROGRAM")
    enemy_atk = 2
    atk = 1
    win_count = 0
    lose_count = 0
    training_count = 1
    
    while True:


        print("_"*25)
        print("Halo Choose Below")
        print("1.Fight")
        print("2.Training")
        print("3.Status")
        print("4.Quit")

        data = str(input("Choose (1/2/3/4): "))


        if data == "1":
            print("Enemy Appears")
            print("1.Fight")
            print("2.Run")

            if win_count > lose_count:
                enemy_atk += win_count
                
            
            data2 = str(input("Choose (1/2): "))
            
            if data2 == "1":

                if atk > enemy_atk:
                    print(f"My Power {atk} VS Enemy Power {enemy_atk}")
                    print("You Won!!!")
                    win_count += 1
                    continue
                elif atk == enemy_atk:
                    print(f"My Power {atk} VS Enemy Power {enemy_atk}")
                    print("not enough!!")
                    continue
                elif atk < enemy_atk:
                    print(f"My Power {atk} VS Enemy Power {enemy_atk}")
                    print("You Lose :(")
                    lose_count += 1
                    continue
            
            elif data2 == "2":
                continue
            
            else:
                continue




        elif data == "2":
            atk += training_count
            training_count += 1
            os.system("cls")

        elif data == "3":
            print(f"atk = {atk}")

        elif data == "4":
            print("Quitting The Program")
            print("-"*20,"100%","-"*20)
            break

        else:
            continue

main()
