from logging import debug
from flask import Flask, redirect, render_template, request, url_for
import base64
#from flask_ngrok import run_with_ngrok

import json   
from os import truncate
import numpy as np
import heartpy as hp
import matplotlib
from sklearn import preprocessing
#matplotlib.use( 'tkagg' )
matplotlib.use('agg')
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pyVHR.signals.video import Video
from pyVHR.methods.pos import POS
#from pyVHR.methods.chrom import CHROM
#from pyVHR.utils.errors import getErrors, printErrors, displayErrors
#from hrvanalysis import remove_outliers, remove_ectopic_beats, interpolate_nan_values
#from hrvanalysis import get_time_domain_features
#from scipy.signal import find_peaks
#from scipy.fft import fft
#import math
#from pyVHR.methods import spo2_utils 
import urllib.request

Video.loadCropFaces = Video.saveCropFaces = False

app = Flask(__name__)
#run_with_ngrok(app)
#Switch Deployment to NGROK and remove extra printing before the final proof of concept

@app.route('/')
def home():
    return "hi"

@app.route('/api', methods=['POST'])
def api():
    url_link = request.json['video_link']
    urllib.request.urlretrieve(url_link, 'video.mp4')
    return redirect(url_for('process'))

@app.route('/api_process')
def process():
    # -- Video object
    videoFilename = "video.mp4"
    #access: videoFilename = "../sampleDataset/alex/alex_resting/cv_camera_sensor_stream_handler.avi"
    video = Video(videoFilename)
    video.getCroppedFaces(detector='mtcnn', extractor='skvideo')

    video.setMask(typeROI='skin_fix',skinThresh_fix=[30, 50])

    params = {"video": video, "verb":0, "ROImask":"skin_adapt", "skinAdapt":0.2,"detrMethod":"tarvainen", "zeroMeanSTDnorm":1}
    m = POS(**params)
    bpmES, timesES, bvpEs, fs, red, green, blue = m.runOffline(**params)

    #pulse = np.average(bpmES)
    #print(pulse)
    red_sig=np.concatenate(red)
    red_sig=red_sig.flatten()

    green_sig=np.concatenate(green)
    green_sig=green_sig.flatten()

    blue_sig=np.concatenate(blue)
    blue_sig=blue_sig.flatten()

    #print(timesES.size)
    #print(red_sig.size)

    arr_BVP=np.concatenate(bvpEs, axis=1)
    arr_BVP=arr_BVP.flatten()
    #print(arr_BVP.size)
    #fs=25
    t=np.linspace(0,1,arr_BVP.size)
    tr=np.linspace(0,1, red_sig.size)
    #plt.plot(tr,red_sig, tr, green_sig, t, arr_BVP)
    #plt.show()


    wd , m = hp.process(arr_BVP, sample_rate = fs,high_precision=True, clean_rr=True, high_precision_fs=50.0)
    #wd = hp.analysis.clean_rr_intervals(working_data = wd, method = 'z-score')

    print("the BPM is", m['bpm'])
    result_dict = {'bpm': m['bpm']}
    return result_dict


if __name__ == '__main__':
    app.run(debug=True)