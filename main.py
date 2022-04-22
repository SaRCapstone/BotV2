import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.base import runTouchApp
from imageai.Detection import ObjectDetection
import os


#Inital screen that is seen once the app is started.
class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Creating the float layout for the screen and adding it.
        fl = FloatLayout()
        self.add_widget(fl)

        #The top two labels of the first screen.
        fl.add_widget(Label(text='Search and Assist', pos=(0, 250)))
        fl.add_widget(Label(text='Pick what color to choose', pos=(0, 190)))

        #Array of rubik cube colors.
        colors = ['Person', 'Bottle', 'Banana', 'Apple', 'Orange', 'Car']

        #Dropdown menu beginning
        #Creating the dropdown object
        dropdown = DropDown()
        for color in colors:
            #Creating the buttons to add to dropdown.
            fl.btn = Button(text='%s' % color, size_hint_y=None, height=44)

            #Binding to the button.
            fl.btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            fl.btn.bind(on_press=self.my_method)

            #Adding button to dropdown.
            dropdown.add_widget(fl.btn)


        #Making the main button for the dropdown menu.
        self.mainbutton = Button(text='Find', size_hint=(None, None), height=50, width=400, pos_hint={'x':.24, 'y':.7})

        #Binding what happens when pressing the mainbutton
        self.mainbutton.bind(on_release=dropdown.open)

        #Changing the mainbutton to have the text of the color chosen.
        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

        fl.add_widget(self.mainbutton)
        #Finished dropdown menu

        #Inital image of a scrambled rubik cube
        #self.rubik = Image(source='rubix.png', size_hint=(None, None), height=150, width=150,
        #                   pos_hint={'x': .39, 'y': .4})

        #Adding the image to the layout
        #fl.add_widget(self.rubik)

        #The search button being added to the screen.
        fl.search = Button(text='Begin Search', size_hint=(None, None), height=50, width=200, pos_hint={'x': .353, 'y': .2})
        fl.search.bind(on_press=self.searching)
        fl.add_widget(fl.search)

    #Method to handle the search button
    def searching(self, instance):
        #Prints the color of the cube being searched for.
        print("Beginning search for ", self.mainbutton.text)

        # execution_path = os.getcwd()
        #
        # detector = ObjectDetection()
        # detector.setModelTypeAsYOLOv3()
        # detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
        # detector.loadModel()
        # # detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"), minimum_percentage_probability=30)
        # custom = detector.CustomObjects(person=True)
        # detections = detector.detectCustomObjectsFromImage(custom_objects=custom,
        #                                                    input_image=os.path.join(execution_path, "image.jpg"),
        #                                                    output_image_path=os.path.join(execution_path,
        #                                                                                   "imagenew.jpg"),
        #                                                    minimum_percentage_probability=30)
        #
        # for eachObject in detections:
        #     print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
        #     print("--------------------------------")

        #Swaps screen once the color is chosen.
        sm.current = "two"

    #Method that changes the image to the selected color side of the rubix cube.
    def my_method(self, instance):
        #Removing the original image to add the new image.
        #self.remove_widget(self.rubik)

        #Adding the new image based off of the selected color.
        if instance.text == "White":
            self.rubik = Image(source='whiterubik.png', size_hint=(None, None), height=150, width=150, pos_hint={'x':.39, 'y':.4})

            self.add_widget(self.rubik)
        elif instance.text == "Green":
            self.rubik = Image(source='greenrubik.png', size_hint=(None, None), height=150, width=150, pos_hint={'x':.39, 'y':.4})

            self.add_widget(self.rubik)
        elif instance.text == "Red":
            self.rubik = Image(source='redrubik.png', size_hint=(None, None), height=150, width=150, pos_hint={'x':.39, 'y':.4})

            self.add_widget(self.rubik)
        elif instance.text == "Yellow":
            self.rubik = Image(source='yellowrubik.png', size_hint=(None, None), height=150, width=150,
                        pos_hint={'x': .39, 'y': .4})

            self.add_widget(self.rubik)
        elif instance.text == "Blue":
            self.rubik = Image(source='bluerubik.png', size_hint=(None, None), height=150, width=150,
                        pos_hint={'x': .39, 'y': .4})

            self.add_widget(self.rubik)
        elif instance.text == "Orange":
            self.rubik = Image(source='orangerubik.png', size_hint=(None, None), height=150, width=150,
                        pos_hint={'x': .39, 'y': .4})

            self.add_widget(self.rubik)


#Second screen that is seen once the search button is pressed.  Just a layout screen so far,
#the buttons on the screen have no functionality yet.
class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Creating the float layout that everything goes on.
        floa = FloatLayout()

        #Adding the layout to the screen
        self.add_widget(floa)

        #Adding the various buttons and labels to the screen.
        floa.add_widget(Label(text='Search and Assist', pos_hint={'y':.45}))
        floa.add_widget(Label(text='Camera View', pos_hint={'y':.39}))
        floa.add_widget(Button(text='Camera Placeholder', size_hint=(.35,.2), pos_hint={'x':.32, 'y':.67}))
        floa.add_widget(Label(text='Map', pos_hint={'y':.14}))
        floa.add_widget(Button(text='Map Placeholder', size_hint=(.35, .2), pos_hint={'x':.32, 'y':.42}))
        floa.add_widget(Button(text='Time Running', size_hint=(.25, .1), pos_hint={'x':.37, 'y':.27}))
        floa.add_widget(Button(text='Speed', size_hint=(.175, .1), pos_hint={'x':.23, 'y':.14}))
        floa.add_widget(Button(text='Battery Status', size_hint=(.2,.1), pos_hint={'x':.53, 'y':.14}))
        floa.add_widget(Button(text='STOP', size_hint=(.25,.1), pos_hint={'x':.37, 'y':.01}))


#Creating the ScreenManager object
sm = ScreenManager()

#Adding the two screens to the ScreenManager
sm.add_widget(ScreenOne(name='one'))
sm.add_widget(ScreenTwo(name='two'))

#Upon starting the app, screen "one" is the current screen.
sm.current = "one"


#Making the app.
class Hello(App):
    def build(self):
        return sm




if __name__ == '__main__':
    Hello().run()
