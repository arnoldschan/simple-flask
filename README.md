# Flask API Docker - Practice

A hands-on exercise to implement Docker


## Docker Terminology
1. Docker Daemon: Runs on host machine, creates and manages docker objects such as images, containers, network, volume, data, etc.
2. Docker Image: A package with all the dependencies and information needed to create a container.
3. Container: A running instance of an image.
4. Docker Hub: A service which we can share image with the team or the public and also it is a repository to store images.
5. Dockerfile: A set of commands executed sequentially to create an image.

![](image/docker-terminology.png)

source: https://dev.to/ankushsinghgandhi/docker-cheat-sheet-56cc


## Steps
Build the Docker image
```bash
docker build -t simple-flask-api .
```

`-t` means we provide a flag tag to the image.

`.` means Docker should refer to the `Dockerfile` in the current directory.


Run the Docker container
```bash
docker run -d -p 5000:5000 simple-flask-app
```

`-d` means we running the container in "detached" mode (in the background).

`-p` means we creating a mapping between the host's port 5000 to the container's port 5000.
If we don't do the port mapping, we can't access the app.

Once the Docker container is running, we can access it in the web browser http://localhost:5000/.



Happy coding!
