# 🚦 Traffic
> As research continues in the development of self-driving cars, one of the key challenges is computer vision, allowing these cars to develop an understanding of their environment from digital images. In particular, this involves the ability to recognize and distinguish road signs – stop signs, speed limit signs, yield signs, and more.  
> To explore this challenger write an AI to identify which traffic sign appears in a photograph.

## 🚀 Summary
  
...


## 📄 Official Description (Adapted)

In this project, you’ll use TensorFlow to build a neural network to classify road signs based on an image of those signs.   
To do so, you’ll need a labeled dataset: a collection of images that have already been categorized by the road sign represented in them.

Several such data sets exist, but for this project, we’ll use the *German Traffic Sign Recognition Benchmark* (GTSRB) dataset, which contains thousands of images of **43** different kinds of road signs.


### 🗂️ Dataset Overview
First, take a look at the data set by opening the `gtsrb` directory.  
Notice that there are 43 subdirectories in this dataset, where:
- Each one is numbered `0` through `42`
- Each one represents a different category (a different type of road sign). 
- Within each one is a collection of images of that type of traffic sign.

### 🔍 Code Overview
Next, take a look at `traffic.py`. 

The `main` function accept as command-line arguments:
- a directory containing the data, and (optionally)
- a filename to which to save the trained model. 

Then:
- The `load_data` function load the data and corresponding labels from the data directory 
- The data and labels are split into training and testing sets. 

After that: 
- The `get_model` function is called to obtain a compiled neural network that is then fitted on the training data. 
- The model is then evaluated on the testing data. - Finally, if the optionally command-line argument was provided, the trained model is saved to disk.

The `load_data` and `get_model` functions was left to be implement.

### ⚙️ Specification
📌 Complete the implementation of `load_data` and `get_model` in `traffic.py` and in a separate file `README.md` document your experimentation process.

#### ✅ `load_data`
_The function should accept as an argument data_dir, and return image arrays and labels for each image in the data set._
- You may assume that `data_dir` will contain one directory named after each category, numbered `0` through `NUM_CATEGORIES - 1`. 
    - Inside each category directory will be some number of image files.
- Use the OpenCV-Python module (`cv2`) to read each image as a `numpy.ndarray` (a numpy multidimensional array).
    - To pass these images into a neural network, the images will need to be the same size, so be sure to resize each image to have width `IMG_WIDTH` and height `IMG_HEIGHT`.
- The function should return a tuple `(images, labels)`. 
    - `images` should be a list of all of the images in the data set, where each image is represented as a `numpy.ndarray` of the appropriate size. 
    - `labels` should be a list of integers, representing the category number for each of the corresponding images in the images list.
- Your function should be platform-independent: that is to say, it should work regardless of operating system. 
    - Note that on macOS, the `/` character is used to separate path components, while the `\` character is used on Windows. 
    - Use `os.sep` and `os.path.join` as needed instead of using your platform’s specific separator character.

#### ✅ `get_model`    
_The  function should return a compiled neural network model._
- You may assume that the input to the neural network will be of the shape (`IMG_WIDTH, IMG_HEIGHT, 3)` 
    - That is, an array representing an image of width IMG_WIDTH, height IMG_HEIGHT, and 3 values for each pixel for red, green, and blue.
- The output layer of the neural network should have `NUM_CATEGORIES` units, one for each of the traffic sign categories.
- The number of layers and the types of layers you include in between are up to you. You may wish to experiment with:
    - Different numbers of convolutional and pooling layers
    - Different numbers and sizes of filters for convolutional layers
    - Different pool sizes for pooling layers
    - Different numbers and sizes of hidden layers dropout

#### ✅ Documentation
- In a separate file called `README.md`, document (in at least a paragraph or two) your experimentation process.  
_What did you try? What worked well? What didn’t work well? What did you notice?_ 

### ⭐ To Keep in Mind
Much of this project is about exploring documentation and investigating different options in `cv2` and `tensorflow` and seeing what results you get when you try them!

### 🔒 Constraints
- You should not modify anything else in `traffic.py` other than the functions the specification calls for you to implement, though:
    - You may write additional functions and/or import other Python standard library modules. 
    - You may also import numpy or pandas, if familiar with them, but you should not use any other third-party Python modules.
    - You may modify the global variables defined at the top of the file to test your program with other values.


### 💡 Hints Provided
- Check out the official Tensorflow Keras overview for some guidelines for the syntax of building neural network layers. 
    - You may find the lecture source code useful as well.
- The OpenCV-Python documentation may prove helpful for reading images as arrays and then resizing them.
- Once you’ve resized an image img, you can verify its dimensions by printing the value of img.shape.  
    - If you’ve resized the image correctly, its shape should be `(30, 30, 3)` (assuming `IMG_WIDTH` and `IMG_HEIGHT` are both 30).
- If you’d like to practice with a smaller data set, you can download a modified dataset that contains only 3 different types of road signs instead of 43.

### 🎯 Solution
| Feature | Commit |
|----------|--------|
|`get_model`| [b6c081f](https://github.com/lucasOlivein/CS50-Harvard/commit/b6c081f8866046b9d7ce4d6b541df5b0ab8cf0e4)
|`load_data`| [14dd83d](https://github.com/lucasOlivein/CS50-Harvard/commit/14dd83d7cfcf5dfaacfd964d9b49f5545ccf865b)
#### 📝 Experimentation
After implementing the `load_data` function, I began exploring how to use TensorFlow to build a neural network. It took me some time to understand the idea of designing a model conceptually and then fitting the data to it, and at first I even wondered, “Where does the data come in?” Eventually this became clearer, and I realized that this step is where the structure responsible for holding and processing the data is built — the model — and only afterward is the data introduced. While experimenting with Sequential models and different layer configurations, I noticed that the results fluctuated too much, the training time wasn’t proportional to the performance gains, and adding more layers didn’t help. The process became mechanical and repetitive, and I lost sight of what I was trying to achieve, so I stepped back to research well-known CNN architectures.

I implemented models such as ResNet, DenseNet, EfficientNet, and ConvNeXt, and observed clear improvements in performance and accuracy. For example, a parameter-reduced version of ConvNeXt achieved 98.85% validation accuracy after 50 epochs, which was impressive. Although I still don’t fully understand why everything works the way it does, I am starting to form ideas about it, and I hope to grasp the full concept in the future. Despite some moments of frustration, this project was ultimately very satisfying, and I genuinely enjoyed it.

| CNN Arch | Commit |
|----------|--------|
| ConvNeXt | [b2e561f](https://github.com/lucasOlivein/CS50-Harvard/commit/b2e561f6c5554fa37d5ab88ef2cb2928823facb0) |
| EfficientNet | [4a6d878](https://github.com/lucasOlivein/CS50-Harvard/commit/4a6d878f82f9f4b81ba5dad290eea9c90025784e)  |
| DenseNet | [c03fb8f](https://github.com/lucasOlivein/CS50-Harvard/commit/c03fb8fa60ffbd04a2137393d182dd9118bd2083) |
| ResNet | [ed888bf](https://github.com/lucasOlivein/CS50-Harvard/commit/ed888bf4af4d2b47df002507773918fa04d379e3) |

### 📚 Source
Based on *Traffic* project from Harvard’s CS50 AI course: https://cs50.harvard.edu/ai/projects/5/traffic/#traffic

### 💾 Downloads
- The distribution code: https://cdn.cs50.net/ai/2023/x/projects/5/traffic.zip  
- The data set for this project: https://cdn.cs50.net/ai/2023/x/projects/5/gtsrb.zip. 
    - Unzip and move the resulting `gtsrb` directory inside of your `traffic` directory.
- The smaller smaller data set: https://cdn.cs50.net/ai/2023/x/projects/5/gtsrb-small.zip
