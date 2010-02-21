'''
Created on Feb 6, 2010

@author: Razvan
'''
from waveapi import events
from waveapi import model
from waveapi import robot
from models import Space



def OnRobotAdded(properties, context):
  """Invoked when the robot has been added.
  
  """
  version = "4"
  
  root_wavelet = context.GetRootWavelet()
  
  # Create a new space
  name = root_wavelet.GetTitle()
  
  # search for existing
  for space in Space.all():
      if space.name == name:
          root_wavelet.CreateBlip().GetDocument().SetText("MASQ-it v" + version + "! MASQ space '" + name + "' already exists.")
          break
  else:
      new_space = Space(name = name)
      new_space.put() 
      
      root_wavelet.CreateBlip().GetDocument().SetText("MASQ-it v" + version + "! MASQ space '" + name + "' is now created.") 
  
  
  
def OnBlipSubmitted(properties, context):
  """Invoked when any blip we are interested in is submitted.
  
  """
  blip_id = properties['blipId']
  blip = context.GetBlipById(blip_id)
  
  if blip.GetDocument().GetText().lower().strip() == "#spaces":
      spaces = ""
      for space in Space.all():
          spaces = spaces + space.name + "\n"
      blip.CreateChild().GetDocument().SetText(spaces)


if __name__ == '__main__':
  masqit = robot.Robot('masq-it', 
      image_url='http://masq-it.appspot.com/icon.png',
      version='1',
      profile_url='http://masq-it.appspot.com/')
  masqit.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  masqit.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
  masqit.Run()
