# Image Processing

## Federal University of Maranhão

### Setup Python

```
sudo apt update

sudo apt install python3.8

sudo apt-get -y install python3-pip

sudo apt-get update

pip3 install flask3
```

### Setup Front-end React.JS

```
sudo apt-get install -y nodejs

npm install --global yarn

```

1. Pull this repo and, on the front directory, run:
```

yarn

yarn start

```

### Running

On terminal, type the following:

```
python3 main.py
```

And then, choose the option you prefer.



### Main goal: to develop, without any library (such as OpenCV), the following:

1. Dithering:
  - Simple threshold;
  - Threshold with random modulation;
  - Threshold with ordered periodic cluster modulation;
  - Threshold with dispersed periodic ordered modulation;
  - Threshold with orderly aperiodic modulation;
  
2. Binary Mathematical Morphology:
  - Erosion
  - Dilation
  - Opening
  - Closure
  - Inner edge
  - Outer edge 
  
3. Monochromatic mathematical morphology:
  - Erosion
  - Dilation
  - Opening
  - Closure
  - Smoothing
  - Gradient 
  
## Results

Example of Dithering - Threshold with dispersed periodic ordered modulation

![alt text](https://github.com/danielaczarref/ImageProcessing-MorphDithering/blob/master/back/img/result.png?raw=true)


- Front-end results, part I:

![alt text](https://github.com/danielaczarref/ImageProcessing-MorphDithering/blob/master/back/img/pic1.png?raw=true)


- Front-end results, part II:

![alt text](https://github.com/danielaczarref/ImageProcessing-MorphDithering/blob/master/back/img/pic2.png?raw=true)
  
## TODO

- Smoothing
- Upload images
