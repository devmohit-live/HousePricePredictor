# HousePricePredictor

A Flask App to that predicts the price of the house, given various parameters like income, average no.of rooms, etc based on USA House Price Dataset , A project to br deployed on docker

## Previews:

![Home](https://raw.githubusercontent.com/devmohit-live/Images_of_repo/master/front.JPG)

![Result Page](https://raw.githubusercontent.com/devmohit-live/Images_of_repo/master/result.JPG)

## Installation :

- ### Install Dokcer : [Docker Installation](https://docs.docker.com/get-docker/)

## Option 1:

- Pull Image : `docker pull devmohitlive/flaskcos`
-  Build a volume for persistant stoarge: `docker volume create flaskstorage`
-  Build a Container with port forwarding on to access within the intranet : `docker run -dit -p [free_port_of_base_system]:5000 -v flaskstorage:/root/ --name [container_name] flaskcos` you can use any free port of your base os.
  > example: `docker run -dit -p 8080:5000 -v flaskstorage:/root/ --name flaskapp flaskcos`

## Option Two: Using docker-composefile(included in repo)

-  Make a directory named flaskapp (not mandatory but recommended) `mkdir flaskapp`

- Install docker-compose: [DockerCompose Installtion](https://docs.docker.com/compose/install/)

-  run this command : `docker-compose up -d`

## Use :

- ### connect to the app ny using your system's(base system) ip along with your port number you specified, Ex: `192.168.43.135:8080`
## Troubleshooting

- Facing package/dependecies problem : _The image has python3 and the packages are as folllows: pip3, flask, sklearn, numpy_
- > **Solution** : Try updating the packages pip3 install -r requirement.txt
- Conatiner is installed correctly but site is unable to connect
- > **Solution** : try these steps:

  1.  _Run this command to know the container name :_ `docker ps`
  2.  _Attach to the container_ : `docker attach conatiner_name`
  3.  _ Run these command:_

  ```
  git clone https://github.com/devmohit-live/HousePricePredictor.git

  python3 "HousePricePredictor/app.py"

  ```

  4. Press : `CTRl p q` keys simultaneously to come out of container
