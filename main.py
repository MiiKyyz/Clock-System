import kivy
import kivymd
from kivy.animation import Animation

from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
import TimerClock
from kivymd.uix.menu import MDDropdownMenu
import datetime
import pytz
import math

from platform import python_version







class MainLayout(Widget):

    StopWatchBool = False
    listNumbers = []
    StopWatchClock = [0,0,0,0]
    TimeZone = []
    TimeZ= []
    country = "Africa/Abidjan"
    OldText = ''

    FontTextTimerClock= 'MATURASC'
    FontTextWatchClock= 'LHANDW'
    FontTextTimeZone = 'FREESCPT'



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.listNumbers = TimerClock.TimerClockSystem.NumberList
        Clock.schedule_interval(self.StopWatch, 0.95)
        Clock.schedule_interval(self.StartTimer, 0.95)
        Clock.schedule_interval(self.RealTimeApp, 0.01)

        self.TextDisplayed = MDDropdownMenu()
        print(math.sqrt(25))
        #self.miky(None)

        #Clock.schedule_interval(self.miky, 0.0001)
    x = 0
    y = 0



    #time zone work
    def TimeZoneWorld(self, country):
        dr_now = datetime.datetime.now(tz=pytz.timezone(country))
        self.ids.TimeZoneLabel.markup = True
        self.ids.TimeZoneLabel.text = f"[font={self.FontTextTimeZone}]{dr_now}[/font]"
        self.ids.Label.markup = True
        self.ids.Label.text = f'[font={self.FontTextTimeZone}]Time in {self.country}[/font] :'


    def TimeZoneDisplay(self, Zone):



        menu_item = [{"text": f'{timezone}',
                      "viewclass": "OneLineListItem",
                      "on_release": lambda x=f"{timezone}": self.CloseMenu(x)}
                     for timezone in Zone]
        self.TextDisplayed.caller =self.ids.WorldZoneText
        self.TextDisplayed.items = menu_item
        self.TextDisplayed.width_mult= 4

        self.TextDisplayed.open()



    def CloseMenu(self, country):
        self.country = country
        self.ids.WorldZoneText.text = f"{country}"



    def RealTimeApp(self, instance):
        #Time zone Work
        self.TimeZoneWorld(self.country)



        if self.ids.WorldZoneText.text != self.OldText:
            self.OldText = self.ids.WorldZoneText.text
            self.new_time_zone = []
            self.TextDisplayed.dismiss()

            if self.ids.WorldZoneText.text:
                if self.ids.WorldZoneText.text in pytz.all_timezones:
                    pass
                else:

                    for tz in pytz.all_timezones:
                        if self.ids.WorldZoneText.text in tz or self.ids.WorldZoneText.text in tz.lower():
                            self.new_time_zone.append(tz)
                    self.TimeZoneDisplay(self.new_time_zone)





        #timer work
        if TimerClock.TimerBool is True:
            self.ids.img1.flip1 -= 1
            self.ids.StartTimerButton.text = "Stop"
            self.ids.DeleteTimerButton.disabled = True


            self.ids.LabelTimer.text = f'[font={self.FontTextTimerClock}]{self.listNumbers[0]}{self.listNumbers[1]}:{self.listNumbers[2]}{self.listNumbers[3]}:{self.listNumbers[4]}{self.listNumbers[5]}[/font]'

            if self.listNumbers[0] == 0 and self.listNumbers[1] == 0 and self.listNumbers[2] == 0 and self.listNumbers[3] == 0 and self.listNumbers[4] == 0 and self.listNumbers[5] == 0:
                TimerClock.TimerBool = False


        elif TimerClock.TimerBool is False:
            self.ids.StartTimerButton.text = "Start"
            self.ids.DeleteTimerButton.disabled = False
            self.ids.LabelTimer.text = f'[font={self.FontTextTimerClock}]{self.listNumbers[0]}{self.listNumbers[1]}:{self.listNumbers[2]}{self.listNumbers[3]}:{self.listNumbers[4]}{self.listNumbers[5]}[/font]'







    #timer clock


        if self.StopWatchBool is True:



            self.ids.img.flip += 1



            if self.StopWatchClock[3] == 6 and self.StopWatchClock[2] == 0 and self.StopWatchClock[1] == 0 and \
                    self.StopWatchClock[0] == 0:
                self.StopWatchClock = [0,0,0,0]
                self.StopWatchBool = False

            self.ids.StopWatchID.text = f'[font={self.FontTextWatchClock}]{self.StopWatchClock[3]}{self.StopWatchClock[2]}:{self.StopWatchClock[1]}{self.StopWatchClock[0]}[/font]'

    def Timer(self):
        TimerClock.TimerClockSystem().Timer()

    def StartTimer(self, instance):

        TimerClock.TimerClockSystem().Startimer()


    def TimerRemove(self):
        time_clock = TimerClock

        time_clock.TimerClockSystem().DeleteNumbers()

        self.ids.LabelTimer.text = f'[font={self.FontTextTimerClock}]{self.listNumbers[0]}{self.listNumbers[1]}:{self.listNumbers[2]}{self.listNumbers[3]}:{self.listNumbers[4]}{self.listNumbers[5]}[/font]'



    def TimerCall(self, Number):
        time_clock = TimerClock

        time_clock.TimerClockSystem().AddNumbers(Number)

        self.ids.LabelTimer.text = f'[font={self.FontTextTimerClock}]{self.listNumbers[0]}{self.listNumbers[1]}:{self.listNumbers[2]}{self.listNumbers[3]}:{self.listNumbers[4]}{self.listNumbers[5]}[/font]'

    #watch clock

    def StopWatchRing(self):

        if self.StopWatchBool is False:
            self.StopWatchBool = True


        elif self.StopWatchBool is True:
            self.StopWatchBool = False




    def StopWatch(self, instance):



        if self.StopWatchBool is False:
            self.ids.StopWatchID.text = f'[font={self.FontTextWatchClock}]{self.StopWatchClock[3]}{self.StopWatchClock[2]}:{self.StopWatchClock[1]}{self.StopWatchClock[0]}[/font]'

        elif self.StopWatchBool is True:





            #self.ids.StopWatchID.text = f'[font={self.FontTextWatchClock}]{self.StopWatchClock[3]}{self.StopWatchClock[2]}:{self.StopWatchClock[1]}{self.StopWatchClock[0]}[/font]'

            if self.StopWatchClock[2] == 9 and self.StopWatchClock[1] == 5 and self.StopWatchClock[0] == 9:
                self.StopWatchClock[2] = 0
                self.StopWatchClock[3] += 1
                self.StopWatchClock[0] = 0
                self.StopWatchClock[1] = 0

            elif self.StopWatchClock[1] == 5 and self.StopWatchClock[0] == 9:

                self.StopWatchClock[2] += 1
                self.StopWatchClock[0] =0
                self.StopWatchClock[1] =0

            else:
                if self.StopWatchClock[0] < 9:
                    self.StopWatchClock[0] += 1
                elif self.StopWatchClock[0] == 9:
                    self.StopWatchClock[0] = 0
                    self.StopWatchClock[1] += 1



    def ThemeTabs(self, TabName):

        if TabName == "WorldZone":
            self.ids.toolbar.md_bg_color = (2/255,9/255,77/255,1)
            self.ids.BottomNavigation.panel_color = (2/255,9/255,77/255,1)


            self.ids.BottomNavigation.text_color_active= (83/255,99/255,252/255,1)

        elif TabName == "Timer":
            self.ids.toolbar.md_bg_color = (82 / 255, 0 / 255, 153 / 255, 1)
            self.ids.BottomNavigation.panel_color = (82 / 255, 0 / 255, 153 / 255, 1)
            self.ids.BottomNavigation.text_color_active= (176/255,88/255,252/255,1)
            #self.ids.BottomNavigation.
        elif TabName == "StopWatch":
            self.ids.toolbar.md_bg_color = (6 / 255, 88 / 255, 97 / 255, 1)
            self.ids.BottomNavigation.panel_color = (6 / 255, 88 / 255, 97 / 255, 1)
            self.ids.BottomNavigation.text_color_active= (27/255,225/255,247/255,1)
            #self.ids.BottomNavigation.





class Clocker(MDApp):
    title = "Clock"
    icon = "icon.png"


    def build(self):
        return MainLayout()


Clocker().run()
