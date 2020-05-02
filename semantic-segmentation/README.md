# Semantic Segmentation


This pretrained model was used to automatically generate segmentation masks for use in the Deep Photo Style Transfer for Interior Design Application.

### Setup

> Run setup.sh to install the dependencies

### Generate masks based on pretrained model
(ResNet50dilated + PPM_deepsup)

Run the following to test:

Replace **PATH_IMG** with path to your image/folder of images and **OUTPUT_FOLDER** with destination of choice.

```
python3 -u test.py 
--imgs PATH_IMG \
--cfg config/ade20k-resnet50dilated-ppm_deepsup.yaml \
  DIR ade20k-resnet50dilated-ppm_deepsup \
  TEST.result OUTPUT_FOLDER \
  TEST.checkpoint epoch_20.pth \
```

For more information on the model, visit: https://github.com/CSAILVision/semantic-segmentation-pytorch
