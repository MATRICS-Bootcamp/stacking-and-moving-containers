# Moving Containers

This tutorial primarily outlines how to push Singulaity containers to Github Packages.  Because Singularity containers are files, moving them around as files is pretty straight forward!  I won't cover Docker since it's less common in research computing scenarios

## Pushing your Singularity container to Github Pacakges

### Step 1: Authentication

To authenticate, you'll need a _Personal Access Token_.  To create a Personal Access Token:

1. Go to your settings on Github
2. At the very bottom on the left, navigate to Developer Settings
3. Under Personal Access Tokens, go to Tokens (classic)
4. Generate a new classic token
5. The mininmal permissions you need to give this token is write:packages
6. Once you've generated your token, put it in a file somewhere safe! Perhaps your `~/.ssh` directory

Now that you have a token to authenticate with, you can authenticate singularity with the following command:

```bash
singularity registry login -p $(cat <token_file_here>) --username <github_username> oras://ghcr.io
```

You could technically place your token in plain text after -p.  I like storing it in a file and then using that file. 

### Step 2: Pushing your container

Assuming you have a container file in your local directory, you can push your container to github with the following command:

```bash
singularity push <your_package_file> oras://ghcr.io/<github_username_or_organization>/<package_name>:<package_tag>
```
* `<github_username_or_organization>`: You need to specify either your Github username or organization to push the container to.
* `<package_name>`: You can name the package anything you'd like
* `<package_tag>`: Tagging containers is a common practice.  There's a variety of strategies: tag the newest version `latest`, tag releases with the version number, tag with the git commit hash, etc...



### Optional Step 4: Linking your container to a repository

If you go to your Github user profile, and then Packages, you should see your package.  There will be an option to link it to a repository!


## Pulling a container from Github Packages

### Optional: Authentication

If your package is private, you'll need to follow the Authentication instructions above to authenticate.

### Pulling with Singularity

You can pull a package from github with the following command:

```bash
singularity pull oras://ghcr.io/<github_username_or_organization>/<package_name>:<package_tag>
```

The package will appear as a .sif file in your current directory!
