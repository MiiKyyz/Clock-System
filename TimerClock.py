

TimerBool = False

class TimerClockSystem:

    NumberList = [0,0,0,0,0,0]


    def Timer(self):
        global TimerBool
        if TimerBool is False:
            TimerBool = True

        elif TimerBool is True:
            TimerBool = False

    def Startimer(self):
        global TimerBool
        if TimerBool is False:
            pass

        elif TimerBool is True:


            if self.NumberList[2] > 6 and self.NumberList[4] > 6:

                self.NumberList[4] = self.NumberList[4] - 6
                self.NumberList[2] = self.NumberList[2] - 6
                self.NumberList[1] += 1

                if self.NumberList[3] == 9:
                    self.NumberList[3] = 0
                    self.NumberList[2] += 1
                elif self.NumberList[3] < 9:
                    self.NumberList[3] += 1

            if self.NumberList[2] == 6 and self.NumberList[3] > 0:
                self.NumberList[1] += 1
                self.NumberList[3] += 1
                self.NumberList[2] = 0
                self.NumberList[5] = 0
                self.NumberList[4] = 0

            if self.NumberList[2] > 6:

                if self.NumberList[2] > 6 and self.NumberList[4] > 6:
                    if self.NumberList[2] > 6:
                        self.NumberList[1] += 1

                    elif self.NumberList[2] < 6:
                        pass
                else:
                    self.NumberList[2] = self.NumberList[2] - 6
                    self.NumberList[1] += 1


            elif self.NumberList[4] > 6:
                self.NumberList[4] = self.NumberList[4] - 6
                self.NumberList[3] += 1


            elif self.NumberList[1] == 0 and self.NumberList[2] == 0 and self.NumberList[3] == 0 and self.NumberList[4] == 0 and self.NumberList[5] == 0:
                self.NumberList[0] -= 1
                self.NumberList[1] = 9
                self.NumberList[2] = 5
                self.NumberList[3] = 9
                self.NumberList[4] = 5
                self.NumberList[5] = 9


            elif self.NumberList[2] == 0 and self.NumberList[3] == 0 and self.NumberList[4] == 0 and self.NumberList[5] == 0:
                self.NumberList[1] -= 1
                self.NumberList[2] = 5
                self.NumberList[3] = 9
                self.NumberList[4] = 5
                self.NumberList[5] = 9


            elif self.NumberList[3] == 0 and self.NumberList[4] == 0 and self.NumberList[5] == 0:
                self.NumberList[2] -= 1
                self.NumberList[3] = 9
                self.NumberList[4] = 5
                self.NumberList[5] = 9


            elif self.NumberList[4] == 0 and self.NumberList[5] == 0:
                self.NumberList[3] -= 1
                self.NumberList[4] = 5
                self.NumberList[5] = 9

            elif self.NumberList[5] == 0:

                if self.NumberList[4] > 0:
                    self.NumberList[5] = 9
                    self.NumberList[4] -= 1

            elif self.NumberList[5] > 0:
                self.NumberList[5] -= 1

    def DeleteNumbers(self):

        if self.NumberList[1] == 0 and self.NumberList[2] == 0 and self.NumberList[3] == 0 and self.NumberList[4] == 0 and self.NumberList[5] == 0:
            pass
        else:

            self.NumberList.pop(len(self.NumberList) - 1)
            self.NumberList.insert(0,0)


    def AddNumbers(self, number):

        if(self.NumberList[0] > 0):
            pass
        else:


            self.NumberList.append(int(number))
            self.NumberList.pop(0)

