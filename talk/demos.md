# Workshop Demos

## Part 1: Essentials

Run these commands from a terminal in the `part1` folder

## Demo 1: Pulling an image

    $ docker pull jupyter/minimal-notebook:lab-4.1.6
    $ docker pull quay.io/jupyter/minimal-notebook:lab-4.1.6
    $ docker images

## Demo 2: Containers

    $ docker run --name jupyter -d quay.io/jupyter/minimal-notebook:lab-4.1.6
    $ docker ps
    $ docker logs jupyter
    $ docker stop jupyter
    $ docker ps -a
    $ docker rm jupyter

## Demo 3: Ports

    $ docker run –-name jupyter -p 8888:8888 -d quay.io/jupyter/minimal-notebook:lab-4.1.6
    $ docker ps
    $ docker logs jupyter

## Demo 4: Volumes

    $ docker stop jupyter && docker rm jupyter
    $ docker run –-name jupyter -p 8888:8888 -d quay.io/jupyter/minimal-notebook:lab-4.1.6
    $ docker stop jupyter && docker rm jupyter
    $ docker run –-name jupyter -p 8888:8888 -v $PWD/work:/home/jovyan/work -d quay.io/jupyter/minimal-notebook:lab-4.1.6

## Demo 5: Docker Compose

    $ docker compose -f jupyter.yaml up -d
    $ docker compose -f jupyter.yaml ps
    $ docker compose -f jupyter.yaml down

## Part 2: Dev Containers

Run these commands from a terminal in the `part2` folder

## Demo 6: Building A Custom Image

    $ docker compose build 
    $ docker compose images
    $ docker images 
    $ docker compose up
    $ docker compose down

## Demo 7: Dev Containers

    - Debugging, no commands

## Part 3: Complex Pipelines in Containers

Run these commands from a terminal in the `part3` folder

## Demo 8: Complex Pipeline

    $ docker compose ps 

## Part 4: Summary

## Cleaning up

    $ docker system prune --all --volumes



