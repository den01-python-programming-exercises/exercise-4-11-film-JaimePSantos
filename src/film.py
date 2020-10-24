class Film:
  name = ""
  age_rating = 0

  def __init__(self,name,ageRating):
    self.name = name
    self.age_rating = ageRating
  
  def name(self):
    return self.name
  
  def age_rating(self):
    return self.age_rating