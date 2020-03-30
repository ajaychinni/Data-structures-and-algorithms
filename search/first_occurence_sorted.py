# -*- coding: utf-8 -*-
# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
import tensorflow as tf

#print(tf.__version__)

import os
working_dir = os.getcwd()
path = working_dir + ':' + working_dir + '/slim'
os.environ['PYTHONPATH'] = path

"""### Test the installation"""

#!python object_detection/builders/model_builder_test.py

"""## **Main code starts**"""

import numpy as np
import os
import glob
import six.moves.urllib as urllib
import sys
import tarfile
import zipfile
import helper

from distutils.version import StrictVersion
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
#import cv2
import imageio
from PIL import Image
from IPython.display import display

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")
from models.research.object_detection.utils import ops as utils_ops

"""### Imports from object detection module"""

from models.research.object_detection.utils import label_map_util
from models.research.object_detection.utils import visualization_utils as vis_util


"""### Now follow https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html#"""

PATH_TO_IMAGES_FOLDER = '../object_detection/images_old'
PATH_TO_ANNOTATIONS_FOLDER = '../object_detection/annotations'
PATH_TO_SCRIPTS_FOLDER = '../object_detection/scripts/preprocessing'
PATH_TO_TRAINING_FOLDER = '../object_detection/training'

"""### Load a frozen model"""

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_FROZEN_GRAPH = '../object_detection/trained-inference-graphs/frozen_inference_graph.pb'

detection_graph = tf.Graph()
with detection_graph.as_default():
	od_graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

"""### Load label map"""

category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_ANNOTATIONS_FOLDER+'/label_map.pbtxt', use_display_name=True)

"""### Run inference"""

def run_inference_for_single_image(model, image):
  image = np.asarray(image)
  # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
  input_tensor = tf.convert_to_tensor(image)
  # The model expects a batch of images, so add an axis with `tf.newaxis`.
  input_tensor = input_tensor[tf.newaxis,...]

  # Run inference
  output_dict = model(input_tensor)

  # All outputs are batches tensors.
  # Convert to numpy arrays, and take index [0] to remove the batch dimension.
  # We're only interested in the first num_detections.
  num_detections = int(output_dict.pop('num_detections'))
  output_dict = {key:value[0, :num_detections].numpy() 
                 for key,value in output_dict.items()}
  output_dict['num_detections'] = num_detections

  # detection_classes should be ints.
  output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)

  # Handle models with masks:
  if 'detection_masks' in output_dict:
    # Reframe the the bbox mask to the image size.
    detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
              output_dict['detection_masks'], output_dict['detection_boxes'],
               image.shape[0], image.shape[1])      
    detection_masks_reframed = tf.cast(detection_masks_reframed > 0.5,
                                       tf.uint8)
    output_dict['detection_masks_reframed'] = detection_masks_reframed.numpy()
    
  return output_dict

"""### Show it on the image"""

def show_inference(model, image_path):
  # the array based representation of the image will be used later in order to prepare the
  # result image with boxes and labels on it.
  image_np = np.array(Image.open(image_path))
  # Actual detection.
  output_dict = run_inference_for_single_image(model, image_np)
  # Visualization of the results of a detection.
  vis_util.visualize_boxes_and_labels_on_image_array(
      image_np,
      output_dict['detection_boxes'],
      output_dict['detection_classes'],
      output_dict['detection_scores'],
      category_index,
      instance_masks=output_dict.get('detection_masks_reframed', None),
      use_normalized_coordinates=True,
      line_thickness=8)

  # display(Image.fromarray(image_np))


TEST_IMAGE_PATH_OLD = '../object_detection/images_old/'
TEST_IMAGE_PATH_NEW = '../object_detection/images_new/'
all_path = [TEST_IMAGE_PATH_OLD,TEST_IMAGE_PATH_NEW]
for folder_path in all_path:
   for image_path in folder_path:
		if image_path.endswith(".png"):
	   	show_inference(detection_model, image_path)
	   	detection(detection_graph,image_path,folder_path)


def detection (detection_graph,image_path,folder_path):
    # Detection
    with detection_graph.as_default():
		with tf.compat.v1.Session(graph=detection_graph) as sess:
		    for image_path in glob.glob(path+"*.png"):
		        #print(image_path)
		        file_name = os.path.basename(image_path)

		        # read the image
		        image_np = np.array(Image.open(image_path).convert(mode='RGB'))
		        #saving orginal copy to send for OCR
		        image_np_orginal_copy = image_np.copy()
		        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
		        image_np_expanded = np.expand_dims(image_np, axis=0)

		        # Extract image tensor
		        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
		        # Extract detection boxes
		        boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
		        # Extract detection scores
		        scores = detection_graph.get_tensor_by_name('detection_scores:0')
		        # Extract detection classes
		        classes = detection_graph.get_tensor_by_name('detection_classes:0')
		        # Extract number of detections
		        num_detections = detection_graph.get_tensor_by_name(
		                'num_detections:0')
		            
		        # Actual detection.
		        (boxes, scores, classes, num_detections) = sess.run(
		                [boxes, scores, classes, num_detections],
		                feed_dict={image_tensor: image_np_expanded})
		            
		        # Visualization of the results of a detection.
		        vis_util.visualize_boxes_and_labels_on_image_array(
		                image_np,
		                np.squeeze(boxes),
		                np.squeeze(classes).astype(np.int32),
		                np.squeeze(scores),
		                category_index,
		                use_normalized_coordinates=True,
		                line_thickness=8)

		        # Display output
		        #display(Image.fromarray(image_np))
			          #Save the image
		        #cv2.imwrite("../object_detection/output_images/"+file_name,image_np)
		        lst = helper.get_coordinates(boxes,scores,classes,num_detections,image_np_orginal_copy)
		        if folder_path == '':
		            imageio.imwrite("../object_detection/output_images_old/"+file_name,image_np)
		        else:
		            imageio.imwrite("../object_detection/output_images_new/"+file_name,image_np)

		        #Saving the list
		        # with open("../object_detection/"+'output_list/'+file_name.split(".")[0]+'.txt','w') as f:
		        #     l = [x.tolist() for x in lst]
		        #     for row in l:
		        #         f.write(str(row))
