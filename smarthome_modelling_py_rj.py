Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Class Rajdevices:
  def__init__(self,name,location,condition):
  self.name= name
  self.location=location
  self.condition=condition
  def click_self (self):
  print ("processing device" + selfdevice.name)
  d1=rajdevices( "bulb","livingroom","working")

  d2=rajdevices( "toaster","kitchen","working")
 
  d3=rajdevices( "tv","livingroom","working")
 
  d4=rajdevices( "washingmachine","wastebin","burnedout")
 
  d5=rajdevices( "ac","livingroom","working")

  d6=rajdevices ( "microwave","kitchen","shortcircuited")
 

  d1.click_self()
  d2.click_self()
  d3.click_self()
  d4.click_self()
  d5.click_self()
  d6.click_self()
 
 Class Remote:
  def__init__(self,u,devicename):
  self.is_working=u
  self.device_name=devicename
  def device__not_processed(self):
  self.is_working=False
  def device_processed(self):
  self.is_working=True

  option1=Remote("True","device1")
  potion2=Remote("True","device2")
  option3=Remote("True","device3")
  option4=Remote("True","device4")
  option5=Remote("True","device5")

  option6=Remote("True","device6")


  option1.device_connected=d1
  option2.device_connected=d2
  option3.device_connected=d3
  option4.device_connected=d4
  option5.device_connected=d5
  option6.device_connected=d6
  
  option1.device_connected.click_self()
  option2.device_connected.click_self()
  option3.device_connected.click_self()
  option4.device_connected.click_self()
  option5.device_connected.click_self()
  option6.device_connected.click_self()