
<h1 align="center">Muchachos TECH</h1>

<div align="center">

</div>

---

<p align="center"> NASA offers a variety of “sonifications” – translations of 2D astronomical data into sound –that provide a new way to experience imagery and other information from space. Advanced instruments currently provide hyperspectral (many color) images from space that are 3D (two spatial dimensions and one color dimension), and sophisticated techniques can be used to enhance 2D astronomical images to make video representations called “fly-throughs” that allow viewers to experience what it would look like to move among space objects in 3D (three simulated spatial dimensions). Your challenge is to design a method to create sonifications of these 3D NASA space datasets to provide a different perceptual path that can help us understand and appreciate the wonders of the universe!
    <br> 
</p>

## 📝 Table of Contents

- [Objectives](#objectives)
- [Idea / Solution](#idea)
- [Dependencies / Limitations](#limitations)
- [Future Scope](#future_scope)
- [Setting up a local environment](#getting_started)
- [Usage](#usage)
- [Technology Stack](#tech_stack)
- [Authors](#authors)

## 🚀 Objectives <a name = "objectives"></a>

Your challenge is to design a method to create sonifications of 3D NASA space datasets. What are some ways that 3D ‘data cubes’ could be converted into sounds to convey the richness of the data? If you want to create a 3D sonification fly-through, how can you convert the video image into sounds that accurately represent what is in the visualization? Do you want to develop a method to sonify a certain data set? Or maybe you want to develop an app that allows people to select data from an archive and then sonifies the selected data according to your prescription? Or perhaps you can develop a way to explore 3D data that merges visual and audio elements?

Think about your audience; how could experiencing your solution enhance their understanding of NASA data? Your audience could be a scientist at a university studying her data about the surface of Mars, a college student at a science museum exploring multi-color images of star-forming clouds, a class of students in a high school learning about Earth’s climate as measured from space, or someone else. Can your sonification tool be accessible to people with low vision, and also enhance visualizations for sighted people? Will you develop a smartphone app, a website, or just a description about how to sonify 3D data for certain NASA data sets?

Don’t forget to clearly explain how your solution sonifies the data!

## 💡 Idea / Solution <a name = "idea"></a>

We generated a platform that is able to take as input a image of space and create a sonification of it.

## ⛓️ Dependencies / Limitations <a name = "limitations"></a>

- As now it only accepts JPG and JPEG images

## 🚀 Future Scope <a name = "future_scope"></a>

Be able to accept more formats and be able to sonify.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development
and testing purposes

### Prerequisites

What things you need to install the software and how to install them.
#### First we will setup the backend.

1. Open the folder backend and install all the necessary dependencies with the following command:

```
pip install <module_name>
```

2. Run the following command to start the backend server:

```
python main.py
```

if done correctly you should see a server running on port 5000.

visit http://localhost:5000/ to see the server running.
you should see a message saying "Hello World"



#### Now we will setup the frontend.

1. Open the folder frontend and install all the necessary dependencies with the following command:

```
  npm install
```

2. Run the following command to start the frontend server:

```
  npm run dev
```

if done correctly you should see a server running on port 3000
visit http://localhost:3000/ to see the server running.


## 🎈 Usage <a name="usage"></a>

![image](https://github.com/guzmanalejandra/SafeAndSound-Gauchos/assets/77400177/4b1dd80e-274a-424d-99a4-a7e81004edf0)
Upload an image and play the audio

## ⛏️ Built With <a name = "tech_stack"></a>

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Server Framework
- [React](https://reactjs.org/) - Web Framework
- [Python](https://www.python.org/) - Server Environment
- [Javascript](https://www.javascript.com/) - Web Environment
- [NextJs](https://nextjs.org/) - Web Framework
- [Tailwind](https://tailwindcss.com/) - CSS Framework

## ✍️ Authors <a name = "authors"></a>

- [@Alejandra Guzman](https://github.com/guzmanalejandra)
- [@Mariana David](https://github.com/marianadaso3)
- [@Jorge Caballeros](https://github.com/JorgeCab2711)
- [@Pablo Escobar](https://github.com/esc20936)

