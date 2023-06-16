class Me:
    def __init__(self, name, surname, dob, age, gender, education, origin_address, current_address, religion, mother, father, Sibling):
        self.name ="Anirudha"
        self.surname = "Behera\n"
        self.dob = "23rd Jan 1997\n"
        self.age = "26\n"
        self.gender = "Male\n"
        self.education = "MSc in EE, IIT, Chicago"
        self.origin_address = "At/Po: Kandhanayagarh\n Street: Nakshetrapur Sahi\n Dist: Nayagarh\n State: " \
                              "Odisha-752024\n India "
        self.current_address = "At: 3144 S Wells Street\n Apt: 1R Chicago\n Illinois USA\n"
        self.religion = "Hindu\n"
        self.mother = "Bishnupriya Behera\n"
        self.father = "Niranjan Behera\n"
        self.sibling = "Sister: Priyapayal Behera\n Brother: Sairanjan Behera"


my_intro = Me("Anirudha", "Behera", "23rd Jan 1997", "26", "Male", "MSc in EE, IIT, Chicago", "At/Po: Kandhanayagarh\n, Street: Nakshetrapur Sahi\n, Dist: Nayagarh\n, State: " \
                              "Odisha-752024\n, India ", "At: 3144 S Wells Street\n, Apt: 1R, Chicago\n, Illinois, USA", "Hindu", "Bishnupriya Behera", "Niranjan Behera", "Sister: Priyapayal Behera\n, Brother: Sairanjan Behera")
print(my_intro.name,
      my_intro.surname, my_intro.dob, my_intro.age, my_intro.gender, my_intro.education,
      my_intro.origin_address, my_intro.current_address,
      my_intro.religion, my_intro.mother, my_intro.father,
      my_intro.sibling)

