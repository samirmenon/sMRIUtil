Author : Samir Menon
Email : smenon <at> stanford.edu

This is a collection of random scripts and advice for analyzing MRI data.


*********************
The Absolute Newbie: 

Assuming you have read a few papers on what the BOLD signal means, and what the limits of fMRI is ('What we can and what we cannot do with fMRI, Logothetis 08'), and that you now want to collect some data.

Broadly, you must:

1. Get trained by your Institutional Review Board (IRB) to conduct experiments with humans.

2. Design a rough study protocol that highlights what subjects will do, and get it approved by your IRB.

3. Design a protocol:
(a) Typically, this involves doing/being-subjected-to a task for some time and then resting for some time. Most analysis contrast the task to the rest periods.
NOTE : Some analysis methods use unsupervised algorithms to simply determine what regions are active at what time (FSL's MELODIC ICA for instance). These may offer unbiased insights into whether your data accurately captures task-related distributions.

Protocol:

                 ~^~^~^~^|
                |         ^~^~^~
Signal : ^~^~^~|                |~~~~~~~~~

             |---------|
Stim   : ----|         |------------------



(b) The time of task vs. rest will strongly influence your experiment's sensitivity. 
Eg. Task time ~= hrf rise time (10-15s), rest time ~= hrf dip time (10s), will maximize your contrast. But then your scan might take too long.

(c) For shorter task times task activity will overlap, so it is best to randomize task presentation and make sure that co-active tasks don't always appear consecutively, which would confound your analysis.
NOTE : Use "optseq" to randomize task presentation. It is a freely downloadable binary (google it).

(d) The more task variations you have, the more you learn about the brain. But remember, that the analysis becomes progressively harded and the statistical significance becomes lower.
TRADEOFF : Task variations VS Statistical power

*********************
The Stimulus Designer:

So you've decided to fun an fMRI trial. Thought up an experiment and are ready to start.

You must now decide how to display information to the subject (visual, audio cues etc.). I use optseq, a python based stimulus presentation tool called VisionEgg. There is some text-stim wrapper code in stimulus. Be sure you install VisionEgg first.
https://github.com/visionegg/visionegg

NOTE : Be sure to time-sync the stimulus and fMRI recordings.
NOTE : There is always operating system jitter. Ie. If you tell the computer to display a stimulus at 10.00 seconds into a trial, it might end up displaying at 10.00 +- 0.05 seconds. This varies from computer to computer as well.


