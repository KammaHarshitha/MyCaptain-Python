#project 1:Basic school administration tool
import csv

def write_into_csv(info_list):
    with open('sttudent_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact Number", "Email ID"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    sttudent_num = 1

    while(condition):
        sttudent_info=input("Enter sttudent information for sttudent #{} in the following format (Name Age Contact_Number Email_ID):")

        # split
        sttudent_info_list = sttudent_info.split(' ')

                                                                                                                                    
        print("\nThe entered information is -\nName: {}\nAge: {}\nContact_number: {}\nE-mail ID: {}"
              .format(sttudent_info_list[0], sttudent_info_list[1], sttudent_info_list[2], sttudent_info_list[3]))


        choice_check = input("Is the entered information correct? (yes/no): ")


        if choice_check == "yes":
           write_into_csv(sttudent_info_list)


           condition_check = input("Enter (yes/no) if you want to enter information for another sttudent: ")
           if condition_check == "yes":
               condition = True
               sttudent_num = sttudent_num + 1
           elif condition_check == "no":
                condition = False
        elif choice_check == "no":
            print("\nPlease re-enter the values!")
