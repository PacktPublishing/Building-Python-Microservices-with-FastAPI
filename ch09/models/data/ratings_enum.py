from enum import Enum

class FoodRatingScale(int, Enum):
    FIVE_STAR = 5
    FOUR_STAR = 4
    THREE_STAR = 3
    TWO_STAR = 2
    ONE_STAR = 1
    
class AmbianceRatingScale(int, Enum):
     STRONGLY_AGREE = 7
     AGREE = 6
     SOMEWHAT_AGREE = 5
     FINE = 4
     SOMEWHAT_DISAGREE = 3
     DISAGREE = 2
     STRONGLY_DISAGREE = 1
    
