var perStudentPetCount = [0,2,1,1,1,1,0,2,1,0,1,1,3,0]

//this is a comment in swift

var numberOfStudents = perStudentPetCount.count //count function let you know how many item in the array

print(perStudentPetCount[5])//print function like in python make an output of the value in the parameter

print(numberOfStudents)

var sum = 0
//for loop let you reach all item in the array
for studentPetCount in perStudentPetCount{
    sum += studentPetCount //the sum of all student pets
}

print(sum)
//the average of pets is sum / numberOfStudents
print(sum / numberOfStudents)