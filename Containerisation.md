# Containerisation

The following steps are required to create a docker container that will run the model prediction code:

1. Install Docker.
   In my case I was runnning ubunte and the installation instructions were [here]([Install Docker Engine on Debian | Docker Docs](https://docs.docker.com/engine/install/debian/#install-using-the-repository)). 
   Instructions for other operating systems are available on [docker.com](https://www.docker.com/).

2. Create a [Dockerfile](https://github.com/BuzzKanga/MLZoomcamp-2023-Mid-Term-Project/blob/main/Dockerfile).
   This file will have all the information necessary to create the docker container.

3. Build the docker container called **car-prices** using the following command:  
   `docker buildx build -t car-prices .`  
   The build process will reference the above Dockerfile.

To run the docker container, use the following command:  
`docker run -it --rm -p 9696:9696 car-prices`
