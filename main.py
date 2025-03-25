import matplotlib.pyplot as plt


print("COMPARE CRICKETS SCORES GRAPHICALLY !\n")

teamAName = input("Enter the name of the first team : ")
teamBName = input("Enter the name of the second team : ")


wickets = [1,2,3,4,5,6,7,8,9, 10]

def inputFunction(teamName):
    team = []
    for i in range(10):
        while True :
            wicket_runs = int(input(f"Enter the runs of {teamName} after falling {i+1} wicket : "))

            if (i==0):
                team.append(wicket_runs)
                break
            elif (wicket_runs<team[i-1]):
                print("Entered score is less than the previous score !")
            else:
                team.append(wicket_runs)
                break
    
    return team

teamA = inputFunction(teamAName)
print("\n\n")
teamB = inputFunction(teamBName)

print(f"\n\nBlue graph - {teamAName}\nRed Graph - {teamBName}")

plt.plot(wickets, teamA)
plt.plot(wickets, teamB)


plt.xlabel("Wickets")
plt.ylabel("Runs")
plt.title("Team Runs Comparision")


plt.show()