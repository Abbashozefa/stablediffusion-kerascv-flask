# stablediffusion-kerascv-flask

To carry out stable diffusion in flask that is text to image generation using keras cv.

Diffusion is basically taking the an image and giving noise to it and then denoising using a neural network. They are Generative Models that explicitly model the probablity density based on a approximation.Thye are found to be more useful that GAN's. Diffusion models learn how to regenerate data.Usually a U-Net architecture is what used to achieve diffusion.What this gives us? It gives us state of the art images that are better than the original image.

Stable Diffusion is similar to diffusion in terms of adding noise to the image, the difference is that while denoising the image we add features to the image according to the prompt that is understood by an NLP model.

Diffusion Model Example:
https://colab.research.google.com/drive/1sjy9odlSSy0RBVgMTgP7s99NXsqglsUL?usp=sharing#scrollTo=buW6BaNga-XH

Using KerasCV stable diffusion can be easily performed on a given prompt. 

Check out this papaer as well on diffusion models:
https://proceedings.nips.cc/paper/2021/file/49ad23d1ec9fa4bd8d77d02681df5cfa-Paper.pdf
