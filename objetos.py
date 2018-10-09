#fabricar un robotsillo que salude 
class Robot:
    message = 'Hello'
    def say_Hello(self,text = ''):
        print(self.message, text)

class Robot_v2(Robot):
    def walk(self):
        print('I can walk !!!!!')

my_first_robot = Robot ()
my_second_robot = Robot()
my_third_robot = Robot_v2()
my_first_robot.message = 'Hola'
#my_first_robot.say_Hello('Pachamama!!!')
my_first_robot.say_Hello()
my_second_robot.say_Hello()
my_third_robot.say_Hello('Everybody! im version two')
my_third_robot.walk()
