class my_family:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def intro(self):
        return "Hi!, I'm {} my age is {} i'm a {}".format(self.name, self.age, self.gender)


class father(my_family):
    name = "Niranjan Behera"
    age = "52"
    gender = "male"


class mother(my_family):
    name = "Bishnupriya Behera"
    age = "48"
    gender = "female"


class sister(my_family):
    name = "Priya Payal Behera"
    age = "21"
    gender = "female"


class brother(my_family):
    name = "Sai Ranjan Behera"
    age = "17"
    gender = "male"


my_father = father("Niranjan Behera", 52, "male")
print(my_father.intro())

my_mother = mother("Bishnupriya Behera", 46, "female")
print(my_mother.intro())

my_sister = sister("Priya Payal Behera", 21, "female")
print(my_sister.intro())

my_brother = father("Sairanjan Behera", 17, "male")
print(my_brother.intro())