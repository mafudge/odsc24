# Introduction to Containers for Data Science / Data Engineering

ODSC '24  
Michael Fudge


## Abstract

In this hands on session, participants will learn how to leverage containers for data science / data engineering workflows. Containers allows us to bundle our application dependencies and configuration into an image, which can be more easily shared with others and deployed to the cloud. The session will explain how to use and build images, configure and run them and handle inter-dependencies between the product you're building and other services such as databases.

Specifics covered:

- how containers work
- what are their advantages in data science / data engineering
- finding images on repositories (docker hub / quay.io)
- creating containers from the image and running it
- exposing resources like ports and volumes
- orchestration with docker-compose
- building / configuring / customizing images to include your specific project dependencies
- integrating your container with the visual studio code editors
- containerizing dependent services like databases and integrating them with your project

Source code from the workshop will be available for attendees on github.

## Prerequisites: Preparing your computer for the workshop

#### NOTE:

Building and running containers can require downloading large files from the internet.  We don't know what the WiFi is going to be like so this section is designed to ready your computer for the workshop in addition to minimizing the amount of internet traffic we will require in the workshop itself. 

### Required software

Software required for the workshop. Please download and install prior to the workshop:

1. **git** This way you can clone this repository. https://git-scm.com/
3. **Visual Studio Code** This is the tool we will use to edit our configurations. https://code.visualstudio.com/
2. **Docker Desktop**. For building, deploying and managing images and containers: https://www.docker.com/products/docker-desktop/  
NOTE for Mac OS Users: Go to Docker settings and make sure "Use Rosetta for x86/amd64 emulation on Apple Silicon" and "Use Virtualization Framework" are enabled.

### Configure Visual Studio Code Plugins

TODO

### Clone this Github Repository

1. Open a terminal or command prompt
2. `cd` into the folder you wish to work from, when it doubt, you can use your home directory: `$ cd ~`
3. Clone this repository `$ git clone https://github.com/mafudge/odsc24`

### Pre-Download the Docker Images used in this workshop

Pre-downloading the docker images will save us all the pain of overloading the conference WiFi.

1. From a terminal / command prompt:
2. `cd` into the `odsc24` folder. `$ cd odsc24`
3. TODO docker-compose pull?

