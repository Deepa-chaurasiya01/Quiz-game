print("Hello, Welcom to !!!The Quiz Game!!!")
answer = input("Are you ready to play (yes/no):")
score = 0
total_q = 10

if answer.lower() == 'yes':
    print("Okay! then Let's play !!!The Quiz Game!!!  \n ")
    answer = input("1.The Pir Panjal range is located in which of the following states?  \n a. Arunachal Pradesh \n b. Jammu and Kashmir \n c. Punjab \n d. Uttarakhand\n")
    if answer.lower() == "b":
        score += 1
        print('correct')
    else:
        print("incorrect:- \n option b. The Pir Panjal ranges lie in the Inner Himalayan region, running from east southeast to west northwest across the states of Himachal Pradesh and Jammu and Kashmir in India as well as Pakistan Administered Kashmir in Pakistan, where the average elevation varies from 1,400 m to 4,100 m . \n ")

    answer = input("2. Which is the Land of the Rising Sun? \n a. China \n b.Taiwan \n c. Australia \n d.Japan \n")
    if answer.lower() == "d":
        score += 1
        print('correct')
    else:
        print("incorrect:- \n option d. Japan is the land of the sun rising \n ")

    answer = input("3.  Which is the most abundant metal in the Earth’s crust? \n a.Aluminium \n b.Nickel \n c.Iron \n d. Silicon \n")
    if answer.lower() == "a":
        score += 1
        print('correct')
    else:
        print("incorrect:- \n  option a. The most abundant element is Oxygen followed by Silicon. Both of these are non-metals. Silicon is followed by Aluminium which is most abundant metal. \n")

    answer = input("4. In which of the following ecosystems, the annual average rate of net plant production is highest? \n a.Temperate Grasslands \n b.Temperate Forests \n c. Savannah \n d.Swamps and Marshes \n")
    if answer.lower() == "d":
        score += 1
        print('correct')
    else:
        print("incorrect:- \n option d.  Thus tropical ecosystems, Swamps and Marshes, and Estuaries generally have highest net production.\n ")

    answer = input("5. In which of the following regions, maize is used as staple food? \n a. Western Europe \n b. Russia \n c. Middle Africa \n d. South-East Asia \n")
    if answer.lower() == "c":
        score += 1
        print('correct')
    else:
        print("incorrect:- \n option c. Maize or corn is a cereal crop that is grown widely throughout the world in a range of agroecological environments. The grains are rich in vitamins A, C and E, carbohydrates, and essential minerals, and contain 9% protein. They are also rich in dietary fiber and calories which are a good source of energy. (Staple food is the name for a food that can be stored easily, and eaten throughout the year.) It’s an important staple food for more than 1.2 billion people in Middle Africa. \n")

    answer = input("6.  Carajás Mine is located in which of the following countries? \n a. Argentina \n b. Brazil \n c. Paraguay \n d. Mexico \n")
    if answer.lower() == "b":
        score += 1
        print('correct')
    else:
        print("incorrect:- \n option b.  The Carajás Mine is the largest iron ore mine in the world. It is located in the state of Pará in the Carajás Mountains of Northern Brazil. \n")

    answer = input("7.  . Four Corners Monument is located in which of the following countries? \n a. United States \n b. Canada \n c. China \n d. Mexico \n")
    if answer.lower() == "a":
        score += 1
        print('correct')
    else:
        print("incorrect:- \n option a.Four Corners Monument is the quadripoint meeting four states of US viz. Arizona, Colorado, New Mexico and Utah. It is located in the South-western United States and is the only point shared by four states in America. It is also a boundary between two semi-autonomous Native American governments viz. The Navajo Nation and Ute Mountain. \n")

    answer = input("8.  Majid Gyre is a feature of which of the following Oceans? \n a. Pacific Ocean \n b. Indian Ocean \n c. Atlantic Oceanc \n d. Arctic Ocean \n")
    if answer.lower() == "b":
        score += 1
        print('correct')
    else:
        print("incorrect:- \n option b.  The Indian Ocean consists of one gyre, the Indian Ocean (Majid) Gyre, which exists mostly in the Southern Hemisphere. It is named after Ahmad Bin Majid, the 15th-century Arab mariner. \n" )

    answer = input("9.The Coriolis force is maximum at __? \n a. Poles \n b. Equator \n c. Tropics \n d. Mountain peaks \n")
    if answer.lower() == "a":
        score += 1
        print('correct')
    else:
        print("incorrect:- \n option a. The Coriolis effect influences the paths of moving objects on Earth and is caused by Earth s rotation. Because Earth s surface rotates at different velocities at different latitudes, objects in motion tend to veer to the right in the Northern Hemisphere and to the left in the Southern Hemisphere. The Coriolis effect is nonexistent at the equator but increases with latitude, reaching a maximum at the poles. \n ")

    answer = input("10.   Who among the following gave the theory of continental drift? \n a. Arthur Holmes \n b. Alfred Wegener \n c. Jean-Baptiste Élie de Beaumont \n d. Harry Hess \n")
    if answer.lower() == "b":
        score += 1
        print('correct')
    else:
        print("incorrect:- \n option b.  According to the theory of plate tectonics, the outermost portion of Earth is composed of a patchwork of thin, rigid lithospheric plates that move horizontally with respect to one another. The idea began as a hypothesis called continental drift proposed by Alfred Wegener at the start of the 20th century. He suggested that about 200 million years ago, all the continents were combined into one large continent (Pangaea) surrounded by a single large ocean (Panthalassa). Harry Hess advanced the idea of sea floor spreading. \n ")

print("Thank you for playing, you got ", score, "question correct.")
mark = (score/total_q)*100
print("Mark: ", str(mark)+'%')
print("see you again!!")
