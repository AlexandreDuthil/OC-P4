class Player:
    def __init__(self, last_name, first_name, birthdate, sex, rating):
        self.last_name = last_name.upper()
        self.first_name = first_name.capitalize()
        self.birthdate = birthdate
        self.sex = sex
        self.rating = rating
        self.attributs = ["last_name", "first_name", "birthdate", "sex", "rating"]
        self.score = 0

    def __repr__(self):
        return """{} {}, {}, sexe : {}, classement : {}""".format(self.last_name, self.first_name, self.birthdate,
                                                                  self.sex, self.rating)
