questions = [
    [
        "The language spoken by the people by India is ?", "Hindi", "French", "JavaScript",
        "Php",  1
    ],
    [
        "The World Largest desert is ?", "Thar", "Sahara", "Kalahari",
        "Sonoran", 2
    ],
    [
        "Mount Everest is located in ?", "USA", "Nepal", "Tibet",
        "China",  2
    ],
    [
        "The device used for measuring altitudes is ?", "altimeter", "ammeter", "audiometer",
        "galvanometer", 1
    ],
    [
        "The Gate way of India is ?", "Chennai", "Mumbai", "Kolkata",
        "New Delhi",  2
    ],
    [
        "Country that was called as Land of Rising Sun ?", "Russia", "Japan", "Korea",
        "Holland",  2
    ],
    [
        "Pink city in India is ?", "Mysore", "Karnataka", "Hyderabad",
        "Jaipur", 4
    ],
    [
        "The state which has desert in India is ?", "Rajasthan", "Punjab", "UP",
        "MP", 1
    ],
    [
        "The largest river in India is ?", "Yamuna", "Kaveri", "Ganga",
        "Bramaputra", 3
    ],
    [
        "One People, One State, One leader was the policy of ?", "Stalin", "Hitler", "JavaScript",
        "Lenin", 2
    ],
    [
        "The hottest planet in the solar system", "Earth", "Venus", "Mars",
        "Jupiter", 2
    ],
    [
        "The river that flows through Delhi is ?", "Ganges", "Indus", "Yamuna",
        "Narmada", 3
    ],
    [
        "Which gas is used for the preparation of Soda water ?", "Oxygen", "Carbon Dioxide", "Ammonia",
        "Hydrogen",  2
    ],
    [
        "Where electricity supply was first introduced in India?", "Darjeeling", "Chennai", "Kolkata",
        "Mumbai", 1
    ],
    [
        "First University in India was founded at?", "Mumbai", "Chennai", "Calcutta",
        "Delhi", 3
    ],
]
money = 0
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000,
          80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
for i in range(0, 15):
    question = questions[i]
    print(f"Quesion for Rs{levels[i]} is ")
    print(question[0])
    print(f"1.{question[1]}          2.{question[2]}")
    print(f"3.{question[3]}          4.{question[4]}")
    reply = int(input("Enter your Answer(0-4) or 0 to quit "))
    if reply == question[-1]:
        print(f"Correct Answer you won {levels[i]}\n\n")
        if i == 4:
            money = levels[i]
        elif i == 9:
            money = levels[i]
        elif i == 14:
            money = levels[i]

    elif reply == 4:
        print(f"You quit.You won Rs{levels[i]}. Thx for playing")
        break
    else:
        print(
            f"Wrong Answer!! Correct Ans is {question[-1]}. You won Rs{money}. Thx for playing  ")
        break
