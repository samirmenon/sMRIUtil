#(C) Samir Menon, 27, May, 2011
from VisionEgg.Core import get_default_screen, Viewport
from VisionEgg.FlowControl import Presentation
from VisionEgg.Text import Text

#This class runs a vision stimulus using VisionEgg.
class CVEggStimText:
  #Some are overwritten by the init func. Here for reference
  text = 'NULL'
  font_sz = 50
  anchor = 'center'
  t = 1
  tscale = 'seconds'

  #initme's arguments are : (text,font-sz,time,t-unit,screen)
  def initMe(self,arg_text,arg_font_sz,arg_t,arg_tscale,arg_screen,arg_r=1.0,arg_g=1.0,arg_b=1.0):
    #member vars init
    self.text = arg_text
    self.font_sz = arg_font_sz
    self.t = arg_t
    self.tscale = arg_tscale
    self.color=(arg_r,arg_g,arg_b)
    #dyn vars
    text_vegg = Text(text=self.text,
            color=self.color,
            position=(arg_screen.size[0]/2,arg_screen.size[1]/2),
            font_size=self.font_sz,
            anchor=self.anchor)
    viewport_vegg = Viewport(screen=arg_screen,
                    size=arg_screen.size,
                    stimuli=[text_vegg])
    #Set up the pres var
    self.pres_vegg = Presentation(go_duration=(arg_t,arg_tscale),viewports=[viewport_vegg])

  def show(self):
    #print self.text_vegg
    self.pres_vegg.go();
