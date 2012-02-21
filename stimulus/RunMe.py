#!/usr/bin/env python
#(C) Samir Menon, 27, May, 2011
# This is a sample script that loads .par stimulus presentation files and runs them. Modify and use.
# It uses VisionEgg

"""Display text strings."""

#Import the generic VisionEgg classes
import VisionEgg
#VisionEgg.start_default_logging(); 
VisionEgg.watch_exceptions();

from VisionEgg.Core import get_default_screen, Viewport
from VisionEgg.FlowControl import Presentation
from VisionEgg.Text import Text

#Import the custom rendering classes
from CVEggStimText import *
from COptSeqLoader import *

#Set up an OpenGL screen
screen = get_default_screen()
screen.parameters.bgcolor = (0.0,0.0,0.0) # background black (RGB)

#**************************
#Initialize this experiment
#**************************
#Load the data and set the parameters
data = COptSeqLoader();
data.load("stim.par");


#**** Manually Set Some Params ****
data.tplan = 5;           #seconds to plan and pick up correct object
data.texec = 8;           #seconds to execute motion
data.treset = 3;          #seconds to bring hand back to position

trial_text = ["Rest", "Tip : Square", "Middle : Square", "Top : Square"];

#**** Automatically Create The Visual Stimuli ****
x = [];              #Will store all the vision egg text sequences
i=0;                 #Counter for vision egg text sequences
len = len(data.seq); #The number of sequences read from a file
total_time = 0.0;    #The total time so far
font_size = 110;

# NOTE TODO : Add a check to make sure the number of trial text entries matches the par file

for ele in range(0,len):
  #********************************
  #*** 1. The Null task : Rest ****
  #********************************
  if data.seq[ele].trial_id == 0:
    x.append(CVEggStimText()); #Create a new text stimulus
    x[i].initMe(trial_text[0],font_size,data.seq[ele].tduration,'seconds',screen,1.0,0.0,0.0);
    total_time = total_time + data.seq[ele].tduration;
    i = i+1;
  #**************************************************
  #*** 2. All other tasks : Plan, Execute, Reset ****
  #************************************************** 
  elif data.seq[ele].trial_id > 0:
    #The planning phase
    x.append(CVEggStimText());
    disp_txt = "Plan: " + trial_text[data.seq[ele].trial_id];
    x[i].initMe(disp_txt,font_size,data.tplan,'seconds',screen,1.0,1.0,0.0);
    i = i+1;
    #The execution
    x.append(CVEggStimText());
    disp_txt = "Execute: " + trial_text[data.seq[ele].trial_id];
    x[i].initMe(disp_txt,font_size,data.texec,'seconds',screen,0.0,1.0,0.3);
    i = i+1;
    #The reset
    x.append(CVEggStimText());
    x[i].initMe('Rest',font_size,data.treset,'seconds',screen,1.0,0.0,0.0);
    i = i+1;
    #Increment the total time so far
    total_time = total_time + data.seq[ele].tduration;
    #Sanity check
    if data.seq[ele].tduration != (data.tplan+data.texec+data.treset):
      print("\nERROR : Trial [",ele, "] duration is inconsistent");

x.append(CVEggStimText());
x[i].initMe('Finished. Good Job!',font_size,10,'seconds',screen);
i = i+1;

#**************************************************
# FINAL: Make VisionEgg Present The Visual Stimuli 
#**************************************************
print("*****************************************************");
print("Experiment : My Cool Experiment (Clearly I wasn't paying enough attention to change the name)");
print("Total Experiment Time (sec):", total_time);
print("Total Text Simuli:", i-1);
print("Task Simuli:", trial_text);
print("Task Planning Time (sec):", data.tplan);
print("Task Execution Time (sec):", data.texec);
print("Task Reset Time (sec):", data.treset);
print("*****************************************************");

of = open("write-stats.txt","w");
of.write("\nTotal Experiment Time (sec):"); of.write(str(total_time));
of.write("\nTotal Text Simuli:"); of.write(str(i-1));
of.write("\nTask Simuli:"); of.write(str(trial_text));
of.write("\nTask Planning Time (sec):"); of.write(str(data.tplan));
of.write("\nTask Execution Time (sec):"); of.write(str(data.texec));
of.write("\nTask Reset Time (sec):"); of.write(str(data.treset));

for ele in range(0,i):
  x[ele].show();

#***************************************************
#                     The End!
#***************************************************

