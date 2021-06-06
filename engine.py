from experta import *

class Age(Fact):
    pass
class Height(Fact):
    pass
class Weight(Fact):
    pass
class Gender(Fact):
    pass
class Calories(Fact):
    value = Field(float, default=0.0)
class Competing(Fact):
    pass
class Intensity(Fact):
    pass
class BMI(Fact):
    pass
class DietPlan(Fact):
    pass
class setOption(Fact):
    pass
class Option(Fact):
    foodSet = Field(str, default="")
    option = Field(str, default="")
    calories = Field(str, default="")
class Set(Fact):
    setCategory = Field(str, default="")
    setFoods = Field(list, default=[])
    setCalories = Field(str, default="")
class Ask(Fact):
    pass

class SADO(KnowledgeEngine):


    @DefFacts()
    def sado_rules(self):
            
        ''' set facts for all food set '''
        ''' terbalik sebab experta baca dari bawah dulu? '''
        yield Option(foodSet="casual",option="C",calories=">=2500")  # maybe tak perlu simpan calories
        yield Option(foodSet="casual",option="B",calories=">=1500 & <2500")
        yield Option(foodSet="casual",option="A",calories="<1500") 
            
        yield Option(foodSet="light",option="F",calories=">=3500 & <4500")
        yield Option(foodSet="light",option="E",calories=">=2500 & <3500")
        yield Option(foodSet="light",option="D",calories="<2500")
            
        yield Option(foodSet="moderate",option="I",calories=">=3500")
        yield Option(foodSet="moderate",option="H",calories=">=2500 & <3500")
        yield Option(foodSet="moderate",option="G",calories="<2500")
            
        yield Option(foodSet="intensive",option="L",calories=">=4500")
        yield Option(foodSet="intensive",option="K",calories=">=3500 & <4500")
        yield Option(foodSet="intensive",option="J",calories="<3500")
            
        yield Set(setCategory="A",setFoods=["Nasi Lemak","Nasi Ayam Bakar","Nasi Hailam"],
                setCalories="<1500")
        yield Set(setCategory="B",setFoods=["Roti Telur","Nasi Arab Mandy","Mee Goreng Mamak"],
                setCalories=">=1500 & <2500")
        yield Set(setCategory="C",setFoods=["Nasi Kerabu + Roti Canai","Nasi Kandar","Chicken Chop"],
                setCalories=">=2500")
            
        yield Set(setCategory="D",setFoods=["Nasi Lemak","Nasi Ayam Bakar","Bihun Tom Yam"],
                setCalories="<2500")
        yield Set(setCategory="E",setFoods=["Roti Telur","Nasi Briyani","Spaghetti"],
                setCalories=">=2500 & <3500")
        yield Set(setCategory="F",setFoods=["Kuey Teow Goreng + Roti Telur","Nasi Kandar","Nasi Goreng Mamak"],
                setCalories=">=3500 & <4500")
            
        yield Set(setCategory="G",setFoods=["Nasi Lemak + Roti Telur","Nasi Ayam Bakar","Pizza"],
                setCalories="<2500")
        yield Set(setCategory="H",setFoods=["Nasi Kerabu + Roti Canai","Nasi Goreng Ayam + Laksa","Nasi Goreng Telur"],
                setCalories=">=2500 & <3500")
        yield Set(setCategory="I",setFoods=["Kuey Teow Goreng + Nasi Lemak + Roti Telur","Nasi Arab Mandy + Bihun Sup",
                "Spaghetti + Chicken Chop + Bihum Tom Yam"],setCalories=">=3500")
            
        yield Set(setCategory="J",setFoods=["Kuey Teow Goreng + Nasi Lemak + Cereal",
                "Nasi Kandar + Nasi Ayam Goreng + Bihun Sup","Bihum Tom Yam"],setCalories="<3500")
        yield Set(setCategory="K",setFoods=["Roti Canai + Nasi Kerabu + Cereal",
                "Nasi Briyani + Nasi Ayam Bakar + Laksa","Mee Goreng Mamak + Nasi Goreng Telur + Pizza"],
                setCalories=">=3500 & <4500")
        yield Set(setCategory="L",setFoods=["Roti Telur + Roti Canai + Kuey Teow Goreng + Cereal",
                "Nasi Kandar + Nasi Goreng Ayam + Bihun Sup","Nasi Goreng Pattaya + Mee Goreng Mamak + Chicken Chop"],
                setCalories=">=4500")
        
    @Rule()
    def startup(self):
        ''' input age, height, weight and gender for calories and bmi '''
        print("Welcome to SADO system")
        # questionAge = "Please enter your age: "
        # resAge = input(questionAge).lower()
        # questionHeight = "Please enter your height (in cm): "
        # resHeight = input(questionHeight).lower()
        # questionWeight = "Please enter your weight (in kg): "
        # resWeight = input(questionWeight).lower()
        # questionGender = "Please enter your gender: "
        # resGender = input(questionGender).lower()
        # self.declare(Age(resAge))
        # self.declare(Height(resHeight))
        # self.declare(Weight(resWeight))
        # self.declare(Gender(resGender))
            
    @Rule(AS.f1 << Gender(MATCH.g),
        AS.f2 << Age(MATCH.a),
        AS.f3 << Height(MATCH.h),
        AS.f4 << Weight(MATCH.w))
    def gender(self, g, a, h, w):
        ''' if male/female, count calories with formula for each gender, then ask if competing '''
        if(g == "male"):
            caloriesFloat = float((10*float(w))+(6.25*float(h))-(5*float(a))+5)
            self.declare(Calories(value = caloriesFloat))
            print("You are a " + g)
        elif(g =="female"):
            caloriesFloat = float((10*float(w))+(6.25*float(h))-(5*float(a))+161)
            self.declare(Calories(value = caloriesFloat))
            print("You are a " + g)
        else:
            print("Invalid gender lul")
        self.declare(Ask("competition-participation")) # todo - sepatutnya takde if else dalam function, buat rules baru
                
    @Rule(AS.f1 << Ask("competition-participation"))
    def if_competing(self, f1):
        ''' determine if competing or not '''
        # resCompeting = input("Are you participating in a competition? [y/n] : ").lower()
        # self.declare(Competing(resCompeting))
        self.retract(f1)
        if(Competing(MATCH.c) == 'y'):
            print("You are competing!")
        elif(Competing(MATCH.c) == 'n'):
            print("You are not competing!")
                
    ''' Rule Section - Determine if competition or not '''
                
    @Rule(AS.f1 << Competing('n'))
    def not_competing(self, f1):
        ''' if not competing, recommend casual planning '''
        self.declare(DietPlan("casual"))
            
    @Rule(AS.f1 << Competing('y'),
        AS.f2 << Height(MATCH.h),
        AS.f3 << Weight(MATCH.w))
    def is_competing(self, h, w):
        # print("How intense are your training?")
        # resIntensity = input("Choose one of the options [low/moderate/high]: ").lower()
        heightInM = int(h)/100
        bmi = int(w)/pow(heightInM,2)
        # self.declare(Intensity(resIntensity))
        # print("You are working out at a " + resIntensity + " intensity")
        if(bmi < 18.5):
            self.declare(BMI("underweight"))
            print("You are underweight")
        elif(bmi >= 18.5 and bmi < 25.0):
            self.declare(BMI("normal"))
            print("You are normal")
        elif(bmi >= 25.0):
            self.declare(BMI("overweight")) 
            print("You are fat lol")# ok you know what, maybe in some condition ada if dalam rule
            
    ''' Rules Section - Determine diet plan for each groups of rule if in competition '''
        
    # low intensity
        
    @Rule(AS.f1 << Intensity("low"),
        OR(
            BMI("normal"),
            BMI("overweight")
            )
        )
    def low_normal_overweight(self):
        self.declare(DietPlan("light"))
            
    @Rule(AS.f1 << Intensity("low"),
        BMI("underweight"))
    def low_underweight(self):
        self.declare(DietPlan("moderate"))
            
        
    # moderate intensity
        
    @Rule(AS.f1 << Intensity("moderate"))
    def moderate_normal(self):
        self.declare(DietPlan("moderate"))
            
    # high intensity
            
    @Rule(AS.f1 << Intensity("high"),
        BMI("overweight"))
    def high_overweight(self):
        self.declare(DietPlan("moderate"))
            
    @Rule(AS.f1 << Intensity("high"),
        OR(
            BMI("normal"),
            BMI("underweight")
            )
        )
    def high_normal_underweight(self):
        self.declare(DietPlan("intensive"))
            
            
    ''' Rules Section - Display Diet Plans '''
        
    @Rule(DietPlan(MATCH.f),
        salience=2)
    def display_assistance(self, f):
        print("For a " + f + " diet plan, these are the options")
        
    @Rule(AS.f1 << DietPlan(MATCH.f),
        Option(foodSet = MATCH.f,
                option = MATCH.o,
                calories = MATCH.c),
        salience=1)
    def display_moderate_plans(self, o, c):
        print(o + "(" + c + "kcal)")
            
            
    ''' Rules Section - Set option based on calories needed '''
        
    @Rule(AS.f1 << DietPlan("casual"),
        AS.f2 << Calories(value=MATCH.cc),
        Option(foodSet = "casual",
                option = MATCH.o,
                calories = MATCH.c))
    def set_calorie_range_casual(self, cc):
        if (cc < 1500.0):
            self.declare(setOption("A"))
        elif (cc >= 1500.0 and cc < 2500.0):
            self.declare(setOption("B"))
        elif (cc >=2500.0):
            self.declare(setOption("C"))
                
    @Rule(AS.f1 << DietPlan("light"),
        AS.f2 << Calories(value=MATCH.cc),
        Option(foodSet = "light",
                option = MATCH.o,
                calories = MATCH.c))
    def set_calorie_range_light(self, cc):
        if (cc < 1500.0):
            self.declare(setOption("D"))
        elif (cc >= 1500.0 and cc < 2500.0):
            self.declare(setOption("E"))
        elif (cc >= 2500.0):
            self.declare(setOption("F"))
        
    @Rule(AS.f1 << DietPlan("moderate"),
        AS.f2 << Calories(value=MATCH.cc),
        Option(foodSet = "moderate",
                option = MATCH.o,
                calories = MATCH.c))
    def set_calorie_range_moderate(self, cc):
        if (cc < 2500.0):
            self.declare(setOption("G"))
        elif (cc >= 2500.0 and cc < 3500.0):
            self.declare(setOption("H"))
        elif (cc >= 3500.0):
            self.declare(setOption("I"))
                
    @Rule(AS.f1 << DietPlan("intensive"),
        AS.f2 << Calories(value=MATCH.cc),
        Option(foodSet = "intensive",
                option = MATCH.o,
                calories = MATCH.c))
    def set_calorie_range_intensive(self, cc):
        if (cc < 3500.0):
            self.declare(setOption("G"))
        elif (cc >= 3500.0 and cc < 4500.0):
            self.declare(setOption("H"))
        elif (cc >= 4500.0):
            self.declare(setOption("I"))
            
    ''' Rules Section - Show options for each diet plan '''
        
    # ? - Kalau underweight, bukan kemungkinan untuk calorie needs rendah tu tinggi? And susah nak masuk set lain
    #     kecuali yang calorie terendah
    @Rule(setOption(MATCH.o),
        Calories(value=MATCH.cc),
        Set(setCategory = MATCH.o,
            setFoods = MATCH.f,
            setCalories = MATCH.c))
    
    def display_foods(self, o, cc, f, c):
        self.title = "Considering you need " + str(cc) + "kcal, you are recommended to eat these in set " + o + ":"
        s = ', '
        self.foods = s.join(f)
        self.recommendation = "All foods in this set contains calories in the " + c + " range."
        print("Considering you need " , cc , " kcal, you are recommended eat these in set " + o +": ")
        for z in f:
            print(z + "\t", end=" ")
        print()
        print("All foods in this set contains calories in the " + c + " range.")


# def main():
#     sado = SADO()
#     sado.reset()
#     sado.declare(Age('21'), Height('168'), Weight('55'), Gender('male'), Competing('y'), Intensity('low'))
#     sado.run()

# if __name__ == "__main__":
#     main()