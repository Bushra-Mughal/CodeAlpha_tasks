# Create a class to take marks and calculate average of each student:
class marks_tracker:

    def __init__(self,student):
        exit=False
        self.marks=[]
        print(f"----Marks of {student}----")
        while exit!=True:
            subject=input("\tEnter subject: ")
            mark=eval(input(f"\tEnter marks of {subject}: "))
            self.marks.append(mark)
            op=input("\tWant to continue? (y | n) ")
            if op=='n' or op=='N':
                exit=True
        # save student's data to a file:
        with open("Student_data.txt","a") as f:
            f.write(f"Student: {student} , Marks: {self.marks} \n")

    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        avg=sum/len(self.marks)
        print("------Average------")
        print(f"\tAverage of marks is: {avg}")

# creating object:
def main():
    exit=False
    while exit!=True:
        name=input("Enter student's name: ")
        st=marks_tracker(name)
        st.average()
        op=input("Want to continue? (y | n) ")
        if op=='n' or op=='N':
            exit=True

# Execution guard:
if __name__=='__main__':
    main()            