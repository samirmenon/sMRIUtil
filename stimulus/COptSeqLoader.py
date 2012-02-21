#(C) Samir Menon, 23, June, 2011
#A class to hold the data for a single display event
#Each display event is:
# Plan <trial-name> 
# Execute <trial-name>
# Reset
class COptSeq:
  tstart = 0.0;        #The start time of this trial wrt the overall expt
  trial_id = 0;        #The trial id
  tduration = 0.0;     #The trial's duration
  trial_name = "bobo"; #The trial's name

#This class loads and stores a set of sequences from an OptSeq
#generated file
#Each OptSeq file contains an entire experiment's stimuli, randomized
#with jitter etc.
#In addition, users may specify planning, execution and reset times
#for each trial. And users may also specify intermediate periods of
#long rest times (in case the subject gets tired).
class COptSeqLoader:
  seq = [];             #Stores all the sequences
  tplan = 0.0;          #The length of the planning phase for this experiment
  texec = 0.0;          #The length of the execution phase for this experiment
  treset = 0.0;         #The length of the reset phase for this experiment
  t_longrest = 0.0;     #The length of the long-rest period
  t_ins_longrest = 0.0; #The time after which a long rest is inserted

  #This function loads the sequences
  def load(self,infile):
    import string

    f = open(infile,'r');
    lines = f.readlines();

    i=0; #counter for self.seq
    for l in lines:
      words = l.split(); #words should contain 5 elements for OptSeq files
      if len(words) != 5:
        print("\nERROR : OptSeqFile is corrupted. Exiting.");
        break;
      self.seq.append(COptSeq()); #Create a new trial and read in the data
      self.seq[i].tstart = string.atof(words[0]);
      self.seq[i].trial_id = string.atoi(words[1]);
      self.seq[i].tduration = string.atof(words[2]);
      self.seq[i].trial_name = words[4];
      i = i+1;
    f.close();

  #This function exports sequences to txt files, one for each sequence id.
  def export(self,infile,outfile,mode,task_types):
    import string

    f = open(infile,'r');
    lines = f.readlines();
    
    ofarr = []; #Create an empty array
    #Open as many files as there are task_types
    for i in range(0,task_types+1):
      of = open(outfile+str(i),mode);
      ofarr.append(of);

    i=0; #counter for self.seq
    for l in lines:
      words = l.split(); #words should contain 5 elements for OptSeq files
      if len(words) != 5:
        print("\nERROR : OptSeqFile is corrupted. Exiting.");
        break;
      self.seq.append(COptSeq()); #Create a new trial and read in the data
      ofarr[int(words[1])].write(words[0]); 
      ofarr[int(words[1])].write("\n");
      i = i+1;
    f.close();
    for i in range(0,task_types+1):
      ofarr[i].close();
