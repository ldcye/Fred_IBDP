# math = 40%
# science = 35%
# english = 25%

math = input("Enter math score: ")
science = input("Enter science score: ")
english = input("Enter english score: ")

final_score = (int(math) * 0.4) + (int(science) * 0.35) + (int(english) * 0.25)

if final_score >= 60:
    sucess = "pass"
else:
    sucess = "fail"

print("Student\'s total weighted score is: " , str(final_score) , sucess+"\n")

print("Student\'s"+ "total"+ "weighted"+ "score"+ "is:" + str(final_score)+ sucess+"\n")

print(" %s %s %s %s %s %.1f" % ("Student's" "total" "weighted" "score" "is: ", final_score, " ", sucess, "\n"))

print(f'{"Student's total weighted score is: "}, (final_score), {sucess}')