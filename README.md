# sorpf-task
The Dual Self and Other Referential Processing/Flanker (SORPF) task in E-Prime

## The Task
This task combines the self and other referential processing task and the [Eriksen flanker task](https://cognitiveatlas.org/task/id/tsk_4a57abb949a4f/) in a block design. This task has four conditions and was adapted from a self-referential + flanker task used by Alcarón and colleagues. [1]
1. Self-referential processing (SELF), in which the participant views an image of themself paired with a descriptive word or phrase and asked "does this word describe you?" then responds either "yes" or "no".
2. Other-referential processing (OTHER), in which the participant views an image of a familiar person (in this case, a character from the TV show Stranger Things) paired with a descriptive word or phrase and is asked "does this word describe the person shown?", then responds either "yes" or "no".
3. Non-social control (MALLEABLE), in which the participant views an image of a stranger paired with a descriptive word or phrase, is asked "can this change?", and instructed (in the training) to answer "yes" or "no" according to whether the descriptive is something that can change about a person, regarless of the person shown with the word.
4. Flanker (FLANKER), in which the participant performs 5 randomised trials of the Eriksen flanker task, interspersed between each of the previously described conditions, as a mental palate cleanser. Each trial is 800ms, during which the participant is instructed to indicate the direction that the center arrow is pointing as quickly as possible. Trials are randomized to include congruent trials (center arrow points in the same direction as the flanking arrows) and incongruent trials (center arrow is pointing in the opposite direction as the flanking arrows).

Between each block, a fixation cross is presented for a randomized duration between 2 and 6 seconds.

## Implementation Notes
1. This task is set up to work with FIU's scanner's BioPac.
However, it was developed on a computer that does not have a serial port, which breaks the task if a serial port device is enabled.
As such, there are a number of if/else statements throughout the task to call the serial port when BioPac is enabled and to not call it when it isn't.
This doesn't completely solve the issue, though, so you need to check the devices that are selected under the experiment's main settings before running the task.
If the task will be run on a computer with a serial port, simply turn on the "Serial" device.
Otherwise, make sure it's off.
2. This task writes out a BIDS-compatible tsv file (i.e., an "events" file).
In BIDS events files, the first column should be "onset" (in seconds).
However, E-Prime has an odd behavior where it writes out numeric values with a leading space, so instead we write out a string-based variable as the first column.
Thus, events files written out by this task need to be corrected (i.e., columns need to be reordered to follow BIDS convention) before they will pass the BIDS validator.
3. The BIDS events files are also not quite tab-delimited, so you will need to convert them.
Pandas can do this pretty easily.
For example, the following should work:

```python
import pandas as pd

df = pd.read_table('example_data/sub-777_ses-1_task-SORPF_run-1.tsv', sep='\s+')
df.to_csv('example_data/sub-777_ses-1_task-SORPF_run-1.tsv', sep='\t',
          line_terminator='\n', na_rep='n/a', index=False)
```
## References
1. Alarcón, G., Pfeifer, J. H., Fair, D. A., & Nagel, B. J. (2018). Adolescent Gender Differences in Cognitive Control Performance and Functional Connectivity Between Default Mode and Fronto-Parietal Networks Within a Self-Referential Context. Frontiers in behavioral neuroscience, 12, 73. doi:10.3389/fnbeh.2018.00073
