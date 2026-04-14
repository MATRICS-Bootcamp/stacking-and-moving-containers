# Stacking Containers

You may need different software versions for different pieces of your workflow.  This tutorial shows you how to work with multiple containers in a single workflow.

Tutorial Overview:
* Build two containers with different python versions
* Submit both containers in serial to a SLURM cluster
  
## Step 1: Building your two containers

In this repo, we have two container definition files: `python_3_11.def` and `python_3_9.def`.  Each builds with a different python version.  

To build these containers, run:

```bash
apptainer build python_3_9.sif python_3_9.def
apptainer build python_3_11.sif python_3_11.def
```

## Step 2: Submitting your containers

### In Serial

Now that your containers are built, you can use them in your workflow! The `submit_serial.submit` file shows an example of how to submit these containers serially, and check they are working.  

You'll see two `apptainer exec` lines - one for each container.  When you run this job via `sbatch submit_serial.submit`, you can confirm the containers are working properly if you see two python versions in the output:

```
Python 3.9.25
Python 3.11.15
```

