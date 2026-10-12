class ElegiblityForMarriage:
    def Elegible(self,gender, age):
        if gender == "male" and age >= 21:
            result = "ELIGIBLE"
        elif gender == "female" and age >= 18:
            result = "ELIGIBLE"
        else:
            result = "NOT ELIGIBLE"
        return result